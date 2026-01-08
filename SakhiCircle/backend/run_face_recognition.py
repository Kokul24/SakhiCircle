"""
Facial Recognition System Runner
Demonstrates how to use the facial recognition modules.
"""

from face_encoder import encode_and_save_face
from face_recognizer import FaceRecognizer
import argparse

def main():
    parser = argparse.ArgumentParser(description="Facial Recognition System")
    parser.add_argument("--mode", choices=["encode", "recognize"], required=True,
                       help="Mode: encode to add faces, recognize to run real-time recognition")
    parser.add_argument("--image", help="Path to image file (required for encode mode)")
    parser.add_argument("--name", help="Name of the person (required for encode mode)")
    # Removed --db-uri since it's now hardcoded

    args = parser.parse_args()

    if args.mode == "encode":
        if not args.image or not args.name:
            print("Error: --image and --name are required for encode mode")
            return

        success = encode_and_save_face(args.image, args.name)
        if success:
            print(f"Successfully encoded and saved face for {args.name}")
        else:
            print("Failed to encode and save face")

    elif args.mode == "recognize":
        try:
            recognizer = FaceRecognizer()
            recognizer.run_recognition_loop()
        except Exception as e:
            print(f"Error running face recognition: {e}")

if __name__ == "__main__":
    main()