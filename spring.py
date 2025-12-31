import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import ( FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *



#the code using symplectic euler



def run():
    #variables
    ls = float(lengthspring.get()) #length of spring
    rm = float(radiusmass.get()) #radius of mass movement
    mass = float(massmass.get()) #mass of point mass

    #functions
    def springpos(ls, rm): # outputs array
        #springattchvec= np.array([ls+rm,0]) #not fixed pos
        springattchvec= np.array([1+rm,0]) #fixed pos
        return springattchvec

    def position(theta, rm): # outputs array
        posvec= np.array([rm * np.cos(theta), rm * np.sin(theta)])
        return posvec 

    def force(theta,ls,rm): # outputs array
        stretchvec = springpos(ls, rm) - position(theta,rm) 
        stretchveclen = np.sqrt(stretchvec.dot(stretchvec))
        extension = stretchveclen - ls
        spring_constant = 1
        forcevec = stretchvec * extension * (1/ stretchveclen) * spring_constant #can change
        return forcevec


    def alpha(theta, ls, rm, mass):
        alpha = force(theta, ls, rm).dot(np.array([-1*np.sin(theta),np.cos(theta)])) * (1/(rm)) *(1/(mass)) 
        return alpha 




    #code goes here
    h = 0.01 #stepsize
    tmax = 5 # max time
    t = np.arange(0,tmax+h,h) #time
    theta0 = 0.2 # initial condition
    v = 0 # initial velocity 

    print(alpha(theta0, ls, rm, mass))

    theta = np.zeros(len(t)) # logging angular position
    theta[0] = theta0 # setting the first term\

    for i in range(0,len(t)-1):
        v = v + alpha(theta[i],ls, rm, mass) * h 
        theta[i+1] = theta[i] + v * h 
        #print(v)
        #print(alpha(theta[i],ls, rm, mass))
    
    print(theta)

    #showing plot
    ax.plot(t, theta)
    fig.suptitle('Angular displacement')
    ax.set_xlabel('t')
    ax.set_ylabel('θ')
    ax.grid(True)

    #finding equilibrium, please change alg later, use liner interpolation if possible
    theta_equil = 0 
    theta_equil_past = 0 
    
    while (alpha(theta_equil, ls, rm, mass)* alpha(theta_equil_past, ls, rm, mass) > 0 or alpha(theta_equil+0.00001,ls,rm,mass) >= 0):
        theta_equil_past = theta_equil
        theta_equil = theta_equil + 0.00001 #please implement binary search


    if alpha(theta_equil, ls, rm, mass) != 0:
        theta_equil = (theta_equil + theta_equil_past)/2
    
    print(theta_equil)
    print(alpha(theta_equil, ls, rm, mass)) 


    # input code for checking when a half cycle completes
    halfperiod = 0 #the halfperiod 
    halfperiodnumber = 0 
    for i in range(0,len(t)-1):
        if (theta[i] - theta_equil)*(theta[i+1] - theta_equil) <= 0:
            halfperiod = halfperiod + t[i]
            halfperiodnumber = halfperiodnumber + 1
    p = 2 * halfperiod/halfperiodnumber

    period.delete(0,END) #displaying period 
    period.insert(0,p)



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
                 font=("Arial", 50),
                 )
massmass.pack()

label_4 = Label(window,
                text="period:",
                font=("Impact",10)
                )
label_4.pack()

period = Entry(window,
                 font=("arial", 50),
                 )
period.pack()

#the run button

run_button = Button(window, 
                    text= "Run", 
                    font=("Arial", 50), 
                    command= run)
run_button.pack()


#the graph part
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master = window)
canvas.get_tk_widget().pack()


window.mainloop()

