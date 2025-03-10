import os
import logging
import numpy as np
from PIL import Image

# Set up logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Try to import TensorFlow
try:
    import tensorflow as tf
    TENSORFLOW_AVAILABLE = True
    logger.info(f"TensorFlow is available (version: {tf.__version__})")
except ImportError:
    TENSORFLOW_AVAILABLE = False
    logger.error("TensorFlow is not available")

def test_model_loading():
    """Test if the model can be loaded successfully."""
    if not TENSORFLOW_AVAILABLE:
        logger.error("TensorFlow is not available, cannot load model")
        return False
    
    # Path to ML model
    model_dir = os.path.join('app', 'models')
    model_file = 'tensorflow_model.h5'
    model_path = os.path.join(model_dir, model_file)
    
    # Check if model exists
    if not os.path.exists(model_path):
        logger.error(f"Model file not found: {model_path}")
        return False
    
    logger.info(f"Model file found: {model_path}")
    
    # Try to load the model
    try:
        logger.info(f"Loading model from {model_path}...")
        model = tf.keras.models.load_model(model_path)
        logger.info("Model loaded successfully")
        logger.info(f"Model summary: {model.summary()}")
        return model
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        return False

def test_model_prediction(model):
    """Test if the model can make predictions."""
    if model is False:
        logger.error("Model is not loaded, cannot test prediction")
        return False
    
    # Create a test image (black image 224x224)
    test_image = Image.new('RGB', (224, 224), color='black')
    
    # Convert to numpy array and normalize
    img_array = np.array(test_image) / 255.0
    
    # Make a prediction
    try:
        logger.info("Making a test prediction...")
        prediction = model.predict(np.expand_dims(img_array, axis=0))
        logger.info(f"Prediction shape: {prediction.shape}")
        logger.info(f"Prediction result: {prediction}")
        return True
    except Exception as e:
        logger.error(f"Error making prediction: {e}")
        return False

if __name__ == "__main__":
    # Test model loading
    model = test_model_loading()
    if model is not False:
        # Test model prediction
        test_model_prediction(model)
    else:
        logger.error("Model loading failed, skipping prediction test") 