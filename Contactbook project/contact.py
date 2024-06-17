from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
from tkinter import ttk

def addContact():

    def clear():
        name.delete(0,END)
        contact.delete(0,END)


    def submit():
        if name.get() == '' or contact.get() == '' or email.get() == '' or address.get() == '':
            messagebox.showerror('Error',"All fields are required")


        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="Rohit@12")
                mycursor = conn.cursor()
            except:
                messagebox.showerror('Error', "Database Connectivity Issue, Try again after Some time")
                return

            try:
                query = 'CREATE DATABASE contactbook'
                mycursor.execute(query)
                query = 'USE contactbook'
                mycursor.execute(query)
                query = 'CREATE TABLE contacts(id INTEGER PRIMARY KEY AUTO_INCREMENT, name VARCHAR(25) NOT NULL, phone BIGINT NOT NULL,email VARCHAR(255) NOT NULL, address VARCHAR(255) NOT NULL)'
                mycursor.execute(query)
            except:
                mycursor.execute('USE contactbook') # using contactsuser in case of database is creared already    

            query = 'select * from contacts where phone=%s and email=%s'
            mycursor.execute(query,(contact.get(),email.get()))

            row = mycursor.fetchone() # it fetch that row where same username exists if username is the same then it will throw error 
            if row != None:
                messagebox.error("error","contact Already exists, Add Different One")
        
            else:
                query = 'insert into contacts(name, phone, email, address) VALUES(%s, %s,%s,%s)'
                mycursor.execute(query,(name.get(),contact.get(),email.get(),address.get()))
                conn.commit() # as we are commiting changes here as well.
                conn.close()
                messagebox.showinfo('success',"Contact is added Successfully")
                clear()
                root.destroy() 
        

    root = Toplevel()

    root.grab_set()
    root.geometry('450x600+800+200')
    root.resizable(False,False)
    root.title('phonebook.com')
    root.iconbitmap("favicon.ico")
    root.configure(background="snow")
    bgimage=ImageTk.PhotoImage(file="mainimage.png")
    bgLabel = Label(root,image=bgimage)
    bgLabel.place(x=-900,y=-50)

    headinglabel = Label(root,text='ADD CONTACTS',font=('verdana',20,'bold'),fg='blue',bg='white')
    headinglabel.place(x=90,y=10)

    namelabel = Label(root,text='Name',font=('microsoft Yahei UI Light',11,'bold'),fg='blue',bg='white')
    namelabel.place(x=70,y=80)

    name = Entry(root,font=('microsoft Yahei UI Light',11),bd=0,fg='blue',bg='white')
    name.place(x=72,y=110,width=300)

    frame = Frame(root,width=300,height=2,bg='blue')
    frame.place(x=72,y=135)



    contactlabel = Label(root,text='Phone Number',font=('microsoft Yahei UI Light',11,'bold'),fg='blue',bg='white')
    contactlabel.place(x=70,y=160)

    contact = Entry(root,font=('microsoft Yahei UI Light',11),bd=0,fg='blue',bg='white')
    contact.place(x=72,y=190,width=300)

    frame = Frame(root,width=300,height=2,bg='blue')
    frame.place(x=72,y=215)


    emaillabel = Label(root,text='Email',font=('microsoft Yahei UI Light',11,'bold'),fg='blue',bg='white')
    emaillabel.place(x=70,y=240)

    email = Entry(root,font=('microsoft Yahei UI Light',11),bd=0,fg='blue',bg='white')
    email.place(x=72,y=270,width=300)

    frame = Frame(root,width=300,height=2,bg='blue')
    frame.place(x=72,y=295)


    addresslabel = Label(root,text='address',font=('microsoft Yahei UI Light',11,'bold'),fg='blue',bg='white')
    addresslabel.place(x=70,y=320)

    address = Entry(root,font=('microsoft Yahei UI Light',11),bd=0,fg='blue',bg='white')
    address.place(x=72,y=350,width=300)

    frame = Frame(root,width=300,height=2,bg='blue')
    frame.place(x=72,y=375)



    button = Button(root,text="Add in List",font=('microsoft Yahei UI Light',11,'bold'),bd=0,activebackground='blue',activeforeground="white",fg='white',bg='blue',command=submit)
    button.place(x=70,y=410,width=300)


    root.mainloop()

def logout():
    root.destroy()
    import main

def search_contacts():

    def search():
        if name.get() == '' and address.get() == '':
            messagebox.showerror('Error','At Least One field required')
        else:
            try:
                conn = pymysql.connect(host='localhost',user='root',password='Rohit@12')
                mycursor = conn.cursor()
            except:
                messagebox.showerror('Error','Database Connection Error')

            
            query = 'USE contactbook'
            mycursor.execute(query)
            query='select * from contacts where name=%s or address=%s'
            mycursor.execute(query,(name.get(),address.get()))
            contactlist.delete(*contactlist.get_children())
            fetched_data = mycursor.fetchall()
            for data in fetched_data:
                datalist=list(data)
                contactlist.insert('',END,values=datalist)

            


    root=Toplevel()

    root.grab_set()
    root.geometry('280x240+1270+345')
    root.resizable(0,0)
    root.title('Search Contacts')
    root.iconbitmap("favicon.ico")
    root.configure(background='snow')
    bgimage=ImageTk.PhotoImage(file="mainimage.png")
    bgLabel = Label(root,image=bgimage)
    bgLabel.place(x=-900,y=-50)

    namelabel = Label(root,text="Enter Name",font=('microsoft Yahei UI Light',12,'bold'),fg='blue',bg='snow')
    namelabel.place(x=36,y=10)

    name = Entry(root,font=('microsoft Yahei UI Light',11),bd=0,fg='blue',bg='snow')
    name.place(x=40,y=40,width=200)
    frame= Frame(root,width=200,height=2,bg='blue')
    frame.place(x=40,y=65)

    optionlabel = Label(root,text="or",font=('microsoft Yahei UI Light',12,'bold'),fg='blue',bg='snow')
    optionlabel.place(x=130,y=80)

    addresslabel = Label(root,text="Enter Address",font=('microsoft Yahei UI Light',12,'bold'),bg='snow',fg='blue')
    addresslabel.place(x=36,y=110)

    address=Entry(root,font=('microsoft Yahei UI Light',11),bd=0,bg='snow',fg='blue')
    address.place(x=40,y=140)
    frame=Frame(root,width=200,height=2,bg='blue')
    frame.place(x=40,y=165)


    button = Button(root,text='search',font=('microsoft',12,'bold'),bd=0,fg='snow',bg='blue',activebackground='blue',activeforeground='snow',command=search)
    button.place(x=40,y=190,width=100)


    root.mainloop()


def update_contacts():

    def update():
        if name.get()== '' or phone.get()== '' or email.get()== '' or address.get()== '': 
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn = pymysql.connect(host='localhost',user='root',password='Rohit@12')
                mycursor = conn.cursor()
            except:
                messagebox.showerror('Error','Database Connection Error, Try Again after Some time')
                return

            query = 'use contactbook'
            mycursor.execute(query)
            
            query = "update contacts set name=%s,phone=%s,email=%s,address=%s where id=%s"
            mycursor.execute(query,(name.get(),phone.get(),email.get(),address.get(),id.get()))
            

            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Contact is Updated successfully")
            root.destroy()

            view_contacts()


    root=Toplevel()

    root.grab_set()
    root.geometry('450x600+800+200')
    root.resizable(0,0)
    root.title('update contacts')
    root.iconbitmap("favicon.ico")
    root.configure(background='snow')
    bgimage=ImageTk.PhotoImage(file="mainimage.png")
    bgLabel = Label(root,image=bgimage)
    bgLabel.place(x=-900,y=-50)

    headinglabel = Label(root,text='UPDATE CONTACTS',font=('verdana',20,'bold'),bg='snow',fg='blue')
    headinglabel.place(x=50,y=5)

    idlabel = Label(root,text='ID',font=('verdana',11,'bold'),bg='snow',fg='blue')
    idlabel.place(x=72,y=70)

    id = Entry(root,font=('microsoft Yahei UI Light',11),bd=0,fg='blue')
    id.place(x=130,y=70,width=50)
    frame= Frame(root,width=50,height=2,bg='blue')
    frame.place(x=130,y=95)

    namelabel = Label(root,text="Name",font=('microsoft',12,'bold'),fg='blue',bg='snow')
    namelabel.place(x=72,y=120)
    

    name = Entry(root,font=('microsoft',11),bd=0,fg='blue',bg='snow')
    name.place(x=75,y=150,width=300)
    frame= Frame(root,width=300,height=2,bg='blue')
    frame.place(x=75,y=175)

    phonelabel = Label(root,text="Contact Number",font=('microsoft',12,'bold'),fg='blue',bg='snow')
    phonelabel.place(x=72,y=200)

    phone = Entry(root,font=('microsoft',11),bd=0,fg='blue',bg='snow')
    phone.place(x=75,y=230,width=300)
    frame= Frame(root,width=300,height=2,bg='blue')
    frame.place(x=75,y=255)

    emaillabel = Label(root,text="Email",font=('microsoft',12,'bold'),fg='blue',bg='snow')
    emaillabel.place(x=72,y=285)

    email = Entry(root,font=('microsoft',11),bd=0,fg='blue',bg='snow')
    email.place(x=75,y=310,width=300)
    frame= Frame(root,width=300,height=2,bg='blue')
    frame.place(x=75,y=335)

    addresslabel = Label(root,text="Address",font=('microsoft',12,'bold'),fg='blue',bg='snow')
    addresslabel.place(x=72,y=360)

    address = Entry(root,font=('microsoft',11),bd=0,fg='blue',bg='snow')
    address.place(x=75,y=385,width=300)
    frame= Frame(root,width=300,height=2,bg='blue')
    frame.place(x=75,y=410)


    button = Button(root,text='update',font=('microsoft',12,'bold'),bd=0,fg='snow',bg='blue',activebackground='blue',activeforeground='snow',command=update)
    button.place(x=75,y=460,width=300)


    indexing = contactlist.focus()
    print(indexing)
    content = contactlist.item(indexing)
    print(content)

    listdata = content['values']
    id.insert(0,listdata[0])
    name.insert(0,listdata[1])
    phone.insert(0,listdata[2])
    email.insert(0,listdata[3])
    address.insert(0,listdata[4])

    root.mainloop()

def delete_contacts():
    try:
        conn = pymysql.connect(host='localhost',user='root',password='Rohit@12')
        mycursor = conn.cursor()
    except:
        messagebox.showerror('Error','Database Connection Error')
    
    indexing = contactlist.focus()
    print(indexing)
    content=contactlist.item(indexing)
    print(content)
    contentId = content['values'][0]
    query='use contactbook'
    mycursor.execute(query)
    query ='delete from contacts where id=%s'
    mycursor.execute(query,(contentId))
    conn.commit()
    conn.close()
    messagebox.showinfo('Deleted',f' This Id{contentId} is deleted successfully')
    
    view_contacts() 
    


def view_contacts():

    try:
        conn = pymysql.connect(host='localhost',user='root',password='Rohit@12')
        mycursor = conn.cursor()
    except:
        messagebox.showerror('Error','Database Connection Error')

    query='use contactbook'
    mycursor.execute(query)
    query='select * from contacts'
    mycursor.execute(query)
    contactlist.delete(*contactlist.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        datalist=list(data)
        contactlist.insert('',END,values=datalist) 

    


root = Tk()  # root is object variable and Tkinter class is called


root.geometry('1800x900+50+50')
root.resizable(False,False)
root.title('contact main page')
root.iconbitmap("favicon.ico")
root.configure(background="snow")
bgimage=ImageTk.PhotoImage(file="mainimage.png")
bgLabel = Label(root,image=bgimage)
bgLabel.place(x=-10,y=0)


headinglabel = Label(root,text='WELCOME TO THE MAIN WINDOW',font=('verdana',23,'bold'),fg='blue',bg='snow')
headinglabel.place(x=550,y=20)

infolabel = Label(root,text="Here you can store your contacts information with ease and trust me it is 'Secured' ",font=('microsoft Yahei UI Light',12,'bold'),bg='snow',fg="blue")
infolabel.place(x=515,y=80)

button = Button(root,text='log Out',font=('microsoft Yahei UI Light',12,'bold'),bd=0,activeforeground="snow",activebackground="blue",fg='snow',bg='blue',cursor='hand2',command=logout)
button.place(x=1500,y=30,width=140)

button = Button(root,text='Add New',font=('microsoft Yahei UI Light',14,'bold'),bd=0,activeforeground="snow",activebackground="blue",fg='snow',bg='blue',cursor='hand2',command=addContact)
button.place(x=300,y=200,width=200)

button = Button(root,text='View',font=('microsoft Yahei UI Light',14,'bold'),bd=0,activeforeground="snow",activebackground="blue",fg='snow',bg='blue',cursor='hand2',command=view_contacts)
button.place(x=550,y=200,width=200)

button = Button(root,text='Update',font=('microsoft Yahei UI Light',14,'bold'),bd=0,activeforeground="snow",activebackground="blue",fg='snow',bg='blue',cursor='hand2',command=update_contacts)
button.place(x=800,y=200,width=200)

button = Button(root,text='Delete',font=('microsoft Yahei UI Light',14,'bold'),bd=0,activeforeground="snow",activebackground="blue",fg='snow',bg='blue',cursor='hand2',command=delete_contacts)
button.place(x=1050,y=200,width=200)

button = Button(root,text='Search',font=('microsoft Yahei UI Light',14,'bold'),bd=0,activeforeground="snow",activebackground="blue",fg='snow',bg='blue',cursor='hand2',command=search_contacts)
button.place(x=1300,y=200,width=200)



rightFrame = Frame(root)
rightFrame.place(x=350,y=300,width=1100,height=500)

scrollbary=Scrollbar(rightFrame,orient=VERTICAL)
scrollbarx=Scrollbar(rightFrame,orient=HORIZONTAL)


contactlist = ttk.Treeview(rightFrame,columns=('id','name','phone','email','address'),xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary.set)

scrollbarx.config(command=contactlist.xview)
scrollbary.config(command=contactlist.yview)

scrollbarx.pack(side=BOTTOM,fill=X)
scrollbary.pack(side=RIGHT,fill=Y)


contactlist.pack(fill=BOTH,expand=1)

contactlist.heading('id',text="Sl.No")
contactlist.heading('name',text="Name")
contactlist.heading('phone',text="Contact Number")
contactlist.heading('email',text="Email Id")
contactlist.heading('address',text="Address")

contactlist.config(show='headings')

contactlist.column('id',width=50,anchor=CENTER)
contactlist.column('name',width=150,anchor=CENTER)
contactlist.column('phone',width=150,anchor=CENTER)
contactlist.column('email',width=200,anchor=CENTER)
contactlist.column('address',width=200,anchor=CENTER)

style = ttk.Style()
style.configure('Treeview',rowheight=40,font=('verdana',10,),foreground='Black')
style.configure('Treeview.Heading',rowheight=60,font=('verdana',10,'bold'),foreground='blue')



root.mainloop()