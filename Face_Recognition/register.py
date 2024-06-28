from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import pymysql


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x800+0+0")

        """Variables"""
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_password=StringVar()
        self.var_password=StringVar()
        self.var_confirm_password=StringVar()

        """Background Image"""
        img=Image.open("face_recognition/regis_back.webp")
        img = img.resize((1530,710), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        lbl_bg=Label (self.root,image=self.photoimg) 
        lbl_bg.place(x= 0,y = 0, relwidth=1,relheight=1)

        """Left Image"""
        img_left=Image.open("face_recognition/regis_here.jpg")
        img_left = img_left.resize((470,550), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_1b1=Label(self.root,image=self.photoimg_left) 
        f_1b1.place(x=80,y=100, width=470, height=550)
        
        """Main Frame"""
        frame = Frame(self.root,bg='white')
        frame.place(x=550,y=100, width=800,height=550)

        register_lbl = Label(frame,text = "REGISTER HERE",font = ("times new roman",22,"bold"),bg = "white",fg = "black")
        register_lbl.place(x=20,y=20)

        """Label and Entry"""
        
        """Row1"""
        fname = Label(frame,text = "First Name",font = ("times new roman",15,"bold"),bg = "white",fg = "black")
        fname.place(x=50,y=100)

        fname_entry= ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text = "Last Name",font = ("times new roman",15,"bold"),bg = "white",fg = "black")
        l_name.place(x=370,y=100)

        l_name_entry= ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        l_name_entry.place(x=370,y=130,width=250)
        # self.txt_lname=ttk.Entry(frame,font=("times new roman",15))
        # self.txt_lname.place(x=370,y=130,width=250)


        """Row2"""
        contact=Label(frame,text = "Contact No.",font = ("times new roman",15,"bold"),bg = "white",fg = "black")
        contact.place(x=50,y=170)
        
        contact_entry= ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        contact_entry.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font = ("times new roman",15,"bold"),bg = "white",fg = "black")
        email.place(x=370,y=170)
        
        email_entry= ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        email_entry.place(x=370,y=200,width=250)


        """Row3"""
        security_Q=Label(frame,text = "Select Security Question",font = ("times new roman",15,"bold"),bg = "white",fg = "black")
        security_Q.place(x=50,y=240)

        combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state = "readonly")
        combo_security_Q["values"] = ("Select","Your Birth Place","Your School Name","Your Teacher Name")
        combo_security_Q.place(x=50,y=270,width=250)
        combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font = ("times new roman",15,"bold"),bg = "white",fg = "black")
        security_A.place(x=370,y=240)
        
        security_A_entry= ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        security_A_entry.place(x=370,y=270,width=250)

        """Row4"""
        password=Label(frame,text = "Password",font = ("times new roman",15,"bold"),bg = "white",fg = "black")
        password.place(x=50,y=310)
        
        password_entry= ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15,"bold"))
        password_entry.place(x=50,y=340,width=250)

        confirm_password = Label(frame,text="Email",font = ("times new roman",15,"bold"),bg = "white",fg = "black")
        confirm_password.place(x=370,y=310)
        
        confirm_password_entry= ttk.Entry(frame,textvariable=self.var_confirm_password,font=("times new roman",15,"bold"))
        confirm_password_entry.place(x=370,y=340,width=250)
  
        """Check Button"""
        self.var_check=IntVar()
        check_btn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font = ("times new roman",15,"bold"),onvalue=1,offvalue=0)
        check_btn.place(x=50,y=390)

        """Register Button"""
        img2=Image.open("face_recognition/regis_btn.png")
        img2=img2.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 = Button(frame,image=self.photoimg2,command=self.register_data,borderwidth=0,cursor="hand2",font = ("times new roman",15,"bold"),fg = "white")
        b1.place(x=10,y=440,width=200)

        """Login Button"""
        img4=Image.open("face_recognition/login_btn.png")
        img4=img4.resize((200,45),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1 = Button(frame,image=self.photoimg4,command=self.return_login,borderwidth=0,cursor="hand2",font = ("times new roman",15,"bold"),fg = "white")
        b1.place(x=330,y=440,width=200)

    """Fuction Declartion"""
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All field are required")
        elif self.var_password.get()!=self.var_confirm_password.get():
            messagebox.showerror("Error","Confirm Password not be same ")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Agree our term condition")
        else:
            conn=pymysql.connect(host = "localhost",user = "root", password = "Yawar@701",database = "face_recognition" )
            my_cursor = conn.cursor()
            query= ("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("INSERT INTO register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_password.get()
 
                                                                                     ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")


    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()