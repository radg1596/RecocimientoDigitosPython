from tkinter import *
from red import *
class Menu():
	def __init__(self):
		self.points = []
		self.cuadros = []
		for i in range(0,42):
			self.cuadros.append("0")
		self.c = Canvas(root, bg="white", width=300, height= 350)
		self.c.configure(cursor="crosshair")
		self.c.pack()
		self.c.bind("<B1-Motion> ", self.point)
		self.c.bind("<Button-3>", self.graph)
		for x in range(1,301,50):
			self.grid = []
			self.grid.append(x)
			self.grid.append(0)
			self.grid.append(x)
			self.grid.append(350)
			self.c.create_line(self.grid, fill = "black")
		for y in range(1,351,50):
			self.grid = []
			self.grid.append(0)
			self.grid.append(y)
			self.grid.append(300)
			self.grid.append(y)
			self.c.create_line(self.grid, fill = "black")
		self.br = Button(root, text = "RECONOCER", command = self.reconoce)
		self.br.pack()
		#self.b_es = Button(root, text = "ESCRIBE EN ARCHIVO", command = escribe)
		#self.b_es.pack()
		self.b_bo = Button(root, text = "REINICIAR", command = self.limpiar)
		self.b_bo.pack()
		self.l = Label (root, text = "Salida")
		self.l.pack()
		root.mainloop()
		
	def point(self, event):
		self.c.create_oval(event.x, event.y, event.x+6, event.y+6, fill="red")
		self.points.append(event.x)
		self.points.append(event.y)
		i = 0
		for y in range(0,301,50):
			for x in range(0,251,50):
				if event.x>x and event.x<x+50 and event.y>y and event.y<y+50:
					#print ("Se prende el cuadro  "+"  " + str(i))
					if self.cuadros[i] == "0":
						self.cuadros[i] = "1"
					#print (cuadros)
					#return points
				i = i +1
				
	def graph(self, event):
		self.c.create_line(self.points, fill = "red")

	def reconoce(self):
		aux = ""
		for cuadro in self.cuadros:
			aux = aux + cuadro + " / "
		aux = aux[0:len(aux)-2]
		out = red.reconocer(Matriz(aux)).to_s()
		out = bin_dec(out)
		if self.l:
			self.l.destroy()
		self.l = Label (root, text = str(out))
		self.l.pack()
		
	def limpiar(self):
		self.c.destroy()
		self.l.destroy()
		self.br.destroy()
		self.b_bo.destroy()
		menu = Menu()

root = Tk()
root.title("Reconocimiento de digitos")
root.resizable(0,0)		
red=Red()
datos=Datos()	
red.entrenar(datos.cargar())
menu = Menu()