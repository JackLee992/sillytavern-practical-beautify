---
name: sillytavern-practical-beautify
description: Apply practical SillyTavern beautification focused on readability, low visual noise, and smooth performance, following the common Chinese "老婆宝/酒馆助手" style of customization. Use when Codex needs to tune a local SillyTavern UI for cleaner visuals, lower blur and motion, compact input, safer mobile performance, or install a reusable beautify preset into the current SillyTavern user profile.
---

# SillyTavern Practical Beautify

Use this skill for pragmatic `SillyTavern` UI cleanup rather than heavy theme overhauls.

## Workflow

1. Read the current `SillyTavern` user settings file.
2. Apply the practical beautify preset with `scripts/apply_practical_beautify.py`.
3. Update keys inside `settings.json -> power_user`, not top-level duplicates.
3. Keep API, secrets, and model settings unchanged.
4. Ask the user to refresh the `SillyTavern` tab after applying.

## Preset Goals

- reduce motion
- reduce blur and shadow noise
- keep compact input
- improve readability with light custom CSS
- avoid expensive visual effects
- keep `waifuMode` off unless the user explicitly wants visual novel mode

## Script

Use:

```powershell
python scripts/apply_practical_beautify.py --settings "C:\Users\Jacklee\SillyTavern\data\default-user\settings.json"
```

Optional mobile-leaning variant:

```powershell
python scripts/apply_practical_beautify.py --settings "C:\Users\Jacklee\SillyTavern\data\default-user\settings.json" --mobile
```

## When To Read References

- Read `references/laopobao-style-notes.md` if you need the rationale behind the preset.
