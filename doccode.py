
from tkinter import * 
from tkinter import messagebox 
import sys 
import os 
import random 
import tkinter.messagebox 
root = Tk() 
root.resizable(width=True, height=True) 
root.geometry('1000x750') 
root.configure(background='black') 
root.title("2D LUDO") 
 
w = PhotoImage(file="whitebox.gif") 
rs = PhotoImage(file="red side 1.png") 
rc = PhotoImage(file="red.gif") 
bs = PhotoImage(file="blue side 1.png") 
gs = PhotoImage(file="green side 1.png") 
ys = PhotoImage(file="yellow side 1.png") 
ct = PhotoImage(file="center.gif") 
t = PhotoImage(file="test.gif") 
gb = PhotoImage(file="greenbox.gif") 
gst = PhotoImage(file="greenstop.gif") 
yb = PhotoImage(file="yellowbox.gif") 
yst = PhotoImage(file="yellowstop.gif") 
blueb = PhotoImage(file="bluebox.gif") 
bluest = PhotoImage(file="bluestop.gif") 
rb = PhotoImage(file="redbox.gif") 
rst = PhotoImage(file="redstop.gif") 
h = PhotoImage(file="head.gif") 
t = PhotoImage(file="tail.gif") 
h1 = PhotoImage(file="head1.gif") 
t1 = PhotoImage(file="tail1.gif") 
h2 = PhotoImage(file="head2.gif") 
t2 = PhotoImage(file="tail2.gif") 
h3 = PhotoImage(file="head3.gif") 
t3 = PhotoImage(file="tail3.gif") 
bc= PhotoImage(file="blue.gif") 
yc= PhotoImage(file="yellow.gif") 
gc= PhotoImage(file="green.gif") 
 
Label(image=rs, width=298, height=298).place(x=-1, y=-1) 
Label(image=bs, width=300, height=300).place(x=(-2), y=(448)) 
Label(image=gs, width=296, height=296).place(x=(450), y=(0)) 
Label(image=ys, width=294, height=294).place(x=(450), y=(450)) 
Label(image=ct, width=150, height=150).place(x=(298), y=(298)) 
 
c = 0 
lx = 0 
bb =0
nc = 0 
rollc = 0 
rolls = [] 
RED = True 
BLUE = False 
GREEN = False 
YELLOW = False 
TURN = True 
REDKILL = False 
BLUEKILL = False 
GREENKILL = False 
YELLOWKILL = False 
 
def board(): 
tkinter.messagebox.showinfo(title=None, message="START GAME: PRESS OKAY & EXIT: 
PRESS CROSS UP IN THE WINDOW") 
v = 0 
z = 0 
 
while (v != 300): 
z = 0 
while (z != 150): 
Label(image=w, width=46, height=46).place(x=(300 + z), y=(0 + v)) 
z = z + 50 
v = v + 50 
 
z = 0 
v = 0 
while (v != 300): 
z = 0 
while (z != 150): 
Label(image=w,width=46, height=46).place(x=(0 + v), y=(300 + z)) 
z = z + 50 
v = v + 50 
 
v = 0 
z = 0 
 
while (v != 300): 
z = 0 
while (z != 150): 
Label(image=w, width=46, height=46).place(x=(300 + z), y=(450 + v)) 
z = z + 50 
v = v + 50 
 
z = 0 
v = 0 
while (v != 300): 
z = 0 
while (z != 150): 
Label(image=w, width=46, height=46).place(x=(450 + v), y=(300 + z)) 
z = z + 50 
v = v + 50 
v = 0 
while (v != 250): 
Label(image=gb, width=46, height=46).place(x=(350), y=(50 + v)) 
v = v + 50 
 
Label(image=gst, width=46, height=46).place(x=(300), y=(100)) 
Label(image=gst, width=46, height=46).place(x=(400), y=(50)) 
 
v = 0 
while (v != 250): 
Label(image=yb, width=46, height=46).place(x=(450 + v), y=(350)) 
v = v + 50 
 
Label(image=yst, width=46, height=46).place(x=(600), y=(300)) 
Label(image=yst, width=46, height=46).place(x=(650), y=(400)) 
 
v = 0 
while (v != 250): 
Label(image=rb, width=46, height=46).place(x=(50 + v), y=(350)) 
v = v + 50 
 
Label(image=rst, width=46, height=46).place(x=(100), y=(400)) 
Label(image=rst, width=46, height=46).place(x=(50), y=(300)) 
 
v = 0 
while (v != 250): 
Label(image=blueb, width=46, height=46).place(x=(350), y=(450 + v)) 
v = v + 50 
 
Label(image=bluest, width=46, height=46).place(x=(300), y=(650)) 
Label(image=bluest, width=46, height=46).place(x=(400), y=(600)) 
 
Label(image=h, width=46, height=46).place(x=250, y=400) 
Label(image=t, width=46, height=46).place(x=300, y=450) 
Label(image=h1, width=46, height=46).place(x=400, y=450) 
Label(image=t1, width=46, height=46).place(x=450, y=400) 
Label(image=h2, width=46, height=46).place(x=450, y=300) 
Label(image=t2, width=46, height=46).place(x=400, y=250) 
Label(image=h3, width=46, height=46).place(x=300, y=250) 
Label(image=t3, width=46, height=46).place(x=250, y=300) 
 
 
def main(): 
 
global box, redbox, bluebox, greenbox, yellowbox, redhome, bluehome, yellowhome, greenhome 
global red, blue, yellow, green, rap, RED, BLUE, GREEN, YELLOW, dice, nc, TURN, bb 
 
if c == 0: 
board() 
box = [Box() for i in range(52)] 
 
redbox = [Box() for i in range(57)] 
bluebox = [Box() for i in range(57)] 
greenbox = [Box() for i in range(57)] 
yellowbox = [Box() for i in range(57)] 
 
redhome = [Box() for i in range(4)] 
bluehome = [Box() for i in range(4)] 
greenhome = [Box() for i in range(4)] 
yellowhome = [Box() for i in range(4)] 
 
red = [Box() for i in range(4)] 
blue = [BBox() for i in range(4)] 
green = [GBox() for i in range(4)] 
yellow = [YBox() for i in range(4)] 
 
 
turn() 
button = Button(root, text=" ROLL DIE ", relief="raised", font=("Arial", 20), command=roll) 
button.place(x=780, y=120) 
 
root.mainloop()