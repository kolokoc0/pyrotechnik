import tkinter as tk
import random


win = tk.Tk()


cas = 60
width = 300
sirka = 15
ux = 20
uy = 150


farby = ["red","green","gray","yellow","blue"]
vyber = 0
temp = False

canvas = tk.Canvas(win, width=500,height=500,bg = "white")
canvas.pack()





def draw_wires():
    global vyber
    canvas.create_text(250,40,text = 'Pyrotechnik', font=("Arial",40), fill="Blue")
    canvas.create_text(250,90,text ="Vyber jeden kablik", fill = "Blue")
    for i in range(5):
        canvas.create_rectangle(ux,uy+(i*sirka),ux+width,uy+sirka+(i*sirka),fill=farby[i])
    vyber = random.choice(farby)
    print(vyber)




def stlacenie(e):
    global temp
    overlap = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    color = canvas.itemcget(overlap,"fill")
    if color == vyber:
        string = canvas.create_text(width/2,250,text ="Vyhral si!!!!",fill="black")
        temp = True
    else:
        canvas.delete("all")

timer= canvas.create_text(400,210, text=cas,font=("Arial",30),fill="red")
def casovac():
    global cas,timer
    if temp==False:
        cas -=1
        canvas.delete(timer)
        timer = canvas.create_text(400,210,text=cas,font=("Arial",30),fill="red")
        if cas>0 and temp==False:
            canvas.after(100,casovac)
        else:
            canvas.delete("all")




draw_wires()
casovac()
canvas.bind("<Button-1>",stlacenie)



win.mainloop()
