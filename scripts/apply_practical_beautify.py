#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


PRACTICAL_CSS = """
/* Practical beautify preset: cleaner chat, less noise, better readability */
#chat .mes,
.mes {
  border-radius: 14px;
}

#send_form,
#top-bar,
.drawer-content,
.inline-drawer-content,
.popup {
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
  box-shadow: none !important;
}

.mes_block,
.mes_text,
.user_text,
.ch_name,
.name_text {
  text-shadow: none !important;
}

#chat .mes {
  border: 1px solid rgba(255, 255, 255, 0.06);
}

textarea,
input,
select,
button {
  border-radius: 10px;
}

body {
  letter-spacing: 0.01em;
}
""".strip()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=4, ensure_ascii=False) + "\n", encoding="utf-8")


def apply_preset(data: dict, mobile: bool) -> dict:
    power_user = data.setdefault("power_user", {})
    power_user["reduced_motion"] = True
    power_user["compact_input_area"] = True
    power_user["noShadows"] = True
    power_user["waifuMode"] = False
    power_user["movingUI"] = False
    power_user["blur_strength"] = 0 if mobile else 1
    power_user["shadow_width"] = 0
    power_user["font_scale"] = 1.02 if mobile else 1.05
    power_user["custom_css"] = PRACTICAL_CSS
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply a practical SillyTavern beautify preset.")
    parser.add_argument("--settings", required=True, help="Path to SillyTavern settings.json")
    parser.add_argument("--mobile", action="store_true", help="Use the mobile-leaning preset")
    args = parser.parse_args()

    settings_path = Path(args.settings)
    data = load_json(settings_path)
    updated = apply_preset(data, args.mobile)
    save_json(settings_path, updated)
    power_user = updated["power_user"]
    print(json.dumps({
        "settings": str(settings_path),
        "mobile": args.mobile,
        "reduced_motion": power_user["reduced_motion"],
        "compact_input_area": power_user["compact_input_area"],
        "blur_strength": power_user["blur_strength"],
        "shadow_width": power_user["shadow_width"],
        "font_scale": power_user["font_scale"]
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
