# 
#install tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Help:
	
	def __init__(self, root):
		self.root = root
		self.root.geometry("1530x790+0+0")
		self.root.title("Face Recognition System")


		title=Label(self.root,text="HELLP DESK",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
		title.place(x=0,y=0,width=1530,height=45)
		
		 # Top Image
		img_top=Image.open("images_project/help.jpeg")
		img_top=img_top.resize((1530,720),Image.LANCZOS)
		self.photoimg_top=ImageTk.PhotoImage(img_top)

		lab1=Label(self.root,image=self.photoimg_top)
		lab1.place(x=0,y=55,width=1530,height=720)
  
		
		info_lab=Label(lab1,text="dfsdlakfhls@gmail.com",font=("times new roman",20,"bold"),bg="white",fg="blue")
		info_lab.place(x=610,y=160) #width=300,height=20
  
  
  
          
		
if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()