from mat import *
import random
archivo=open("wb.txt", "r")

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
		#self.w = mat_al(4,15)
		#self.b = mat_al(4,1)
		self.w = Matriz(archivo.readline())
		self.b = Matriz(archivo.readline())
		############################Numero cero
		self.tipos.append(Tipo(" 1 / 1 / 1  " +
							 "/  1 / 0 / 1  " + 
							 "/  1 / 0 / 1  " +
							 "/  1 / 0 / 1  " +
							 "/  1 / 1 / 1  " ,		"0 / 0 / 0 / 0"))
							 
		self.tipos.append(Tipo(" 0 / 0 / 0  " + 
							  "/ 1 / 1 / 1  " +
							  "/ 1 / 0 / 1  " +
							  "/ 1 / 0 / 1  " +
							  "/ 1 / 1 / 1  " ,		"0 / 0 / 0 / 0"))
							  
		self.tipos.append(Tipo(" 1 / 1 / 1  " +
							  "/ 1 / 0 / 1  " +
							  "/ 1 / 0 / 1  " +
							  "/ 1 / 1 / 1  " +
							  "/ 0 / 0 / 0  " ,		"0 / 0 / 0 / 0"))
							  
		self.tipos.append(Tipo(" 0 / 0 / 0  " +
							  "/ 1 / 1 / 1  " +
							  "/ 1 / 0 / 1  " +
							  "/ 1 / 1 / 1  " +
							  "/ 0 / 0 / 0  " ,		"0 / 0 / 0 / 0"))
							  
		self.tipos.append(Tipo(" 0 / 0 / 0  " +
							  "/ 0 / 0 / 0  " +
							  "/ 1 / 1 / 1  " +
							  "/ 1 / 0 / 1  " +
							  "/ 1 / 1 / 1  " ,		"0 / 0 / 0 / 0"))
		#######################Numero uno
		self.tipos.append(Tipo(" 0 / 0 / 1  " +
							  "/ 0 / 0 / 1  " + 
							  "/ 0 / 0 / 1  " + 
							  "/ 0 / 0 / 1  " + 
							  "/ 0 / 0 / 1  " ,		"0 / 0 / 0 / 1"))
	
		self.tipos.append(Tipo(" 0 / 1 / 0  " +
							  "/ 0 / 1 / 0  " + 
							  "/ 0 / 1 / 0  " + 
							  "/ 0 / 1 / 0  " + 
							  "/ 0 / 1 / 0  " ,		"0 / 0 / 0 / 1"))
							  
		self.tipos.append(Tipo(" 1 / 0 / 0  " +
							  "/ 1 / 0 / 0  " + 
							  "/ 1 / 0 / 0  " + 
							  "/ 1 / 0 / 0  " +
							  "/ 1 / 0 / 0  " ,		"0 / 0 / 0 / 1"))
		
		self.tipos.append(Tipo(" 0 / 0 / 1  " + 
							  "/ 0 / 1 / 1  " +
							  "/ 0 / 0 / 1  " + 
							  "/ 0 / 0 / 1  " +
							  "/ 0 / 0 / 1  " ,		"0 / 0 / 0 / 1"))
							  
		self.tipos.append(Tipo(" 0 / 1 / 0  " + 
							  "/ 1 / 1 / 0  " + 
							  "/ 0 / 1 / 0  " +
							  "/ 0 / 1 / 0  " +
							  "/ 0 / 1 / 0  " ,		"0 / 0 / 0 / 1"))
							  
		self.tipos.append(Tipo(" 0 / 1 / 0  " + 
							  "/ 1 / 1 / 0  " + 
							  "/ 0 / 1 / 0  " + 
							  "/ 0 / 1 / 0  " +
							  "/ 1 / 1 / 1  " ,		"0 / 0 / 0 / 1"))
		
		self.tipos.append(Tipo(" 0 / 0 / 0  " + 
						      "/ 0 / 1 / 0  " + 
							  "/ 1 / 1 / 0  " +
							  "/ 0 / 1 / 0  " +
							  "/ 0 / 1 / 0  ",		"0 / 0 / 0 / 1"))
						  
		self.tipos.append(Tipo(" 0 / 0 / 0  " + 
							  "/ 0 / 0 / 1  " + 
							  "/ 0 / 0 / 1  " + 
							  "/ 0 / 0 / 1  " +
							  "/ 0 / 0 / 1  " ,		"0 / 0 / 0 / 1"))
							  
		self.tipos.append(Tipo(" 0 / 0 / 0  " + 
							  "/ 0 / 1 / 0  " + 
							  "/ 0 / 1 / 0  " + 
							  "/ 0 / 1 / 0  " +
							  "/ 0 / 1 / 0  " ,		"0 / 0 / 0 / 1"))
							  
		self.tipos.append(Tipo(" 0 / 0 / 0  " + 
							  "/ 1 / 0 / 0  " + 
							  "/ 1 / 0 / 0  " + 
							  "/ 1 / 0 / 0  " +
							  "/ 1 / 0 / 0  " ,		"0 / 0 / 0 / 1"))
		#############################Numero dos
		self.tipos.append(Tipo(" 1 / 1 / 1  " +
							  "/ 0 / 0 / 1  " +
							  "/ 1 / 1 / 1  " +
							  "/ 1 / 0 / 0  " + 
							  "/ 1 / 1 / 1  " ,		"0 / 0 / 1 / 0"))
							  
		self.tipos.append(Tipo(" 1 / 1 / 1  " + 
							  "/ 0 / 0 / 1  " +
							  "/ 0 / 1 / 0  " + 
							  "/ 1 / 0 / 0  " + 
							  "/ 1 / 1 / 1  " ,		"0 / 0 / 1 / 0"))
							  
		self.tipos.append(Tipo(" 0 / 1 / 1  " +
							  "/ 0 / 0 / 1  " +
							  "/ 0 / 1 / 0  " +
							  "/ 1 / 0 / 0  " + 
							  "/ 1 / 1 / 1  " ,		"0 / 0 / 1 / 0"))
							  
		self.tipos.append(Tipo(" 0 / 1 / 1  " + 
						      "/ 0 / 0 / 1  " + 
							  "/ 1 / 1 / 0  " +
							  "/ 1 / 0 / 0  " +
							  "/ 1 / 1 / 1  " ,		"0 / 0 / 1 / 0"))
							  
		self.tipos.append(Tipo(" 0 / 1 / 1  " +
							  "/ 0 / 0 / 1  " +
							  "/ 1 / 1 / 1  " +
							  "/ 1 / 0 / 0  " + 
							  "/ 1 / 1 / 1  " ,		"0 / 0 / 1 / 0"))
							  
		self.tipos.append(Tipo(" 0 / 0 / 0  " + 
							  "/ 1 / 1 / 1  " +
							  "/ 0 / 1 / 0  " +
							  "/ 1 / 0 / 0  " +
							  "/ 1 / 1 / 1  " ,		"0 / 0 / 1 / 0"))
		############################Numero tres
		self.tipos.append(Tipo(" 1 / 1 / 1  " + 
							  "/ 0 / 0 / 1  " +
							  "/ 0 / 1 / 1  " + 
							  "/ 0 / 0 / 1  " +
							  "/ 1 / 1 / 1  " ,		"0 / 0 / 1 / 1"))
							 
		self.tipos.append(Tipo(" 1 / 1 / 1  " +
							  "/ 0 / 0 / 1  " +
							  "/ 1 / 1 / 1  " +
							  "/ 0 / 0 / 1  " + 
							  "/ 1 / 1 / 1  " ,		"0 / 0 / 1 / 1"))
							  
		self.tipos.append(Tipo(" 0 / 1 / 1  " +
							  "/ 0 / 0 / 1  " +
							  "/ 1 / 1 / 1  " +
							  "/ 0 / 0 / 1  " +
							  "/ 0 / 1 / 1  " ,		"0 / 0 / 1 / 1"))
							  
		self.tipos.append(Tipo(" 0 / 1 / 1  " +
							  "/ 0 / 0 / 1  " +
							  "/ 0 / 1 / 1  " +
							  "/ 0 / 0 / 1  " +
							  "/ 0 / 1 / 1  " ,		"0 / 0 / 1 / 1"))
							  
		self.tipos.append(Tipo(" 0 / 0 / 0  " +
							  "/ 1 / 1 / 1  " +
							  "/ 0 / 1 / 1  " +
							  "/ 0 / 0 / 1  " +
							  "/ 1 / 1 / 1  " ,		"0 / 0 / 1 / 1"))
		##########################Numero cuatro
		self.tipos.append(Tipo(" 1 / 0 / 1  " +
							  "/ 1 / 0 / 1  " +
							  "/ 1 / 1 / 1  " +
							  "/ 0 / 0 / 1  " +
							  "/ 0 / 0 / 1  " ,		"0 / 1 / 0 / 0"))
		###########################Numero cinco
		self.tipos.append(Tipo(" 1 / 1 / 1  " +
							  "/ 1 / 0 / 0  " +
							  "/ 1 / 1 / 1  " +
							  "/ 0 / 0 / 1  " +
							  "/ 1 / 1 / 1  " ,		"0 / 1 / 0 / 1"))
		############################Numero seis
		self.tipos.append(Tipo(" 1 / 1 / 1  " +
							  "/ 1 / 0 / 0  " +
							  "/ 1 / 1 / 1  " +
							  "/ 1 / 0 / 1  " +
							  "/ 1 / 1 / 1  " ,		"0 / 1 / 1 / 0"))
		###########################Numero siete
		self.tipos.append(Tipo(" 1 / 1 / 1  " +
							  "/ 0 / 0 / 1  " +
							  "/ 0 / 0 / 1  " +
							  "/ 0 / 0 / 1  " +
							  "/ 0 / 0 / 1  " ,		"0 / 1 / 1 / 1"))
		############################Numero ocho
		self.tipos.append(Tipo(" 1 / 1 / 1  " +
							  "/ 1 / 0 / 1  " +
							  "/ 1 / 1 / 1  " +
							  "/ 1 / 0 / 1  " +
							  "/ 1 / 1 / 1  " ,		"1 / 0 / 0 / 0"))
		###########################Numero nueve
		self.tipos.append(Tipo(" 1 / 1 / 1  " +
							  "/ 1 / 0 / 1  " +
							  "/ 1 / 1 / 1  " +
							  "/ 0 / 0 / 1  " +
							  "/ 1 / 1 / 1  " ,		"1 / 0 / 0 / 1"))
		archivo.close()

		
		
		
		
		
		
		

#mat = Matriz(archivo.readline())
#mat = Matriz(archivo.readline())
#print (mat)		
		
		
		
		
