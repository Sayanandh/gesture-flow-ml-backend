# Gesture Flow Backend

This is the backend service for the Gesture Flow application, which provides sign language interpretation via a REST API.

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

## Deployment

### Render.com

1. Create a new Web Service on Render.com
2. Connect your GitHub repository
3. Configure the service:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn run:app`
   - **Environment Variables**: Set as needed

## Future Improvements

- Implement actual sign language recognition using machine learning models
- Add support for video processing
- Implement user authentication
- Add logging and monitoring 