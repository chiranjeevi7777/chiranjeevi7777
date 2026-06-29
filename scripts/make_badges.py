import os

BADGE_TEMPLATE = """<svg viewBox="0 0 {width} 36" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label} badge">
  <rect x="0" y="0" width="{width}" height="36" rx="4" fill="#161616" stroke="{color}" stroke-width="1.5"/>
  <circle cx="20" cy="18" r="5" fill="{color}"/>
  <text x="34" y="23" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="700" fill="#F0F0F0" letter-spacing="1">{label}</text>
</svg>
"""

BADGES = [
    ("OPERATIONAL", "#4ADE80"),
    ("IN PROGRESS", "#FFB200"),
    ("EXPERIMENTAL", "#FF7A00"),
    ("ARCHIVED", "#666666"),
    ("AI ENGINEER", "#FFB200"),
    ("OPEN TO WORK", "#4ADE80"),
]

OUT_DIR = "/home/claude/garage/assets/badges"
os.makedirs(OUT_DIR, exist_ok=True)

for label, color in BADGES:
    width = len(label) * 9 + 50
    svg = BADGE_TEMPLATE.format(width=width, label=label, color=color)
    fname = label.lower().replace(" ", "-")
    with open(os.path.join(OUT_DIR, f"{fname}.svg"), "w") as f:
        f.write(svg)
    print(f"wrote {fname}.svg")
