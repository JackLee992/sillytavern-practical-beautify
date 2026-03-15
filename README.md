# sillytavern-practical-beautify

Apply a practical `SillyTavern` beautify preset focused on readability, low visual noise, and smooth performance.

This repo is not a heavy theme pack. It is a Codex skill plus a small script that writes a conservative UI preset into `settings.json -> power_user`.

## What It Does

- reduces motion
- reduces blur and shadow noise
- keeps compact input enabled
- applies light custom CSS for cleaner message blocks
- avoids changing API, secret, or model settings

## Repository Layout

- `SKILL.md`: Codex skill instructions
- `scripts/apply_practical_beautify.py`: applies the preset to `SillyTavern` settings
- `references/laopobao-style-notes.md`: rationale behind the preset

## Quick Start

Desktop-leaning preset:

```powershell
python scripts/apply_practical_beautify.py --settings "C:\Users\Jacklee\SillyTavern\data\default-user\settings.json"
```

Mobile-leaning preset:

```powershell
python scripts/apply_practical_beautify.py --settings "C:\Users\Jacklee\SillyTavern\data\default-user\settings.json" --mobile
```

## Important Detail

`SillyTavern` UI settings belong under `settings.json -> power_user`.

This repo intentionally writes there instead of editing loose top-level duplicates, because top-level duplicates may not control the actual active UI state in recent `SillyTavern` versions.

## Scope

This repo is a practical baseline, not a replacement for full third-party themes like:

- `Moonlit Echoes Theme`
- `Not-A-Discord-Theme`

Use it when you want a cleaner default UI with low risk and low visual overhead.

## Related Repos

- `sillytavern-codex-bridge`
- `sillytavern-character-card`
