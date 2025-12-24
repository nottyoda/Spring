import numpy as np
from matplotlib import pyplot as plt
from tkinter import *


#the code using symplectic euler
def run():
    #variables
    ls = float(lengthspring.get()) #length of spring
    rm = float(radiusmass.get()) #radius of mass movement
    mass = float(massmass.get()) #mass of point mass

    #functions
    
    #def force(theta):


    #def alpha(theta, force, mass):


    #checking variables
    lengthspring.delete(0,END)
    radiusmass.delete(0,END)
    massmass.delete(0,END)

    lengthspring.insert(0,ls)
    radiusmass.insert(0,rm)
    massmass.insert(0,mass)


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


label_1 = Label(window,
                text="Length of spring:",
                font=("Impact",10)
                )
label_1.pack()

lengthspring = Entry(window, 
              font=("Arial", 50),
              )
lengthspring.pack()



label_2 = Label(window,
                text="Radius of Path:",
                font=("Impact",10)
                )
label_2.pack()

radiusmass = Entry(window, 
              font=("Arial", 50),
              )
radiusmass.pack()

label_3 = Label(window,
                text="Mass of mass:",
                font=("Impact",10)
                )
label_3.pack()

massmass = Entry(window,
                 font=("arial", 50),
                 )
massmass.pack()


run_button = Button(window, 
                    text= "Run", 
                    font=("Arial", 50), 
                    command= run)
run_button.pack()



window.mainloop()

