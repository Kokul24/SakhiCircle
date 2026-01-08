# Facial Recognition System

This module provides a complete facial recognition system using OpenCV, face_recognition (dlib-based), and MongoDB.

## Features

- **Database Integration**: Store face encodings in MongoDB with metadata
- **Face Encoding**: Extract 128-dimensional face encodings from images
- **Real-time Recognition**: Webcam-based face recognition with live video feed
- **HOG Model**: Uses CPU-friendly HOG model for face detection
- **Error Handling**: Robust error handling for missing faces and connection issues

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure MongoDB is running locally or provide Atlas connection string.

## Usage

### Adding Faces to Database

Use the encoder to add faces:

```python
from face_encoder import encode_and_save_face

# Encode and save a face
success = encode_and_save_face(
    image_path="path/to/person.jpg",
    name="John Doe",
    metadata={"age": 30, "department": "Engineering"}
)
```

Or use the command-line runner:

```bash
python run_face_recognition.py --mode encode --image path/to/person.jpg --name "John Doe"
```

### Real-time Face Recognition

Run the recognition system:

```python
from face_recognizer import FaceRecognizer

recognizer = FaceRecognizer()
recognizer.run_recognition_loop()
```

Or use the command-line runner:

```bash
python run_face_recognition.py --mode recognize
```

Press 'q' to quit the recognition loop.

## Configuration

### MongoDB Connection

The system is configured to use the same MongoDB Atlas connection as the main Sakhi-Score application. No additional configuration is needed.

### Recognition Parameters

- **Tolerance**: Default 0.6 (lower values = stricter matching)
- **Model**: HOG (CPU-friendly) vs CNN (GPU-accelerated, more accurate)

## Modules

- `face_db.py`: Database connection and operations
- `face_encoder.py`: Face encoding extraction and storage
- `face_recognizer.py`: Real-time face recognition
- `run_face_recognition.py`: Command-line interface

## Error Handling

- Checks for face detection in images
- Handles database connection failures
- Webcam access validation
- Graceful shutdown on errors

## Performance Notes

- HOG model provides good balance of speed and accuracy on CPU
- For better accuracy, consider using CNN model (requires GPU)
- Face encodings are loaded into memory for fast comparison
- Real-time performance depends on hardware and number of known faces