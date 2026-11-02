#!/bin/sh

HOME_DIR=$(getent passwd "$(whoami)" | cut -d: -f6)
exec "$HOME_DIR/.pyenv/shims/python3" "$@"
