#draw 300 lines on the screen

#import library
from tkinter import *                       #Tk
#initialize the screen
w = Canvas(Tk(), width=900, height=400)     #Tk
w.pack()                                    #Tk

#draw lines. a lot.
for i in range(300):
    x = i * 20
    '''
    if i % 2 == 0:
        color= "#ff0000"
    else:
        color= "#0000ff"
    '''
    color= "#000000"
    w.create_line(x, 180, x+20, 220, fill=color)     #Tk

mainloop()                                  #Tk
