import cv2
import numpy as np
import face_recognition
import os
import time
from datetime import datetime, date
import threading
from tkinter import Tk
class FaceRecognitionApp:
    def __init__(self, root):
        self.RECOGNITION_THRESHOLD = 0.4
        self.lastMarkedDate = {}
        self.path = r"C:\Users\91799\Desktop\Pythonic-pioneers\data"
        self.images = []
        self.classNames = []
        self.myList = os.listdir(self.path)

        for cl in self.myList:
            curImg = cv2.imread(f"{self.path}/{cl}")
            self.images.append(curImg)
            self.classNames.append(os.path.splitext(cl)[0])

        self.encodeListKnown = self.findEncodings(self.images)
        print("Encoding Complete")

        self.cap = cv2.VideoCapture(0)
        self.run_face_recognition()

    def findEncodings(self, images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def markAttendanceWithDelay(self, name):
        self.markAttendance(name)
        # Introduce a time delay (e.g., 30 seconds) in a separate thread
        threading.Thread(target=lambda: time.sleep(3500)).start()

    # def markAttendance(self, name):
    #     with open("Attendance.csv", "r+") as f:
    #         myDataList = f.readlines()
    #         nameList = [line.split(",")[0] for line in myDataList]
    #         if name not in nameList:
    #             now = datetime.now()
    #             dtString = now.strftime("%Y-%m-%d,%H:%M:%S")

    #             subject = "";
    #             current_time = datetime.now().time()
    #             # in this section we deal with subject wise attendance 
    #             # for wednesday 
    #             if current_time > 08:00:00  && current_time < 09:00:00 :
    #                 subject = "OS"
    #             elif current_time > 09:00:00  && current_time < 10:00:00 :
    #                 subject = "CN"
    #             elif current_time > 10:00:00  && current_time < 11:00:00 :
    #                 subject = "At"
    #             # Check if the person was already marked today
    #             if name in self.lastMarkedDate and self.lastMarkedDate[name] == date.today():
    #                 print(f"{name} has already been marked today.")
    #             else:
    #                 f.write(f"\n{name},{dtString},{subject}")
    #                 self.lastMarkedDate[name] = date.today()
    #                 print(f"{name} marked for attendance on {date.today()}.")
    def markAttendance(self, name):
        with open("Attendance.csv", "r+") as f:
            myDataList = f.readlines()
            nameList = [line.split(",")[0] for line in myDataList]
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime("%Y-%m-%d,%H:%M:%S")
                day = datetime.today().strftime("%A")
                subject = ""
                current_time = datetime.now().time()
                if (day == "Monday") : 
                    if current_time >= datetime.strptime("08:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("09:30:00", "%H:%M:%S").time():
                        subject = "CN"
                    elif current_time >= datetime.strptime("09:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("10:30:00", "%H:%M:%S").time():
                        subject = "AM-IV"
                    elif current_time >= datetime.strptime("10:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("11:30:00", "%H:%M:%S").time():
                        subject = "OS"
                    elif current_time >= datetime.strptime("11:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("12:30:00", "%H:%M:%S").time():
                        subject = "COA"
                    elif current_time >= datetime.strptime("13:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("14:30:00", "%H:%M:%S").time():
                        subject = "LabOS"
                
                elif (day == "Tuesday") : 
                    if current_time >= datetime.strptime("08:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("09:30:00", "%H:%M:%S").time():
                        subject = "CN"
                    elif current_time >= datetime.strptime("09:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("10:30:00", "%H:%M:%S").time():
                        subject = "AM-IV"
                    elif current_time >= datetime.strptime("10:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("11:30:00", "%H:%M:%S").time():
                        subject = "COA"
                    elif current_time >= datetime.strptime("11:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("12:30:00", "%H:%M:%S").time():
                        subject = "PHY"
                    elif current_time >= datetime.strptime("13:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("15:30:00", "%H:%M:%S").time():
                        subject = "LabOS"
                elif (day == "Wednesday") : 
                    if current_time >= datetime.strptime("08:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("09:30:00", "%H:%M:%S").time():
                        subject = "CN"
                    elif current_time >= datetime.strptime("09:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("10:30:00", "%H:%M:%S").time():
                        subject = "AM-IV"
                    elif current_time >= datetime.strptime("10:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("11:30:00", "%H:%M:%S").time():
                        subject = "OS"
                    elif current_time >= datetime.strptime("11:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("12:30:00", "%H:%M:%S").time():
                        subject = "COA"
                    elif current_time >= datetime.strptime("13:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("15:30:00", "%H:%M:%S").time():
                        subject = "LabPHY"
                elif (day == "Thursday") : 
                    if current_time >= datetime.strptime("08:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("09:30:00", "%H:%M:%S").time():
                        subject = "OS"
                    elif current_time >= datetime.strptime("09:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("10:30:00", "%H:%M:%S").time():
                        subject = "PHY"
                    elif current_time >= datetime.strptime("10:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("11:30:00", "%H:%M:%S").time():
                        subject = "COA"
                    elif current_time >= datetime.strptime("11:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("12:30:00", "%H:%M:%S").time():
                        subject = "AT"
                    elif current_time >= datetime.strptime("13:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("15:30:00", "%H:%M:%S").time():
                        subject = "LabCN"
                        
                elif (day == "Friday") : 
                    if current_time >= datetime.strptime("08:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("09:30:00", "%H:%M:%S").time():
                        subject = "OS"
                    elif current_time >= datetime.strptime("09:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("10:30:00", "%H:%M:%S").time():
                        subject = "AM-IV"
                    elif current_time >= datetime.strptime("10:30:00", "%H:%M:%S").time() and current_time < datetime.strptime("11:30:00", "%H:%M:%S").time():
                        subject = "AT"
                        
                else : 
                    if current_time >= datetime.strptime("10:44:00", "%H:%M:%S").time() and current_time < datetime.strptime("10:45:50", "%H:%M:%S").time():
                        subject = "CN"
                    elif current_time >= datetime.strptime("00:04:00", "%H:%M:%S").time() and current_time < datetime.strptime("00:05:30", "%H:%M:%S").time():
                        subject = "AM-IV"
                    elif current_time >= datetime.strptime("10:00:00", "%H:%M:%S").time() and current_time < datetime.strptime("11:00:00", "%H:%M:%S").time():
                        subject = "OS"
                    elif current_time >= datetime.strptime("10:00:00", "%H:%M:%S").time() and current_time < datetime.strptime("11:00:00", "%H:%M:%S").time():
                        subject = "COA"
                    elif current_time >= datetime.strptime("10:00:00", "%H:%M:%S").time() and current_time < datetime.strptime("11:00:00", "%H:%M:%S").time():
                        subject = "LabOS"
                        
                        
                if name in self.lastMarkedDate and self.lastMarkedDate[name] == date.today():
                    print(f"{name} has already been marked today.")
                else:
                    f.write(f"\n{name},{dtString},{subject}")
                    self.lastMarkedDate[name] = date.today()
                    print(f"{name} marked for attendance on {date.today()}.")

    def run_face_recognition(self):
        while True:
            success, img = self.cap.read()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(self.encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(self.encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex] and min(faceDis) <= self.RECOGNITION_THRESHOLD:
                    name = self.classNames[matchIndex].upper()
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
                    self.markAttendanceWithDelay(name)
                else:
                    name = "Unknown"
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
                    cv2.putText(
                        img,
                        name,
                        (x1 + 6, y2 - 6),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (255, 0, 0),
                        2,
                    )
                    self.markAttendanceWithDelay(name)

                

            cv2.imshow("Webcam", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Break the loop with 'q' key
                break

        # Release the video capture object and close all OpenCV windows
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionApp(root)
    root.mainloop()
    


# import cv2
# import numpy as np
# import os
# import time
# from datetime import datetime, date
# import threading
# from tkinter import Tk
# import dlib
# import face_recognition

# import face_recognition_models
# # from face_recognition_models import face_model
# # from face_recognition_models.facenet import FaceNet
# class FaceRecognitionApp:
#     def __init__(self, root):
#         self.RECOGNITION_THRESHOLD = 0.8
#         self.lastMarkedDate = {}
#         self.path = r"C:\Users\91799\Desktop\Pythonic-pioneers\data"
#         self.images = []
#         self.classNames = []
#         self.myList = os.listdir(self.path)

#         for cl in self.myList:
#             curImg = cv2.imread(f"{self.path}/{cl}")
#             self.images.append(curImg)
#             self.classNames.append(os.path.splitext(cl)[0])

#         # Initialize the model here
#         self.model = face_recognition_models.face_model()
#         self.encodeListKnown = self.findEncodings(self.images)
#         print("Encoding Complete")

#         self.cap = cv2.VideoCapture(0)
#         self.detector = dlib.get_frontal_face_detector()

#         self.run_face_recognition()

#     def findEncodings(self, images):
#         encodeList = []
#         for img in images:
#             img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#             encode = self.model.embed_from_image(img)
#             encodeList.append(encode)
#         return encodeList

#     def markAttendanceWithDelay(self, name):
#         self.markAttendance(name)
#         # Introduce a time delay (e.g., 30 seconds) in a separate thread
#         threading.Thread(target=lambda: time.sleep(3500)).start()

#     def markAttendance(self, name):
#         with open("Attendance.csv", "r+") as f:
#             myDataList = f.readlines()
#             nameList = [line.split(",")[0] for line in myDataList]
#             if name not in nameList:
#                 now = datetime.now()
#                 dtString = now.strftime("%Y-%m-%d,%H:%M:%S")

#                 # Check if the person was already marked today
#                 if name in self.lastMarkedDate and self.lastMarkedDate[name] == date.today():
#                     print(f"{name} has already been marked today.")
#                 else:
#                     f.write(f"\n{name},{dtString}")
#                     self.lastMarkedDate[name] = date.today()
#                     print(f"{name} marked for attendance on {date.today()}.")

#     def run_face_recognition(self):
#         while True:
#             success, img = self.cap.read()
#             imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             facesCurFrame = self.detector(imgGray)

#             for face in facesCurFrame:
#                 x1, y1, w, h = face.left(), face.top(), face.width(), face.height()
#                 x2, y2 = x1 + w, y1 + h
#                 face_img = img[y1:y2, x1:x2]
#                 face_img = cv2.resize(face_img, (96, 96))
#                 face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)

#                 encodeCurFrame = self.model.embed_from_image(face_img)
#                 matches = face_recognition_models.face_distance(self.encodeListKnown, encodeCurFrame)
#                 matchIndex = np.argmin(matches)

#                 if matches[matchIndex] < self.RECOGNITION_THRESHOLD:
#                     name = self.classNames[matchIndex].upper()
#                     cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                     cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#                     cv2.putText(
#                         img,
#                         name,
#                         (x1 + 6, y2 - 6),
#                         cv2.FONT_HERSHEY_COMPLEX,
#                         1,
#                         (255, 255, 255),
#                         2,
#                     )
#                     self.markAttendanceWithDelay(name)
#                 else:
#                     name = "Unknown"
#                     cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
#                     cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
#                     cv2.putText(
#                         img,
#                         name,
#                         (x1 + 6, y2 - 6),
#                         cv2.FONT_HERSHEY_COMPLEX,
#                         1,
#                         (255, 0, 0),
#                         2,
#                     )
#                     self.markAttendanceWithDelay(name)

#             cv2.imshow("Webcam", img)
#             if cv2.waitKey(1) & 0xFF == ord('q'):  # Break the loop with 'q' key
#                 break

#         # Release the video capture object and close all OpenCV windows
#         self.cap.release()
#         cv2.destroyAllWindows()

# if __name__ == "__main__":
#     root = Tk()
#     obj = FaceRecognitionApp(root)
#     root.mainloop()