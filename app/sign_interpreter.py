import os
import time
import random
from PIL import Image
import numpy as np

# Mock gestures for demonstration
MOCK_GESTURES = [
    {"label": "Hello", "confidence": 0.92},
    {"label": "Thank you", "confidence": 0.88},
    {"label": "Yes", "confidence": 0.95},
    {"label": "No", "confidence": 0.91},
    {"label": "Please", "confidence": 0.87},
    {"label": "Help", "confidence": 0.89},
    {"label": "Sorry", "confidence": 0.86},
    {"label": "Good", "confidence": 0.93},
    {"label": "Bad", "confidence": 0.85},
    {"label": "Love", "confidence": 0.94}
]

# Mock phrases for demonstration
MOCK_PHRASES = [
    "Hello, how are you?",
    "Thank you for your help",
    "Yes, I understand",
    "No, I don't agree",
    "Please help me",
    "I need assistance",
    "Sorry for the confusion",
    "That's good news",
    "I'm not feeling well",
    "I love this app"
]

def interpret_sign_language(image, source='camera'):
    """
    Mock function to interpret sign language from an image.
    
    In a real implementation, this would use a machine learning model.
    
    Args:
        image: PIL Image object
        source: Source of the image ('camera', 'image', or 'video')
        
    Returns:
        dict: Interpretation results
    """
    # Simulate processing time
    time.sleep(1)
    
    # Generate a unique filename for the image
    timestamp = int(time.time() * 1000)
    filename = f"sign_capture_{timestamp}.jpg"
    
    # In a real implementation, you might save the image for later analysis
    # image.save(os.path.join('uploads', filename))
    
    # Mock detection - in a real implementation, this would use ML
    # Select random gestures (1-3)
    num_gestures = random.randint(1, 3)
    detected_gestures = random.sample(MOCK_GESTURES, num_gestures)
    
    # Select a random phrase
    interpretation_text = random.choice(MOCK_PHRASES)
    
    # Generate a confidence score
    confidence = random.uniform(0.75, 0.98)
    
    # Return the results
    return {
        'text': interpretation_text,
        'confidence': confidence,
        'source': source,
        'detectedGestures': detected_gestures,
        'timestamp': timestamp
    }

def preprocess_image(image):
    """
    Preprocess an image for the sign language model.
    
    Args:
        image: PIL Image object
        
    Returns:
        numpy.ndarray: Preprocessed image
    """
    # Resize to a standard size
    image = image.resize((224, 224))
    
    # Convert to RGB if not already
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Convert to numpy array and normalize
    img_array = np.array(image) / 255.0
    
    return img_array 