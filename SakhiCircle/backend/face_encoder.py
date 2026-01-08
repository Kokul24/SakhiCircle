"""
Face Encoding Module
Processes images to extract face encodings and save them to the database.
"""

import face_recognition
import cv2
import numpy as np
from typing import List, Optional, Dict, Any
from face_db import FaceDatabase

def load_image(image_path: str) -> np.ndarray:
    """
    Load an image from file path.

    Args:
        image_path: Path to the image file.

    Returns:
        Image as numpy array in RGB format.
    """
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Could not load image from {image_path}")
    # Convert BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def extract_face_encoding(image: np.ndarray) -> Optional[np.ndarray]:
    """
    Extract face encoding from an image.

    Args:
        image: Image as numpy array in RGB format.

    Returns:
        128-dimensional face encoding vector, or None if no face detected.
    """
    # Find face locations using HOG model (default, CPU-friendly)
    face_locations = face_recognition.face_locations(image, model="hog")

    if not face_locations:
        print("No face detected in the image")
        return None

    # Assume the first face if multiple are present
    if len(face_locations) > 1:
        print(f"Multiple faces detected ({len(face_locations)}), using the first one")

    # Extract encoding for the first face
    encodings = face_recognition.face_encodings(image, face_locations)

    if encodings:
        return encodings[0]
    else:
        print("Failed to extract encoding from detected face")
        return None

def encode_and_save_face(image_path: str, name: str, metadata: Optional[Dict[str, Any]] = None,
                        db_connection_string: Optional[str] = None) -> bool:
    """
    Process an image, extract face encoding, and save to database.

    Args:
        image_path: Path to the image file.
        name: Name of the person.
        metadata: Additional metadata.
        db_connection_string: MongoDB connection string.

    Returns:
        True if successful, False otherwise.
    """
    try:
        # Load image
        image = load_image(image_path)

        # Extract encoding
        encoding = extract_face_encoding(image)

        if encoding is None:
            return False

        # Save to database
        db = FaceDatabase(connection_string=db_connection_string)
        db.save_face_encoding(name, encoding.tolist(), metadata)
        db.close_connection()

        print(f"Successfully encoded and saved face for {name}")
        return True

    except Exception as e:
        print(f"Error processing image: {e}")
        return False

# Example usage
if __name__ == "__main__":
    # Replace with actual image path and person name
    image_path = "path/to/person_image.jpg"
    person_name = "John Doe"
    metadata = {"age": 30, "department": "Engineering"}

    success = encode_and_save_face(image_path, person_name, metadata)
    if success:
        print("Face encoding saved successfully")
    else:
        print("Failed to save face encoding")