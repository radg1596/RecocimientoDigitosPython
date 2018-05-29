from tkinter import *
from red import *
arch = open("sal.txt", "w+")
arch.close()

root = Tk()
root.title("Reconocimiento de digitos")
root.resizable(0,0)

points = []
cuadros = []
for i in range(0,42):
	cuadros.append("0")

def point(event):
	c.create_oval(event.x, event.y, event.x+6, event.y+6, fill="red")
	points.append(event.x)
	points.append(event.y)
	
	i = 0
	for y in range(0,301,50):
		for x in range(0,251,50):
			if event.x>x and event.x<x+50 and event.y>y and event.y<y+50:
				#print ("Se prende el cuadro  "+"  " + str(i))
				if cuadros[i] == "0":
					cuadros[i] = "1"
				#print (cuadros)
				return points
			i = i +1
		
	return points
	
def graph(event):
	#global theline
	c.create_line(points, fill = "red")


c = Canvas(root, bg="white", width=300, height= 350)
c.configure(cursor="crosshair")
c.pack()
c.bind("<B1-Motion> ", point)
c.bind("<Button-3>", graph)
for x in range(1,301,50):
	grid = []
	grid.append(x)
	grid.append(0)
	grid.append(x)
	grid.append(350)
	c.create_line(grid, fill = "black")
for y in range(1,351,50):
	grid = []
	grid.append(0)
	grid.append(y)
	grid.append(300)
	grid.append(y)
	c.create_line(grid, fill = "black")

def reconoce():
	aux = ""
	for cuadro in cuadros:
		aux = aux + cuadro + " / "
	aux = aux[0:len(aux)-2]
	out = red.reconocer(Matriz(aux)).to_s()
	out = bin_dec(out)
	l = Label (root, text = str(out))
	l.pack()
	
def escribe():
	arch = open("sal.txt", "a")#a
	sal = "\n\t\tself.tipos.append(Tipo (self.cad_fm (\n\t\t\t\t\t\t\t \""
	i=1
	for cuadro in cuadros:
		#print (check.valor.get())
		if float(cuadro) == 0:
			valor = "."
		else:
			valor = "1"
		if i==7:
			sal = sal + "\" +\n\t\t\t\t\t\t\t \"" 
			i = 1
		sal = sal+valor
		i = i+1
	sal = sal + "\" ) ,		\"0 / 0 / 1 / 0\"))"
	print (sal)
	arch.write(sal)

br = Button(root, text = "RECONOCER", command = reconoce)
br.pack()

b_es = Button(root, text = "ESCRIBE EN ARCHIVO", command = escribe)
b_es.pack()

red=Red()
datos=Datos()	
red.entrenar(datos.cargar())
root.mainloop()