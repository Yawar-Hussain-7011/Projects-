from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import pymysql
from register import Register
from main import Face_Recognition_System
import random
from time import strftime
from datetime import datetime

# def main():
#     win=Tk()
#     app=Login_Window(win)
#     win.mainloop


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x800+0+0")
        
        """Background"""
        img111=Image.open("face_recognition/back_login.jpg")
        img111 = img111.resize((1530,850),Image.Resampling.LANCZOS)
        self.photoimg111 = ImageTk.PhotoImage(img111)

        bg_lbl=Label(self.root, image=self.photoimg111) 
        bg_lbl.place(x=0,y=0, width=1530, height=850)

        title=Label(text="Welcome to ATTENDANCE SYSTEM Using VisionPulse System",font = ("times new roman",30,"bold"),bg = "white",fg = "red")
        title.place(x=0,y=0,width=1550,height=35)


        frame = Frame(self.root,bg = 'white')
        frame.place(x=610,y=170, width=340,height=450)

        
        """Login Image"""
        img1=Image.open("face_recognition/login.jpeg")
        img1 = img1.resize((100,100), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbl_img1=Label (image=self.photoimg1,bg = 'white',borderwidth=0) 
        lbl_img1.place(x= 730,y = 175, width=100, height=100)

        get_str = Label(frame,text = "Get Started",font = ("times new roman",20,"bold"),bg = "white",fg = "black")
        get_str.place(x = 95,y = 100)

        """label"""
        username=lbl = Label(frame,text = "Username",font = ("times new roman",15,"bold"),bg = "white",fg = "black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font = ("times new roman",15,"bold")) 
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text ="Password",font = ("times new roman",15,"bold"),bg = "white",fg = "black")
        password.place(x=70,y=215)

        self.txtpass=ttk.Entry(frame,font = ("times new roman",15,"bold")) 
        self.txtpass.place(x=40,y=250,width=270)

        """Icon Image"""
        
        img2=Image.open("face_recognition/login.jpeg")
        img2=img2.resize((25,25), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl_img1=Label (image=self.photoimg2,bg = 'black',borderwidth=0) 
        lbl_img1.place(x=650,y=323, width=25,height=25)


        img3=Image.open("face_recognition/paswd.jpg")
        img3 = img3.resize((25,25), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbl_img1=Label (image=self.photoimg3,bg = 'black',borderwidth=0) 
        lbl_img1.place(x=650,y=395, width=25, height=25)
        
        """Login Button"""
        login_button=Button(frame,command=self.login,text ="Login",font = ("times new roman",19,"bold"),bd= 3,relief=RIDGE,bg = "white",fg = "black",activeforeground="white",activebackground="red")
        login_button.place(x=110,y=290,width=120,height=35)

        """Register Button"""
        register_button=Button(frame,text ="New User Register",command=self.register_window,font = ("times new roman",18,"bold"),bd= 3,relief=RIDGE,bg = "white",fg = "black",activeforeground="white",activebackground="red")
        register_button.place(x=15,y=335,width=295)

        """Forget Button"""
        forget_button=Button(frame,text ="Forget Password",command=self.forget_password_window,font = ("times new roman",18,"bold"),bd= 3,relief=RIDGE,bg = "white",fg = "black",activeforeground="white",activebackground="red")
        forget_button.place(x=10,y=390,width=300)
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    
    """Login"""
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get() == "ashu":
            messagebox.showinfo("Success","Welcome")
        else:
            conn=pymysql.connect(host = "localhost",user = "root", password = "Yawar@701",database = "face_recognition" )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()

                                                                            ))
            row=my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("Yes and No","Access Only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app= Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            
            conn.commit()
            conn.close()
    
    """Rest"""
    def reset_password(self):
        if self.combo_security_Q.get() == "Select": 
            messagebox.showerror("Error","Select security question",parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_new_password.get() == "":
            messagebox.showerror("Error","Please enter the new paasword",parent=self.root2)
        else:
            conn=pymysql.connect(host = "localhost",user = "root", password = "Yawar@701",database = "face_recognition" )
            my_cursor = conn.cursor()
            query=("Select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error","=Please enter correct answer",parent=self.root2)
            else:
                query=("Update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been rest,please login ID",parent=self.root2)
                self.root2.destroy()    




    

    
    """Forget Pasword"""
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address and reset password ")
        else:
            conn=pymysql.connect(host = "localhost",user = "root", password = "Yawar@701",database = "face_recognition" )
            my_cursor = conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row == None:
                messagebox.showerror("My Error","=Please enter the valid Username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text ="Forget Password",font = ("times new roman",20,"bold"),bg = "white",fg = "black") 
                l.place(x=0,y=10, relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state = "readonly")
                self.combo_security_Q["values"] = ("Select","Your Birth Place","Your School Name","Your Teacher Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font = ("times new roman",15,"bold"),bg = "white",fg = "black")
                security_A.place(x=50,y=150)
                
                self.txt_security= ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=200)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)
                
                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_new_password.place(x=50,y=250,width=250)
                
                reset_btn=Button(self.root2,text="Rest",command=self.reset_password,font=("times new roman",15,"bold"),bg="red",fg="white")
                reset_btn.place(x=100,y=290)

       







if __name__ == "__main__":
    # main()
    root=Tk()
    app=Login_Window(root)
    root.mainloop()
