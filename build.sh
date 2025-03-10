#!/usr/bin/env bash
# build.sh - Custom build script for Render.com

set -o errexit

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Creating necessary directories..."
mkdir -p app/uploads
mkdir -p app/models

echo "Downloading ML models..."
python download_models.py

echo "Build completed successfully!" 