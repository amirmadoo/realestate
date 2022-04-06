import tkinter as tk
from tkinter import ttk
from cProfile import label
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
from turtle import back, bgcolor, bgpic, color
from tkinter import *
import tkinter.messagebox
import sqlite3
from tkinter import messagebox

# root window
root = tk.Tk()
root.geometry('1000x600')
root.title('Find Your Home')
root.resizable(0,0)
bg = PIL.Image.open("sellbg.jpg")
photo = ImageTk.PhotoImage(bg)
label = Label(image=photo).place(x=0, y=0,relwidth=1,relheight=1)

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=950, height=550)
frame2 = ttk.Frame(notebook, width=950, height=550)
frame3 = ttk.Frame(notebook, width=950, height=550)
frame4 = ttk.Frame(notebook, width=950, height=550)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
# add frames to notebook

notebook.add(frame1, text='Home Page')
notebook.add(frame2, text='Sell')
notebook.add(frame3, text='Buy')
notebook.add(frame4, text='Commercial')

#adding buttons and labels to  home page

# profframe = Frame(frame1, height="300", width="935", bg="red")
# profframe.place(x=10,y=10)
# label_temp= Label(profframe,text="Logo of our Application",font=("Helvetica", 50, 'italic', 'underline'), fg="black")
# label_temp.pack()
# Button(frame1, text='Feedback', width=20, bg='blue', fg='white' ).place(x=750, y=500)


# adding buttons and labels to sell frame   
label_1= Label(frame2, text="Post Your Property", font=("Helvetica", 20, 'italic', 'underline'), bg="white")
label_1.place(x=10, y=10)
label_2= Label(frame2, text="Owner's Name:", font=("Helvetica", 15), bg="white")
label_2.place(x=10, y=50)
entry_2= Entry(frame2, font = ('calibre',10,'normal'),bg="white", fg="black")
entry_2.place(x=155, y=52, height=25, width=180)
label_3= Label(frame2, text="Telephone No:", font=("Helvetica", 15), bg="white")
label_3.place(x=350, y=50)
entry_3= Entry(frame2, font = ('calibre',10,'normal'),bg="white", fg="black")
entry_3.place(x=485, y=52, height=25, width=180)
label_4= Label(frame2, text="Email Id:", font=("Helvetica", 15), bg="white")
label_4.place(x=10, y=90)
entry_4= Entry(frame2, font = ('calibre',10,'normal'),bg="white", fg="black")
entry_4.place(x=155, y=92, height=25, width=180)
menu= StringVar()
menu.set("Select Property Type.")
drop= OptionMenu(frame2, menu,"Apartment or Flats", "Bungalow","Villa","Row Houses")
drop.place(x=350, y=90)
menu= StringVar()
menu.set("How many BHK?")
drop= OptionMenu(frame2, menu,"1 BHK", "2 BHK","3 BHK","4 BHK", "5 BHK", "6+ BHK")
drop.place(x=530, y=90)
label_5= Label(frame2, text="Super Area(in sqft):", font=("Helvetica", 13), bg="white")
label_5.place(x=10, y=130)
entry_5= Entry(frame2, font = ('calibre',10,'normal'),bg="white", fg="black")
entry_5.place(x=165, y=132, height=20, width=90)
label_6= Label(frame2, text="Carpet Area(in sqft):", font=("Helvetica", 13), bg="white")
label_6.place(x=265, y=130)
entry_6= Entry(frame2, font = ('calibre',10,'normal'),bg="white", fg="black")
entry_6.place(x=423, y=132, height=20, width=90)
menu= StringVar()
menu.set("Status?")
drop= OptionMenu(frame2, menu,"Ready To Move", "Under Construction")
drop.place(x=10, y=170)
menu= StringVar()
menu.set("New Property or Resale")
drop= OptionMenu(frame2, menu,"New Property", "Resale")
drop.place(x=165, y=170)
label_9= Label(frame2, text="Any Other Facilities:", font=("Helvetica", 14), bg="white")
label_9.place(x=10, y=210)
text_facilities=Text(
    frame2, 
    height=5, 
    width=80
)
text_facilities.place(x=190,y=210)
menu= StringVar()
menu.set("Select State.")
drop= OptionMenu(frame2, menu,"Andhra Pradesh", "Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal")
drop.place(x=10, y=300)
label_8= Label(frame2, text="City or Village:", font=("Helvetica", 13), bg="white")
label_8.place(x=155, y=305)
entry_8= Entry(frame2, font = ('calibre',10,'normal'),bg="white", fg="black")
entry_8.place(x=270, y=307, height=20, width=120)
label_10=Label(frame2,text="Landmark:", font=("Helvetica", 13), bg="white")
label_10.place(x=410,y=305)
entry_10= Entry(frame2, font = ('calibre',10,'normal'),bg="white", fg="black")
entry_10.place(x=495, y=307, height=20, width=120)
label_11= Label(frame2, text="Address:", font=("Helvetica", 15), bg="white")
label_11.place(x=10, y=345)
text_add=Text(
    frame2,
    height=3,
    width=80
)
text_add.place(x=105,y=345)
label_12= Label(frame2, text="Price:", font=("Helvetica", 15), bg="white")
label_12.place(x=10, y=420)
entry_12= Entry(frame2, font = ('calibre',10,'normal'),bg="white", fg="black")
entry_12.place(x=80, y=422, height=25, width=120)
menu= StringVar()
menu.set("Unit")
drop= OptionMenu(frame2, menu,"Cr", "lac", "thousand", "BTC")
drop.place(x=195, y=420)
Button(frame2, text='Post', width=20, bg='green', fg='white' ).place(x=400, y=480)
#sell frame done

#starting with the  page


root.mainloop()