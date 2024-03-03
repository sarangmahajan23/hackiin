import cv2
import csv
from datetime import datetime
import time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
recognizer = cv2.face.FisherFaceRecognizer_create()
recognizer.read("fisher.xml")

f = open('labels.csv','r')
reader = csv.reader(f)
labels = {int(row[0]): row[1] for row in list(reader)}

print(labels)
marked = {}

def setup_attendance_file():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    f = open(current_date + '_attendance.csv', 'a+', newline='')
    lnwriter = csv.writer(f)
    return f, lnwriter

def initialize_attendance():
    return {label: False for label in labels.values()}

def mark_attendance(name, attendance, lnwriter):
    if name not in marked:    
        attendance[name] = True
        current_time = datetime.now().strftime("%H:%M:%S")
        lnwriter.writerow([name, current_time])
        marked.update({name:1})

def detect_and_mark_attendance(frame, attendance, lnwriter):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray,(800,400))
        id_, confidence = recognizer.predict(roi_gray)
        print(confidence)
        
        if confidence >7000:
            print(labels[id_])
            name = labels[id_]
            mark_attendance(name, attendance, lnwriter)

            color = (255, 0, 0)
            thickness = 2
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness)
            cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, thickness)

    return frame

def main():
    video_capture = cv2.VideoCapture(0)
    f, lnwriter = setup_attendance_file()
    attendance = initialize_attendance()

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        marked_frame = detect_and_mark_attendance(frame, attendance, lnwriter)
        cv2.imshow('Face Recognition Attendance System', marked_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    for name, present in attendance.items():
        if present:
            mark_attendance(name, attendance, lnwriter)

    video_capture.release()
    cv2.destroyAllWindows()
    f.close()

if __name__ == "__main__":
    time.sleep(7)
    main()