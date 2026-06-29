# Widget setup guide

The garage dashboard uses three kinds of widgets. Two work immediately with zero setup. One needs your GitHub username swapped in. Three need API keys.

## 1. Zero-setup widgets (already live)

These hit public third-party services and require nothing from you beyond a working `username` parameter:

- `github-readme-stats.vercel.app` — stats card, top languages card
- `github-readme-streak-stats.herokuapp.com` — streak stats
- `github-readme-activity-graph.vercel.app` — contribution activity graph
- `github-profile-trophy.vercel.app` — trophy case
- `komarev.com/ghpvc` — profile view counter
- `quotes-github-readme.vercel.app` — random developer quote

**Setup:** find-and-replace `chiranjeevi7777` with your actual GitHub username everywhere in `README.md`.

```bash
# from the repo root
sed -i '' 's/chiranjeevi7777/your-actual-username/g' README.md   # macOS
sed -i 's/chiranjeevi7777/your-actual-username/g' README.md      # Linux
```

These public widget services occasionally rate-limit or go down. If a card stops rendering, check the service's GitHub repo for an open incident, or self-host (most have a one-click Vercel deploy button in their README).

## 2. The contribution snake (`.github/workflows/snake.yml`)

This workflow renders your contribution graph as an animated snake eating through it, and commits the output SVG to an `output` branch.

**Setup:**
1. Push this repo (with the `.github/workflows/snake.yml` file) to `github.com/chiranjeevi7777/chiranjeevi7777` — it must be your **profile repo** (the special repo named exactly after your username).
2. No secrets needed — it uses the default `GITHUB_TOKEN`, which is auto-provided.
3. Go to **Settings → Actions → General** and ensure "Read and write permissions" is enabled for the `GITHUB_TOKEN` (needed so the workflow can push to the `output` branch).
4. Run the workflow manually once from the **Actions** tab (`workflow_dispatch`) to generate the first snake, instead of waiting for the nightly cron.
5. It will create an `output` branch automatically — the README already points at `https://raw.githubusercontent.com/chiranjeevi7777/chiranjeevi7777/output/dist/snake-dark.svg`.

## 3. WakaTime coding time (`.github/workflows/wakatime.yml`)

Shows real coding-time stats pulled from your WakaTime account.

**Setup:**
1. Create a free account at [wakatime.com](https://wakatime.com) and install the editor plugin for VS Code / JetBrains / Vim / whichever you use.
2. Code for at least a day so there's data to show.
3. Grab your API key from your [WakaTime settings page](https://wakatime.com/settings/api-key).
4. In your GitHub repo: **Settings → Secrets and variables → Actions → New repository secret**:
   - `WAKATIME_API_KEY` → your WakaTime key
   - `GH_TOKEN` → a [personal access token](https://github.com/settings/tokens) with `repo` scope (the default `GITHUB_TOKEN` doesn't have write access to push the updated README from this particular action)
5. Run the workflow once manually to confirm it commits a stats block.

If you'd rather skip WakaTime entirely, delete `.github/workflows/wakatime.yml` and remove the "Now playing"/coding-time references from the README — the rest of the page works fine without it.

## 4. Spotify "now playing"

The `novatorem` Spotify widget needs its own deploy — it's not something this repo's Actions can run for you.

**Setup:**
1. Fork [novatorem/novatorem](https://github.com/novatorem/novatorem).
2. Follow its README to connect your Spotify account and deploy to Vercel.
3. Replace `novatorem-chiranjeevi7777.vercel.app` in this README with your actual deployed Vercel URL.

If you don't use Spotify, delete that `<img>` line and the "Now playing" heading — nothing else depends on it.

## 5. Customizing the industrial theme

All custom SVGs live under `assets/`. The palette is defined per-file rather than via shared CSS (GitHub strips `<style>` blocks with external dependencies in some contexts, so colors are hardcoded per SVG for reliability). To retheme:

- **Section signs** (`assets/dividers/sign-*.svg`): regenerate via `scripts/make_signs.py` — edit the `SECTIONS` list and accent colors at the top of the script, then rerun.
- **Project cards** (`assets/project-cards/*.svg`): regenerate via `scripts/make_project_cards.py` — edit the `PROJECTS` list (name, tagline, status, version, stack, roadmap, progress %).
- **Badges** (`assets/badges/*.svg`): regenerate via `scripts/make_badges.py`.
- **One-off illustrations** (`banner.svg`, `garage.svg`, `dashboard.svg`, `shipping-dock.svg`, `coffee-corner.svg`, `tool-wall.svg`): hand-authored, edit directly. Each uses two accent colors — `#FFB200` (industrial yellow) and `#FF7A00` (orange) — find-and-replace those hex values to retheme everything at once.

Run all three generator scripts from the repo root:

```bash
python3 scripts/make_signs.py
python3 scripts/make_project_cards.py
python3 scripts/make_badges.py
```

## 6. Adding a new project to the showcase

1. Add an entry to the `PROJECTS` list in `scripts/make_project_cards.py`.
2. Rerun `python3 scripts/make_project_cards.py` — it writes a new SVG to `assets/project-cards/`.
3. Add an `<img>` block for it in the **Project Showcase** section of `README.md`, following the existing pattern.
