import cv2


def setup_camera():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Could not open webcam.")
        exit()
    cam.set(3, 640)
    cam.set(4, 480)
    return cam


def detect_faces(image, scaleFactor=1.2, minNeighbors=5, minSize=None):
    return faceCascade.detectMultiScale(image, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=minSize)


def virtual_assistant():
    # Placeholder for your virtual assistant logic
    print("Virtual Assistant Activated!")


def recognize_faces(cam, recognizer, names, faceCascade, font, minW, minH):
    while True:
        ret, img = cam.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detect_faces(converted_image, scaleFactor=1.2, minNeighbors=5,
                             minSize=(int(minW), int(minH)))

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])

            if 0 <= id < len(names):
                recognized_name = names[id]
                accuracy_percent = round(100 - accuracy)
            else:
                recognized_name = "unknown"
                accuracy_percent = round(100 - accuracy)

            cv2.putText(img, recognized_name, (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, f"{accuracy_percent}%", (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

            if accuracy_percent >= 50:
                virtual_assistant()

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break

    print("Thanks for using this program, have a good day.")
    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX

    id = 2
    names = ['', 'divjot']

    cam = setup_camera()

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    recognize_faces(cam, recognizer, names, faceCascade, font, minW, minH)
