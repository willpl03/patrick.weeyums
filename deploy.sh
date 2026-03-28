#!/bin/bash
# ─────────────────────────────────────────────────────────
# deploy.sh — Build and publish to GitHub Pages
# Usage: ./deploy.sh
# ─────────────────────────────────────────────────────────

set -e  # Stop on any error

echo "🔨 Building site..."
pelican content -s pelicanconf.py -o output

echo "🚀 Deploying to GitHub Pages..."
ghp-import -n -p -f output

echo "✅ Done! Site will be live at:"
echo "   https://willpl03.github.io/patrick.weeyums"
echo "   (allow 1-2 minutes for GitHub to update)"
