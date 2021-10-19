import random
from tkinter import * 
import tkinter as tk
import time
import webbrowser

def dadoD4():
        a=modificador.get()
        b=int(a)
        sal=random.randint(1,4)
        salio=sal+b
        resultado.config(text=salio,font="Pixeboy 17")

def dadoD6():
        a=modificador.get()
        b=int(a)
        sal=random.randint(1,6)
        salio=sal+b
        resultado.config(text=salio,font="Pixeboy 17")
        
def dadoD8():
        a=modificador.get()
        b=int(a)
        sal=random.randint(1,8)
        salio=sal+b
        resultado.config(text=salio,font="Pixeboy 17")        

def dadoD10():
        a=modificador.get()
        b=int(a)
        sal=random.randint(1,10)
        salio=sal+b
        resultado.config(text=salio,font="Pixeboy 17")
           
def dadoD12():
        a=modificador.get()
        b=int(a)    
        sal=random.randint(1,12)
        salio=sal+b
        resultado.config(text=salio,font="Pixeboy 17")   
                
def dadoD20():
        a=modificador.get()
        b=int(a)
        sal=random.randint(1,20)
        salio=sal+b
        resultado.config(text=salio,font="Pixeboy 17")   

def tiradaDeMoneda():
    time.sleep(0.1)
    tiro=random.randint(1,2)
    if tiro==int(1):  
        resultado.config(text="🙂",font="Pixeboy 17")
    else:
         resultado.config(text="╬",font="Pixeboy 15")
 
def borrarResultado():
    resultado.config(text=" ")  
    
def webLinkedin():
    webbrowser.open("https://www.linkedin.com/in/adrian-edgardo-ceballos-44567517b")  



#----------------------------------------------------------------VENTANA
ventana = tk.Tk()
ventana.title("Dados D&D")
canvas = Canvas(ventana, width = 235, height = 270)
ventana.resizable(0,0)
canvas.pack() 
canvas["bg"] = "#4399AA"
img = PhotoImage(file="magoinicio.png")
canvas.create_image(0,0, anchor=NW, image=img)
#--------------------------------------------------------------ETIQUETAS
resultado=tk.Label()
modificador= Spinbox(ventana, from_=0, to=100)
#-----------------------------------------------------ETIQUETAS POSICION
resultado.place(x=105,y=90, width=30, height=30)
modificador.place(x=180, y=160, width=30, height=24)
#----------------------------------------------------------------BOTONES
botond4=tk.Button(text="D4",command=dadoD4,font="Pixeboy")
botond6=tk.Button(text="D6",command=dadoD6,font="Pixeboy")
botond8=tk.Button(text="D8",command=dadoD8,font="Pixeboy")
botond10=tk.Button(text="D10",command=dadoD10,font="Pixeboy")
botond12=tk.Button(text="D12",command=dadoD12,font="Pixeboy")
botond20=tk.Button(text="D20",command=dadoD20,font="Pixeboy")
boton_tirarmoneda=tk.Button(text="✨Tirar moneda✨",font="Pixeboy 13",command=tiradaDeMoneda)
boton_borrarTiradaDados=tk.Button(text="🎲 Borrar resultado 🏐",font="Pixeboy 13",command=borrarResultado)
boton_linkedin=tk.Button(text="Por Adrian ceballos",font="Pixeboy 13",command=webLinkedin)
#🗻📜✂-✊🏻✋🏻✌🏻-🏆---------------------------------------BOTONES POSICION
botond4.place(x=30,y=130,width=30,height=25)
botond6.place(x=60,y=130,width=30,height=25)
botond8.place(x=90,y=130,width=30,height=25)
botond10.place(x=120,y=130,width=30,height=25)
botond12.place(x=150,y=130,width=30,height=25)
botond20.place(x=180,y=130,width=30,height=25)
boton_tirarmoneda.place(x=30,y=160,width=150,height=25)
boton_borrarTiradaDados.place(x=30,y=190,width=180,height=25)
boton_linkedin.place(x=30,y=220,width=180,height=25)

ventana.mainloop()
