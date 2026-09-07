#!/usr/bin/env bash
# Script d'installation globale des skills pour Linux & macOS
set -e

TARGET_DIR="$HOME/.gemini/config/skills"
mkdir -p "$TARGET_DIR"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$SCRIPT_DIR/skills"

echo "📦 Installation des compétences dans $TARGET_DIR..."

for skill in "$SOURCE_DIR"/*; do
  if [ -d "$skill" ]; then
    skill_name="$(basename "$skill")"
    cp -R "$skill" "$TARGET_DIR/"
    echo "  ✓ Skill installé : $skill_name"
  fi
done

echo ""
echo "✨ Tous les skills sont installés et disponibles globalement !"
