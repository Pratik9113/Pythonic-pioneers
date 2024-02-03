import cvzone
import cv2
import os
import pickle
import face_recognition
import numpy as np

cap = cv2.VideoCapture(0)  # Use index 0 for the default camera

# Set predefined capture size
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

background_path = r"C:\Users\91799\Desktop\Pythonic-pioneers\Resources\background.png"
imgBackground = cv2.imread(background_path)

# Import the mode image into a list

# List for mode
folderModePath = r"C:\Users\91799\Desktop\Pythonic-pioneers\Images"
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

print(len(imgModeList))

if imgBackground is None:
    print(f"Failed to load background image: {background_path}")
    exit()

# Load the encoding file
print("Loading encoding file")
file = open("EncodeFile.p", "rb")
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print(studentIds)
print("Loading encoding file ended")

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture frame")
        break

    # Scale of images
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCumFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCumFrame)

    imgBackground[162 : 162 + 480, 55 : 55 + 640] = img
    imgBackground[44 : 44 + 633, 808 : 808 + 414] = imgModeList[1]

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCumFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)
        print("Match index:", matchIndex)

        if matches[matchIndex]:
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            # print("faceLoc:", faceLoc)

            # Adjusted bbox without scaling
            bbox = (55 + x1, 162 + y1, x2 - x1, y2 - y1)
            print("Adjusted bbox:", bbox)

            imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)

    cv2.imshow("Face Attendance", imgBackground)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
