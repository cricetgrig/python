import numpy as np
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


def display(type, Z, N):
    if type == ' Тепловая карта':
        ax.set_title("Тепловая карта");
        ax.imshow(Z.transpose(), aspect='auto')
        canvas.draw()
    elif type == ' Анимация':
        def animate(i):
            line.set_ydata(Z[i])
            return line, 
        line, = ax.plot(Z[0])
        ax.set(ylim=[-4, 4])
        ax.set_title("Анимация");
        ani = animation.FuncAnimation(fig, animate, np.arange(1,N), interval= 25, blit=False)
        canvas.draw()

def result(): 
    ax.clear()
    N = int(N_ent.get())
    D = float(D_ent.get())
    dt = float(dt_ent.get())
    M = int(NT_ent.get())
    h = (2*np.pi)/N
    x = np.linspace(0,2*np.pi,N)
    u0 = np.sin(3*x)
    fu0 = np.fft.fft(u0)

    l_func = (lambda x: ((4*D)/(h**2))*np.sin((x*h)/4)**2)    
    lambd = np.empty(N)
    for i in range(int(N//2)+1):
        lambd[i] = l_func(i)
        lambd[-i] = lambd[i]
    Z = np.empty((M,N))
    Z[0]  = u0

    def F(u,t):
        return np.sin(0.1*u+t)

    um=u0
    fum=fu0
    S = 2
    fus = fum
    for m in range(1,M):
        us = um
        fus = fum
        for s in range(S):
            f1 = F(um, (m-1)*dt)
            f2 = F(us, m*dt)
            ff = np.fft.fft(f1+f2)
            fus = ((2 - dt*lambd)*fum + dt*ff)/(2 + dt*lambd)
            us = np.fft.ifft(fus)
        Z[m] = us.real
        um = us
        fum = fus

    display(display_type.get(), Z, N)
    
window = Tk() 
fig = plt.Figure(figsize = (9,5))
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().grid(column=0,row=5,columnspan=9, rowspan = 5)


window.geometry('1000x600')
window.title("Уравнение диффузии в кольце")

N_lablel = Label(window, text='N = ', font='Ubuntu')
D_label = Label(window, text='D = ', font='Ubuntu')
dt_label = Label(window, text='dt = ', font='Ubuntu')
NT_label = Label(window, text='NT = ', font='Ubuntu')
N_ent = Entry(window, width=15, font='Ubuntu')
D_ent = Entry(window, width=15, font='Ubuntu')
dt_ent = Entry(window, width=15, font='Ubuntu')
NT_ent = Entry(window, width=15, font='Ubuntu')
button = Button(window, width=40, text = "Run", command = result)

display_label = Label(window, text = "Выберите вид отображения:", font = ("Ubuntu", 12))
display_type = ttk.Combobox(window, width = 27) 
display_type['values'] = (' Анимация', ' Тепловая карта')
display_type.current(0)
display_label.grid(row = 3, column = 0, columnspan = 2)
display_type.grid(row = 3, column = 2, columnspan = 4) 

N_lablel.grid(row=0, column=0)
N_ent.grid(row=0, column=1)
D_label.grid(row=1, column=0)
D_ent.grid(row=1, column=1)
dt_label.grid(row=0, column=2)
dt_ent.grid(row=0, column=3)
NT_label.grid(row=1, column=2)
NT_ent.grid(row=1, column=3)

button.grid(row=4, column=0, columnspan = 10)
 
window.mainloop()