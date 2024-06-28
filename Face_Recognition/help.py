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


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry ("1530x790+0+0")
        self.root.title("Face Recogniton System")


        title_lbl = Label(self.root,text = "HELP DESK",font = ("times new roman",35,"bold"),bg = "white",fg = "red")
        title_lbl.place(x = 0,y = 0,width=1530,height=45)

        img_top =Image.open("face_recognition/helpi.jpg")
        img_top = img_top.resize((1530,720), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_1b1=Label(self.root, image=self.photoimg_top) 
        f_1b1.place(x=0,y=55,width=1530, height=720)

        dev_label = Label(f_1b1,text = "Email: ",font=("times new roman",20,"bold"),bg = "white")
        dev_label.place(x=550,y=280)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()