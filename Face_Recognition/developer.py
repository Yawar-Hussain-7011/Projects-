from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import pymysql
import cv2
import os
import csv
from tkinter import filedialog


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry ("1530x790+0+0")
        self.root.title("Face Recogniton System")


        title_lbl = Label(self.root,text = "DEVELOPER",font = ("times new roman",35,"bold"),bg = "white",fg = "red")
        title_lbl.place(x = 0,y = 0,width=1530,height=45)

        img_top =Image.open("face_recognition/devep.jpg")
        img_top = img_top.resize((1530,720), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_1b1=Label(self.root, image=self.photoimg_top) 
        f_1b1.place(x=0,y=55,width=1530, height=720)

        """Frame"""
        main_frame = Frame(f_1b1,bd=2,bg= "white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1 =Image.open("face_recognition/devep.jpg")
        img_top1 = img_top1.resize((200,200), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_1b1=Label(main_frame, image=self.photoimg_top1) 
        f_1b1.place(x=300,y=0,width=200, height=200)

        """Developer"""
        dev_label = Label(main_frame,text = "Hello Students",font=("times new roman",20,"bold"),bg = "white")
        dev_label.place(x=0,y=5)

        dev_label = Label(main_frame,text = "My Name Vision",font=("times new roman",20,"bold"),bg = "white")
        dev_label.place(x = 0, y = 40)

        dev_label = Label(main_frame,text = "Pulse System",font=("times new roman",20,"bold"),bg = "white")
        dev_label.place(x = 0, y = 80)

        dev_label = Label(main_frame,text = "To Detect face and",font=("times new roman",20,"bold"),bg = "white")
        dev_label.place(x = 0, y = 120)

        dev_label = Label(main_frame,text = "Mark Attendance",font=("times new roman",20,"bold"),bg = "white")
        dev_label.place(x = 0, y = 160)


        img2 =Image.open("face_recognition/take.jpeg")
        img2 = img2.resize((500,390), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_1b1=Label(main_frame, image=self.photoimg2) 
        f_1b1.place(x=0,y=210,width=500, height=390)





















if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()