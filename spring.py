import numpy as np
from matplotlib import pyplot as plt
from tkinter import *


#the code using symplectic euler
#def run():
    #variables
    #ls = 1 #length of spring
    #rp = 1 #radius of mass
    #mass = 1 #mass of point mass

    #functions

    #def force(theta):


    #def alpha(theta, force, mass):


#window stuff
window = Tk()
window.geometry("200x200")
window.title("Bouncepadset")
icon = PhotoImage(file='astro_card.png')
window.iconphoto(True, icon)

#stuff in the window
label = Label(window,
              text="CATCH!!",
              font=('Impact',50,'bold'),
              relief=RAISED,
              bd=10,
              padx= 10,
              pady=20)
label.pack()

entry = Entry(window, 
              font=("Arial", 50),
              )
entry.pack
run_button = Button(window, text= "Run", command= run)
run_button.pack()



window.mainloop()

