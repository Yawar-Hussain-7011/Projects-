from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from time import strftime
from datetime import datetime
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendances import Attendance
from developer import Developer
from help import Help



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")
  
       
        # First image
        img=Image.open("face_recognition/college.jpg")
        img = img.resize((500,130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_1b1=Label (self.root, image=self.photoimg) 
        f_1b1. place(x= 0,y = 0, width=500, height=130)


        #Second image
        img1=Image.open("face_recognition/face_scan.jpg")
        img1 = img1.resize((500,130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_1b1=Label (self.root, image=self.photoimg1) 
        f_1b1. place(x= 500,y = 0, width=500, height=130)


        # Third image
        img2=Image.open("face_recognition/college2.jpg")
        img2 = img2.resize((500,130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_1b1=Label (self.root, image=self.photoimg2) 
        f_1b1. place(x= 1000,y = 0, width=550, height=130)



        #big image
        img3=Image.open("face_recognition/bigimage.png")
        img3 = img3.resize((1530,710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img=Label (self.root, image=self.photoimg3) 
        bg_img.place(x= 0,y = 130, width=1530, height=710)

        title_lbl = Label(bg_img,text = "VISION PULSE SYSTEM SOFTWERE",font = ("times new roman",35,"bold"),bg = "white",fg = "black")
        title_lbl.place(x = 0,y = 0,width=1530,height=45)

        """Time"""
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000,time)
        
        lbl = Label(title_lbl,font = ("times new roman",14,"bold"),bg = "white",fg = "red")
        lbl.place(x = 0,y = 0,width=100,height=50)
        time() 


        #Student button
        img4=Image.open("face_recognition/student.jpg")
        img4 = img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image=self.photoimg4,command=self.student_details,cursor = "hand2")
        b1.place(x = 200,y = 100,width=220,height=220)

        b1_1 = Button(bg_img,text = "Student Details",command=self.student_details,cursor = "hand2",font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x = 200,y = 300,width=220,height=40)


        #Detect face button
        img5=Image.open("face_recognition/face_detect.jpg")
        img5 = img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoimg5,command = self.face_data,cursor = "hand2")
        b1.place(x = 500,y = 100,width=220,height=220)

        b1_1 = Button(bg_img,text = "Face Detector",command = self.face_data,cursor = "hand2",font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x = 500,y = 300,width=220,height=40)


        #Attendance
        img6=Image.open("face_recognition/attendance.jpg")
        img6 = img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image=self.photoimg6,cursor = "hand2",command=self.attendances_data)
        b1.place(x = 800,y = 100,width=220,height=220)

        b1_1 = Button(bg_img,text = "Attendance",cursor = "hand2",command=self.attendances_data,font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x = 800,y = 300,width=220,height=40) 


        # Help
        img7=Image.open("face_recognition/Help.jpg")
        img7 = img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,image=self.photoimg7,cursor = "hand2",command=self.help_data)
        b1.place(x = 1100,y = 100,width=220,height=220)

        b1_1 = Button(bg_img,text = "Help Desk",cursor = "hand2",command=self.help_data,font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x = 1100,y = 300,width=220,height=40)


        # Train
        img8=Image.open("face_recognition/train.jpg")
        img8 = img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,image=self.photoimg8,cursor = "hand2",command = self.train_data)
        b1.place(x = 200,y = 380,width=220,height=220)

        b1_1 = Button(bg_img,text = "Train Data",command = self.train_data,cursor = "hand2",font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x = 200,y = 580,width=220,height=40)


        # Photo
        img9=Image.open("face_recognition/photos.jpg")
        img9 = img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img,image=self.photoimg9,cursor = "hand2",command=self.open_img)
        b1.place(x = 500,y = 380,width=220,height=220)

        b1_1 = Button(bg_img,text = "Photos",cursor = "hand2",command=self.open_img,font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x = 500,y = 580,width=220,height=40)


        # Developer
        img10=Image.open("face_recognition/developer.jpg")
        img10 = img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,image=self.photoimg10,cursor = "hand2",command=self.developer_data)
        b1.place(x = 800,y = 380,width=220,height=220)

        b1_1 = Button(bg_img,text = "Developer",cursor = "hand2",command=self.developer_data,font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x = 800,y = 580,width=220,height=40)


        # Exit
        img11=Image.open("face_recognition/exit.jpg")
        img11 = img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img,image=self.photoimg11,cursor = "hand2",command=self.iExit)
        b1.place(x = 1100,y = 380,width=220,height=220)

        b1_1 = Button(bg_img,text = "Exit",cursor = "hand2",command=self.iExit,font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
        b1_1.place(x = 1100,y = 580,width=220,height=40)

    def open_img(self):
        os.startfile("face_recognition\data")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project", parent = self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

    """Function button"""
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Student(self.new_window)

    """Train Function"""
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    
    """Face Recognition"""
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    """Attendance"""
    def attendances_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    """Developer"""
    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)
    
    """Help Desk"""
    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()