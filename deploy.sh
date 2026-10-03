#!/bin/bash
# ─────────────────────────────────────────────────────────
# deploy.sh — Build and publish to GitHub Pages
# Usage: ./deploy.sh
# ─────────────────────────────────────────────────────────

set -e  # Stop on any error

echo "🔨 Building site..."
python3 -m pelican content -s pelicanconf.py -o output

echo "🚀 Deploying to GitHub Pages..."
python3 -m ghp_import -n -p -f output

echo "✅ Done! Site will be live at:"
echo "   https://www.weeeyums.com"
echo "   (allow 1-2 minutes for GitHub to update)"
