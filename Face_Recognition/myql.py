#Creating a connection
import pymysql
# import mysql.connector


conn= pymysql.connect(
    host = "localhost",
    user = "root",
    password= "Yawar@701",
    database = "face_recognition"
)
if conn:
    print("Connection made")
else:
    print("Error")

# """ Creating a database"""

import pymysql

conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password= "Yawar@701",
    database = "face_recognition"
)

my_cursor = conn.cursor()

# Writing an SQL query for creating a database
sql = "CREATE DATABASE IF NOT EXISTS Face_recognition;"


# Executing SQL command
my_cursor.execute(sql)

# Closing the connection
conn.close()

"""Creating a Table"""

conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "Yawar@701",
    database = "face_recognition"
)

# create cursor
my_cursor = conn.cursor()

# # Writing an SQL query for creating a table
sql = """CREATE TABLE IF NOT EXISTS face_recognition.student_id (
  `Dep` VARCHAR(45) NULL,
  `Course` VARCHAR(45) NULL,
  `Year` VARCHAR(45) NULL,
  `Semester` VARCHAR(45) NULL,
  `id` INT NULL,
  `Name` VARCHAR(45) NULL,
  `Division` VARCHAR(45) NULL,
  `Roll` VARCHAR(45) NULL,
  `Gender` VARCHAR(45) NULL,
  `Dob` VARCHAR(45) NULL,
  `Email` VARCHAR(45) NULL,
  `Phone` VARCHAR(45) NULL,
  `Address` VARCHAR(45) NULL,
  `Teacher` VARCHAR(45) NULL,
  `PhotoSample` VARCHAR(45) NULL);"""

# Executing SQL command
my_cursor.execute(sql)

# Closing the connection
conn.close()


# from tkinter import*
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox
# from time import strftime
# from datetime import datetime
# import mysql.connector
# import cv2
# import os
# import numpy as np
# import pymysql


#=============== FULL WINDOE FRAME ================#
# class Face_Recognition:
#     def _init_(self,root):
#         self.root=root
#         self.root.geometry("1550x800+0+0")
    #     self.root.title("Face Recognition System")

    # # title bar
    #     title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="dark green")
        # title_lbl.place(x=0,y=0,width=1550,height=45)

    # #left image:
        
    #     img_left=Image.open(r"Face Recognition System\face_recognition_left.jpg")
    #     img_left=img_left.resize((650,800),Image.Resampling.LANCZOS)
    #     self.photoimg_left=ImageTk.PhotoImage(img_left)

    #     f_lbl=Label(self.root,image=self.photoimg_left)
    #     f_lbl.place(x=0,y=50,width=650,height=800)

#     # right image:
        
#         img_right=Image.open(r"Face Recognition System\face_recognition_right.jpg")
#         img_right=img_right.resize((950,800),Image.Resampling.LANCZOS)
#         self.photoimg_right=ImageTk.PhotoImage(img_right)

#         f_lbl=Label(self.root,image=self.photoimg_right)
#         f_lbl.place(x=650,y=50,width=950,height=800)


#     # button:
        
#         b1_1=Button(f_lbl,text="FACE RECOGNITION",cursor="hand2",font=("times new roman",20,"bold"),bg="red",fg="black")
#         b1_1.place(x=300,y=600,width=300,height=50)

#   # =============== ATTENDANCE =====================#
    # def mark_attendance(self,i,r,n,d):
    #     with open("attendance.csv","r+",newline="\n") as f:
    #         myDataList=f.readlines()
    #         name_list=[]
    #         for line in myDataList:
    #             entry=line.split((","))       #example: Disha,11,computer,student_id
    #             name_list.append(entry[0])
    #         if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
    #             now=datetime.now()
    #             d1=now.strftime("%D/%M/%Y")
    #             dtString=now.strftime("%H:%M:%S")
                # f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")  


#   # ============= FACE RECOGNITION =========================#
#     def face_recog(self):
#         def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
#             gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#             features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            # coord=[]

            # for (x,y,w,h) in features:
            #     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
            #     id,predict=clf.predict(gray_image[y:y+h,x:x+w])
            #     confidence=int((100*(1-predict/300)))

#                 conn=pymysql.connect(host="localhost",username="root",password="Test@123",database="face_recognition")
#                 my_cursor=conn.cursor()

#                 my_cursor.execute("Select Name from student where Student_id="+str(id))
#                 n=my_cursor.fetchone()
#                 n="+".join(n)

#                 my_cursor.execute("select Roll from student where Student_id="+str(id))
#                 r=my_cursor.fetchone()
#                 r="+".join(r)

#                 my_cursor.execute("select Dep from student where Student_id="+str(id))
#                 d=my_cursor.fetchone()
#                 d="+".join(d)

#                 my_cursor.execute("select Student_id from student where Student_id="+str(id))
#                 i=my_cursor.fetchone()
#                 i="+".join(i)

                # if confidence>77:
                #     cv2.putText(img,f"Student_id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                #     cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                #     cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                #     cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                #     self.mark_attendance(i,r,n,d)
                # else:
                #     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                #     cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

#                 coord=[x,y,w,h]

#             return coord 

        # def recognize(img,clf,faceCascade):
        #     coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
        #     return img

        # faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        # clf=cv2.face.LBPHFaceRecognizer_create()
        # clf.read("classifier.xml")

        # video_cap=cv2.VideoCapture(0)

        # while True:
        #     ret,img=video_cap.read()
        #     img=recognize(img,clf,faceCascade)
        #     cv2.imshow("Welcome To Face Recognition",img)

        #     if cv2.waitkey(1)==13:
        #         break
        #     video_cap.release()
        #     cv2.destroyAllWindow()



# if __name__ =="_main_":
#     root=Tk()
#     obj=Face_Recognition(root)
#     root.mainloop()













# from tkinter import*
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox
# from time import strftime
# from datetime import datetime
# import mysql.connector
# import pymysql
# import cv2
# import os
# import numpy as np


# class Face_Recognition:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry ("1530x790+0+0")
#         self.root.title("face Recogniton System")
        
#         """title bar"""
#         title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="red")
#         title_lbl.place(x=0,y=0,width=1550,height=45)


#         """left image:"""
        
#         img_top=Image.open("face_recognition/FD_image_top.png")
#         img_top=img_top.resize((650,700),Image.Resampling.LANCZOS)
#         self.photoimg_top=ImageTk.PhotoImage(img_top)

#         f_lbl=Label(self.root,image=self.photoimg_top)
#         f_lbl.place(x=0,y=55,width=650,height=700)

#         """bottom image"""

#         img_bottom=Image.open("face_recognition/FD_image_bottom.png")
#         img_bottom=img_bottom.resize((950,700),Image.Resampling.LANCZOS)
#         self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

#         f_lbl=Label(self.root,image=self.photoimg_bottom)
#         f_lbl.place(x=650,y=55,width=950,height=700)

#         """button"""  
#         b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new romen",18,"bold"),bg="red",fg="white")
#         b1_1.place(x=365,y=620,width=200,height=40)      

    #     """ATTENDANCE"""
    # def mark_attendance(self,i,r,n,d):
    #     with open("attendance.csv","r+",newline="\n") as f:
    #         myDataList=f.readlines()
    #         name_list=[]
    #         for line in myDataList:
    #             entry=line.split((","))       
    #             name_list.append(entry[0])
    #         if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
    #             now=datetime.now()
    #             d1=now.strftime("%D/%M/%Y")
    #             dtString=now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present") 

#         """FACE RECOGNITION"""

        # def face_recog(self):
        #     def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
        #         gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #         features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

        #         coord=[]

        #         for (x,y,w,h) in features:
        #             cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        #             id,predict=clf.predict(gray_image[y:y+h,x:x+w])
        #             confidence=int((100*(1-predict/300)))
 
        #             conn = pymysql.connect(host = "localhost",user = "root", password = "Yawar@701",database = "face_recognition" )
        #             my_cursor = conn.cursor()

        #             my_cursor.execute("Select Name from the student where Student_id"+str(id))
        #             n=my_cursor.fetchone()
        #             n="+".join(n)

        #             my_cursor.execute("select Roll from student where Student_id="+str(id))
        #             r=my_cursor.fetchone()
        #             r="+".join(r)

        #             my_cursor.execute("select Dep from student where Student_id="+str(id))
        #             d=my_cursor.fetchone()
        #             d="+".join(d)

        #             my_cursor.execute("select Student_id from student where Student_id="+str(id))
        #             i=my_cursor.fetchone()
        #             i="+".join(i)

        #             if confidence>77:
        #                 cv2.putText(img,f"Student_id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
        #                 cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
        #                 cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
        #                 cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
        #                 self.mark_attendance(i,r,n,d)
        #             else:
        #                 cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
        #                 cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
        #             coord = [x,y,w,y]

        #         return coord
            
            # def recognize(img,clf,faceCascade):
            #     coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            #     return img
            
            # faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            # clf=cv2.face.LBPHFaceRecognizer_create()
            # clf.read("classifier.xml")

            # video_cap=cv2.VideoCapture(0)

            # while True:
            #     ret,img=video_cap.read()
            #     img=recognize(img,clf,faceCascade)
            #     cv2.imshow("Welcome To Face Recognition",img)

            #     if cv2.waitkey(1)==13:
            #         break
            # video_cap.release()
            # cv2.destroyAllWindow()


 


# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_Recognition(root)
#     root.mainloop()








# from tkinter import*
# from tkinter import ttk
# from PIL import Image,ImageTk
# import os
# from student import Student
# from train import Train
# from Face_Recognition.face_rec import Face_Recognition
# from attendances import Attendance



# class Face_Recognition_System:
#     def __init__(self,root):
#         self. root=root
#         self. root. geometry ("1530x790+0+0")
#         self.root. title("face Recogniton System")
  
       
#         # First image
#         img=Image.open("face_recognition/college.jpg")
#         img = img.resize((500,130), Image.Resampling.LANCZOS)
#         self.photoimg = ImageTk.PhotoImage(img)

#         f_1b1=Label (self.root, image=self.photoimg) 
#         f_1b1. place(x= 0,y = 0, width=500, height=130)


#         #Second image
#         img1=Image.open("face_recognition/face_scan.jpg")
#         img1 = img1.resize((500,130), Image.Resampling.LANCZOS)
#         self.photoimg1 = ImageTk.PhotoImage(img1)

#         f_1b1=Label (self.root, image=self.photoimg1) 
#         f_1b1. place(x= 500,y = 0, width=500, height=130)


#         # Third image
#         img2=Image.open("face_recognition/college2.jpg")
#         img2 = img2.resize((500,130), Image.Resampling.LANCZOS)
#         self.photoimg2 = ImageTk.PhotoImage(img2)

#         f_1b1=Label (self.root, image=self.photoimg2) 
#         f_1b1. place(x= 1000,y = 0, width=550, height=130)



#         #big image
#         img3=Image.open("face_recognition/bigimage.png")
#         img3 = img3.resize((1530,710), Image.Resampling.LANCZOS)
#         self.photoimg3 = ImageTk.PhotoImage(img3)

#         bg_img=Label (self.root, image=self.photoimg3) 
#         bg_img.place(x= 0,y = 130, width=1530, height=710)

#         title_lbl = Label(bg_img,text = "FACE_RECOGNITION ATTENDANCE SYSTEM SOFTWERE",font = ("times new roman",35,"bold"),bg = "white",fg = "red")
#         title_lbl.place(x = 0,y = 0,width=1530,height=45)


#         #Student button
#         img4=Image.open("face_recognition/student.jpg")
#         img4 = img4.resize((220,220),Image.Resampling.LANCZOS)
#         self.photoimg4 = ImageTk.PhotoImage(img4)

#         b1 = Button(bg_img,image=self.photoimg4,command=self.student_details,cursor = "hand2")
#         b1.place(x = 200,y = 100,width=220,height=220)

#         b1_1 = Button(bg_img,text = "Student Details",command=self.student_details,cursor = "hand2",font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
#         b1_1.place(x = 200,y = 300,width=220,height=40)


#         #Detect face button
#         img5=Image.open("face_recognition/face_detect.jpg")
#         img5 = img5.resize((220,220),Image.Resampling.LANCZOS)
#         self.photoimg5 = ImageTk.PhotoImage(img5)

#         b1 = Button(bg_img,image=self.photoimg5,command = self.face_data,cursor = "hand2")
#         b1.place(x = 500,y = 100,width=220,height=220)

#         b1_1 = Button(bg_img,text = "Face Detector",command = self.face_data,cursor = "hand2",font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
#         b1_1.place(x = 500,y = 300,width=220,height=40)


#         #Attendance
#         img6=Image.open("face_recognition/attendance.jpg")
#         img6 = img6.resize((220,220),Image.Resampling.LANCZOS)
#         self.photoimg6 = ImageTk.PhotoImage(img6)

#         b1 = Button(bg_img,image=self.photoimg6,cursor = "hand2",command=self.attendances_data)
#         b1.place(x = 800,y = 100,width=220,height=220)

#         b1_1 = Button(bg_img,text = "Attendance",cursor = "hand2",command=self.attendances_data,font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
#         b1_1.place(x = 800,y = 300,width=220,height=40) 


#         # Help
#         img7=Image.open("face_recognition/Help.jpg")
#         img7 = img7.resize((220,220),Image.Resampling.LANCZOS)
#         self.photoimg7 = ImageTk.PhotoImage(img7)

#         b1 = Button(bg_img,image=self.photoimg7,cursor = "hand2")
#         b1.place(x = 1100,y = 100,width=220,height=220)

#         b1_1 = Button(bg_img,text = "Help Desk",cursor = "hand2",font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
#         b1_1.place(x = 1100,y = 300,width=220,height=40)


#         # Train
#         img8=Image.open("face_recognition/train.jpg")
#         img8 = img8.resize((220,220),Image.Resampling.LANCZOS)
#         self.photoimg8 = ImageTk.PhotoImage(img8)

#         b1 = Button(bg_img,image=self.photoimg8,cursor = "hand2",command = self.train_data)
#         b1.place(x = 200,y = 380,width=220,height=220)

#         b1_1 = Button(bg_img,text = "Train Data",command = self.train_data,cursor = "hand2",font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
#         b1_1.place(x = 200,y = 580,width=220,height=40)


#         # Photo
#         img9=Image.open("face_recognition/photos.jpg")
#         img9 = img9.resize((220,220),Image.Resampling.LANCZOS)
#         self.photoimg9 = ImageTk.PhotoImage(img9)

#         b1 = Button(bg_img,image=self.photoimg9,cursor = "hand2",command=self.open_img)
#         b1.place(x = 500,y = 380,width=220,height=220)

#         b1_1 = Button(bg_img,text = "Photos",cursor = "hand2",command=self.open_img,font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
#         b1_1.place(x = 500,y = 580,width=220,height=40)


#         # Developer
#         img10=Image.open("face_recognition/developer.jpg")
#         img10 = img10.resize((220,220),Image.Resampling.LANCZOS)
#         self.photoimg10 = ImageTk.PhotoImage(img10)

#         b1 = Button(bg_img,image=self.photoimg10,cursor = "hand2")
#         b1.place(x = 800,y = 380,width=220,height=220)

#         b1_1 = Button(bg_img,text = "Developer",cursor = "hand2",font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
#         b1_1.place(x = 800,y = 580,width=220,height=40)


#         # Exit
#         img11=Image.open("face_recognition/exit.jpg")
#         img11 = img11.resize((220,220),Image.Resampling.LANCZOS)
#         self.photoimg11 = ImageTk.PhotoImage(img11)

#         b1 = Button(bg_img,image=self.photoimg11,cursor = "hand2")
#         b1.place(x = 1100,y = 380,width=220,height=220)

#         b1_1 = Button(bg_img,text = "Exit",cursor = "hand2",font = ("times new roman",15,"bold"),bg = "darkblue",fg = "white")
#         b1_1.place(x = 1100,y = 580,width=220,height=40)

#     def open_img(self):
#         os.startfile("face_recognition\data")

#     """Function button"""
#     def student_details(self):
#         self.new_window = Toplevel(self.root)
#         self.app=Student(self.new_window)

#     """Train Function"""
#     def train_data(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Train(self.new_window)
    
#     """Face Recognition"""
#     def face_data(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Face_Recognition(self.new_window)

#     """Attendance"""
#     def attendances_data(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Attendance(self.new_window)



# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_Recognition_System(root)
#     root.mainloop()