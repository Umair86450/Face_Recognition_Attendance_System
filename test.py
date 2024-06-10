# from tkinter import *
# from tkinter import ttk, messagebox, filedialog
# from PIL import Image, ImageTk
# import mysql.connector
# import os
# import csv

# mydata = []

# class Attendance:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x710+0+0")
#         self.root.title("Face Recognition System")

#         # Variable Initialization
#         self.var_atten_id = StringVar()
#         self.var_atten_roll = StringVar()
#         self.var_atten_name = StringVar()
#         self.var_atten_dep = StringVar()
#         self.var_atten_time = StringVar()
#         self.var_atten_date = StringVar()
#         self.var_atten_attendance = StringVar()

#         # Load and resize the first image
#         img_path1 = "images_project/face detector.jpeg"
#         img1 = Image.open(img_path1).resize((800, 200), Image.LANCZOS)
#         self.photoimg1 = ImageTk.PhotoImage(img1)

#         # Load and resize the second image
#         img_path2 = "images_project/face detector.jpeg"
#         img2 = Image.open(img_path2).resize((800, 200), Image.LANCZOS)
#         self.photoimg2 = ImageTk.PhotoImage(img2)

#         # Load the background image
#         bg_img = Image.open("images_project/background.jpeg").resize((1530, 710), Image.LANCZOS)
#         self.photoimg_bg = ImageTk.PhotoImage(bg_img)

#         # Create labels to display images
#         f_lbl1 = Label(self.root, image=self.photoimg1)
#         f_lbl1.place(x=0, y=0, width=800, height=200)
#         f_lbl2 = Label(self.root, image=self.photoimg2)
#         f_lbl2.place(x=800, y=0, width=800, height=200)
#         bg_lab = Label(self.root, image=self.photoimg_bg)
#         bg_lab.place(x=0, y=200, width=1530, height=710)

#         # Title
#         title = Label(bg_lab, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="green")
#         title.place(x=0, y=0, width=1530, height=45)

#         # Main frame
#         main_frame = Frame(bg_lab, bd=2)
#         main_frame.place(x=20, y=55, width=1480, height=600)

#         # Left frame
#         left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
#         left_frame.place(x=10, y=10, width=730, height=580)

#         # Left label frame image
#         img_path_left = "images_project/uni 1.jpeg"
#         img_left = Image.open(img_path_left).resize((720, 150), Image.LANCZOS)
#         self.photoimg_left = ImageTk.PhotoImage(img_left)
#         lab2 = Label(left_frame, image=self.photoimg_left)
#         lab2.place(x=5, y=0, width=720, height=150)

#         left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
#         left_inside_frame.place(x=0, y=135, width=720, height=400)

#         # Label and Entry Widgets
#         labels = ["AttendanceID:", "Roll:", "Name:", "Department:", "Time:", "Date:"]
#         entry_vars = [self.var_atten_id, self.var_atten_roll, self.var_atten_name, self.var_atten_dep, self.var_atten_time, self.var_atten_date]

#         for i, label_text in enumerate(labels):
#             label = Label(left_inside_frame, text=label_text, font=("times new roman", 13, "bold"), bg="white")
#             label.grid(row=i, column=0, padx=10, pady=5, sticky=W)
#             entry = ttk.Entry(left_inside_frame, textvariable=entry_vars[i], font=("times new roman", 13, "bold"))
#             entry.grid(row=i, column=1 if i % 2 == 0 else 3, padx=10, pady=5, sticky=W)

#         # Attendance Status
#         attendance_label = Label(left_inside_frame, text="Attendance Status", bg="white", font=("times new roman", 11, "bold"))
#         attendance_label.grid(row=3, column=2, pady=8)
#         self.atten_status = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendance, width=22, font=("times new roman", 11, "bold"), state="readonly")
#         self.atten_status["values"] = ("Status", "Present", "Absent")
#         self.atten_status.grid(row=3, column=3, pady=8)
#         self.atten_status.current(0)

#         # Button Frame
#         btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
#         btn_frame.place(x=0, y=300, width=715, height=35)

#         btn_texts = ["Import csv", "Export csv", "Update", "Reset"]
#         btn_commands = [self.import_csv, self.export_csv, self.update_data, self.reset_data]

#         for i, (text, command) in enumerate(zip(btn_texts, btn_commands)):
#             btn = Button(btn_frame, text=text, command=command, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
#             btn.grid(row=0, column=i)

#         # Right frame
#         right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
#         right_frame.place(x=750, y=10, width=720, height=580)

#         table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
#         table_frame.place(x=5, y=5, width=700, height=455)

#         # Scroll bar table
#         scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
#         scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

#         self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
#         scroll_x.pack(side=BOTTOM, fill=X)
#         scroll_y.pack(side=RIGHT, fill=Y)
#         scroll_x.config(command=self.AttendanceReportTable.xview)
#         scroll_y.config(command=self.AttendanceReportTable.yview)

#         self.AttendanceReportTable.heading("id", text="Attendance ID")
#         self.AttendanceReportTable.heading("roll", text="Roll")
#         self.AttendanceReportTable.heading("name", text="Name")
#         self.AttendanceReportTable.heading("department", text="Department")
#         self.AttendanceReportTable.heading("time", text="Time")
#         self.AttendanceReportTable.heading("date", text="Date")
#         self.AttendanceReportTable.heading("attendance", text="Attendance")

#         self.AttendanceReportTable["show"] = "headings"
        
#         for col in ("id", "roll", "name", "department", "time", "date", "attendance"):
#             self.AttendanceReportTable.column(col, width=100)

#         self.AttendanceReportTable.pack(fill=BOTH, expand=1)
#         self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

#     # Import CSV
#     def import_csv(self):
#         global mydata
#         mydata.clear()
#         fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
#         with open(fln) as myfile:
#             csvread = csv.reader(myfile, delimiter=",")
#             for i in csvread:
#                 mydata.append(i)
#             self.fetch_data(mydata)

#     # Export CSV
#     def export_csv(self):
#         try:
#             if len(mydata) < 1:
#                 messagebox.showerror("No Data", "No Data Found.", parent=self.root)
#                 return False
#             fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
#             with open(fln, mode="w", newline="") as myfile:
#                 exp_write = csv.writer(myfile, delimiter=",")
#                 for i in mydata:
#                     exp_write.writerow(i)
#                 messagebox.showinfo("Data Export", "Your data exported to " + os.path.basename(fln) + " successfully")
#         except Exception as ex:
#             messagebox.showerror("Error", f"Due to :{str(ex)}", parent=self.root)

#     # Update Data
#     def update_data(self):
#         if self.var_atten_id.get() == "":
#             messagebox.showerror("Error", "Please enter attendance id", parent=self.root)
#         else:
#             try:
#                 Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
#                 if Update > 0:
#                     conn = mysql.connector.connect(host="localhost", username="root", password="00000", database="face_recognizer") 
#                     my_cursor = conn.cursor()
#                     my_cursor.execute("update student set roll=%s, name=%s, department=%s, time=%s, date=%s, attendance=%s where id=%s", (
#                         self.var_atten_roll.get(),
#                         self.var_atten_name.get(),
#                         self.var_atten_dep.get(),
#                         self.var_atten_time.get(),
#                         self.var_atten_date.get(),
#                         self.var_atten_attendance.get(),
#                         self.var_atten_id.get()
#                     ))
#                 else:
#                     if not Update:
#                         return
#                 messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
#                 conn.commit()
#                 self.fetch_data()
#                 conn.close()
#             except Exception as es:
#                 messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

#     # Get Cursor
#     def get_cursor(self, event=""):
#         cursor_focus = self.AttendanceReportTable.focus()
#         content = self.AttendanceReportTable.item(cursor_focus)
#         data = content["values"]

#         self.var_atten_id.set(data[0])
#         self.var_atten_roll.set(data[1])
#         self.var_atten_name.set(data[2])
#         self.var_atten_dep.set(data[3])
#         self.var_atten_time.set(data[4])
#         self.var_atten_date.set(data[5])
#         self.var_atten_attendance.set(data[6])

#     # Reset Data
#     def reset_data(self):
#         self.var_atten_id.set("")
#         self.var_atten_roll.set("")
#         self.var_atten_name.set("")
#         self.var_atten_dep.set("")
#         self.var_atten_time.set("")
#         self.var_atten_date.set("")
#         self.var_atten_attendance.set("Status")

#     # Fetch Data
#     def fetch_data(self, rows=None):
#         if rows is None:
#             rows = []
#         self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
#         for row in rows:
#             self.AttendanceReportTable.insert("", END, values=row)

# if __name__ == "__main__":
#     root = Tk()
#     obj = Attendance(root)
#     root.mainloopimport os
from tkinter import *
import tkinter
import os
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendance
from developer import Developer
from help import Help


class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Load images
        self.images = {}
        self.load_images()

        # Set up the interface
        self.setup_interface()

    def load_images(self):
        image_paths = {
            "university": "images_project/university.jpeg",
            "face_recognition": "images_project/face recognition.jpeg",
            "uni1": "images_project/uni 1.jpeg",
            "background": "images_project/background.jpeg",
            "student": "images_project/student.jpeg",
            "face_detector": "images_project/face detector.jpeg",
            "attendance": "images_project/attendence.jpeg",
            "help_desk": "images_project/help desk.jpeg",
            "train_data": "images_project/trian data.jpeg",
            "photos": "images_project/photos.jpeg",
            "developer": "images_project/Developer.jpeg",
            "exit": "images_project/exit.jpeg"
        }

        for key, path in image_paths.items():
            try:
                img = Image.open(path)
                if key == "background":
                    img = img.resize((1530, 710), Image.LANCZOS)
                else:
                    img = img.resize((220, 220), Image.LANCZOS)
                self.images[key] = ImageTk.PhotoImage(img)
            except Exception as e:
                print(f"Error loading image {path}: {e}")

    def setup_interface(self):
        # First row images
        self.create_image_label("university", 0, 0, 510, 130)
        self.create_image_label("face_recognition", 500, 0, 510, 130)
        self.create_image_label("uni1", 1000, 0, 510, 130)

        # Background image
        bg_img = Label(self.root, image=self.images["background"])
        bg_img.place(x=0, y=130, width=1530, height=710)

        # Title
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Time
        lbl_time = Label(title_lbl, font=("times new roman", 14, "bold"), bg="white", fg="green")
        lbl_time.place(x=0, y=0, width=110, height=50)
        self.update_time(lbl_time)

        # Buttons
        buttons = [
            ("student", "Student Details", self.student_detail, 200, 100),
            ("face_detector", "Face Detector", self.face_data, 500, 100),
            ("attendance", "Attendance", self.attendance_data, 800, 100),
            ("help_desk", "Help Desk", self.help_data, 1100, 100),
            ("train_data", "Train Data", self.train_data, 200, 380),
            ("photos", "Photos", self.open_img, 500, 380),
            ("developer", "Developer", self.developer_data, 800, 380),
            ("exit", "Exit", self.iExit, 1100, 380)
        ]

        for img_key, text, command, x, y in buttons:
            self.create_button(bg_img, img_key, text, command, x, y)

    def create_image_label(self, img_key, x, y, width, height):
        lbl = Label(self.root, image=self.images[img_key])
        lbl.place(x=x, y=y, width=width, height=height)

    def create_button(self, parent, img_key, text, command, x, y):
        b = Button(parent, image=self.images[img_key], cursor="hand2", command=command)
        b.place(x=x, y=y, width=220, height=220)
        b_text = Button(parent, text=text, cursor="hand2", command=command, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b_text.place(x=x, y=y + 200, width=220, height=40)

    def update_time(self, lbl):
        string = strftime("%H:%M:%S %p")
        lbl.config(text=string)
        lbl.after(1000, self.update_time, lbl)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        iExit = messagebox.askyesno("Face Recognition", "Are you sure you want to exit?", parent=self.root)
        if iExit > 0:
            self.root.destroy()

    # Function buttons
    def student_detail(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()

