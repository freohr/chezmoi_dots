#!/bin/bash

NAME=$1

if [ -z $NAME ]; then
  echo "Vault name must not be empty"
  exit 1
fi

OBSIDIAN_CONFIG_DIR="./$NAME/.obsidian"
OBSIDIAN_BASE_CONFIG_DIR="/home/stephen/.config/obsidian/default-vault-config"

mkdir -p "$OBSIDIAN_CONFIG_DIR/plugins"

ln -sf "$OBSIDIAN_BASE_CONFIG_DIR/themes" "$OBSIDIAN_CONFIG_DIR/"
ln -sf "$OBSIDIAN_BASE_CONFIG_DIR/hotkeys.json" "$OBSIDIAN_CONFIG_DIR/"
ln -sf "$OBSIDIAN_BASE_CONFIG_DIR/appearance.json" "$OBSIDIAN_CONFIG_DIR/"

cp "$OBSIDIAN_BASE_CONFIG_DIR/community-plugins.json" "$OBSIDIAN_CONFIG_DIR/"
for plugin in "$OBSIDIAN_BASE_CONFIG_DIR/plugins/*"; do ln -sf $(realpath "$plugin") -t "$OBSIDIAN_CONFIG_DIR/plugins/" ; done

echo "Created Obsidian Vault in $NAME"
