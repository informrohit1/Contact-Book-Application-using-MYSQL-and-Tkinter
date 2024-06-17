from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


def forget_password():

    def clear():
        username.delete(0,END)
        newpassword.delete(0,END)
        confirmpassword(0,END)

    def password_enter(event):
        newpassword.config(show='*')

    def confirm_password(event):
        confirmpassword.config(show='*')

    def changepassword():
        if username.get() == '' or newpassword.get() == "" or confirmpassword.get() == '':
            messagebox.showerror('Error',"All fielda are required",parent=root)
        elif newpassword.get() != confirmpassword.get():
            messagebox.showerror('Error',"password and confirm password should be the same , check again",parent=root)
        else:
            try:
                conn = pymysql.connect(host='localhost',user='root',password='Rohit@12')
                mycursor = conn.cursor()
            except:
                messagebox.showerror('Error','Database Connection Error, Try Again after Some time')
                return

            query = 'use userdata'
            mycursor.execute(query)
            query = "Select * from data where username = %s"
            mycursor.execute(query,(username.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error',"Invalid username, Check Again")
                clear()
            else:
                query = "update data set password = %s where username = %s"
                mycursor.execute(query,(newpassword.get(),username.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Password changed successfully, login Again")
                root.destroy()



    root = Toplevel()
    # root.destroy()
    # import forgotpassword
    
    #root = Tk()  # root is object variable and Tkinter class is called
    root.grab_set()
    root.geometry('450x600+800+200')
    root.resizable(False,False)
    root.title('forget password page')
    root.iconbitmap("favicon.ico")
    root.configure(background="white")
    bgimage=ImageTk.PhotoImage(file="mainimage.png")
    bgLabel = Label(root,image=bgimage)
    bgLabel.place(x=-950,y=-100)

    heading = Label(root,text="FORGET PASSWORD",font=('verdana',18,'bold'),fg="blue",bg="white")
    heading.place(x=70,y=10)

    usernamelabel = Label(root,text="Username",font=('microsoft Yahei UI Light',11,"bold"),fg="Blue",bg="white")
    usernamelabel.place(x=70,y=100)

    username= Entry(root,font=('microsoft Yahei UI Light',"11"),bd=0,fg="Blue",bg="white")
    username.place(x=70,y=130,width=300)

    frame=Frame(root,width=300,height=2,bg="blue")
    frame.place(x=70,y=155)


    passwordlabel = Label(root,text="New Password",font=('microsoft Yahei UI Light',11,"bold"),fg="Blue",bg="white")
    passwordlabel.place(x=70,y=175)

    newpassword = Entry(root,font=('microsoft Yahei UI Light',"11"),bd=0,fg="Blue",bg="white")
    newpassword.place(x=70,y=205,width=300)
    newpassword.insert(0,'')

    newpassword.bind('<FocusIn>',password_enter)

    frame=Frame(root,width=300,height=2,bg="blue")
    frame.place(x=70,y=230)


    confirmpasswordlabel = Label(root,text="Confirm Password",font=('microsoft Yahei UI Light',11,"bold"),fg="Blue",bg="white")
    confirmpasswordlabel.place(x=70,y=250)

    confirmpassword= Entry(root,font=('microsoft Yahei UI Light',"11"),bd=0,fg="Blue",bg="white")
    confirmpassword.place(x=70,y=280,width=300)
    confirmpassword.insert(0,'')

    confirmpassword.bind("<FocusIn>",confirm_password)

    frame=Frame(root,width=300,height=2,bg="blue")
    frame.place(x=70,y=305)

    button=Button(root,text="Submit",font=('Microsoft Yahei UI Light','11'),bg="Blue",fg="white",bd=0,activebackground="blue",activeforeground="white",command=changepassword)
    button.place(x=70,y=345,width=300)
    root.mainloop()





def user_Enter(event): # using event variable to avoid error
    if username.get() == "Username":
        username.delete(0,END)

def password_enter(event):
    password.config(show='*')
    if password.get() == "Password":
        password.delete(0,END)

# def hide():
#     open_eye.configure(file="closed_eye.png")
#     password.config(show='*')
#     eyeButton.config(command=show)

# def show():
#     open_eye.config(file="open_eye.png")
#     password.config(show='')
#     eyeButton.config(command=hide)

def clear():
    username.delete(0,END)
    password.delete(0,END)

def signup_page():
    root.destroy()
    import signup


def login_user():
    if username.get() == "" or password.get() == "":
        messagebox.showerror('Error',"All fields are required")
    
    else:
        try:
            conn=pymysql.connect(host="localhost",user="root",password="Rohit@12")
            mycursor = conn.cursor()
        except:
            messagebox.showerror('Error',"Database connection error, try after some time")
            return
        
        query = 'use userdata'
        mycursor.execute(query)
        query = "Select * from data where username = %s and password = %s"
        mycursor.execute(query,(username.get(),password.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error',"Invalid username or password Check Again")
            clear()
        else:
            messagebox.showinfo("Welcome","Login successfully")
            clear()
            root.destroy()
            import contact
            
            
            


root = Tk()  # root is object variable and Tkinter class is called


root.geometry('450x600+800+200')
root.resizable(False,False)
root.title('Login page')
root.iconbitmap("favicon.ico")
root.configure(background="white")
bgimage=ImageTk.PhotoImage(file="mainimage.png")
bgLabel = Label(root,image=bgimage)
bgLabel.place(x=-950,y=-100)  # or we can use bgLabel.place(x=0,y=0) but the zise of dialog box will be fixed and not dynamic

heading = Label(root,text="USER LOGIN",font=('verdana',20,'bold'),bg="white",fg='Blue')
heading.place(x=115,y=20)

username = Entry(root,width=30,font=('microsoft Yahei UI Light',11,'bold'),bd=0,fg="Blue")  
username.place(x=75,y=115)
username.insert(0,'Username')

username.bind('<FocusIn>',user_Enter)

frame1=Frame(root,width=300,height=2,bg="Blue")
frame1.place(x=75,y=140)

password = Entry(root,width=30,font=('microsoft Yahei UI Light',11,'bold'),bd=0,fg="Blue")  
password.place(x=75,y=175)
password.insert(0,'Password')

password.bind('<FocusIn>',password_enter)

frame1=Frame(root,width=300,height=2,bg="Blue")
frame1.place(x=75,y=200)

# open_eye=PhotoImage(file="open_eye.png")
# eyeButton = Button(root,image=open_eye,height=20,width=20,bd=0,activebackground="white",bg="white",cursor="hand2",
#                                         )
# eyeButton.place(x=350,y=175)


forgetButton = Button(root,text="Forget Password?",bd=0,activebackground="white",bg="white",cursor="hand2"
                        ,font=('microsoft Yahei UI Light',11,'bold'),fg="blue",activeforeground="blue",command=forget_password)
forgetButton.place(x=220,y=210)


loginButton = Button(root,text="Login",bd=0,activebackground="blue",font=('microsoft Yahei UI Light',11,'bold'),
                            fg="White",bg="Blue",cursor="hand2",activeforeground="white",command=login_user)
loginButton.place(x=75,y=280,width=300)


signupLabel = Label(root,text="New User?",font=('microsoft Yahei UI Light',10,"bold"),fg='blue',bg='white')
signupLabel.place(x=120,y=360)

signupButton = Button(root,text="Create Account",bd=0,activebackground="white",font=('microsoft Yahei UI Light',11,'bold underline'),
                            fg="blue",bg="white",cursor="hand2",activeforeground="blue",command=signup_page)
signupButton.place(x=205,y=355,width=160)





root.mainloop()