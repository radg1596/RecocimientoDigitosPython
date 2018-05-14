from mat import *
import random
archivo=open("wb.txt", "r")

"""
Recibe el numero de renglones y columnas
Retorna una matriz inicializada de manera aleatoria de esas dimesiones
"""
def mat_al(renglones, columnas):
	aux = ""
	for i in range(0,renglones):
		for j in range (0,columnas):
			aux = aux + " " + str(round(random.uniform(-2.5,2.5), 2))
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
Esta clase sólo se encarga de contener los datos de entrenamiento
"""
class Datos():
	w=Matriz(""); b=Matriz("")
	"""DATOS DE ENTRENAMIENTO"""
	def cargar(self):
		self.tipos=[]
		#self.w = mat_al(4,42)
		#self.b = mat_al(4,1)
		self.w = Matriz(archivo.readline())
		self.b = Matriz(archivo.readline())
		##############################################Cero
		self.tipos.append(Tipo(" 0 / 1 / 1 / 1 / 1 / 0 " +
							 "/  1 / 0 / 0 / 0 / 0 / 1 " + 
							 "/  1 / 0 / 0 / 0 / 0 / 1 " +
							 "/  1 / 0 / 0 / 0 / 0 / 1 " + 
							 "/  1 / 0 / 0 / 0 / 0 / 1 " +
							 "/  1 / 0 / 0 / 0 / 0 / 1 " +
							 "/  0 / 1 / 1 / 1 / 1 / 0 " ,		"0 / 0 / 0 / 0"))
							 
		self.tipos.append(Tipo(" 1 / 1 / 1 / 1 / 1 / 1 " +
							 "/  1 / 0 / 0 / 0 / 0 / 1 " + 
							 "/  1 / 0 / 0 / 0 / 0 / 1 " +
							 "/  1 / 0 / 0 / 0 / 0 / 1 " + 
							 "/  1 / 0 / 0 / 0 / 0 / 1 " +
							 "/  1 / 0 / 0 / 0 / 0 / 1 " +
							 "/  1 / 1 / 1 / 1 / 1 / 1 " ,		"0 / 0 / 0 / 0"))
							 
		self.tipos.append(Tipo(" 0 / 0 / 1 / 1 / 0 / 0 " +
							 "/  0 / 1 / 0 / 0 / 1 / 0 " + 
							 "/  1 / 0 / 0 / 0 / 0 / 1 " +
							 "/  1 / 0 / 0 / 0 / 0 / 1 " + 
							 "/  1 / 0 / 0 / 0 / 0 / 1 " +
							 "/  0 / 1 / 0 / 0 / 1 / 0 " +
							 "/  0 / 0 / 1 / 1 / 0 / 0 " ,		"0 / 0 / 0 / 0"))				  
	##############################################Uno	
		self.tipos.append(Tipo(" 0 / 0 / 0 / 1 / 0 / 0 " +
							 "/  0 / 0 / 1 / 1 / 0 / 0 " + 
							 "/  0 / 1 / 0 / 1 / 0 / 0 " +
							 "/  0 / 0 / 0 / 1 / 0 / 0 " + 
							 "/  0 / 0 / 0 / 1 / 0 / 0 " +
							 "/  0 / 0 / 0 / 1 / 0 / 0 " +
							 "/  0 / 1 / 1 / 1 / 1 / 1 " ,		"0 / 0 / 0 / 1"))
							 
		self.tipos.append(Tipo(" 0 / 0 / 0 / 1 / 0 / 0 " +
							 "/  0 / 0 / 1 / 1 / 0 / 0 " + 
							 "/  0 / 1 / 0 / 1 / 0 / 0 " +
							 "/  0 / 0 / 0 / 1 / 0 / 0 " + 
							 "/  0 / 0 / 0 / 1 / 0 / 0 " +
							 "/  0 / 0 / 0 / 1 / 0 / 0 " +
							 "/  0 / 0 / 0 / 1 / 0 / 0 " ,		"0 / 0 / 0 / 1"))
							 
		self.tipos.append(Tipo(" 0 / 0 / 0 / 1 / 0 / 0 " +
							 "/  0 / 0 / 0 / 1 / 0 / 0 " + 
							 "/  0 / 0 / 0 / 1 / 0 / 0 " +
							 "/  0 / 0 / 0 / 1 / 0 / 0 " + 
							 "/  0 / 0 / 0 / 1 / 0 / 0 " +
							 "/  0 / 0 / 0 / 1 / 0 / 0 " +
							 "/  0 / 0 / 0 / 1 / 0 / 0 " ,		"0 / 0 / 0 / 1"))
	##############################################Dos
		self.tipos.append(Tipo(" 0 / 0 / 1 / 1 / 1 / 0 " +
							 "/  0 / 1 / 0 / 0 / 1 / 0 " + 
							 "/  0 / 0 / 0 / 0 / 1 / 0 " +
							 "/  0 / 0 / 0 / 1 / 1 / 0 " + 
							 "/  0 / 0 / 1 / 0 / 0 / 0 " +
							 "/  0 / 1 / 0 / 0 / 0 / 0 " +
							 "/  0 / 1 / 1 / 1 / 1 / 0 " ,		"0 / 0 / 1 / 0"))

		self.tipos.append(Tipo(" 0 / 1 / 1 / 1 / 1 / 0 " +
							 "/  1 / 0 / 0 / 0 / 0 / 1 " + 
							 "/  0 / 0 / 0 / 0 / 1 / 0 " +
							 "/  0 / 0 / 0 / 1 / 0 / 0 " + 
							 "/  0 / 0 / 1 / 0 / 0 / 0 " +
							 "/  0 / 1 / 0 / 0 / 0 / 0 " +
							 "/  1 / 1 / 1 / 1 / 1 / 1 " ,		"0 / 0 / 1 / 0"))

		self.tipos.append(Tipo(" 1 / 1 / 1 / 1 / 1 / 1 " +
							 "/  0 / 0 / 0 / 0 / 0 / 1 " + 
							 "/  0 / 0 / 0 / 0 / 0 / 1 " +
							 "/  1 / 1 / 1 / 1 / 1 / 1 " + 
							 "/  1 / 0 / 0 / 0 / 0 / 0 " +
							 "/  1 / 0 / 0 / 0 / 0 / 0 " +
							 "/  1 / 1 / 1 / 1 / 1 / 1 " ,		"0 / 0 / 1 / 0"))	
	##############################################Tres
		self.tipos.append(Tipo(" 1 / 1 / 1 / 1 / 1 / 1 " +
							 "/  0 / 0 / 0 / 0 / 0 / 1 " + 
							 "/  0 / 0 / 0 / 0 / 0 / 1 " +
							 "/  1 / 1 / 1 / 1 / 1 / 1 " + 
							 "/  0 / 0 / 0 / 0 / 0 / 1 " +
							 "/  0 / 0 / 0 / 0 / 0 / 1 " +
							 "/  1 / 1 / 1 / 1 / 1 / 1 " ,		"0 / 0 / 1 / 1"))

		self.tipos.append(Tipo(" 0 / 1 / 1 / 1 / 1 / 0 " +
							 "/  1 / 0 / 0 / 0 / 0 / 1 " + 
							 "/  0 / 0 / 0 / 0 / 0 / 1 " +
							 "/  0 / 0 / 1 / 1 / 1 / 0 " + 
							 "/  0 / 0 / 0 / 0 / 0 / 1 " +
							 "/  1 / 0 / 0 / 0 / 0 / 1 " +
							 "/  0 / 1 / 1 / 1 / 1 / 0 " ,		"0 / 0 / 1 / 1"))

		self.tipos.append(Tipo(" 0 / 1 / 1 / 1 / 1 / 0 " +
							 "/  0 / 0 / 0 / 0 / 1 / 0 " + 
							 "/  0 / 0 / 0 / 0 / 1 / 0 " +
							 "/  0 / 0 / 1 / 1 / 1 / 0 " + 
							 "/  0 / 0 / 0 / 0 / 1 / 0 " +
							 "/  0 / 0 / 0 / 0 / 1 / 0 " +
							 "/  0 / 1 / 1 / 1 / 1 / 0 " ,		"0 / 0 / 1 / 1"))		
	##############################################Cuatro
		self.tipos.append(Tipo(" 1 / 0 / 0 / 0 / 0 / 1 " +
							 "/  1 / 0 / 0 / 0 / 0 / 1 " + 
							 "/  1 / 0 / 0 / 0 / 0 / 1 " +
							 "/  1 / 1 / 1 / 1 / 1 / 1 " + 
							 "/  0 / 0 / 0 / 0 / 0 / 1 " +
							 "/  0 / 0 / 0 / 0 / 0 / 1 " +
							 "/  0 / 0 / 0 / 0 / 0 / 1 " ,		"0 / 1 / 0 / 0"))
							 
		self.tipos.append(Tipo(" 0 / 0 / 0 / 1 / 1 / 0 " +
							 "/  0 / 0 / 1 / 0 / 1 / 0 " + 
							 "/  0 / 1 / 0 / 0 / 1 / 0 " +
							 "/  1 / 0 / 0 / 0 / 1 / 0 " + 
							 "/  1 / 1 / 1 / 1 / 1 / 1 " +
							 "/  0 / 0 / 0 / 0 / 1 / 0 " +
							 "/  0 / 0 / 0 / 0 / 1 / 0 " ,		"0 / 1 / 0 / 0"))
							 
		self.tipos.append(Tipo(" 0 / 0 / 0 / 0 / 1 / 0 " +
							 "/  0 / 0 / 0 / 1 / 1 / 0 " + 
							 "/  0 / 0 / 1 / 0 / 1 / 0 " +
							 "/  0 / 1 / 0 / 0 / 1 / 0 " + 
							 "/  1 / 1 / 1 / 1 / 1 / 0 " +
							 "/  0 / 0 / 0 / 0 / 1 / 0 " +
							 "/  0 / 0 / 0 / 0 / 1 / 0 " ,		"0 / 1 / 0 / 0"))
	##############################################Cinco
		self.tipos.append(Tipo(" 1 / 1 / 1 / 1 / 1 / 1 " +
							 "/  1 / 0 / 0 / 0 / 0 / 0 " + 
							 "/  1 / 0 / 0 / 0 / 0 / 0 " +
							 "/  1 / 1 / 1 / 1 / 1 / 1 " + 
							 "/  0 / 0 / 0 / 0 / 0 / 1 " +
							 "/  0 / 0 / 0 / 0 / 0 / 1 " +
							 "/  1 / 1 / 1 / 1 / 1 / 1 " ,		"0 / 1 / 0 / 1"))
							 
		self.tipos.append(Tipo(" 1 / 1 / 1 / 1 / 1 / 1 " +
							 "/  1 / 0 / 0 / 0 / 0 / 0 " + 
							 "/  1 / 0 / 0 / 0 / 0 / 0 " +
							 "/  0 / 1 / 1 / 1 / 1 / 0 " + 
							 "/  0 / 0 / 0 / 0 / 0 / 1 " +
							 "/  0 / 0 / 0 / 0 / 0 / 1 " +
							 "/  1 / 1 / 1 / 1 / 1 / 0 " ,		"0 / 1 / 0 / 1"))
							 
		self.tipos.append(Tipo(" 0 / 1 / 1 / 1 / 1 / 0 " +
							 "/  0 / 1 / 0 / 0 / 0 / 0 " + 
							 "/  0 / 1 / 1 / 1 / 0 / 0 " +
							 "/  0 / 0 / 0 / 0 / 1 / 0 " + 
							 "/  0 / 0 / 0 / 0 / 1 / 0 " +
							 "/  0 / 1 / 0 / 0 / 1 / 0 " +
							 "/  0 / 0 / 1 / 1 / 0 / 0 " ,		"0 / 1 / 0 / 1"))

		archivo.close()

		
		
"""Pivote
		self.tipos.append(Tipo(" 0 / 0 / 0 / 0 / 0 / 0 " +
							 "/  0 / 0 / 0 / 0 / 0 / 0 " + 
							 "/  0 / 0 / 0 / 0 / 0 / 0 " +
							 "/  0 / 0 / 0 / 0 / 0 / 0 " + 
							 "/  0 / 0 / 0 / 0 / 0 / 0 " +
							 "/  0 / 0 / 0 / 0 / 0 / 0 " +
							 "/  0 / 0 / 0 / 0 / 0 / 0 " ,		"0 / 0 / 0 / 0"))
	"""		
		
		
		
		
		
		
		
