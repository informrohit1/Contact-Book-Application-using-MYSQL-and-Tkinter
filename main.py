from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def signup_page():
    root.destroy()
    import signup

def login_page():
    root.destroy()
    import login

root=Tk()


root.geometry('1800x900+50+50')
root.resizable(False,False)
root.title('phonebook.com')
root.iconbitmap("favicon.ico")
root.configure(background="white")
bgimage=ImageTk.PhotoImage(file="mainimage.png")
bgLabel = Label(root,image=bgimage)
bgLabel.place(x=-10,y=0) 

headinglabel = Label(root,text='WELCOME',font=("verdana",25,'bold'),bg='white',fg="blue")
headinglabel.place(x=800,y=20)
headinglabel = Label(root,text='TO',font=("verdana",20,'bold'),bg='white',fg="blue")
headinglabel.place(x=885,y=70)
headinglabel = Label(root,text='Phonebook.com',font=("verdana",25,'bold'),bg='white',fg="blue")
headinglabel.place(x=740,y=110)

infolabel = Label(root,text="Here you can store your contacts with ease and trust me it is 'Secured' ",font=('microsoft Yahei UI Light',12,'bold'),bg='white',fg="blue")
infolabel.place(x=600,y=160)

# infolabel2 = Label(root,text="and trust me it is 'Secured' ",font=('microsoft Yahei UI Light',11,'bold'),bg='white',fg="blue")
# infolabel2.place(x=100,y=165)

loginlabel = Label(root,text="I have an account?",font=('microsoft Yahei UI Light',12,'bold'),bg='white',fg="blue")
loginlabel.place(x=760,y=240)

loginbutton = Button(root,text="Login Here",font=("verdana",12),bd=0,bg="blue",fg="white",activebackground="blue",activeforeground="white",command=login_page)
loginbutton.place(x=760,y=270,width=300)
textlabel = Label(root,text="or",font=("verdana",16,'bold'),bg="white",fg="blue")
textlabel.place(x=895,y=305)

signuplabel = Label(root,text="New User? Create Account",font=('microsoft Yahei UI Light',11,'bold'),bg='white',fg="blue")
signuplabel.place(x=760,y=340)

signupbutton = Button(root,text="Create Account",font=("verdana",12),bd=0,bg="blue",fg="white",activebackground="blue",activeforeground="white",command=signup_page)
signupbutton.place(x=760,y=370,width=300)




root.mainloop()
