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

known_face_encodings = []
known_face_names = []

known_person1_image = face_recognition.load_image_file("./data/Laukik_D10C_41.jpeg")
known_person2_image = face_recognition.load_image_file("./data/sahil_d10c_37.jpeg")
known_person3_image = face_recognition.load_image_file("./data/sai_D10C_46.jpeg")

known_person1_encoding = face_recognition.face_encodings(known_person1_image)[0]
known_person2_encoding = face_recognition.face_encodings(known_person2_image)[0]
known_person3_encoding = face_recognition.face_encodings(known_person3_image)[0]

known_face_names.append("Laukik")
known_face_names.append("Sahil")
known_face_names.append("Sai")

known_face_encodings.append(known_person1_encoding)
known_face_encodings.append(known_person2_encoding)
known_face_encodings.append(known_person3_encoding)

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

while True:

    ret, frame = cap.read()
    
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame,face_locations)
    
    for(top, right, bottom , left), face_encoding in zip(face_locations,face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
        name= "Unknown"
        
        if True in matches :
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            
            
        cv2.rectangle(frame, (left,top), (right,bottom), (0,0,255),2)
        cv2.putText(frame,name,(left,top-10), cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,255),2)
        
    cv2.imshow("Video", frame)
    
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()