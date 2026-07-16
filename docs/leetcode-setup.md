# LeetCode Integration Setup Guide

This guide explains how to set up automatic LeetCode statistics syncing with your GitHub profile.

## Overview

Your LeetCode progress is now automatically fetched and displayed on your GitHub profile README. The integration includes:

- ✅ Real-time problem stats (Easy, Medium, Hard)
- ✅ Total problems solved
- ✅ Top programming languages used
- ✅ Badges earned
- ✅ Automatic updates every 6 hours

## Setup Instructions

### Step 1: Add GitHub Secret

1. Go to your repository settings: https://github.com/chiranjeevi7777/chiranjeevi7777/settings/secrets/actions
2. Click **"New repository secret"**
3. Create a secret with:
   - **Name:** `LEETCODE_USERNAME`
   - **Value:** `Chiranjeevi7R`

### Step 2: Verify GitHub Actions

1. Navigate to `.github/workflows/leetcode-stats.yml` in your repo
2. Go to the **Actions** tab to monitor the workflow
3. The workflow runs:
   - Every 6 hours automatically
   - On manual trigger via "Run workflow"

### Step 3: Monitor Updates

Check these files after the workflow runs:
- `data/leetcode_stats.json` — Raw stats data
- `README.md` — Updated profile with stats badge

## Files Included

```
├── .github/workflows/
│   └── leetcode-stats.yml          # GitHub Actions workflow
├── scripts/
│   └── fetch_leetcode_stats.py     # Stats fetching script
├── data/
│   └── leetcode_stats.json         # Generated stats file
└── docs/
    └── leetcode-setup.md           # This file
```

## How It Works

1. **GitHub Actions** runs on schedule (every 6 hours)
2. **Python script** queries LeetCode GraphQL API
3. **Stats are parsed** and saved to `data/leetcode_stats.json`
4. **README is referenced** with live badges
5. **Changes are committed** automatically

## API Integration

The integration uses LeetCode's public GraphQL API to fetch:
- Problem statistics by difficulty
- User profile information
- Badge achievements
- Language statistics

**No API key required!** LeetCode's GraphQL endpoint is publicly accessible.

## Troubleshooting

### Workflow Not Running
- Check if Actions are enabled in repo settings
- Verify `LEETCODE_USERNAME` secret is set
- Check workflow logs in Actions tab

### Data Not Updating
- Verify LeetCode username is correct: `Chiranjeevi7R`
- Check that the account is public on LeetCode
- Wait for the next scheduled run (6 hours max)

### Stats Missing
- Ensure you've solved at least one problem on LeetCode
- LeetCode stats are updated daily on their platform
- Try manual workflow trigger: Actions → leetcode-stats → Run workflow

## Manual Updates

To manually trigger an update:

1. Go to Actions tab
2. Select "Update LeetCode Stats" workflow
3. Click "Run workflow" → "Run workflow"
4. Stats will update within 1-2 minutes

## Customization

### Change Update Frequency

Edit `.github/workflows/leetcode-stats.yml`:

```yaml
schedule:
  # Change from 6 hours to your preferred interval
  - cron: '0 */6 * * *'  # Every 6 hours
  # Examples:
  # - cron: '0 0 * * *'   # Daily at midnight
  # - cron: '0 */4 * * *' # Every 4 hours
  # - cron: '0 9 * * 1'   # Weekly on Monday at 9 AM
```

### Add More Stats

Modify `scripts/fetch_leetcode_stats.py` to include:
- Problem categories
- Recent submissions
- Contest ratings
- Study plans progress

## Security

- ✅ No API keys required (public endpoint)
- ✅ Credentials stored securely in GitHub Secrets
- ✅ Read-only operations (no modifications to LeetCode)
- ✅ Automated commits use GitHub Actions bot account

## References

- [LeetCode GraphQL API](https://leetcode.com/graphql)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

## Next Steps

1. ✅ Verify GitHub Actions is enabled
2. ✅ Add `LEETCODE_USERNAME` secret
3. ✅ Manual trigger workflow to test
4. ✅ Monitor stats updates in `data/leetcode_stats.json`
5. ✅ Check README for updated badge

Happy grinding! 🚀
