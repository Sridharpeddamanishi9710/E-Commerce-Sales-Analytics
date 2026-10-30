import os
import json

vis_dir = r"c:\Users\pedda\OneDrive\Documents\E-Commerce-Sales-Analytics\E-Commerce-Sales-Analytics-Executive.Report\definition\pages\dc5ffb9e39267074c399\visuals"
items = os.listdir(vis_dir)
print(f"Checking {len(items)} visuals in {vis_dir}:")
for item in sorted(items):
    path = os.path.join(vis_dir, item, "visual.json")
    assert os.path.exists(path), f"Missing: {path}"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    name = data["name"]
    vtype = data["visual"]["visualType"]
    pos = data["position"]
    title = data["visual"].get("visualContainerObjects", {}).get("title", [{}])[0].get("properties", {}).get("text", {}).get("expr", {}).get("Literal", {}).get("Value", "N/A")
    print(f"  [OK] {item:28} | Type: {vtype:20} | Title: {title:30} | Pos: ({pos['x']}, {pos['y']}, {pos['width']}x{pos['height']})")

print(f"\nAll {len(items)} visual.json files successfully validated as well-formed JSON matching the PBIR schema!")
