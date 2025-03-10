import os
import logging
import numpy as np
from PIL import Image
from app.sign_interpreter import load_ml_model, preprocess_image

# Set up logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_model_loading():
    """Test if the model can be loaded successfully."""
    logger.info("Testing model loading...")
    result = load_ml_model()
    logger.info(f"Model loaded successfully: {result}")
    return result

def test_model_prediction():
    """Test if the model can make predictions."""
    from app.sign_interpreter import ml_model, is_model_loaded
    
    if not is_model_loaded or ml_model is None:
        logger.error("Model is not loaded, cannot test prediction")
        return False
    
    # Create a test image (black image 224x224)
    test_image = Image.new('RGB', (224, 224), color='black')
    
    # Preprocess the image
    processed_image = preprocess_image(test_image)
    
    # Make a prediction
    try:
        logger.info("Making a test prediction...")
        prediction = ml_model.predict(np.expand_dims(processed_image, axis=0))
        logger.info(f"Prediction shape: {prediction.shape}")
        logger.info(f"Prediction result: {prediction}")
        return True
    except Exception as e:
        logger.error(f"Error making prediction: {e}")
        return False

if __name__ == "__main__":
    # Test model loading
    if test_model_loading():
        # Test model prediction
        test_model_prediction()
    else:
        logger.error("Model loading failed, skipping prediction test") 