import cv2
import numpy as np
from PIL import Image
import os

def load_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    face_samples = []
    ids = []

    for image_path in image_paths:
        gray_img = Image.open(image_path).convert('L')
        img_arr = np.array(gray_img, 'uint8')
        id = int(os.path.split(image_path)[-1].split(".")[1])
        faces = detect_faces(img_arr)

        for (x, y, w, h) in faces:
            face_samples.append(img_arr[y:y + h, x:x + w])
            ids.append(id)

    return face_samples, ids

def detect_faces(image):
    return detector.detectMultiScale(image, scaleFactor=1.3, minNeighbors=5)

def train_recognizer(faces, ids):
    recognizer = cv2.face.LBPHFaceRecognizer_create(radius=1, neighbors=8, grid_x=8, grid_y=8)
    recognizer.train(faces, np.array(ids))
    recognizer.write('trainer/trainer.yml')

def main():
    print("Training faces. It will take a few seconds. Wait ...")
    faces, ids = load_images_and_labels('samples')

    if not faces:
        print("Error: No faces found for training.")
        return

    try:
        train_recognizer(faces, ids)
        print("Model trained. Now we can recognize your face.")
    except Exception as e:
        print(f"Error during training: {e}")

if __name__ == "__main__":
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    main()
