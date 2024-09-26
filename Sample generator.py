import cv2
import os

# Initialize face detector
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Create directory for storing sample images
sample_dir = 'samples'
if not os.path.exists(sample_dir):
    os.makedirs(sample_dir)

# Initialize webcam
webcam = cv2.VideoCapture(1)

# Initialize variables for subject ID and sample count
subject_id = input('Enter subject ID: ')
sample_count = 10

# Loop to capture and save sample images
while True:
    # Read frame from webcam
    ret, frame = webcam.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # For each detected face
    for (x, y, w, h) in faces:
        # Increment sample count
        sample_count += 1

        # Draw rectangle around detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Save the detected face as a sample image
        cv2.imwrite(os.path.join(sample_dir, f'{subject_id}_{sample_count}.jpg'), gray[y:y+h, x:x+w])

    # Display frame with detected faces
    cv2.imshow('Sample Generator', frame)

    # Break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and destroy all windows
webcam.release()
cv2.destroyAllWindows()