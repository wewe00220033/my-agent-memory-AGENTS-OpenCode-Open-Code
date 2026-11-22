## 🧩 Surgical Zero-Unpack Electron ASAR Single-File Patcher (Reference Implementation)

عند الحاجة لتعديل ملف واجهة وحيد (مثل `out/renderer/index.html`) داخل أرشيف Electron `app.asar` دون المساس بآلاف الملفات أو إفساد الإضافات الثنائية (`.node` / `.exe`):

```python
def build_patched_asar(clean_source_asar: Path, output_tmp_asar: Path, new_entry_bytes: bytes, target_rel: str) -> None:
    header, base_offset = parse_asar_header(clean_source_asar)
    with clean_source_asar.open("rb") as src_f:
        src_f.seek(base_offset)
        payload_size = clean_source_asar.stat().st_size - base_offset

        node = get_asar_node(header, target_rel)
        node["offset"] = str(payload_size)
        node["size"] = len(new_entry_bytes)
        node["integrity"] = compute_asar_integrity(new_entry_bytes)

        json_bytes = json.dumps(header, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        json_size = len(json_bytes)
        pad_len = (4 - (json_size % 4)) % 4
        u2 = 4 + json_size + pad_len
        header_size = u2 + 4
        pickle_header = struct.pack("<IIII", 4, header_size, u2, json_size) + json_bytes + (b"\x00" * pad_len)

        with output_tmp_asar.open("wb") as out_f:
            out_f.write(pickle_header)
            shutil.copyfileobj(src_f, out_f, length=16 * 1024 * 1024)
            out_f.write(new_entry_bytes)
```
- المرجع الكامل: `~\.gemini\antigravity\scratch\opencode-rtl-patcher\opencode_rtl_patcher.py`

---

## 🧩 Frida `DexClassLoader` BootClassLoader Isolation Against App R8 Shadowing (Reference Implementation)

عند حقن مكتبة خارجية (`module.apk` مثل Play Billing) داخل تطبيق أندرويد مضغوط بـ R8 (`com.google.android.apps.subscriptions.red`)، يلتقط `DexClassLoader` كلاسات التطبيق المضغوطة أولاً بسبب `Parent-First Delegation` إذا مرّرت `context.getClassLoader()` — مما يسبب `NoSuchMethodError` صامتاً داخل `FutureTask` (مثل `Purchase.getPurchaseToken()` أثناء `queryPurchasesAsync`). الحل القياسي تمرير `BootClassLoader` (`getParent()`) وتأخير التنفيذ على الـ Main Looper عبر `QRClass`:

```javascript
// Isolate module.apk from app's R8-shrunk Billing classes inside base.apk
var DexClassLoader = Java.use("dalvik.system.DexClassLoader");
var appCl = context.getClassLoader();
var parentCl = (appCl && typeof appCl.getParent === "function" && appCl.getParent() != null)
    ? appCl.getParent()
    : appCl;
var dexLoader = DexClassLoader.$new(
    MODULE_APK,                                // Must be chmod 0444 on Android 14/15 W^X
    context.getCodeCacheDir().getAbsolutePath(),
    null,
    parentCl
);
Java.classFactory.loader = dexLoader;
```
- المرجع الكامل: `D:\SMS\.hRhRhRhRhRhR\repo_echiiiro\frida-auto-trial.js` (والتوثيق في `GOOGLE_ONE_HYBRID_REFERENCE.md`)

---

## 🧩 PowerShell 5.1 Non-Hanging `adb start-server` + MuMu 15 `boot_id` Deduplication + Single-Wrap Array Guard (Reference Implementation)

في Windows PowerShell 5.1:
1. لا تستخدم `Start-Process -Wait` مع `adb start-server` (ينتظر `adb fork-server` للأبد)؛ استخدم `ProcessStartInfo` بـ `WaitForExit(8000)`.
2. محاكي MuMu 15 واحد يرد على بورتات متعددة (`16384`, `7555`, `5555`) + `emulator-5554`؛ افرز بالـ `boot_id` وتفادَ `adb devices` طالما وجدت TCP ports فعالة.
3. أرجع `@($list.ToArray())` من الدالة وغلف بـ `@(Func ...)` مرة واحدة عند المستدعي لتجنب Unrolling لعنصر واحد أو التغليف المزدوج (`Object[][]`).
4. لا تستخدم `param()` إذا كان السكربت يستقبل `--flags`؛ حلّل `$args` يدوياً.

```powershell
function Start-AdbDaemon {
    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = $script:ADB
    $psi.Arguments = 'start-server'
    $psi.UseShellExecute = $false
    $psi.CreateNoWindow = $true
    $proc = [System.Diagnostics.Process]::Start($psi)
    if ($proc) {
        if (-not $proc.WaitForExit(8000)) {
            try { $proc.Kill() } catch {}
        }
        $proc.Dispose()
    }
}

function Find-ConnectedDevices {
    $found = New-Object System.Collections.Generic.List[string]
    $seenBootIds = @{}
    foreach ($port in @(16384, 16416, 16448, 16480, 16512, 7555, 5555)) {
        $candidate = "127.0.0.1:$port"
        $conn = Invoke-Adb @('connect', $candidate) -IgnoreExit
        if ($conn -match '(?i)cannot connect|refused|failed to connect|timed out') { continue }
        $state = (Invoke-Adb @('-s', $candidate, 'get-state') -IgnoreExit).Trim()
        if ($state -ne 'device') { continue }

        $bootId = (Invoke-Adb @('-s', $candidate, 'shell', 'cat /proc/sys/kernel/random/boot_id') -IgnoreExit).Trim()
        $dedupeKey = if ($bootId -match '^[0-9a-fA-F-]{8,}$') { $bootId } else { $candidate }
        if (-not $seenBootIds.ContainsKey($dedupeKey)) {
            $seenBootIds[$dedupeKey] = $candidate
            $found.Add($candidate)
        }
    }
    return @($found.ToArray())
}
# Call site single-wrap: $connected = @(Find-ConnectedDevices)
```
- المرجع الكامل: `D:\SMS\.hRhRhRhRhRhR\repo_echiiiro\auto-trial.ps1` و `D:\SMS\.hRhRhRhRhRhR\repo_echiiiro\hybrid-trial.ps1`
