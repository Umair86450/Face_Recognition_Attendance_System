from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np 

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System") 

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new toman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x= 0, y=0, width=1530, height=45)

        #            --------top image-------------
        # Load and resize image 
        # img_path = "images_project/uni 1.jpeg"
        img_path = "img/facialrecognition.png"
        img_top = Image.open(img_path)
        img_top = img_top.resize((1530, 325), Image.LANCZOS)  # Use Image.LANCZOS as an alternative of Image.ANTIALIAS

        # Keep a reference to the PhotoImage object 
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # Create a label to display the image
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        # ----------------Button----------
        b1_1 = Button(self.root, text="TRAIN DATA",command= self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="red", fg="white" )
        b1_1.place(x=0, y=380, width=1530, height=60)




        #            --------bottom image-------------
        # Load and resize image 
        # img_path = "images_project/face detector.jpeg"
        img_path = "img/clg.jpg"
        img_bottom = Image.open(img_path)
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)  # Use Image.LANCZOS as an alternative of Image.ANTIALIAS

        # Keep a reference to the PhotoImage object 
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        # Create a label to display the image
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)

    
    # def train_classifier(self):
    #     data_dir = ("data")
    #     path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]


    #     faces = []
    #     ids = []
    #     for image in path:
    #         img = Image.open(image).convert('L')   #  Gray scale image
    #         imageNp = np.array(img,'uint8')
    #         id = int(os.path.split(image)[1].split('.')[1])

    #         # C:\Users\Hp\Desktop\face recognition system\data\user.3.1.jpg
    #         # 0                                                 1

    #         faces.append(imageNp)
    #         ids.append(id)
    #         cv2.imshow("Training", imageNp)
    #         cv2.waitKey(1)  == 13
    #     ids = np.array(ids)

    #     # ============Train classifier and save======================
    #     clf = cv2.face.LBPHFaceRecognizer_create()
    #     clf.train(faces, ids)
    #     clf.write("classifier.xml")
    #     cv2.destroyAllWindows()
    #     messagebox.showinfo("Result", " Training datassets completed")    
                                                          
    # def train_classifier(self):
    #     data_dir = "data"
    #     path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

    #     faces = []
    #     ids = []
    #     for image in path:
    #         img = Image.open(image).convert('L')   # Gray scale image
    #         imageNp = np.array(img,'uint8')
    #         id = int(os.path.split(image)[1].split('.')[1])
    #         faces.append(imageNp)
    #         ids.append(id)
    #         cv2.imshow("Training", imageNp)
    #         cv2.waitKey(1)
    #     ids = np.array(ids)

    #     # Train classifier and save
    #     clf = cv2.face.LBPHFaceRecognizer_create()
        
    #     clf.train(faces, ids)
    #     clf.write("classifier.xml")
    #     cv2.destroyAllWindows()
    #     messagebox.showinfo("Result", "Training dataset completed")
    
    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
    
        faces = []
        ids = []
    
        for image in path:
            img = Image.open(image).convert('L')  # Gray scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
    
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)
    
        ids = np.array(ids)
    
        # TRAIN THEN SAVE
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Log-Detect: Training", "Training datasets completed!!")
    






if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
