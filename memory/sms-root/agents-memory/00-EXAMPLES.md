# 📚 المرجع القياسي للأكواد (Reference Implementations)

## 🦆 Duck.ai V5 Dynamic Multi-Engine (Zero-Browser + Pure Requests)

```python
"""
Duck.ai Pure Requests Architecture (V5 Golden Standard)
- صفر كوكيز نهائياً (Stateless 100%)
- حل تحديات JSA في الذاكرة بنسبة تطابق 100% مع متصفح Chrome الحقيقي (Bit-Exact Matching)
- تدوير البصمات والأجهزة لتخطي كوتا الصور اليومية
- إجبار الموديل على توليد الصور عبر forced tool calling
"""
import json
import base64
import hashlib
import time
import uuid
import random
from curl_cffi import requests
from py_mini_racer import MiniRacer

STACK = (
    "Error\nat l (https://duck.ai/dist/duckai-dist/entry.duckai.2d2656b1fcd20ced62d9.js:2:2148242)\n"
    "at async https://duck.ai/dist/duckai-dist/entry.duckai.2d2656b1fcd20ced62d9.js:2:1868221"
)

_DOM_MOCK_TEMPLATE = r"""
var Element = function Element(){};
var HTMLElement = function HTMLElement(){};
var HTMLDivElement = function HTMLDivElement(){};
var HTMLIFrameElement = function HTMLIFrameElement(){};
var HTMLSpanElement = function HTMLSpanElement(){};
var HTMLMetaElement = function HTMLMetaElement(){};
var HTMLDocument = function HTMLDocument(){};
var Node = function Node(){};

var window = globalThis;
var self = window;
window.top = window;
window.self = window;
window.parent = window;
window.Element = Element;
window.HTMLElement = HTMLElement;
window.HTMLDivElement = HTMLDivElement;
window.HTMLIFrameElement = HTMLIFrameElement;
window.HTMLSpanElement = HTMLSpanElement;
window.HTMLMetaElement = HTMLMetaElement;
window.HTMLDocument = HTMLDocument;
window.Node = Node;
window.Array = Array;
window.Proxy = Proxy;
window.Symbol = Symbol;
window.JSON = JSON;
window.Window = function Window() {};
window.__DDG_BE_VERSION__ = '1';
window.hasOwnProperty = function(p){
    return Object.prototype.hasOwnProperty.call(this, p);
};

var navigator = {
    userAgent: "__UA__",
    webdriver: false
};

function mkEl(tag){
    tag = (tag || 'div').toLowerCase();
    var el = {
        tagName: tag.toUpperCase(),
        _html: '',
        _attrs: {},
        style: {
            cssText: '',
            display: 'inline-block',
            getPropertyValue: function(){ return 'inline-block'; }
        },
        textContent: 'x',
        innerText: 'x',
        offsetWidth: 20,
        offsetHeight: 20,
        scrollHeight: 20,
        children: [],
        childNodes: []
    };
    var VOID_TAGS = {area:1,base:1,br:1,col:1,embed:1,hr:1,img:1,input:1,
                     link:1,meta:1,param:1,source:1,track:1,wbr:1};

    function serialize(nodes){
        var out = '';
        for (var i = 0; i < nodes.length; i++){
            var n = nodes[i];
            if (VOID_TAGS[n.tag]){ out += '<' + n.tag + '>'; continue; }
            out += '<' + n.tag + '>' + serialize(n.kids) + '</' + n.tag + '>';
        }
        return out;
    }

    function parseTree(html){
        var roots = [], stack = [], total = 0;
        if (!html) return {roots: roots, total: 0};
        var re = /<(\/?)([a-zA-Z][\w-]*)((?:[^>"']|"[^"]*"|'[^']*')*?)(\/?)>/g, m;
        while ((m = re.exec(html)) !== null){
            var closing = m[1] === '/';
            var tag = m[2].toLowerCase();
            var selfclose = m[4] === '/';
            if (closing){
                if (tag === 'br'){
                    var node = {tag: 'br', kids: []};
                    if (stack.length) stack[stack.length - 1].kids.push(node);
                    else roots.push(node);
                    total++;
                    continue;
                }
                var idx = -1;
                for (var i = stack.length - 1; i >= 0; i--){
                    if (stack[i].tag === tag){ idx = i; break; }
                }
                if (idx < 0) continue;
                var node = stack.splice(idx, 1)[0];
                if (stack.length) stack[stack.length - 1].kids.push(node);
                else roots.push(node);
                total++;
                continue;
            }
            var el = {tag: tag, kids: []};
            total++;
            if (selfclose || VOID_TAGS[tag]){
                if (stack.length) stack[stack.length - 1].kids.push(el);
                else roots.push(el);
            } else {
                stack.push(el);
            }
        }
        while (stack.length){
            var rest = stack.pop();
            if (stack.length) stack[stack.length - 1].kids.push(rest);
            else roots.push(rest);
        }
        return {roots: roots, total: total};
    }

    Object.defineProperty(el, 'innerHTML', {
        get: function(){
            if (!this._html) return '<p></p>';
            return serialize(parseTree(this._html).roots);
        },
        set: function(v){
            this._html = v;
            var t = parseTree(v);
            this._descendants = t.total;
            this.children = t.roots.map(function(n){ return mkEl(n.tag); });
            this.childNodes = this.children.slice();
        }
    });
    el.getAttribute = function(a){
        if (a === 'sandbox') return "allow-scripts allow-same-origin";
        if (a === 'content') return "default-src 'none'; script-src 'unsafe-inline';";
        if (a === 'http-equiv') return 'Content-Security-Policy';
        return '';
    };
    el.setAttribute = function(a, v){ el._attrs[a] = v; };
    el.getBoundingClientRect = function(){
        return { width: 20, height: 20, top: 0, left: 0, bottom: 20, right: 20 };
    };
    el.querySelectorAll = function(sel){
        if (sel === '*'){
            var all = [];
            for (var i = 0; i < (this._descendants || 0); i++) all.push(mkEl('div'));
            return all;
        }
        return [mkEl('div')];
    };
    el.getElementsByTagName = function(){ return [mkEl('span')]; };
    el.querySelector = function(sel){
        if (sel === 'meta' || (sel && sel.indexOf('meta') >= 0)){
            var m = mkEl('meta');
            m.getAttribute = function(a){
                return a === 'content' ? "default-src 'none'; script-src 'unsafe-inline';" : '';
            };
            return m;
        }
        return mkEl('div');
    };
    el.appendChild = function(c){ return c; };
    el.removeChild = function(c){ return c; };
    return el;
}

function makeCspMeta(){
    var meta = mkEl('meta');
    var cspDoc = {
        get: function(key){
            if (key === '__DDG_BE_VERSION__'){
                var v = mkEl('meta');
                v.getAttribute = function(a){
                    return a === 'content' ? "default-src 'none'; script-src 'unsafe-inline';" : '';
                };
                return v;
            }
            return null;
        },
        querySelector: function(){ return null; },
        head: null,
        body: mkEl('body')
    };
    cspDoc.head = {
        querySelector: function(sel){
            return (sel && sel.indexOf('Content-Security-Policy') >= 0)
                ? makeCspMeta() : null;
        }
    };
    meta.contentDocument = cspDoc;

    var win = { document: cspDoc, navigator: navigator };
    win.self = win;
    win.top = win;
    win.window = win;
    win.Array = Array;
    win.Proxy = Proxy;
    win.Symbol = Symbol;
    win.JSON = JSON;
    win.Window = function Window(){};
    meta.contentWindow = win;

    meta.getAttribute = function(a){
        if (a === 'content') return "default-src 'none'; script-src 'unsafe-inline';";
        if (a === 'sandbox') return "allow-scripts allow-same-origin";
        if (a === 'http-equiv') return 'Content-Security-Policy';
        return '';
    };
    return meta;
}

function makeIframe(){
    var f = mkEl('iframe');
    f.srcdoc = 'DuckDuckGo Fraud & Abuse';
    var win = {};
    win.self = win;
    win.top = win;
    win.window = win;
    win.document = mkEl('document');
    win.Array = Array;
    win.Proxy = Proxy;
    win.Symbol = Symbol;
    win.JSON = JSON;
    win.Window = function Window(){};
    f.contentWindow = win;
    f.contentDocument = win.document;
    return f;
}

var head = {
    querySelector: function(sel){
        return (sel && sel.indexOf('Content-Security-Policy') >= 0)
            ? makeCspMeta() : null;
    }
};

var document = {
    head: head,
    body: mkEl('body'),
    createElement: function(tag){
        return (tag || '').toLowerCase() === 'iframe' ? makeIframe() : mkEl(tag);
    },
    querySelector: function(sel){
        if (sel && sel.indexOf('meta') >= 0) return makeCspMeta();
        return makeIframe();
    },
    querySelectorAll: function(){ return [mkEl('div')]; },
    getElementsByTagName: function(){ return [mkEl('div')]; },
    get: function(key){ return null; }
};
window.document = document;

function getComputedStyle(el){
    return {
        getPropertyValue: function(){ return 'inline-block'; },
        display: 'inline-block'
    };
}
"""

def solve_duck_challenge(raw_vqd_hash: str, user_agent: str) -> str:
    challenge_code = base64.b64decode(raw_vqd_hash).decode("utf-8", errors="ignore")
    dom_env = _DOM_MOCK_TEMPLATE.replace("__UA__", user_agent.replace('"', '\\"'))

    ctx = MiniRacer()
    ctx.eval(dom_env)

    runner = """
    var __result = null;
    var __error = null;
    (%s).then(res => {
        __result = JSON.stringify(res);
    }).catch(err => {
        __error = String(err) + "\\n" + (err ? err.stack : "");
    });
    """ % challenge_code
    ctx.eval(runner)

    res_str = None
    for _ in range(80):
        res_str = ctx.eval("__result")
        if res_str:
            break
        time.sleep(0.01)

    if not res_str:
        err = ctx.eval("__error")
        raise RuntimeError(f"Challenge execution failed: {err}")

    raw_res = json.loads(res_str)

    hashed_client = []
    for item in raw_res.get("client_hashes", []):
        d = hashlib.sha256(item.encode("utf-8")).digest()
        hashed_client.append(base64.b64encode(d).decode("utf-8"))

    raw_res["client_hashes"] = hashed_client
    raw_res["meta"]["origin"] = "https://duck.ai"
    raw_res["meta"]["stack"] = STACK
    raw_res["meta"]["duration"] = str(random.randint(7, 16))

    return base64.b64encode(json.dumps(raw_res).encode("utf-8")).decode("utf-8")
```
