from tkinter import *
import math

# Funcion para agregar digitos.

def agregar_digitos(digito):
    actual = resultado.get()
    resultado.delete(0,END)
    resultado.insert(0, actual + str(digito))


# Funciones para realizar las operaciones

def suma():
    try:
        num1 = resultado.get()
        resultado.delete(0,END)
        global operacion
        operacion = "suma"
        global num_guardado
        num_guardado = float(num1)
    
    except:
        input_text.set("Error")


def resta():
    num1 = resultado.get()
    resultado.delete(0, END)
    global operacion
    operacion = "resta"
    global num_guardado
    num_guardado = float(num1)


def multiplicacion():
    num1 = resultado.get()
    resultado.delete(0, END)
    global operacion
    operacion = "multiplicacion"
    global num_guardado
    num_guardado = float(num1)


def division():
    num1 = resultado.get()
    resultado.delete(0, END)
    global operacion
    operacion = "division"
    global num_guardado
    num_guardado = float(num1)


def num_pi():
    try:
        num1 = resultado.get()
        resultado.delete(0,END)
        resultado.insert(0,math.pi)

    except:
        input_text.set("Error")


def calcular():
    try:
        num2 = resultado.get()
        resultado.delete(0,END)
        if operacion == "suma":
            resultado.insert(0, num_guardado + float(num2))
        elif operacion == "resta":
            resultado.insert(0, num_guardado - float(num2))
        elif operacion == "multiplicacion":
            resultado.insert(0, num_guardado * float(num2))
        elif operacion == "division":
            resultado.insert(0, num_guardado / float(num2))

    except:
        borrar
        input_text.set("Error")


def raiz():
    try:
        num1 = resultado.get()
        resultado.delete(0,END)
        resultado.insert(0, math.sqrt(float(num1)))

    except:
        input_text.set("Error")


def logaritmo():
    try:
        num1 = resultado.get()
        resultado.delete(0,END)
        resultado.insert(0, math.log(float(num1)))

    except:
        input_text.set("Error")


def exp_num():
    try:
        num1= resultado.get()
        resultado.delete(0,END)
        resultado.insert(0,math.exp(float(num1)))
        
    
    except:
        borrar
        input_text.set("Error")


def borrar():
    try:

        global num_guardado
        operacion = ("")
        num_guardado = ("")
        input_text.set(num_guardado)
    
    except:
        input_text.set("Error")
    
    

# Crear la ventana principal

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("392x650")

ventana.configure(background= "gray20")
color_button =("gray50")


# Definir el ancho y el alto de los botones.

button_wide = 11
button_height = 3


# Crear caja de texto para mostrar el resultado

input_text = StringVar()
resultado = Entry(ventana, font=('arial',20,'bold'),width=22,
textvariable= input_text,bd=20,insertwidth = 4, bg = "lavender", justify = "right")
resultado.place(x=10,y=60)


# Crear botones para los dígitos y operaciones

Button_0 = Button(ventana,text= "0", bg= color_button, width= button_wide, height= button_height, command= lambda:agregar_digitos(0)).place(x=18, y = 180)
Button_1 = Button(ventana,text= "1", bg= color_button, width= button_wide, height= button_height, command= lambda:agregar_digitos(1)).place(x=107, y = 180)
Button_2 = Button(ventana,text= "2", bg= color_button, width= button_wide, height= button_height, command= lambda:agregar_digitos(2)).place(x=198, y = 180)
Button_3 = Button(ventana,text= "3", bg= color_button, width= button_wide, height= button_height, command= lambda:agregar_digitos(3)).place(x=288, y = 180)

Button_4 = Button(ventana,text= "4", bg= color_button, width= button_wide, height= button_height, command= lambda:agregar_digitos(4)).place(x=18, y = 250)
Button_5 = Button(ventana,text= "5", bg= color_button, width= button_wide, height= button_height, command= lambda:agregar_digitos(5)).place(x=108, y = 250)
Button_6 = Button(ventana,text= "6", bg= color_button, width= button_wide, height= button_height, command= lambda:agregar_digitos(6)).place(x=198, y = 250)
Button_7 = Button(ventana,text= "7", bg= color_button, width= button_wide, height= button_height, command= lambda:agregar_digitos(7)).place(x=288, y = 250)

Button_8 = Button(ventana,text= "8", bg= color_button, width= button_wide, height= button_height, command= lambda:agregar_digitos(8)).place(x=18, y = 320)
Button_9 = Button(ventana,text= "9", bg= color_button, width= button_wide, height= button_height, command= lambda:agregar_digitos(9)).place(x=108, y = 320)

Button_P = Button(ventana,text= "π", bg= color_button, width= button_wide, height= button_height,command= lambda:num_pi()).place(x=198, y = 320)
Button_coma = Button(ventana,text= ",", bg= color_button, width= button_wide, height= button_height, command= lambda:agregar_digitos(".")).place(x=288, y = 320)

Add_Button = Button(ventana,text= "+", bg= color_button, width= button_wide, height= button_height,command= lambda:suma(),).place(x=18, y = 390)
Subtrc_Button = Button(ventana,text= "-", bg= color_button, width= button_wide, height= button_height, command= lambda:resta()).place(x=108, y = 390)
Multiply_Button = Button(ventana,text= "x", bg= color_button, width= button_wide, height= button_height, command= lambda:multiplicacion()).place(x=198, y = 390)
Division_Button = Button(ventana,text= "/", bg= color_button, width= button_wide, height= button_height, command= lambda:division()).place(x=288, y = 390)

Sqrt_Button = Button(ventana,text= "√", bg= color_button, width= button_wide, height= button_height, command= lambda:raiz()).place(x=18, y = 460)
EXP_Button = Button(ventana,text= "EXP", bg= color_button, width= button_wide, height= button_height,command= lambda:exp_num()).place(x=108, y = 460)
ln_Button = Button(ventana,text= "ln", bg= color_button, width= button_wide, height= button_height, command= lambda:logaritmo()).place(x=198, y = 460)
C_Button = Button(ventana,text= "C", bg= "red", width= button_wide, height= button_height,command= borrar).place(x=288, y = 460)


Equal_Button = Button(ventana,text= "=", bg= color_button, width= 15, height= 3,command= calcular).place(x=135, y = 550)




# Ejecutar la ventana principal

ventana.mainloop()




