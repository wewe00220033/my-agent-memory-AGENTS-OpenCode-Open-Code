# Arabic Keyboard Shortcuts Fix & Lessons Learned

## Issue Description
On Windows when the Arabic keyboard layout is active:
- Physical keys generate Arabic characters (`ش` for A, `ؤ` for C, `ر` for V, `ء` for X, `ئ` for Z, `م` for L, etc.).
- Inside Chromium/Electron webviews (such as the Antigravity Agent Chat window), Chromium's native text-editing handlers only look for Latin characters for built-in shortcuts (`Ctrl+A`, `Ctrl+C`, `Ctrl+V`, `Ctrl+X`, `Ctrl+Z`) and navigation shortcuts (`Ctrl+L`).
- Because Chromium does not consume `Ctrl + [Arabic Letter]`, the unhandled key events leak out of the chat webview and bubble up to the VS Code IDE workbench.
- The IDE workbench matches the physical scancode (e.g. `KeyA`) to global editor commands (`editor.action.selectAll`, `undo`), triggering selection or changes on whatever file tab is open on the left instead of the chat.

## Established Solution
1. **AutoHotkey Standalone Fix (Active & Recommended):**
   - Tool location: `~\AppData\Local\Programs\ArabicShortcutsFix\AutoHotkey64.exe`
   - Script location: `~\AppData\Local\Programs\ArabicShortcutsFix\FixArabicShortcuts.ahk`
   - Maps physical scancodes to virtual keycodes:
     - `$^sc01E::Send("^{vk41}")` (Ctrl + A / ش -> Select All)
     - `$^sc02E::Send("^{vk43}")` (Ctrl + C / ؤ -> Copy)
     - `$^sc02F::Send("^{vk56}")` (Ctrl + V / ر -> Paste)
     - `$^sc02D::Send("^{vk58}")` (Ctrl + X / ء -> Cut)
     - `$^sc02C::Send("^{vk5A}")` (Ctrl + Z / ئ -> Undo)
     - `$^+sc02C::Send("^+{vk5A}")` (Ctrl + Shift + Z / ئ -> Redo)
     - `$^sc015::Send("^{vk59}")` (Ctrl + Y / غ -> Redo)
     - `$^sc026::Send("^{vk4C}")` (Ctrl + L / م -> Open/Focus Chat)
     - `$^sc025::Send("^{vk4B}")` (Ctrl + K / ن -> Inline Chat)
     - `$^sc01F::Send("^{vk53}")` (Ctrl + S / س -> Save)
     - `$^sc021::Send("^{vk46}")` (Ctrl + F / ب -> Find)
     - `$^sc019::Send("^{vk50}")` (Ctrl + P / ح -> Quick Open)
   - Windows Startup launcher: `~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\ArabicShortcutsFix.cmd`
   - Quick launcher batch files on Desktop and `Downloads\111`: `تشغيل_إصلاح_الكيبورد.bat` (Saved as pure ASCII without BOM).

2. **VS Code `keybindings.json` Rules:**
   - Must use `-` to explicitly unbind default global commands before scoping them with `when: "editorTextFocus"`:
     ```json
     [
       { "key": "[REDACTED:KV_SECRET]", "command": "-editor.action.selectAll" },
       { "key": "[REDACTED:KV_SECRET]", "command": "editor.action.selectAll", "when": "editorTextFocus" },
       { "key": "[REDACTED:KV_SECRET]", "command": "-undo" },
       { "key": "[REDACTED:KV_SECRET]", "command": "undo", "when": "editorTextFocus" }
     ]
     ```

3. **Critical Warning: DO NOT Patch `jetskiAgent/main.js` Directly:**
   - `jetskiAgent/main.js` is a bundled and minified React application (~14 MB).
   - In-place string replacements in minified JavaScript lead to scope collision / syntax errors causing complete blank screen failures.
   - Always rely on AutoHotkey OS-level interception or `keybindings.json` scoping.
