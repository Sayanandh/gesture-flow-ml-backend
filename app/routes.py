import os
import time
import base64
import json
from io import BytesIO
from flask import Blueprint, request, jsonify
from PIL import Image
import numpy as np

from app.sign_interpreter import interpret_sign_language

main_bp = Blueprint('main', __name__)

@main_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify the API is running."""
    return jsonify({
        'status': 'healthy',
        'timestamp': time.time()
    })

@main_bp.route('/api/interpret', methods=['POST'])
def interpret_image():
    """
    Endpoint to interpret sign language from an image.
    
    Expects a JSON with:
    - image: base64 encoded image
    - source: 'camera', 'image', or 'video'
    """
    if not request.json or 'image' not in request.json:
        return jsonify({'error': 'No image provided'}), 400
    
    try:
        # Get the image data
        image_data = request.json.get('image')
        source = request.json.get('source', 'camera')
        
        # Remove the data:image/jpeg;base64, prefix if present
        if ',' in image_data:
            image_data = image_data.split(',')[1]
        
        # Decode the base64 image
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes))
        
        # Save the image for debugging (optional)
        timestamp = int(time.time() * 1000)
        filename = f"sign_capture_{timestamp}.jpg"
        image_path = os.path.join('app/uploads', filename)
        image.save(image_path)
        
        # Process the image
        result = interpret_sign_language(image, source)
        
        # Add the image path to the result
        result['imagePath'] = filename
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/interpret/video', methods=['POST'])
def interpret_video():
    """
    Endpoint to interpret sign language from a video.
    
    Expects a JSON with:
    - video: base64 encoded video or video URL
    """
    if not request.json or 'video' not in request.json:
        return jsonify({'error': 'No video provided'}), 400
    
    try:
        # Get the video data
        video_data = request.json.get('video')
        
        # Remove the data:video/mp4;base64, prefix if present
        if ',' in video_data:
            video_data = video_data.split(',')[1]
        
        # Decode the base64 video
        video_bytes = base64.b64decode(video_data)
        
        # Save the video for processing
        timestamp = int(time.time() * 1000)
        filename = f"sign_video_{timestamp}.mp4"
        video_path = os.path.join('app/uploads', filename)
        
        with open(video_path, 'wb') as f:
            f.write(video_bytes)
        
        # In a real implementation, we would extract frames from the video
        # and process each frame, then combine the results
        
        # For now, we'll use a mock implementation that returns random results
        # In a real implementation, you would use a video processing library like OpenCV
        
        # Mock processing - extract a frame from the middle of the video
        # This would be replaced with actual video processing
        
        # For the mock implementation, we'll just return a random result
        result = {
            'text': 'Video interpretation is not fully implemented yet',
            'confidence': 0.85,
            'source': 'video',
            'detectedGestures': [
                {"label": "Hello", "confidence": 0.92},
                {"label": "Thank you", "confidence": 0.88}
            ],
            'timestamp': timestamp,
            'videoPath': filename
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/interpret/live', methods=['POST'])
def interpret_live():
    """
    Endpoint to interpret sign language from a live camera feed.
    
    Expects a JSON with:
    - image: base64 encoded image frame
    - frame_number: sequential frame number for tracking
    """
    if not request.json or 'image' not in request.json:
        return jsonify({'error': 'No image provided'}), 400
    
    try:
        # Get the image data
        image_data = request.json.get('image')
        frame_number = request.json.get('frame_number', 0)
        
        # Remove the data:image/jpeg;base64, prefix if present
        if ',' in image_data:
            image_data = image_data.split(',')[1]
        
        # Decode the base64 image
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes))
        
        # Process the image
        result = interpret_sign_language(image, 'camera')
        
        # Add frame number to the result
        result['frame_number'] = frame_number
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500 