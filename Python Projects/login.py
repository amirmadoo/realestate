'''
Author - DAMM Group
App Name - Find Your Home
Working - For finding suitable flats, houses, Bungalows, etc for purchasing
'''
#Dividing the code into three parts
'''
:LOGIN/REGISTER PAGE
:MAIN SELL PAGE
:MAIN BUY PAGE
:LOGOUT PAGE
'''

#Importing all the modules
from cProfile import label
import email
from struct import pack
import tkinter as tk
import turtle
from unicodedata import name
from PIL import Image,ImageTk
import PIL.Image
from tkinter import *
from tkinter import font
from turtle import back, bgpic, color
from tkinter import *
import tkinter.messagebox
import sqlite3
from tkinter import messagebox

#First designing the first window of app
# i.e setting background images and dimensions for the window we will work in
root = Tk()
root.geometry("1024x682+0+0")
root.config(bg="white")
root.resizable(0,0)

bg = PIL.Image.open("bgimage.jpg")
photo = ImageTk.PhotoImage(bg)
label = Label(image=photo).place(x=0, y=0,relwidth=1,relheight=1)

left = PIL.Image.open("your.jpg")
left = ImageTk.PhotoImage(left)
label = Label(image=left).place(x=80, y=100,width=450,height=500)

right_frame=Frame (root,bg="white")
right_frame.place(x=480, y=100, width=500, height=500)

#creating users database

# conn = sqlite3.connect('users.db')

# #create cursor
# c = conn.cursor()

# #Creating tablwe
# '''
# c.execute("""CREATE TABLE users (
#     first_name text,
#     last_name text,
#     email_id text,
#     mobile_no integer,
#     paaswd text
# )""")
# '''
# # commit changes
# conn.commit()

# # close connection
# conn.close()

#creating properties database

conn = sqlite3.connect('users.db')

# #create cursor
# c = conn.cursor()

# c.execute("""CREATE TABLE user_properties (
#     OwnerN text,
#     mobile_no integer,
#     emailid text,
#     propertytype text,
#     bhks text,
#     superarea integer,
#     carpetarea integer,
#     status text,
#     rpoption text,
#     facilities text,
#     state text,
#     cityvill text,
#     landmark text,
#     address text,
#     price integer,
#     unit text
# )""")


# commit changes
# conn.commit()

# close connection
# conn.close()


#command for the login button

def validate():

    username = entry_1.get()
    passw_entry = entry_2.get()
    if username=='' or passw_entry=='':
        messagebox.showerror('Error', 'Feilds cannot be empty!')
    else:
      #open database
      conn = sqlite3.connect('users.db')
      #select query
      cursor = conn.execute('SELECT * from users where email_id="%s" and paaswd="%s"'%(username,passw_entry))
      #fetch data 
      if cursor.fetchone():
       messagebox.showinfo('Login Status', 'Logged in Successfully!')
       root.destroy()
       import home
       home()
      else:
       messagebox.showerror('Login Status', 'invalid username or password')
def register():
    root.destroy()
    reg=Tk()
    reg.geometry("1024x682+0+0")
    reg.config(bg="white")
    reg.resizable(0,0)
    bg = PIL.Image.open("bgimage.jpg")
    photo = ImageTk.PhotoImage(bg)
    label = Label(image=photo).place(x=0, y=0,relwidth=1,relheight=1)
    left = PIL.Image.open("your.jpg")
    left = ImageTk.PhotoImage(left)
    label = Label(image=left).place(x=80, y=100,width=450,height=500)
    right_frame=Frame (reg,bg="white")
    right_frame.place(x=480, y=100, width=500, height=500)
    def regist():
        name = entry_1.get()
        last = entry_2.get()
        email = entry_3.get()
        mobile = entry_4.get()
        password = entry_5.get()
        check_counter=0
        warn = ""
        if name == "":
            warn = "Name can't be empty"
        else:
            check_counter += 1
        if last == "":
            warn = "Last Name can't be empty"
        else:
            check_counter += 1
        if email == "":
            warn = "Email can't be empty"
        else:
            check_counter += 1
        if mobile  == "":
            warn = "Contact can't be empty"
        else:
            check_counter += 1
        if password == "":
            warn = "Feilds cannot be empty"
        else:
            check_counter += 1
        
        if check_counter == 5:
            try:
                con = sqlite3.connect('users.db')
                cur = con.cursor()
                cur.execute("INSERT INTO users VALUES (:first_name, :last_name, :email_id, :mobile_no, :paaswd)", {
                            'first_name': name,
                            'last_name': last,
                            'email_id': email,
                            'mobile_no': mobile,
                            'paaswd': password
                            })
                con.commit()
                messagebox.showinfo('confirmation', 'Registered Successfully')
                reg.destroy()
                import home
                home()
            except Exception as ep:
                messagebox.showerror('', ep) 
        else:
            messagebox.showerror('Error', warn)
    def close():
        reg.destroy()
    label_0 = Label(right_frame, text="Register here..", font=('courier', 15, 'bold'),fg="blue")
    label_0.place(x=90, y=53)

    label_1 = Label(right_frame, text="First Name", width=20, font=("bold", 10),fg="blue")
    label_1.place(x=70, y=130)
    entry_1 = Entry(right_frame, font = ('calibre',10,'normal'),bg="#A9A9A9")
    entry_1.place(x=240, y=130)

    label_2 = Label(right_frame, text="Last Name", width=20, font=("bold", 10),fg="blue")
    label_2.place(x=68, y=180)
    entry_2 = Entry(right_frame, font = ('calibre',10,'normal'),bg="#A9A9A9")
    entry_2.place(x=240, y=180)

    label_3 = Label(right_frame, text="Email", width=20, font=("bold", 10),fg="blue")
    label_3.place(x=70, y=230)
    entry_3 = Entry(right_frame, font = ('calibre',10,'normal'),bg="#A9A9A9")
    entry_3.place(x=240, y=230)

    label_4 = Label(right_frame, text="Enter Mobile", width=20, font=("bold", 10),fg="blue")
    label_4.place(x=70, y=280)
    entry_4 = Entry(right_frame, font = ('calibre',10,'normal'),bg="#A9A9A9")
    entry_4.place(x=240, y=280)

    label_5 = Label(right_frame, text="Set Password", width=20, font=("bold", 10),fg="blue")
    label_5.place(x=70, y=330)
    entry_5 = Entry(right_frame, font = ('calibre',10,'normal'), show = '*', bg="#A9A9A9")
    entry_5.place(x=240, y=330)

    Button(right_frame, text='Submit', width=20, bg='green', fg='white', command=regist).place(x=300, y=450)
    Button(right_frame, text='Close', width=20, bg='green', fg='white', command=close).place(x=50, y=450)
    reg.mainloop()

# Now setting widgets(labels, textboxes, and buttons) for login

label_0 = Label(right_frame, text="Already a user?...Login", width=30, font=('courier', 15, 'bold'),fg="blue")
label_0.place(x=90, y=53)

label_1 = Label(right_frame, text="Username", width=20, font=("bold", 10),fg="blue")
label_1.place(x=80, y=130)

entry_1= Entry(right_frame, font = ('calibre',10,'normal'),bg="#A9A9A9")
entry_1.place(x=240, y=130)

label_2 = Label(right_frame, text="Password", width=20, font=("bold", 10),fg="blue")
label_2.place(x=80, y=180)

entry_2= Entry(right_frame, font = ('calibre',10,'normal'), show = '*', bg="#A9A9A9")
entry_2.place(x=240, y=180)

Button(right_frame, text='Log In', width=20, bg='green', fg='white', command=validate).place(x=180, y=250)

label_3 = Label(right_frame, text="New User? Please Resgister!", width=30, font=('courier', 15, 'bold'),bg="white")
label_3.place(x=90, y=350)

Button(right_frame, text='Register', width=20, bg='Blue', fg='white', command=register ).place(x=180, y=400)
root.mainloop()


    
      