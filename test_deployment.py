#!/usr/bin/env python
"""
Test script for the Gesture Flow ML backend deployment.
This script sends a test request to the backend API to verify it's working.
"""

import requests
import base64
import json
import argparse
import os
from PIL import Image
import io

def test_health(url):
    """Test the health endpoint."""
    response = requests.get(f"{url}/health")
    print(f"Health check status code: {response.status_code}")
    if response.status_code == 200:
        print(f"Response: {response.json()}")
        return True
    return False

def test_interpret(url, image_path):
    """Test the interpret endpoint with an image."""
    # Load and encode the image
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    # Prepare the request
    data = {
        "image": encoded_string,
        "source": "test"
    }
    
    # Send the request
    response = requests.post(
        f"{url}/api/interpret",
        headers={"Content-Type": "application/json"},
        data=json.dumps(data)
    )
    
    print(f"Interpret status code: {response.status_code}")
    if response.status_code == 200:
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return True
    else:
        print(f"Error: {response.text}")
        return False

def create_test_image():
    """Create a simple test image if none is provided."""
    # Create a simple image with text
    img = Image.new('RGB', (300, 300), color=(73, 109, 137))
    
    # Save to a temporary file
    img_path = "test_image.jpg"
    img.save(img_path)
    
    print(f"Created test image at {img_path}")
    return img_path

def main():
    parser = argparse.ArgumentParser(description="Test the Gesture Flow ML backend deployment")
    parser.add_argument("--url", default="http://localhost:5000", help="Backend URL")
    parser.add_argument("--image", help="Path to test image")
    
    args = parser.parse_args()
    
    print(f"Testing backend at {args.url}")
    
    # Test health endpoint
    if not test_health(args.url):
        print("Health check failed. Make sure the backend is running.")
        return
    
    # Test interpret endpoint
    image_path = args.image
    if not image_path:
        image_path = create_test_image()
    
    if not os.path.exists(image_path):
        print(f"Error: Image file {image_path} not found")
        return
    
    test_interpret(args.url, image_path)

if __name__ == "__main__":
    main() 