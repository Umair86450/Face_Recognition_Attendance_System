
#install tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class Developer:
	
	def __init__(self, root):
		self.root = root
		self.root.geometry("1530x790+0+0")
		self.root.title("Face Recognition System")


		title=Label(self.root,text="Developer",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
		title.place(x=0,y=0,width=1530,height=45)
		
		 # Top Image
		# img_top=Image.open("images_project/uni 1.jpeg")
		img_path = "img/dev.jpg"
		img_top = Image.open(img_path)
		img_top=img_top.resize((1530,720),Image.LANCZOS)
		self.photoimg_top=ImageTk.PhotoImage(img_top)

		lab1=Label(self.root,image=self.photoimg_top)
		lab1.place(x=0,y=55,width=1530,height=720)

		#  Frame
		main_frame=Frame(lab1,bd=2,bg="white")
		main_frame.place(x=1000,y=0,width=500,height=600)
  
        
  
        
        
		img_main2=Image.open("images_project/Developer.jpeg")
		img_main2=img_main2.resize((200,200),Image.LANCZOS)
		self.photoimg_main2=ImageTk.PhotoImage(img_main2)

		img_main_lbl=Label(main_frame,image=self.photoimg_main2)
		img_main_lbl.place(x=300,y=0,width=200,height=200)

		info_lab=Label(main_frame,text="------------ Personal Info -----------",font=("times new roman",15,"bold"),bg="white",fg="red")
		info_lab.place(x=0,y=5) #width=300,height=20

		info1_lab=Label(main_frame,text="Name: Muhammad Umair",font=("times new roman",15,"bold"),bg="white",fg="blue")
		info1_lab.place(x=0,y=45) #width=300,height=20

		info2_lab=Label(main_frame,text="Sex: Male",font=("times new roman",15,"bold"),bg="white",fg="blue")
		info2_lab.place(x=0,y=90) #width=300,height=20

		info3_lab=Label(main_frame,text="Year:  4th",font=("times new roman",15,"bold"),bg="white",fg="blue")
		info3_lab.place(x=0,y=135) #width=300,height=20

		info4_lab=Label(main_frame,text="Branch: BAghdad",font=("times new roman",15,"bold"),bg="white",fg="blue")
		info4_lab.place(x=0,y=170) #width=300,height=20
  
		img_main3=Image.open("images_project/Developer.jpeg")
		img_main3=img_main3.resize((500,400),Image.LANCZOS)
		self.photoimg_main3=ImageTk.PhotoImage(img_main3)

		img_main_lbl=Label(main_frame,image=self.photoimg_main3)
		img_main_lbl.place(x=0,y=200,width=500,height=400)

		
		
if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
