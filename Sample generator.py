import cv2

# Open the webcam
cam = cv2.VideoCapture(0)  # Try using -1 as the index
if not cam.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Set video frame dimensions
cam.set(3, 640)  # Set video FrameWidth
cam.set(4, 480)  # Set video FrameHeight

# Load the Haar Cascade classifier
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
if detector.empty():
    print("Error: CascadeClassifier not loaded.")
    exit()

# Input for face ID
face_id = input("Enter a Numeric user ID here: ")

print("Taking samples, look at the camera....")
count = 0  # Initializing sampling face count

while True:
    # Read frames from the webcam
    ret, img = cam.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Convert the frame to grayscale
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = detector.detectMultiScale(converted_image, 1.3, 5)

    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1

        # Save the face samples
        cv2.imwrite("samples/face." + str(face_id) + '.' + str(count) + ".jpg",
                    converted_image[y:y + h, x:x + w])

        # Display the frame with the rectangle
        cv2.imshow('image', img)

    # Wait for a key press, break if 'ESC' is pressed
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif count >= 10:
        break

# Release the webcam and close all windows
print("Samples taken, closing the program....")
cam.release()
cv2.destroyAllWindows()
