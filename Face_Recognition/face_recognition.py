from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import pymysql
import cv2 
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry ("1530x790+0+0")
        self.root.title("face Recogniton System")


        """title bar"""
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1550,height=45)


        """left image:"""
        
        img_top=Image.open("face_recognition/FD_image_top.png")
        img_top=img_top.resize((650,700),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)

        """bottom image"""

        img_bottom=Image.open("face_recognition/FD_image_bottom.png")
        img_bottom=img_bottom.resize((950,700),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)

        """button"""  
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",
                    font=("times new romen",18,"bold"),bg="Red",fg="white")
        b1_1.place(x=365,y=620,width=200,height=40)
       
        """ATTENDANCE"""
    def mark_attendance(self,i,r, n, d):
        with open("Face_Recognition/attendance.csv", "a") as f:
            now = datetime.now()
            date = now.strftime("%d/%m/%Y")
            time = now.strftime("%H:%M:%S")
            f.write(f"{d}, {i}, {n}, {r}, {date}, {time}, Present\n")
    
    """FACE RECOGNITION"""
    def face_recog(self):    
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            
            
            coord=[]

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                id, predict = clf.predict(gray_image[y:y + h ,x:x + w])
                confidence = int((100*(1-predict/300)))
                
                
                conn=mysql.connector.connect(host = "localhost",user = "root", password = "Yawar@701",
                                             database = "face_recognition" )
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Dep FROM student WHERE Student_id = " +str(id))
                d=my_cursor.fetchone()
                
                print("Department:", d)
                d = my_cursor.fetchone()
                


                my_cursor.execute("SELECT Student_id FROM student WHERE Student_id = " +str(id))
                i=my_cursor.fetchone()
                print("Student ID:", i)
                i = my_cursor.fetchone()
                
            
                my_cursor.execute("SELECT Name FROM student WHERE Student_id = " +str(id))
                n=my_cursor.fetchone()
                print("Name:", n)
                n = my_cursor.fetchone()

                my_cursor.execute("SELECT Roll FROM student WHERE Student_id = " +str(id))
                r=my_cursor.fetchone()
                print("Roll:", r)
                r = my_cursor.fetchone()

                


        
                if confidence > 77:
                    cv2.putText(img,f"Department:{d}",(x, y - 5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Student_id:{i}",(x, y - 75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x, y - 30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x, y - 55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img,(x , y),(x + w ,y + h),(0, 0, 255), 3)
                    cv2.putText(img,"Unknown Face",(x , y - 5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255), 3)
                
                coord = [x, y, w, y]

            return coord
              
            
        def recognize(img, clf, faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255), "Face", clf)
            return img
            
        face_cascade=cv2.CascadeClassifier("Face_Recognition/haarcascade_frontalface_default.xml")
        clf=cv2.face_LBPHFaceRecognizer.create()
        clf.read("Face_Recognition/classifier.xml")

        video_capture = cv2.VideoCapture(0)

        while True:
            ret, img = video_capture.read()
            frame = recognize(img, clf, face_cascade)
            cv2.imshow("Welcome To Face Recognition", img)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
          
        video_capture.release()
        cv2.destroyAllWindows()
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()








