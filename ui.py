from tkinter import *
from red import *
ventana = Tk()

class Check():
	def __init__(self, ventana, i, j):
		self.valor = IntVar()
		Checkbutton(
			ventana, variable = self.valor).grid(row = i, column = j)
	
class UI:
	def __init__(self, ventana, red, datos):
		self.checks = []
		for i in range (1, 8):
			for j in range(1, 7):
				self.checks.append(Check(ventana, i , j))
		boton_reconocer = Button(ventana, text = "RECONOCER", command = self.reconoce)
		boton_reconocer.grid(row = 9 , column = 9)
		Label (ventana, text = "Es el numero: ").grid(row = 10, column = 9)
		b_limpiar = Button(ventana, text = "LIMPIAR", command = self.limpiar)
		b_limpiar.grid(row = 12, column = 9)
		b_ent = Button(ventana, text = "ENTRENAR", command = self.entrena)
		b_ent.grid(row = 13, column = 9)
		
	def reconoce(self):
		aux = ""
		cont = 0 
		for check in self.checks:
			aux = aux  + " " + str(check.valor.get()) + " /"
		entrada = aux[0:len(aux)-1]
		out = red.reconocer(Matriz(entrada)).to_s()
		out = bin_dec(out)
		Label (ventana, text = str(out)).grid(row = 11, column = 9)
		
	def limpiar(self):
		ui = UI(ventana, red, datos)
		
	def entrena(self):
		red.entrenar( datos.cargar() )
				

red=Red()
datos=Datos()	
ui = UI(ventana, red, datos)
mainloop()


