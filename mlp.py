from os import close
from tkinter import *
import tkinter
from tkinter import font
from tkinter import ttk

from pygame import mixer
import pygame
from tkinter import messagebox
from tkinter import filedialog
import os
from pygame import time
import time
from ttkthemes import themed_tk as tk
# import threading


root = tk.ThemedTk()
root.get_themes()
root.set_theme("black")
playlist = []

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack()

topframe = Frame(rightframe)
topframe.pack()

midframe = Frame(rightframe)
midframe.pack()

rewframe = Frame(rightframe)
rewframe.pack()

# creating menu bar
menubar = Menu(root)

root.iconbitmap(r'favicon.ico')

root.config(menu = menubar)
filelabel = Label(root,text="Let's Chill Dude!",fg="blue",relief=FLAT)

filelabel.pack(pady=10)

lengthlabel1 = Label(root,text="Total length: --:--",fg= "blue",relief=GROOVE)
lengthlabel1.pack(pady = 10)


# currenttimelabel1 = Label(root,text="Remmaining Time: --:--",fg="blue",relief=GROOVE)
# currenttimelabel1.pack(pady=15)
def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_list(filename_path)

def add_to_list(f):
    f = os.path.basename(filename_path)
    index = 0
    playlistbox.insert(index, f)
    playlist.insert(index, filename_path)
    index += 1
    # playlistbox.pack()   
def del_song():
    selected_song = playlistbox.curselection()
    selected_song= int(selected_song[0])
    playlistbox.delete(selected_song)     
    playlist.pop(selected_song)
def close_win():
    root.destroy()


#create thr sub menu
submenu = Menu(menubar,tearoff=0)
submenu2 = Menu(menubar,tearoff=0)
submenu3 = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "File",menu = submenu)
submenu.add_command(label = "Open",command = browse_file)
submenu.add_command(label = "Exit",command = close_win )
menubar.add_cascade(label = "Help",menu = submenu2)
menubar.add_cascade(label = "Mode",menu = submenu3)




mixer.init()
root.title("DIScord-E-fiy")
# root.configure(bg="grey2")

#____________________________
photo1 = PhotoImage(file = "playbtn.png")
photo2 = PhotoImage(file = "pausebtn.png")
photo3 = PhotoImage(file="resumebtn.png")
photo4 = PhotoImage(file = "stopbtn.png")
photo5 = PhotoImage(file = "rewindbtn.png")
mute1 = PhotoImage(file = "mute.png")
vol1 = PhotoImage(file = "unmute.png")
#___________________________________
def abou_us():
    tkinter.messagebox.showinfo('DIScord-E-fiy','builded by team discord,anky,capti,silver,dingo,chandler')
#-------------------------Time___________________---------->
def showdetails():
    
    filelabel['text']="Playing: "+''+os.path.basename(filename_path)
    a= mixer.Sound(filename_path)
    totallength = a.get_length()
    mins, secs =divmod(totallength, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthlabel1['text']="Total length"+'-'+timeformat

    # t1 = threading.Thread(target = start_count,args=(totallength,))
    # t1.start()
    

# global paused
# def start_count(t):
#     while t and mixer.music.get_busy():
        
#         mins, secs = divmod(t, 60)
#         mins = round(mins)
#         secs = round(secs)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         currenttimelabel1['text']="Remaining Time"+'-'+timeformat
        
#         time.sleep(1)
#         t -= 1
    
    


def playmusic():
    
    try:
        selected_song = playlistbox.curselection()
        selected_song= int(selected_song[0])
        play_it = playlist[selected_song]
        
        global statusbar
        mixer.music.load(play_it)
        mixer.music.play()
        statusbar['text']="Playing: "+''+os.path.basename(play_it)
        showdetails()
    except:
        tkinter.messagebox.showerror('File not found','I am not cunt Normie,This is not music file!!')
#---------------------

paused = False
def pause_music():
    mixer.music.pause()
    paused = True
    statusbar['text']="Paused"
    
#---------------------------
def resume():
    mixer.music.unpause()
    statusbar['text']="Playing:resumed"
#------------------
def stop_music():
    mixer.music.stop()
    statusbar['text']="Music Stopped"
#--------------------
def set_vol(val):
    volume = float(val)/100
    mixer.music.set_volume(volume)
def rewind_music():
    mixer.music.play()
    statusbar['text']="Music restarted"
    #__--------------------------
muted = False
def mute_music():
    global muted
    
    if muted:
        mixer.music.set_volume(0.6)
        volbtn.configure(image=vol1)
        scale.set(60)
        muted = False
    else:
        mixer.music.set_volume(0.0)
        volbtn.configure(image=mute1)
        scale.set(0)
        muted = True
#_________modes functions______________
def darkmode():
    root.configure(bg="black")
    rewframe.configure(bg="black")
    midframe.configure(bg="black")
    leftframe.configure(bg="black")
    topframe.configure(bg="black")
    rightframe.configure(bg="black")
def whitemode():
    root.configure(bg="snow")
    rewframe.configure(bg="snow")
    midframe.configure(bg="snow")
    leftframe.configure(bg="snow")
    topframe.configure(bg="snow")
    rightframe.configure(bg="snow")
def greenmode():
    root.configure(bg="lawn green")
    rewframe.configure(bg="lawn green")
    midframe.configure(bg="lawn green")
    leftframe.configure(bg="lawn green")
    topframe.configure(bg="lawn green")
    rightframe.configure(bg="lawn green")
def bluemode():
    root.configure(bg="Deepskyblue2")
    rewframe.configure(bg="Deepskyblue2")
    midframe.configure(bg="Deepskyblue2")
    leftframe.configure(bg="Deepskyblue")
    topframe.configure(bg="Deepskyblue")
    rightframe.configure(bg="Deepskyblue")
def greymode():
    root.configure(bg="grey26")
    rewframe.configure(bg="grey26")
    midframe.configure(bg="grey26")
    leftframe.configure(bg="grey26")
    topframe.configure(bg="grey26")
    rightframe.configure(bg="grey26")
def pinkmode():
    root.configure(bg="hotpink")
    rewframe.configure(bg="hotpink")
    midframe.configure(bg="hotpink")
    leftframe.configure(bg="hotpink")
    topframe.configure(bg="hotpink")
    rightframe.configure(bg="hotpink")
def redmode():
    root.configure(bg="red")
    rewframe.configure(bg="red")
    midframe.configure(bg="red")
    leftframe.configure(bg="red")
    topframe.configure(bg="red")
    rightframe.configure(bg="red")
#_____________________________
def on_close():
    tkinter.messagebox.showinfo('Close',"Hey!You Dumb no one closes DIScord-E-fy,are you ok?")
    stop_music()
    root.destroy()








# color modes ________________-----------------
submenu3.add_command(label = "Dark mode",command =darkmode )
submenu3.add_command(label = "White mode",command =whitemode )
submenu3.add_command(label = "Green mode",command =greenmode )
submenu3.add_command(label = "Blue Mode",command =bluemode )
submenu3.add_command(label = "Grey Mode",command =greymode )
submenu3.add_command(label = "Pink Mode",command =pinkmode )
submenu3.add_command(label = "Red Mode",command =redmode )

playlistbox = Listbox(leftframe)
playlistbox.pack()
#- - - - - - - - ---------------
addbtn = ttk.Button(leftframe,text="+ADD",command=browse_file)
addbtn.pack(side=LEFT,padx= 5)
#---------------------
delbtn = ttk.Button(leftframe,text="-REMOVE",command=del_song)
delbtn.pack(side=RIGHT)

plbtn = ttk.Button(midframe,text="This button will play song",image=photo1,command=playmusic)
plbtn.pack(side=LEFT)
#--------------------
pausebtn = ttk.Button(midframe,text="PAUSE",image=photo2,command=pause_music)
pausebtn.pack(side=LEFT)
#--------------------
resbtn = ttk.Button(midframe,text="RESUME",image=photo3,command=resume)
resbtn.pack(side=LEFT)
#-------------------------
stopbtn = ttk.Button(midframe,text="STOP",image=photo4,command=stop_music)
stopbtn.pack(side=LEFT)
#---------------------------
rewindbtn = ttk.Button(rewframe,image=photo5,command=rewind_music)
rewindbtn.grid(row=1,column=0,padx=10)
#---------------------
volbtn = ttk.Button(rewframe,image=vol1,command=mute_music)
volbtn.grid(row=1,column=3,padx=10)
#-------------------------------------------
# modebtn = Button(midframe,text="Mode",command=mode)
# modebtn.pack()
scale = ttk.Scale(rewframe,from_=0,to=100,orient=HORIZONTAL,command=set_vol)
scale.set(69)
mixer.music.set_volume(69)
scale.grid(row=1,column=1 ,pady=25)
#---------------
menubar.add_cascade(label = "About DISfie",command = abou_us)
statusbar = ttk.Label(root,text="WELCOME to DIScord-E-fiy,YOU TRUU LObber",font="goathic,10,italic")
statusbar.pack(side=BOTTOM,fill=X)

root.protocol("WM_DELETE_WINDOW",on_close)
root.mainloop()
