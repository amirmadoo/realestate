from itertools import count
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
photo1 = ImageTk.PhotoImage(bg)
label = Label(image=photo1).place(x=0, y=0,relwidth=1,relheight=1)

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=950, height=550)
frame2 = ttk.Frame(notebook, width=950, height=550)
frame3 = ttk.Frame(notebook, width=950, height=550)
# frame4 = ttk.Frame(notebook, width=950, height=550)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
# add frames to notebook

notebook.add(frame1, text='Home')
notebook.add(frame2, text='Sell')
notebook.add(frame3, text='Buy')
# notebook.add(frame4, text='Commercial')

#creaing register button command
def postproperty():
    ownername=entry_2.get()
    telephoneno=entry_3.get()
    emailid=entry_4.get()
    propertytype=menu1.get()
    bhk=menu2.get()
    superarea=entry_5.get()
    carpetarea=entry_6.get()
    status=menu3.get()
    neworresale=menu4.get()
    facilities=text_facilities.get("1.0",END)
    state=menu5.get()
    cityorvillage=entry_8.get()
    landmark=entry_10.get()
    address=text_add.get("1.0",END)
    price=entry_12.get()
    try:
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        cur.execute("INSERT INTO user_properties VALUES (:OwnerN, :mobile_no, :emailid, :propertytype, :bhks, :superarea, :carpetarea, :status, :rpoption, :facilities, :state, :cityvill, :landmark, :address, :price)", {
                            'OwnerN': ownername,
                            'mobile_no': telephoneno,
                            'emailid': emailid,
                            'propertytype': propertytype,
                            'bhks': bhk,
                            'superarea': superarea,
                            'carpetarea': carpetarea,
                            'status': status,
                            'rpoption':neworresale,
                            'facilities': facilities,
                            'state': state,
                            'cityvill': cityorvillage,
                            'landmark': landmark,
                            'address': address,
                            'price':price,
                            })
        con.commit()
        
        messagebox.showinfo('confirmation', 'Property Added Successfully!')
        entry_2.delete(0, END)
        entry_3.delete(0, END)
        entry_4.delete(0, END)
        
        entry_5.delete(0, END)
        entry_6.delete(0, END)
        entry_2.delete(0, END)
    
        text_facilities.setvar('')
       
        entry_8.delete(0, END)
        entry_10.delete(0, END)
        text_add.delete(0, END)
        entry_12.delete(0, END)

    except Exception as ep:
        messagebox.showerror('', ep) 

#creating help and support command
def helpS():
    root = tk.Tk()
    root.geometry('400x600')
    root.title('Help And Support')
    root.resizable(0,0)
    userquery=Label(root, text="Email your Query at:", width=40, bg='grey', fg='white')
    userquery.place(x=10, y= 10)
    e = Entry(root, bg="grey", width=40)
    e.insert(END, 'fydh2002@email.com')
    e.configure(state='readonly')
    e.place(x=10, y=35)
    oRlabel=Label(root, text="OR",font = ('Arial',30,'normal'), fg='Black')
    oRlabel.place(x=6,y=100)

    
    
'''
                             HOME Page
'''
#adding buttons and labels to  home page
right_frame=Frame(frame1,bg="grey")
right_frame.place(x=705, y=1,height=600,width=300)
left_label = Label(frame1,text="FIND YOUR DREAM HOME", width=99, bg='grey', fg='white').place(x=1, y=5)
bg = PIL.Image.open("images (1).jpeg")
photo = ImageTk.PhotoImage(bg)
left_label2 = Label(frame1,image=photo).place(x=1, y=30,height=243,width=700)
# label1=Label(right_frame,text="Name", font=("Helvetica", 20, 'italic', 'underline'), bg="white")
# label1.place(x=10, y=10)
username_img=ImageTk.PhotoImage(PIL.Image.open("username.png"))
my_Label=Label(right_frame,image=username_img, bg='grey').place(x=6, y=5)
# username= Entry(right_frame, text="xyz@email.com", font=("Helvetica", 15), bg="grey", width=11)
# username.place(x=110, y=45)
e = Entry(right_frame, bg="grey")
e.insert(END, 'xyz@email.com')
e.configure(state='readonly')
e.place(x=110, y=45)
Button(right_frame, text='Edit Profile', width=25, bg='blue', fg='black' ).place(x=6, y=100)
Button(right_frame, text='Help And Support', width=25, bg='blue', fg='black', command=helpS ).place(x=6, y=150)
right_label=Label(right_frame, text="Feedback", width=10,bg='grey',fg='white',font=("Helvetica", 30)).place(x=6,y=200)
text_feedback=Text(
    right_frame, 
    height=10, 
    width=28
)
def feedback():
    feedback=text_feedback.get()
    conn = sqlite3.connect('feedback.db')
    

    conn.execute("INSERT INTO feed (review) \
        VALUES (feedback)")

    conn.commit()
    messagebox.showinfo('Feedback Submitted!')
    conn.close()
text_feedback.place(x=6,y=250)
Button(right_frame, text='Submit', width=25, bg='Green', fg='white',command=feedback ).place(x=31, y=420)
Button(right_frame, text='Log out', width=25, bg='red', fg='black' ).place(x=6, y=500)

'''
                              SELL FRAME
'''
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
menu1= StringVar()
menu1.set("Select Property Type.")
drop= OptionMenu(frame2, menu1,"Apartment or Flats", "Bungalow","Villa","Row Houses")
drop.place(x=350, y=90)
menu2= StringVar()
menu2.set("How many BHK?")
drop= OptionMenu(frame2, menu2,"1 BHK", "2 BHK","3 BHK","4 BHK", "5 BHK", "6+ BHK")
drop.place(x=530, y=90)
label_5= Label(frame2, text="Super Area(in sqft):", font=("Helvetica", 13), bg="white")
label_5.place(x=10, y=130)
entry_5= Entry(frame2, font = ('calibre',10,'normal'),bg="white", fg="black")
entry_5.place(x=165, y=132, height=20, width=90)
label_6= Label(frame2, text="Carpet Area(in sqft):", font=("Helvetica", 13), bg="white")
label_6.place(x=265, y=130)
entry_6= Entry(frame2, font = ('calibre',10,'normal'),bg="white", fg="black")
entry_6.place(x=423, y=132, height=20, width=90)
menu3= StringVar()
menu3.set("Status?")
drop= OptionMenu(frame2, menu3,"Ready To Move", "Under Construction")
drop.place(x=10, y=170)
menu4= StringVar()
menu4.set("New Property or Resale")
drop= OptionMenu(frame2, menu4,"New Property", "Resale")
drop.place(x=165, y=170)
label_9= Label(frame2, text="Any Other Facilities:", font=("Helvetica", 14), bg="white")
label_9.place(x=10, y=210)
text_facilities=Text(
    frame2, 
    height=5, 
    width=80
)
text_facilities.place(x=190,y=210)
menu5= StringVar()
menu5.set("Select State.")
drop= OptionMenu(frame2, menu5,"Andhra Pradesh", "Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal")
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
Button(frame2, text='Post', width=20, bg='green', fg='white', command=postproperty).place(x=400, y=480)
#sell frame done

'''
                                Buy Frame
'''
def query_database():
    conn=sqlite3.connect('users.db')
    c=conn.cursor()
    c.execute("SELECT * FROM user_properties")
    records=c.fetchall()
    global count
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[14], record[6], record[8], record[9], record[4], record[5], record[14]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[14], record[6], record[8], record[9], record[4], record[5], record[14]),
                           tags=('oddrow',))
        count += 1
    conn.commit()

    # Close our connection
    conn.close()



style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")


# Create a Treeview Frame
tree_frame = Frame(frame3)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll: Scrollbar = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)
bsb:Scrollbar = Scrollbar(tree_frame,orient=HORIZONTAL)
bsb.pack(side=BOTTOM,fill=X)
# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
bsb_tree = ttk.Treeview(tree_frame, xscrollcommand=bsb.set, selectmode='extended')

my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)
bsb.config(command=bsb_tree.xview)



# Define Our Columns
my_tree['columns'] = ("Location", "SuperArea", "Status", "Type", "Property type", "Bhk", "Price")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Location", anchor=W, width=140)
my_tree.column("SuperArea", anchor=W, width=140)
my_tree.column("Status", anchor=CENTER, width=100)
my_tree.column("Type", anchor=CENTER, width=140)
my_tree.column("Property type", anchor=CENTER, width=140)
my_tree.column("Bhk", anchor=CENTER, width=140)
my_tree.column("Price", anchor=CENTER, width=140)


# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Location", text="Location", anchor=W)
my_tree.heading("SuperArea", text="Super Area", anchor=W)
my_tree.heading("Status", text="Status", anchor=CENTER)
my_tree.heading("Type", text="Type", anchor=CENTER)
my_tree.heading("Property type", text="Property type", anchor=CENTER)
my_tree.heading("Bhk", text="BHK", anchor=CENTER)
my_tree.heading("Price", text="Price", anchor=CENTER)

query_database()

#search button
search_frame = Label(frame3, text="")
search_frame.pack(padx=10, pady=10)


# Add entry box
search_entry = Entry(search_frame, font=("Helvetica", 18))
search_entry.pack(pady=20, padx=20)

search_frame = Button(search_frame,text="Search")
search_frame.pack(pady=20,padx=20)










#starting with the  page


root.mainloop()