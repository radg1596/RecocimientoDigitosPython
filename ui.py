from tkinter import *
from red import *
ventana = Tk()
arch = open("sal.txt", "w+")
arch.close()

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
		b_es = Button(ventana, text = "ESCRIBE EN ARCHIVO", command = self.escribe)
		b_es.grid(row = 14, column = 19)
		
	def reconoce(self):
		aux = ""
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
		
	def escribe(self):
		arch = open("sal.txt", "a")#a
		sal = "\t\tself.tipos.append(Tipo (self.cad_fm (\n\t\t\t\t\t\t\t \""
		i=1
		for check in self.checks:
			#print (check.valor.get())
			if check.valor.get() == 0:
				valor = "."
			else:
				valor = "1"
			if i==7:
				sal = sal + "\" +\n\t\t\t\t\t\t\t \"" 
				i = 1
			sal = sal+valor
			i = i+1
		sal = sal + "\" ) ,		\"0 / 0 / 0 / 0\"))"
		print (sal)
		arch.write(sal)				

red=Red()
datos=Datos()	
red.entrenar(datos.cargar())
ui = UI(ventana, red, datos)
mainloop()


