from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top image
        # img_path = "images_project/uni 1.jpeg"
        img_path = "img/face_detector1.jpg"
        img_top = Image.open(img_path)
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # Bottom image
        # img_path = "images_project/uni 1.jpeg"
        img_path = "img/face.jpg"
        img_bottom = Image.open(img_path)
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # Button
        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 18, "bold"), bg="red", fg="white")
        b1_1.place(x=365, y=620, width=200, height=60)
        # --------------------


    # # ===== mark attendance =================
    # def mark_attendance(self, id, roll, name, dep):
    #     with open("sheet.csv", "r+", newline="\n") as f:
    #         myDataList = f.readlines()
    #         name_list = []
    #         for line in myDataList:
    #             entry = line.split(",")
    #             name_list.append(entry[0])
    #         if (id not in name_list) and (roll not in name_list) and (name not in name_list) and (dep not in name_list):
    #             now = datetime.now()
    #             d1 = now.strftime("%d/%m/%Y")
    #             dtString = now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{id},{roll},{name},{dep},{dtString},{d1},Present")


    #  
    # def face_recog(self):
    #     recognized_ids = set()  # Track recognized IDs

    #     def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
    #         gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #         features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
    #         coord = []

    #         for (x, y, w, h) in features:
    #             cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
    #             id, predict = clf.predict(gray_image[y:y + h, x:x + w])
    #             confidence = int((100 * (1 - predict / 300)))

    #             if id not in recognized_ids:  # Check if ID has already been recognized
    #                 conn = mysql.connector.connect(
    #                     host="localhost",
    #                     user="root",
    #                     password="00000",
    #                     database="face_recognizer"
    #                 )
    #                 my_cursor = conn.cursor()

    #                 my_cursor.execute("SELECT Name FROM student WHERE Student_id=%s", (str(id),))
    #                 name = my_cursor.fetchone()
    #                 name = ''.join(name) if name else ""

    #                 my_cursor.execute("SELECT Roll FROM student WHERE Student_id=%s", (str(id),))
    #                 roll = my_cursor.fetchone()
    #                 roll = ''.join(roll) if roll else ""

    #                 my_cursor.execute("SELECT Dep FROM student WHERE Student_id=%s", (str(id),))
    #                 dep = my_cursor.fetchone()
    #                 dep = ''.join(dep) if dep else ""

    #                 if confidence > 77:
    #                     cv2.putText(img, f"ID:{id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
    #                     cv2.putText(img, f"Roll:{roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
    #                     cv2.putText(img, f"Name:{name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
    #                     cv2.putText(img, f"Department:{dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
    #                     self.mark_attendance(id, roll, name, dep)
    #                     recognized_ids.add(id)  # Add ID to recognized set
    #                     break  # Break out of the loop once attendance is marked

    #             coord = [x, y, w, h]

    #         return coord

    #     def recognize(img, clf, faceCascade):
    #         coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
    #         return img

    #     faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    #     clf = cv2.face.LBPHFaceRecognizer_create()
    #     clf.read("classifier.xml")

    #     video_cap = cv2.VideoCapture(0)

    #     while True:
    #         ret, img = video_cap.read()
    #         img = recognize(img, clf, faceCascade)
    #         cv2.imshow("Welcome To Face Recognition", img)

    #         if cv2.waitKey(1) == 13 or len(recognized_ids) > 0:  # Stop the loop if Enter key is pressed or attendance marked
    #             break

    #     video_cap.release()
    #     cv2.destroyAllWindows()


# 0
# 000000000000000000000000000000000000000000
     # ===== mark attendance =================
    def mark_attendance(self, id, roll, name, dep):
        with open("sheet.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for lines in myDataList:
                entry = lines.split(",")
                name_list.append(entry[0])
            if ((id not in name_list) and (roll not in name_list) and (name not in name_list) and (dep not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{id},{roll},{name},{dep},{dtString},{d1},Present")
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf, cursor):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            
            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))
                conn = mysql.connector.connect(host="localhost", username="root", password="00000", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select Name from student where Student_id=%s", (str(id),))
                name = my_cursor.fetchone()
                name = "" if name is None else "+".join(map(str, name))
                my_cursor.execute("select Roll from student where Student_id=%s", (str(id),))
                roll = my_cursor.fetchone()
                roll = "" if roll is None else "+".join(map(str, roll))
                my_cursor.execute("select Dep from student where Student_id=%s", (str(id),))
                dep = my_cursor.fetchone()
                dep = "" if dep is None else "+".join(map(str, dep))
                my_cursor.execute("select Student_id from student where Student_id=%s", (str(id),))
                id = my_cursor.fetchone()
                id = "" if id is None else "+".join(map(str, id))
                if confidence > 77:
                    cv2.putText(img, f"ID: {id}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll: {roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(id, roll, name, dep)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, y]
            return coord
        
        def recognize(img, clf, faceCascade, cursor):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf, cursor)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0)
        
        conn = mysql.connector.connect(host="localhost", username="root", password="00000", database="face_recognizer")
        my_cursor = conn.cursor()
        
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade, my_cursor)
            cv2.imshow("Welcome To Face Recognition", img)
            
            if cv2.waitKey(1) == 13:
                break
            
        video_cap.release()
        cv2.destroyAllWindows()

# 00000000000000000000000000

        
    # # ===== mark attendance =================
    # def mark_attendance(self, id, roll, name, dep):
    #     with open("sheet.csv", "r+", newline="\n") as f:
    #         myDataList = f.readlines()
    #         name_list = []
    #         for line in myDataList:
    #             entry = line.split(",")
    #             name_list.append(entry[0])
    #         if (id not in name_list) and (roll not in name_list) and (name not in name_list) and (dep not in name_list):
    #             now = datetime.now()
    #             d1 = now.strftime("%d/%m/%Y")
    #             dtString = now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{id},{roll},{name},{dep},{dtString},{d1},Present")
                
                

    # # ===== face recognition =================
    # def face_recog(self):
    #     def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
    #         gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #         features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
    #         coord = []

    #         for (x, y, w, h) in features:
    #             cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
    #             id, predict = clf.predict(gray_image[y:y + h, x:x + w])
    #             confidence = int((100 * (1 - predict / 300)))

    #             conn = mysql.connector.connect(
    #                 host="localhost",
    #                 user="root",
    #                 password="00000",
    #                 database="face_recognizer"
    #             )
    #             my_cursor = conn.cursor()

    #             my_cursor.execute("SELECT Name FROM student WHERE Student_id=%s", (str(id),))
    #             name = my_cursor.fetchone()
    #             name = ''.join(name) if name else ""

    #             my_cursor.execute("SELECT Roll FROM student WHERE Student_id=%s", (str(id),))
    #             roll = my_cursor.fetchone()
    #             roll = ''.join(roll) if roll else ""

    #             my_cursor.execute("SELECT Dep FROM student WHERE Student_id=%s", (str(id),))
    #             dep = my_cursor.fetchone()
    #             dep = ''.join(dep) if dep else ""

    #             if confidence > 77:
    #                 cv2.putText(img, f"ID:{id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
    #                 cv2.putText(img, f"Roll:{roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
    #                 cv2.putText(img, f"Name:{name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
    #                 cv2.putText(img, f"Department:{dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
    #                 self.mark_attendance(id, roll, name, dep)
    #             else:
    #                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
    #                 cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

    #             coord = [x, y, w, h]

    #         return coord
    
    #     def recognize(img, clf, faceCascade):
    #         coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
    #         return img

    #     faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    #     clf = cv2.face.LBPHFaceRecognizer_create()
    #     clf.read("classifier.xml")

    #     video_cap = cv2.VideoCapture(0)

    #     while True:
    #         ret, img = video_cap.read()
    #         img = recognize(img, clf, faceCascade)
    #         cv2.imshow("Welcome To Face Recognition", img)

    #         if cv2.waitKey(1) == 13:
    #             break

    #     video_cap.release()
    #     cv2.destroyAllWindows()

        
    

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
