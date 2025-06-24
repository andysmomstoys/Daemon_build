#!/bin/bash

echo "🔧 Installing dependencies for Linux..."

sudo apt update
sudo apt install -y python3 python3-pip rustc julia ffmpeg portaudio19-dev

pip3 install -r requirements.txt

echo "✅ Daemon environment setup complete on Linux."
