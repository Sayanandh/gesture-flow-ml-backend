# Gesture Flow Backend - ML Sign Language Interpreter

This is the backend service for the Gesture Flow application, which provides sign language interpretation via a REST API using machine learning.

## Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository
2. Navigate to the backend directory
3. Create a virtual environment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
5. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

> **Note on Dependencies**: The requirements.txt file specifies numpy==1.24.3 to ensure compatibility between tensorflow-cpu and scikit-learn. If you update any ML libraries, make sure to check for potential version conflicts.

### Running Locally

1. Make sure your virtual environment is activated
2. Run the Flask application:
   ```
   python run.py
   ```
3. The API will be available at `http://localhost:5000`

## API Endpoints

### Health Check
- **URL**: `/health`
- **Method**: `GET`
- **Response**: JSON with status and timestamp

### Interpret Image
- **URL**: `/api/interpret`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "image": "base64_encoded_image_data",
    "source": "camera" // or "image" or "video"
  }
  ```
- **Response**: JSON with interpretation results

### Interpret Video
- **URL**: `/api/interpret/video`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "video": "base64_encoded_video_data"
  }
  ```
- **Response**: JSON with interpretation results

### Interpret Live Camera Feed
- **URL**: `/api/interpret/live`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "image": "base64_encoded_image_data",
    "frame_number": 123
  }
  ```
- **Response**: JSON with interpretation results

## Deployment to Render.com

### Step 1: Create a GitHub Repository
1. Create a new GitHub repository
2. Push your backend code to the repository

### Step 2: Sign Up for Render.com
1. Go to [Render.com](https://render.com/) and sign up for an account
2. Verify your email address

### Step 3: Create a New Web Service
1. From your Render dashboard, click "New" and select "Web Service"
2. Connect your GitHub repository
3. Select the repository containing your backend code

### Step 4: Configure the Web Service
1. Give your service a name (e.g., "gesture-flow-ml-backend")
2. Set the Environment to "Python 3"
3. Set the Build Command to: `./build.sh`
4. Set the Start Command to: `gunicorn run:app`
5. Select an appropriate plan (Free tier is fine for starting)
6. Under "Advanced" settings, add the following environment variables:
   - `FLASK_APP=run.py`
   - `FLASK_ENV=production`
   - `FLASK_DEBUG=0`

### Step 5: Deploy
1. Click "Create Web Service"
2. Wait for the deployment to complete (this may take a few minutes)
3. Once deployed, Render will provide you with a URL for your service (e.g., `https://gesture-flow-ml-backend.onrender.com`)

### Troubleshooting Deployment Issues

If you encounter dependency conflicts during deployment:

1. **Check numpy version**: Make sure numpy version is compatible with both TensorFlow and scikit-learn
2. **Simplify dependencies**: If you're not using all ML libraries, remove unnecessary ones
3. **Check logs**: In the Render dashboard, check the build logs for specific errors
4. **Use a custom build script**: The provided `build.sh` script helps handle dependency installation

### Step 6: Update Your Flutter App
1. Update the backend URL in your Flutter app to point to your Render.com service URL
2. Test the connection to ensure everything is working properly

## ML Model Information

The backend currently uses a mock implementation for demonstration purposes. To implement actual ML models:

1. Place your trained models in the `app/models` directory
2. Update the `sign_interpreter.py` file to use your models
3. Redeploy the service

## Future Improvements

- Implement actual sign language recognition using machine learning models
- Add support for video processing with frame extraction
- Implement user authentication
- Add logging and monitoring
- Optimize performance with caching and async processing 