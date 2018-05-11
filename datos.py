from mat import *
import random
def mat_al(renglones, columnas):
	aux = ""
	for i in range(0,renglones):
		for j in range (0,columnas):
			aux = aux + " " + str(round(random.uniform(-0.5,0.5), 2))
		aux = aux + " /"
	return Matriz(aux[0:len(aux)-1])
"""
Clase TIPO
Cada tipo tiene su matriz de entrada así como su target
"""
class Tipo():
	def __init__(self, p, t):
		self.p=Matriz(p) 
		self.t=Matriz(t)
"""
Esta clase sólo se encarga de contener los datos de todos los ejercicios
"""
class Datos():
	w=Matriz(""); b=Matriz("")
	"""AND"""
	def cargar(self):
		self.tipos=[]
		self.w=mat_al(4,15)
		print("hola" + self.w.imprimir())
		self.b=mat_al(4,1)
		#0
		self.tipos.append(Tipo("1 / 1 / 1  / 1 / 0 / 1  / 1 / 0 / 1  / 1 / 0 / 1  / 1 / 1 / 1" ,	"0 / 0 / 0 / 0"))
		self.tipos.append(Tipo("0 / 0 / 0  / 1 / 1 / 1  / 1 / 0 / 1  / 1 / 0 / 1  / 1 / 1 / 1",		"0 / 0 / 0 / 0"))
		self.tipos.append(Tipo("1 / 1 / 1  / 1 / 0 / 1  / 1 / 0 / 1  / 1 / 1 / 1  / 0 / 0 / 0",		"0 / 0 / 0 / 0"))
		#1
		self.tipos.append(Tipo("0 / 0 / 1  / 0 / 0 / 1  / 0 / 0 / 1  / 0 / 0 / 1  / 0 / 0 / 1" ,	"0 / 0 / 0 / 1"))
		self.tipos.append(Tipo("0 / 1 / 1  / 0 / 0 / 1  / 0 / 0 / 1  / 0 / 0 / 1  / 0 / 0 / 1" ,	"0 / 0 / 0 / 1"))
		self.tipos.append(Tipo("0 / 0 / 1  / 0 / 1 / 1  / 0 / 0 / 1  / 0 / 0 / 1  / 0 / 0 / 1" ,	"0 / 0 / 0 / 1"))
		self.tipos.append(Tipo("0 / 0 / 0  / 0 / 0 / 1  / 0 / 0 / 1  / 0 / 0 / 1  / 0 / 0 / 1" ,	"0 / 0 / 0 / 1"))
		self.tipos.append(Tipo("0 / 1 / 0  / 0 / 1 / 0  / 0 / 1 / 0  / 0 / 1 / 0  / 0 / 1 / 0" ,	"0 / 0 / 0 / 1"))
		self.tipos.append(Tipo("0 / 1 / 0  / 1 / 1 / 0  / 0 / 1 / 0  / 0 / 1 / 0  / 1 / 1 / 1",		"0 / 0 / 0 / 1"))
		self.tipos.append(Tipo("0 / 1 / 0  / 1 / 1 / 0  / 0 / 1 / 0  / 0 / 1 / 0  / 0 / 1 / 0",		"0 / 0 / 0 / 1"))
		#2
		self.tipos.append(Tipo("1 / 1 / 1  / 0 / 0 / 1  / 1 / 1 / 1  / 1 / 0 / 0  / 1 / 1 / 1" ,	"0 / 0 / 1 / 0"))
		self.tipos.append(Tipo("1 / 1 / 1  / 0 / 0 / 1  / 0 / 1 / 0  / 1 / 0 / 0  / 1 / 1 / 1" ,	"0 / 0 / 1 / 0"))
		self.tipos.append(Tipo("0 / 1 / 1  / 0 / 0 / 1  / 0 / 1 / 0  / 1 / 0 / 0  / 1 / 1 / 1" ,	"0 / 0 / 1 / 0"))
		self.tipos.append(Tipo("0 / 1 / 1  / 0 / 0 / 1  / 1 / 1 / 0  / 1 / 0 / 0  / 1 / 1 / 1" ,	"0 / 0 / 1 / 0"))
		self.tipos.append(Tipo("0 / 1 / 1  / 0 / 0 / 1  / 1 / 1 / 1  / 1 / 0 / 0  / 1 / 1 / 1" ,	"0 / 0 / 1 / 0"))
		self.tipos.append(Tipo("0 / 0 / 0  / 1 / 1 / 1  / 0 / 1 / 0  / 1 / 0 / 0  / 1 / 1 / 1" ,	"0 / 0 / 1 / 0"))
		#3
		self.tipos.append(Tipo("1 / 1 / 1  / 0 / 0 / 1  / 0 / 1 / 1  / 0 / 0 / 1  / 1 / 1 / 1" ,	"0 / 0 / 1 / 1"))
		self.tipos.append(Tipo("1 / 1 / 1  / 0 / 0 / 1  / 1 / 1 / 1  / 0 / 0 / 1  / 1 / 1 / 1" ,	"0 / 0 / 1 / 1"))
		self.tipos.append(Tipo("0 / 1 / 1  / 0 / 0 / 1  / 1 / 1 / 1  / 0 / 0 / 1  / 0 / 1 / 1" ,	"0 / 0 / 1 / 1"))
		self.tipos.append(Tipo("0 / 1 / 1  / 0 / 0 / 1  / 0 / 1 / 1  / 0 / 0 / 1  / 0 / 1 / 1" ,	"0 / 0 / 1 / 1"))
		self.tipos.append(Tipo("0 / 0 / 0  / 1 / 1 / 1  / 0 / 1 / 1  / 0 / 0 / 1  / 1 / 1 / 1" ,	"0 / 0 / 1 / 1"))
		#4
		self.tipos.append(Tipo("1 / 0 / 1  / 1 / 0 / 1  / 1 / 1 / 1  / 0 / 0 / 1  / 0 / 0 / 1" ,	"0 / 1 / 0 / 0"))
		#5
		self.tipos.append(Tipo("1 / 1 / 1  / 1 / 0 / 0  / 1 / 1 / 1  / 0 / 0 / 1  / 1 / 1 / 1" ,	"0 / 1 / 0 / 1"))
		#6
		self.tipos.append(Tipo("1 / 1 / 1  / 1 / 0 / 0  / 1 / 1 / 1  / 1 / 0 / 1  / 1 / 1 / 1" ,	"0 / 1 / 1 / 0"))
		#7
		self.tipos.append(Tipo("1 / 1 / 1  / 0 / 0 / 1  / 0 / 0 / 1  / 0 / 0 / 1  / 0 / 0 / 1" ,	"0 / 1 / 1 / 1"))
		#8
		self.tipos.append(Tipo("1 / 1 / 1  / 1 / 0 / 1  / 1 / 1 / 1  / 1 / 0 / 1  / 1 / 1 / 1" ,	"1 / 0 / 0 / 0"))
		#9
		self.tipos.append(Tipo("1 / 1 / 1  / 1 / 0 / 1  / 1 / 1 / 1  / 0 / 0 / 1  / 1 / 1 / 1" ,	"1 / 0 / 0 / 1"))