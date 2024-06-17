from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def password_enter(event):
    password.config(show='*')
    # if password.get() == "":
    #     password.delete(0,END)

def confirm_password(event):
    repassword.config(show='*')
    # if repassword.get() == "":
    #     repassword.delete(0,END)

def clear():
    email.delete(0,END)
    user.delete(0,END)
    password.delete(0,END)
    repassword.delete(0,END)

def loginpage():
    root.destroy()
    import login

def connectdatabase():
    if email.get() == '' or user.get() == '' or password.get() == '' or repassword.get() == '' :
        messagebox.showerror('Error',"All fields are required")
    elif password.get() != repassword.get():
        messagebox.showerror('Error', "Passwords Mismatched, Check again !")
    elif len(user.get()) >20:
        messagebox.showerror('Error', "Username should not exceed 20 characters")
    else:
        try:
            conn=pymysql.connect(host="localhost",user="root",password="Rohit@12")
            mycursor = conn.cursor()
        except:
            messagebox.showerror('Error', "Database Connectivity Issue, Try again after Some time")
            return

        try:
            query = 'CREATE DATABASE userdata'
            mycursor.execute(query)
            query = 'USE userdata'
            mycursor.execute(query)
            query = 'CREATE TABLE data(id INTEGER PRIMARY KEY AUTO_INCREMENT, email VARCHAR(255) NOT NULL, username VARCHAR(20) NOT NULL,password VARCHAR(20) NOT NULL)'
            mycursor.execute(query)
        except:
            mycursor.execute('USE userdata') # using contactsuser in case of database is creared already    

        query = 'select * from data where username=%s'
        mycursor.execute(query,(user.get()))

        row = mycursor.fetchone() # it fetch that row where same username exists if username is the same then it will throw error 
        if row != None:
            messagebox.error("error","Username Already exists, use another username")
        
        else:
            query = 'insert into data(email, username, password) VALUES(%s, %s, %s)'
            mycursor.execute(query,(email.get(),user.get(),password.get()))
            conn.commit() # as we are commiting changes here as well.
            conn.close()
            messagebox.showinfo('success',"Account is Successfully Created")
            clear()
            root.destroy()
            import login
        

root=Tk()

root.geometry('450x600+800+200')
root.resizable(False,False)
root.title('Signup page')
root.iconbitmap("favicon.ico")
root.configure(background="white")
bgimage=ImageTk.PhotoImage(file="mainimage.png")
bgLabel = Label(root,image=bgimage)
bgLabel.place(x=-1000,y=-30)  


heading = Label(root,text="CREATE ACCOUNT",font=('verdana',20,'bold'),bg="white",fg='Blue')
heading.grid(row=0,column=0,padx=70,pady=10)

emailLabel = Label(root,text="Email",font=('microsoft Yahei UI Light',11,"bold"),fg='blue',bg='white')
emailLabel.place(x=72,y=80)

email = Entry(root,width=30,font=('microsoft Yahei UI Light',11),bd=0,fg="Blue")
email.place(x=75,y=110,width=300)
frame1=Frame(root,width=300,height=2,bg="Blue")
frame1.place(x=75,y=135)

userLabel = Label(root,text="Username",font=('microsoft Yahei UI Light',11,"bold"),fg='blue',bg='white')
userLabel.place(x=72,y=150)

user = Entry(root,width=30,font=('microsoft Yahei UI Light',11),bd=0,fg="Blue")
user.place(x=75,y=180,width=300)
frame1=Frame(root,width=300,height=2,bg="Blue")
frame1.place(x=75,y=205)

passwordLabel = Label(root,text="Password",font=('microsoft Yahei UI Light',11,"bold"),fg='blue',bg='white')
passwordLabel.place(x=72,y=220)

password = Entry(root,width=30,font=('microsoft Yahei UI Light',11),bd=0,fg="Blue")
password.place(x=75,y=250,width=300)
password.insert(0,'')

password.bind('<FocusIn>',password_enter)
frame1=Frame(root,width=300,height=2,bg="Blue")
frame1.place(x=75,y=275)

repasswordLabel = Label(root,text="Confirm Password",font=('microsoft Yahei UI Light',11,"bold"),fg='blue',bg='white')
repasswordLabel.place(x=72,y=290)

repassword = Entry(root,width=30,font=('microsoft Yahei UI Light',11),bd=0,fg="Blue")
repassword.place(x=75,y=320,width=300)
repassword.insert(0,'')

repassword.bind('<FocusIn>',confirm_password)

frame1=Frame(root,width=300,height=2,bg="Blue")
frame1.place(x=75,y=345)

signupButton = Button(root,text="SignUp",bd=0,activebackground="blue",font=('microsoft Yahei UI Light',11,'bold'),
                            fg="White",bg="Blue",cursor="hand2",activeforeground="white",command=connectdatabase)
signupButton.place(x=75,y=380,width=300)

loginLabel = Label(root,text="Already have an account?",font=('verdana',10),fg='blue',bg='white')
loginLabel.place(x=95,y=445)
loginButton = Button(root,text="login",bd=0,activebackground="white",font=('microsoft Yahei UI Light',11,'bold underline'),
                            fg="blue",bg="white",cursor="hand2",activeforeground="blue",command=loginpage)
loginButton.place(x=290,y=440)



root.mainloop()