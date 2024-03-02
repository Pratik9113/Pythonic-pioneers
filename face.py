# # import cv2
# # import numpy as np
# # import face_recognition
# # import os
# # from datetime import datetime

# # # from PIL import ImageGrab

# # path = r"C:\Users\91799\Desktop\face reco using firefox\data"
# # images = []
# # classNames = []
# # myList = os.listdir(path)
# # print(myList)
# # for cl in myList:
# #     curImg = cv2.imread(f"{path}/{cl}")
# #     images.append(curImg)
# #     classNames.append(os.path.splitext(cl)[0])
# # print(classNames)


# # def findEncodings(images):
# #     encodeList = []

# #     for img in images:
# #         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# #         encode = face_recognition.face_encodings(img)[0]
# #         encodeList.append(encode)
# #     return encodeList


# # # def markAttendance(name):
# # #     with open("Attendance.csv", "r+") as f:
# # #         myDataList = f.readlines()


# # #         nameList = []
# # #         for line in myDataList:
# # #             entry = line.split(",")
# # #             nameList.append(entry[0])
# # #             if name not in nameList:
# # #                 now = datetime.now()
# # #                 dtString = now.strftime("%H:%M:%S")
# # #                 f.writelines(f"\n{name},{dtString}")
# # def markAttendance(name):
# #     with open("Attendance.csv", "r+") as f:
# #         myDataList = f.readlines()

# #         nameList = [line.split(",")[0] for line in myDataList]
# #         if name not in nameList:
# #             now = datetime.now()
# #             dtString = now.strftime("%H:%M:%S")
# #             f.write(f"\n{name},{dtString}")


# # #### FOR CAPTURING SCREEN RATHER THAN WEBCAM
# # # def captureScreen(bbox=(300,300,690+300,530+300)):
# # #     capScr = np.array(ImageGrab.grab(bbox))
# # #     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
# # #     return capScr

# # encodeListKnown = findEncodings(images)
# # print("Encoding Complete")

# # cap = cv2.VideoCapture(0)

# # while True:
# #     success, img = cap.read()
# #     # img = captureScreen()
# #     imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
# #     imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

# #     facesCurFrame = face_recognition.face_locations(imgS)
# #     encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

# #     for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
# #         matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
# #         faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
# #         # print(faceDis)
# #         matchIndex = np.argmin(faceDis)

# #         if matches[matchIndex]:
# #             name = classNames[matchIndex].upper()
# #             # print(name)
# #             y1, x2, y2, x1 = faceLoc
# #             y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
# #             cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
# #             cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
# #             cv2.putText(
# #                 img,
# #                 name,
# #                 (x1 + 6, y2 - 6),
# #                 cv2.FONT_HERSHEY_COMPLEX,
# #                 1,
# #                 (255, 255, 255),
# #                 2,
# #             )
# #             markAttendance(name)

# #     cv2.imshow("Webcam", img)
# #     cv2.waitKey(1)





# import cv2
# import numpy as np
# import face_recognition
# import os
# import time
# from datetime import datetime
# import threading
# from datetime import datetime, date

# # A dictionary to store the last marked date for each person
# lastMarkedDate = {}
# path = r"C:\Users\91799\Desktop\Pythonic-pioneers\data"
# images = []
# classNames = []
# myList = os.listdir(path)
# print(myList)
# for cl in myList:
#     curImg = cv2.imread(f"{path}/{cl}")
#     images.append(curImg)
#     classNames.append(os.path.splitext(cl)[0])
# print(classNames)

# def findEncodings(images):
#     encodeList = []
#     for img in images:
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encode = face_recognition.face_encodings(img)[0]
#         encodeList.append(encode)
#     return encodeList

# # def markAttendance(name):
# #     with open("Attendance.csv", "r+") as f:
# #         myDataList = f.readlines()
# #         nameList = [line.split(",")[0] for line in myDataList]
# #         if name not in nameList:
# #             now = datetime.now()
# #             dtString = now.strftime("%H:%M:%S")
# #             f.write(f"\n{name},{dtString}")
# # def markAttendance(name):
# #     with open("Attendance.csv", "r+") as f:
# #         myDataList = f.readlines()
# #         nameList = [line.split(",")[0] for line in myDataList]
# #         if name not in nameList:
# #             now = datetime.now()
# #             dtString = now.strftime("%H:%M:%S")
# #             f.write(f"\n{name},{dtString}")
            
# #             # Introduce a time delay (e.g., 30 seconds)
# #             time.sleep(30)

# # encodeListKnown = findEncodings(images)
# # print("Encoding Complete")

# # cap = cv2.VideoCapture(0)


# # def markAttendance(name):
# #     with open("Attendance.csv", "r+") as f:
# #         myDataList = f.readlines()
# #         nameList = [line.split(",")[0] for line in myDataList]
# #         if name not in nameList:
# #             now = datetime.now()
# #             dtString = now.strftime("%H:%M:%S")
# #             f.write(f"\n{name},{dtString}")

# # def markAttendanceWithDelay(name):
# #     markAttendance(name)
# #     # Introduce a time delay (e.g., 30 seconds) in a separate thread
# #     threading.Thread(target=lambda: time.sleep(30)).start()

# def markAttendance(name):
#     with open("Attendance.csv", "r+") as f:
#         myDataList = f.readlines()
#         nameList = [line.split(",")[0] for line in myDataList]
#         if name not in nameList:
#             now = datetime.now()
#             dtString = now.strftime("%H:%M:%S")
            
#             # Check if the person was already marked today
#             if name in lastMarkedDate and lastMarkedDate[name] == date.today():
#                 print(f"{name} has already been marked today.")
#             else:
#                 f.write(f"\n{name},{dtString}")
#                 lastMarkedDate[name] = date.today()
#                 print(f"{name} marked for attendance on {date.today()}.")
                
# def markAttendanceWithDelay(name):
#     markAttendance(name)
#     # Introduce a time delay (e.g., 30 seconds) in a separate thread
#     threading.Thread(target=lambda: time.sleep(30)).start()

# encodeListKnown = findEncodings(images)
# print("Encoding Complete")

# cap = cv2.VideoCapture(0)

# # while True:
# #     success, img = cap.read()
# #     imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
# #     imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

# #     facesCurFrame = face_recognition.face_locations(imgS)
# #     encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

# #     for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
# #         matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
# #         faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
# #         matchIndex = np.argmin(faceDis)

# #         if matches[matchIndex]:
# #             name = classNames[matchIndex].upper()
# #         else:
# #             name = "Unknown Face"

# #         y1, x2, y2, x1 = faceLoc
# #         y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
# #         cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
# #         cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
# #         cv2.putText(
# #             img,
# #             name,
# #             (x1 + 6, y2 - 6),
# #             cv2.FONT_HERSHEY_COMPLEX,
# #             1,
# #             (255, 255, 255),
# #             2,
# #         )
# #         if name != "Unknown Face":
# #             markAttendance(name)

# #     cv2.imshow("Webcam", img)
# #     cv2.waitKey(1)

# RECOGNITION_THRESHOLD = 0.6
# while True:
#     success, img = cap.read()
#     imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#     imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

#     facesCurFrame = face_recognition.face_locations(imgS)
#     encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

#     for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
#         matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
#         faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        
#         # if faceDis.size > 0:  # Ensures there's at least one face encoding to compare
#         #     matchIndex = np.argmin(faceDis)

#         #     if matches[matchIndex]:
#         #         name = classNames[matchIndex].upper()  # Recognized face
#         #     else:
#         #         name = "Unknown Face"  # Face is detected but not recognized
#         # else:
#         #     name = "Unknown Face"  # No face encodings, treat as unknown
#         if matches and min(faceDis) <= RECOGNITION_THRESHOLD:
#             matchIndex = np.argmin(faceDis)
#             name = classNames[matchIndex].upper()
#         else:
#             name = "Unknown Face"

#         y1, x2, y2, x1 = faceLoc
#         y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#         cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#         cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#         cv2.putText(
#             img,
#             name,
#             (x1 + 6, y2 - 6),
#             cv2.FONT_HERSHEY_COMPLEX,
#             1,
#             (255, 255, 255),
#             2,
#         )
#         if name != "Unknown Face":
#             markAttendanceWithDelay(name)  # Use the modified function if you want the delay

#     cv2.imshow("Webcam", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):  # Break the loop with 'q' key
#         break

# # Release the video capture object and close all OpenCV windows
# cap.release()
# cv2.destroyAllWindows()



import cv2
import numpy as np
import face_recognition
import os
import time
from datetime import datetime
import threading
from datetime import datetime, date
RECOGNITION_THRESHOLD = 0.8
# A dictionary to store the last marked date for each person
lastMarkedDate = {}
path = r"C:\Users\91799\Desktop\Pythonic-pioneers\data"
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f"{path}/{cl}")
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendanceWithDelay(name):
    markAttendance(name)
    # Introduce a time delay (e.g., 30 seconds) in a separate thread
    threading.Thread(target=lambda: time.sleep(30)).start()

def markAttendance(name):
    with open("Attendance.csv", "r+") as f:
        myDataList = f.readlines()
        nameList = [line.split("_")[0] for line in myDataList]
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime("%H:%M:%S")

            # Check if the person was already marked today
            if name in lastMarkedDate and lastMarkedDate[name] == date.today():
                print(f"{name} has already been marked today.")
            else:
                f.write(f"\n{name},{dtString}")
                lastMarkedDate[name] = date.today()
                print(f"{name} marked for attendance on {date.today()}.")

encodeListKnown = findEncodings(images)
print("Encoding Complete")

cap = cv2.VideoCapture(0)

# while True:
#     success, img = cap.read()
#     imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#     imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

#     facesCurFrame = face_recognition.face_locations(imgS)
#     encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

#     for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
#         matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
#         faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        
#         if matches and min(faceDis) <= RECOGNITION_THRESHOLD:
#             matchIndex = np.argmin(faceDis)
#             name = classNames[matchIndex].upper()
#         else:
#             name = "Unknown"

#         y1, x2, y2, x1 = faceLoc
#         y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#         cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#         cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#         cv2.putText(
#             img,
#             name,
#             (x1 + 6, y2 - 6),
#             cv2.FONT_HERSHEY_COMPLEX,
#             1,
#             (255, 255, 255),
#             2,
#         )
#         if name != "Unknown":
#             markAttendanceWithDelay(name)
#         else :
#             markAttendanceWithDelay("Unknown")
#     cv2.imshow("Webcam", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):  # Break the loop with 'q' key
#         break

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    unknownEncodings = []
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(
                img,
                name,
                (x1 + 6, y2 - 6),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (255, 255, 255),
                2,
            )
            markAttendance(name)
        else : 
            name = "Unknown"
            markAttendance(name)

    cv2.imshow("Webcam", img)
    cv2.waitKey(1)

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
