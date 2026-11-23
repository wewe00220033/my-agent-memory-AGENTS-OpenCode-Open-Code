# Fish-lens review of S1 capsule

- id: `ses_e01f5d49cffeG092186VMGoHW5`
- title: Fish-lens review of S1 capsule
- date: 2026-11-21 12:17:21
- directory: D:/SMS/.hRhR_gateway-service
- parent: `ses_e02073e05ffehgYIVxPQ1PPyjI`
- agent: critic
- model: upstage-studio/claude-fable-5-1
- messages: 4 (user 1, assistant 3)
- archived: false

## 4 · user (2026-11-21 12:17:21)

You are a subagent spawned by another session.
# Inspection Capsule
LENS: fish
Stage: S1 (bridge_tools / bridge_doctor.py) — final gate before [FINAL_APPROVED]

## 1) Goal
Daily stdlib-only checker `bridge_doctor.py`: (a) bridge `/health` JSON (status==ok, session_configured/valid True, models_count int>=1), (b) five governance rules over `data["agents"]` in an opencode config JSON (three agents, read *opencode.json* deny for all, planner shell/edit deny + subagent executor/critic allow, executor subagent/question deny + edit deny on PLAN/DUET_LOG/TASKS/duet_resume, critic * * deny + read/grep/glob allow + no allow on edit/shell/subagent/write), (c) three tool files exist and are non-empty; ASCII table report + `--json`; exit 0/1 without Traceback.

## 2) Constraints
- READ-ONLY review. You MUST NOT read any file matching `*opencode.json*` (governance rule). Do not run shell, do not edit anything.
- Allowed to read: `D:\SMS\.hRhR_gateway-service\tools\bridge_doctor.py`, `D:\SMS\.hRhR_gateway-service\tools\test_bridge_doctor.py`, `D:\SMS\.hRhR_gateway-service\tools\PLAN.md`.
- Spec: stdlib only; checks never raise (CATCH = OSError, ValueError, TypeError, AttributeError, KeyError); no ANSI; no value outside `data["agents"]` echoed; tests use tempfile + fake opener (io.BytesIO), no real network, config fixtures named `sample_agents_cfg.json`.

## 3) Actual Changes
- `bridge_doctor.py` (381 lines, new): constants (REQUIRED_AGENTS, DEFAULT_*, DEFAULT_TOOL_PATHS, CATCH); `check_health` L53-101; `_has_rule` L107-116; `check_agents_config` L119-201 (violations aggregated with '; '); `check_tools` L207-231; `format_report` L237-277; `_safe_streams` L283-294 (hasattr reconfigure guard); `_build_parser` L297-338 (7 args); `main(argv=None, opener=None)` L341-377; `sys.exit(main())` L381.
- `test_bridge_doctor.py` (478 lines, new): 29 tests — CheckHealthTests 8, CheckAgentsConfigTests 11, CheckToolsTests 2, FormatReportTests 2, MainCliTests 6 (incl. subprocess on dynamically-obtained free closed port, `--timeout 1`, subprocess timeout=30, explicit temp `--config/--run-tests/--duet-status/--make-capsule`).
- No other files touched by executor.

## 4) Test Evidence (literal, from planner's independent run of `tools\run_tests.cmd all`)
```
Ran 25 tests in 0.222s
OK
Ran 29 tests in 1.105s
OK
Ran 41 tests in 0.181s
OK
```
No FAILED / ERROR / Traceback in output. (Known, out-of-scope: run_tests.cmd exit code unreliable due to %ERRORLEVEL% inside parenthesized block; acceptance = literal unittest text.)

## 5) Concern
- `check_agents_config` is existence-only matching; does any code path echo config values (secret leak) or raise outside CATCH (e.g. non-hashable/odd types in permissions)?
- `format_report([])` -> `OVERALL: FAIL (0/0)`; `_ascii()` replaces non-ASCII with '?'. Any hidden Windows/encoding or test-isolation flaw (real network, real config read, flaky port test)?

Return findings as [Blocker] / [Major] / [Nitpick], each backed by `file:line` or test output, then a final line `VERDICT: PASS` or `VERDICT: BLOCK`.

## 5 · assistant (2026-11-21 12:17:21)

Starting read-only fish-lens review: reading `bridge_doctor.py` first.

## 15 · assistant (2026-11-21 12:17:36)

Reading `test_bridge_doctor.py` next to verify test isolation (fake opener, tempfile, port test).

## 25 · assistant (2026-11-21 12:18:05)

VERDICT: PASS

Reviewed `bridge_doctor.py` (381 lines) and `test_bridge_doctor.py` (478 lines) under LENS=fish; no `*opencode.json*` touched, no shell, no edits.

Concern checks:
- Secret leak: none. `bridge_doctor.py:160` echoes only `agent[index]`; `:169` echoes constants passed by `require()`; `:196` echoes `action` only when it equals a member of `_CRITIC_FORBIDDEN_ALLOW_ACTIONS`. Confirmed by `test_bridge_doctor.py:249` and `:275`.
- Odd types: `in` on a tuple (`:195`) and `==` (`:114-116`) need no hashing; non-dict/non-list shapes are gated at `:133,:136,:148,:152,:157`; `UnicodeDecodeError`/`JSONDecodeError` are `ValueError` subclasses, inside CATCH (`:26`).
- `format_report([])` -> `OVERALL: FAIL (0/0 checks passed)` is documented (`:245`) and consistent with `main` (`:364`). `--json` uses `json.dumps` default `ensure_ascii=True` (`:373`), no ANSI anywhere.
- Isolation: every `check_health` call injects a fake opener (`io.BytesIO`, `:85-98`); all configs are `tempfile` + `sample_agents_cfg.json` (`:66-73`); subprocess test passes explicit `--config/--run-tests/--duet-status/--make-capsule` (`:357-371`) so `DEFAULT_CONFIG` (`bridge_doctor.py:17`) is never opened. Test count 8+11+2+2+6 = 29 matches `Ran 29 tests ... OK`.

[Nitpick] `bridge_doctor.py:67-69` + `:103`: `urlopen`/`response.read()` can raise `http.client.HTTPException` subclasses (`BadStatusLine`, `IncompleteRead`) which are not `OSError`, so they escape CATCH and would print a Traceback. CATCH is spec-mandated, so this is a spec gap, not an executor defect — consider adding `http.client.HTTPException` in a follow-up.
[Nitpick] `test_bridge_doctor.py:374-380`: port is released before the subprocess starts (TOCTOU); a concurrent bind could turn "refused" into a live listener and flake the test. Rare on a dev box; `--timeout 1` + `timeout=30` bound the damage.
[Nitpick] Capsule line refs drift ~3 lines from the file: `check_health` is actually `:56-104`, `_has_rule` `:110-119`, `check_agents_config` `:122-204`, `format_report` `:240-277`. Code is unaffected; fix the capsule before `[FINAL_APPROVED]`.
