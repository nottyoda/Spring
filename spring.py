import numpy as np
from matplotlib import pyplot as plt
from tkinter import *

#the spring constant
spring_constant = 1

#the code using symplectic euler
#variables
ls = 0
rm = 0
mass = 0
#functions
def springpos():
    springattchvec= np.array([ls+rm,0])
    return springattchvec

def position(theta):
    posvec= np.array([rm * np.cos(theta), rm * np.sin(theta)])
    return posvec 

def force(theta):
    stretchvec = position(theta) - springpos()
    stretchveclen = np.sqrt(strechvec.dot(stretchvec))
    extension = stretchveclen - ls
    forcevec = stretchvec * extension * (1/ stretchveclen) * spring_constant 
    return forcevec


def alpha(theta, forcevec, mass):
    forcevec[0]




def run():
    #variables
    ls = float(lengthspring.get()) #length of spring
    rm = float(radiusmass.get()) #radius of mass movement
    m = float(massmass.get()) #mass of point mass

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
label.pack()

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

