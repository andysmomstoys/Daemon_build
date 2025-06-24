#!/bin/bash

echo "🔧 Installing dependencies for macOS..."

# Ensure Homebrew is installed
if ! command -v brew &>/dev/null; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

brew install python3 rust julia ffmpeg portaudio

pip3 install -r requirements.txt

echo "✅ Daemon environment setup complete on macOS."
