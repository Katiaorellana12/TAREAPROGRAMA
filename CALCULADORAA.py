#PLACIDO ISMAEL LUNA ARGUETA
#KATIA GUADALUPE ORELLANA ROMERO
from this import s
from tkinter import *
from tkinter import messagebox

def suma():
	s = num1.get() + num2.get()
	messagebox.showinfo("TOTAL", s)

def resta():
	r = num1.get() - num2.get()
	messagebox.showinfo("TOTAL", r)


def multiplicacion():
	m = num1.get() * num2.get()
	messagebox.showinfo("TOTAL", m)


def division():
	d = num1.get() / num2.get()
	messagebox.showinfo("TOTAL", d)


def modulo():
	mo = num1.get() % num2.get()
	messagebox.showinfo("TOTAL", mo)

def exponente():
	ex = num1.get()**num2.get()
	messagebox.showinfo("TOTAL", ex)




ventana= Tk()     
num1 = IntVar()
num2 = IntVar()
opcion = IntVar()
ventana.geometry("400x400")
ventana.config(bg="coral")
ventana.title("CALCULADORA")

etiqueta1 = Label(ventana,text="Valor 1: ", bg="black", fg="white")
etiqueta1.place(x=10,y=40)
etiqueta2 = Label(ventana,text="Valor 2: ",bg="black", fg="white" )
etiqueta2.place(x=10,y=70)


caja1 = Entry(ventana,textvariable=num1 ,bg="pink", fg="black")
caja1.place(x=100,y=40)
caja2 = Entry(ventana,textvariable=num2,bg="pink", fg="black" )
caja2.place(x=100,y=70)

radio1 = Radiobutton(ventana,text="Suma",value=1,variable=opcion, command=suma, bg="black", fg="white")
radio1.place(x=10,y=100)
radio2 = Radiobutton(ventana,text="Resta",value=2,variable=opcion , command= resta, bg="black", fg="white" )
radio2.place(x=110,y=100)
radio3 = Radiobutton(ventana,text="Multiplicación",value=3,variable=opcion, command=multiplicacion, bg="black", fg="white" )
radio3.place(x=10,y=130)
radio4 = Radiobutton(ventana,text="División",value=4,variable=opcion , command=division, bg="black", fg="white" )
radio4.place(x=110,y=130)
radio5 = Radiobutton(ventana,text="Modulo",value=5,variable=opcion,command= modulo, bg="black", fg="white" )
radio5.place(x=10,y=160)
radio6 = Radiobutton(ventana,text="Exponente",value=6,variable=opcion, command=exponente, bg="black", fg="white" )
radio6.place(x=110,y=130)

ventana.mainloop()