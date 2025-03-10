#!/usr/bin/env python
"""
Script to download ML models during deployment.
This can be used to fetch models from cloud storage or other sources.
"""

import os
import sys
import logging
import requests
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Model information
MODEL_DIR = os.path.join(os.path.dirname(__file__), 'app', 'models')
MODEL_URLS = {
    'tensorflow_model.h5': os.environ.get('MODEL_URL', 'https://drive.google.com/file/d/1JSJVe7OVJdtE1NfgF3t5Q1Iltfi7MItO/view?usp=sharing')
}

def download_model(url, filename):
    """Download a model file from a URL."""
    try:
        logger.info(f"Downloading model from {url} to {filename}")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        logger.info(f"Successfully downloaded {filename}")
        return True
    except Exception as e:
        logger.error(f"Error downloading model: {e}")
        return False

def main():
    """Main function to download all models."""
    # Create model directory if it doesn't exist
    Path(MODEL_DIR).mkdir(parents=True, exist_ok=True)
    
    success = True
    for model_name, model_url in MODEL_URLS.items():
        model_path = os.path.join(MODEL_DIR, model_name)
        
        # Skip if model already exists
        if os.path.exists(model_path):
            logger.info(f"Model {model_name} already exists, skipping download")
            continue
        
        # Download the model
        if not download_model(model_url, model_path):
            success = False
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main()) 