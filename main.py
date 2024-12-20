    ############################################# IMPORTING ################################################
from functions import *
import tkinter as tk
from tkinter import Menu, ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image,ImageTk
import pandas as pd
import datetime
import time

############################################# FUNCTIONS ################################################
def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200,tick)

def changeOnHover(button, colorOnHover, colorOnLeave, fontcOnHover, fontcOnLeave):
 
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover,fg=fontcOnHover) if (button['state']!="disabled") else None)
 
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave, fg=fontcOnLeave))

def changeOnHoverClear(text,text2,button, colorOnHover, colorOnLeave, fontcOnHover, fontcOnLeave):
 
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover,fg=fontcOnHover,text=text))
 
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave, fg=fontcOnLeave,text=text2))
def show_gif(after_gif_callback):
    # Create a Toplevel window
    gif_window = tk.Toplevel(window)
    gif_window.title("Tutorial")
    gif_window.geometry("400x400")  # Adjust size as needed
    gif_window.configure(bg="white")
    
    # Add a heading label
    heading = tk.Label(gif_window, text="Tutorial", font=("times", 20, "bold"), bg="white", fg="black")
    heading.pack(pady=10)
    
    # Load the GIF
    gif_path = "tutorial.gif"  # Replace with your GIF file path
    gif_image = Image.open(gif_path)
    gif_label = tk.Label(gif_window, bg="white")
    gif_label.pack()

    # Function to animate the GIF
    def animate_gif(count):
        frame = count % gif_image.n_frames  # Loop through frames
        gif_image.seek(frame)
        gif_photo = ImageTk.PhotoImage(gif_image)
        gif_label.config(image=gif_photo)
        gif_label.image = gif_photo
        gif_window.after(100, animate_gif, count + 1)  # Adjust delay as needed
    
    animate_gif(0)

    # Function to close the window and trigger the callback
    def close_and_trigger_callback():
        gif_window.destroy()  # Close the GIF window
        after_gif_callback()  # Trigger the next function

    # Add an OK button to close the window
    ok_button = tk.Button(
        gif_window, text="OK", command=close_and_trigger_callback, font=("times", 15), bg="#ff8d84", fg="white"
    )
    ok_button.pack(pady=20)

    gif_window.transient(window)  # Make it modal (stays on top of the main window)
    gif_window.grab_set()  # Block interaction with the main window
    gif_window.mainloop()

    
############################################################################

################################################################################







# ######################################## USED STUFFS ############################################
    
# global key
# key = ''

# ts = time.time()
# date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
# day,month,year=date.split("-")

# mont={'01':'January',
#       '02':'February',
#       '03':'March',
#       '04':'April',
#       '05':'May',
#       '06':'June',
#       '07':'July',
#       '08':'August',
#       '09':'September',
#       '10':'October',
#       '11':'November',
#       '12':'December'
#       }
window = tk.Tk()
window.geometry("1280x720")
window.resizable(True,False)
window.title("Attendance System")
window.configure(background='#262523')



frame1 = tk.Frame(window, bg="#262523",highlightbackground="white", highlightthickness=2)
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg="#262523",highlightbackground="white", highlightthickness=2)
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="Face Recognition Based Attendance System" ,fg="white",bg="#262523" ,width=55 ,height=1,font=('times', 29, ' bold '))
message3.place(x=10, y=10)

frame3 = tk.Frame(window, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(window, bg="#c4c6ce")
frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)




datef = tk.Label(frame4, text = day+"-"+mont[month]+"-"+year+"   |   ", fg="#e58905",bg="#262523" ,width=55 ,height=1,font=('times', 15, ' bold '))
datef.pack(fill='both',expand=1)

clock = tk.Label(frame3,fg="#e58905",bg="#262523" ,width=55 ,height=1,font=('times', 15, ' bold '), anchor="w")
clock.pack(fill='both',expand=1)
tick()

head2 = tk.Label(frame2, text="For New Registrations", padx=124,fg="black",bg="#dfdfdf" ,font=('times', 17, ' bold '), highlightbackground="white", highlightthickness=2, anchor="center")
head2.grid(row=0,column=0)

head1 = tk.Label(frame1, text="For Already Registered", padx=126,fg="black",bg="#dfdfdf" ,font=('times', 17, ' bold '), highlightbackground="white", highlightthickness=2)
head1.place(x=0,y=0)

lbl = tk.Label(frame2, text="Enter ID",width=20  ,height=1  ,fg="white"  ,bg="#262523" ,font=('times', 17, ' bold ') )
lbl.place(x=80, y=55)

txt = tk.Entry(frame2,width=28 ,fg="black",font=('times', 15, ' bold '))
txt.place(x=80, y=88)

lbl2 = tk.Label(frame2, text="Enter Name",width=20  ,fg="white"  ,bg="#262523" ,font=('times', 17, ' bold '))
lbl2.place(x=80, y=140)

txt2 = tk.Entry(frame2,width=28 ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(x=80, y=173)

message1 = tk.Label(frame2, text="1)Take Images  >>>  2)Save Profile" ,bg="#262523" ,fg="white"  ,width=39 ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
message1.place(x=7, y=230)

message = tk.Label(frame2, text="" ,bg="#00aeff" ,fg="black"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
# message.place(x=7, y=450)

lbl3 = tk.Label(frame1, text="Attendance",width=20  ,fg="white"  ,bg="#262523"  ,height=1 ,font=('times', 17, ' bold '))
lbl3.place(x=100, y=43)

res=0
exists = os.path.isfile("EmployeeDetails/EmployeeDetails.csv")
if exists:
    with open("EmployeeDetails/EmployeeDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    res = (res // 2)
    csvFile1.close()
else:
    res = 0
message.configure(text='Total Registrations till now  : '+str(res))

##################### MENUBAR #################################

menubar = tk.Menu(window,relief='ridge')
filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label='Light Mode', command=lambda:mode(filemenu))
filemenu.add_command(label='Change Password', command = change_pass)
filemenu.add_command(label='Contact Us', command = contact)
filemenu.add_command(label='Exit',command = window.destroy)
menubar.add_cascade(label='Help',font=('times', 29, ' bold '),menu=filemenu)

################## TREEVIEW ATTENDANCE TABLE ####################
style=ttk.Style()
style.theme_use('clam')
style.configure("Treeview.Heading", background="#8fc42b")
tv= ttk.Treeview(frame1,height =13,columns = ('name','date','intime','outtime'))

tv.column('#0',width=82)
tv.column('name',width=130)
tv.column('date',width=133)
tv.column('intime',width=65)
tv.column('outtime',width=65)
tv.grid(row=2,column=0,padx=(0,0),pady=(80,0),columnspan=4)
tv.heading('#0',text ='ID')
tv.heading('name',text ='NAME')
tv.heading('date',text ='DATE')
tv.heading('intime',text ='INTIME')
tv.heading('outtime',text ='OUTTIME')

###################### SCROLLBAR ################################

scroll=ttk.Scrollbar(frame1,orient='vertical',command=tv.yview)
scroll.grid(row=2,column=4,padx=(0,100),pady=(80,0),sticky='ns')
tv.configure(yscrollcommand=scroll.set)

###################### BUTTONS ##################################

clearButton = tk.Button(frame2, text="Clear", command=lambda:clear(txt,message1)  ,fg="black"  ,bg="#ff8d84"  ,width=6 ,activebackground = "white" ,font=('times', 10, ' bold '), borderwidth=6)
clearButton.place(x=365, y=86)
clearButton2 = tk.Button(frame2, text="Clear", command=lambda:clear2(txt2,message1)  ,fg="black"  ,bg="#ff8d84"  ,width=6 , activebackground = "white" ,font=('times', 10, ' bold '), borderwidth=6)
clearButton2.place(x=365, y=172)    
takeImg = tk.Button(
    frame2, text="Take Images",
    command=lambda: show_gif(
        lambda: TakeImages(window, txt, txt2, message, message1, trainImg)
    ),
    fg="white", bg="#262523",
    width=34, height=1, activebackground="white",
    font=("times", 15, "bold"), borderwidth=10
)
takeImg.place(x=30, y=300)
trainImg = tk.Button(frame2, text="Save Profile", command=lambda:psw(window,message,message1) ,fg="white"  ,bg="#262523"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '), borderwidth=10,state="disabled")
trainImg.place(x=30, y=380)
trackImg = tk.Button(frame1, text="Take Attendance", command=lambda:TrackImages(window,tv)  ,fg="white"  ,bg="#262523"  ,width=35  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '), borderwidth=10)
trackImg.place(x=30,y=380)
quitWindow = tk.Button(frame1, text="Quit", command=window.destroy  ,fg="black"  ,bg="#ff8d84"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '),borderwidth=10)
quitWindow.place(x=30, y=500)
Att = tk.Button(frame1, text="Show Attendance", command=lambda:att(tv)  ,fg="white"  ,bg="#262523"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '),borderwidth=10)
# Att.place(x=30, y=440)


changeOnHover(takeImg, "#2df900", "#262523","black","white")
changeOnHover(trainImg, "#2df900", "#262523","black","white")

changeOnHover(clearButton,"#ea2a2a","#ff8d84","black","black")
changeOnHover(clearButton2,"#ea2a2a","#ff8d84","black","black")

changeOnHover(trackImg, "#2df900", "#262523","black","white")
changeOnHover(quitWindow, "#ea2a2a","#ff8d84","black","white")
changeOnHover(Att, "#2df900", "#262523","black","white")

##################### END ######################################
att(tv)
window.configure(menu=menubar)
# window.attributes('-fullscreen', True)
window.mainloop()

####################################################################################################
