# Installation guide

This turns `README.md` into your live GitHub profile page.

## Quick start

1. **Create your profile repo.** On GitHub, create a new repository named *exactly* the same as your username (e.g. if your username is `jdoe`, the repo is `jdoe/jdoe`). GitHub will show a banner offering to template this for you — choose that, or create it manually and make it public.
2. **Copy these files into it:**
   ```
   README.md
   assets/
   .github/workflows/
   docs/
   scripts/
   ```
3. **Replace the placeholder.** Every instance of `chiranjeevi7777` needs to become your real GitHub username:
   ```bash
   grep -rl 'chiranjeevi7777' . --include='*.md' --include='*.yml' | xargs sed -i 's/chiranjeevi7777/your-actual-username/g'
   ```
   (On macOS, `sed -i` needs an empty backup-suffix argument: `sed -i '' 's/.../.../g'`.)
4. **Replace "Chiranjeevi" and the project names** in `README.md` and `assets/banner.svg` with your own name and your own actual repositories. The four sample projects (ScholarGuard AI, KnowledgeVault AI, CardioVision AI, NextBook) are placeholders from the original spec — swap them for real shipped work, or keep them as a template structure and edit the content.
5. **Push to `main`.** GitHub renders `README.md` automatically as your profile page at `github.com/your-username`.
6. **Enable the dynamic widgets** — see [`docs/widget-setup.md`](./docs/widget-setup.md) for the snake animation, WakaTime, and Spotify setup (all optional; the page works without them).

## What renders with zero extra setup

Once `chiranjeevi7777` is replaced, these work immediately on push:
- Banner, garage door, tool wall, dashboard frame, shipping dock, coffee corner illustrations (all local SVG, no dependencies)
- All section signs and project workbench cards (local SVG)
- GitHub stats, top languages, streak stats, activity graph, trophy case, profile view counter, developer quote (public third-party widgets keyed only to your username)

## What needs one extra step

- **Contribution snake** — needs the Action run once manually from the **Actions** tab after first push (see widget-setup guide, section 2)
- **WakaTime coding stats** — needs a WakaTime account + API key in repo secrets (section 3)
- **Spotify now playing** — needs a separate Vercel deploy of the `novatorem` widget (section 4)

If you don't want to bother with the last two, delete those specific lines from `README.md` — nothing else breaks.

## Asset optimization notes

- All hand-authored SVGs avoid embedded fonts and external image references — they're self-contained and render in GitHub's sandboxed SVG viewer without extra requests.
- Animations use native SVG `<animate>` (SMIL), which GitHub's `camo` image proxy and markdown renderer both support — no JavaScript required, no compatibility issues.
- File sizes are kept under ~6KB per asset by using flat fills and simple paths instead of embedded raster images or complex gradients.
- If you want even smaller files, run them through [SVGO](https://github.com/svg/svgo): `npx svgo assets/**/*.svg`.

## Folder structure reference

```
.
├── README.md                      ← the profile page itself
├── INSTALL.md                     ← this file
├── docs/
│   └── widget-setup.md            ← dynamic widget configuration
├── scripts/
│   ├── make_signs.py              ← regenerates section dividers
│   ├── make_project_cards.py      ← regenerates workbench project cards
│   └── make_badges.py             ← regenerates status badges
├── .github/workflows/
│   ├── snake.yml                  ← contribution snake generator
│   └── wakatime.yml               ← coding-time stats updater
└── assets/
    ├── banner.svg                 ← animated garage-door header
    ├── garage.svg                 ← entrance illustration
    ├── tool-wall.svg              ← pegboard background strip
    ├── dashboard.svg              ← telemetry panel frame
    ├── shipping-dock.svg          ← shipping dock illustration
    ├── coffee-corner.svg          ← break room illustration
    ├── dividers/                  ← 11 hanging section signs + hazard strip
    ├── project-cards/             ← 4 workbench-style project cards
    └── badges/                    ← 6 status pill badges
```
