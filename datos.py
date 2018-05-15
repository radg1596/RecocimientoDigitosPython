from mat import *
import random

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
Recibe una cadena en binario
Retorna su equivalente en decimal
"""
def bin_dec(numero):
	acum = 0
	i = 0
	lista = numero.split()
	for e in lista[::-1]:
		acum = acum + float(e)*(2**i)
		i = i+1
	if acum>9:
		return 0
	return int(acum)
	
"""
Clase TIPO
Cada tipo tiene su matriz de entrada así como su target
"""
class Tipo():
	def __init__(self, p, t):
		self.p=Matriz(p
			) 
		self.t=Matriz(t)

		
"""
Esta clase sólo se encarga de contener los datos de entrenamiento
"""
class Datos():
	"""
	Simplifica el proceso de introducir los datos de entrenamiento.
	"""
	def cad_fm(self, cadena):
		aux = ""
		for i in range(0,len(cadena)):
			if cadena[i] == ".":
				aux = aux + " " + "0" + " /"
			else:
				aux = aux + " " + cadena[i] + " /"
		return aux[0:len(aux)-1]
	"""DATOS DE ENTRENAMIENTO"""
	def cargar(self):
		archivo=open("wb.txt", "r")
		self.tipos=[]
		#self.w = mat_al(4,42)
		#self.b = mat_al(4,1)
		self.w = Matriz(archivo.readline())
		self.b = Matriz(archivo.readline())
		##############################################Cero
		self.tipos.append(Tipo (self.cad_fm (
							 ".1111." +
							 "1....1" + 
							 "1....1" +
							 "1....1" + 
							 "1....1" +
							 "1....1" +
							 ".1111." ) ,		"0 / 0 / 0 / 0"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 "111111" +
							 "1....1" + 
							 "1....1" +
							 "1....1" + 
							 "1....1" +
							 "1....1" +
							 "111111" ) ,		"0 / 0 / 0 / 0"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 "..11.." +
							 ".1..1." + 
							 "1....1" +
							 "1....1" + 
							 "1....1" +
							 ".1..1." +
							 "..11.." ) ,		"0 / 0 / 0 / 0"))

		self.tipos.append(Tipo (self.cad_fm (
							 "1111.." +
							 "1..1.." + 
							 "1..1.." +
							 "1..1.." + 
							 "1..1.." +
							 "1..1.." +
							 "1111.." ) ,		"0 / 0 / 0 / 0"))	

		self.tipos.append(Tipo (self.cad_fm (
							 "..1111" +
							 "..1..1" + 
							 "..1..1" +
							 "..1..1" + 
							 "..1..1" +
							 "..1..1" +
							 "..1111" ) ,		"0 / 0 / 0 / 0"))

		self.tipos.append(Tipo (self.cad_fm (
							 ".1111." +
							 ".1..1." + 
							 ".1..1." +
							 ".1..1." + 
							 ".1..1." +
							 ".1..1." +
							 ".1111." ) ,		"0 / 0 / 0 / 0"))	

		self.tipos.append(Tipo (self.cad_fm (
							 ".1111." +
							 ".1..1." + 
							 ".1..1." +
							 ".1.11." + 
							 ".11.1." +
							 ".1..1." +
							 ".1111." ) ,		"0 / 0 / 0 / 0"))

		self.tipos.append(Tipo (self.cad_fm (
							 "......" +
							 "..11.." + 
							 ".1..1." +
							 ".1..1." + 
							 ".1..1." +
							 ".1..1." +
							 "..11.." ) ,		"0 / 0 / 0 / 0"))

		self.tipos.append(Tipo (self.cad_fm (
							 "..11.." +
							 ".1..1." + 
							 ".1..1." +
							 ".1..1." + 
							 ".1..1." +
							 ".1..1." +
							 "..11.." ) ,		"0 / 0 / 0 / 0"))		

	##############################################Uno	
		self.tipos.append(Tipo (self.cad_fm (
							 "...1.." +
							 "..11.." + 
							 ".1.1.." +
							 "...1.." + 
							 "...1.." +
							 "...1.." +
							 "...1.." ) ,		"0 / 0 / 0 / 1"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 "...1.." +
							 "..11.." + 
							 ".1.1.." +
							 "...1.." + 
							 "...1.." +
							 "...1.." +
							 ".11111" ) ,		"0 / 0 / 0 / 1"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 "1....." +
							 "1....." + 
							 "1....." +
							 "1....." + 
							 "1....." +
							 "1....." +
							 "1....." ) ,		"0 / 0 / 0 / 1"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 ".1...." +
							 ".1...." + 
							 ".1...." +
							 ".1...." + 
							 ".1...." +
							 ".1...." +
							 ".1...." ) ,		"0 / 0 / 0 / 1"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 "..1..." +
							 "..1..." + 
							 "..1..." +
							 "..1..." + 
							 "..1..." +
							 "..1..." +
							 "..1..." ) ,		"0 / 0 / 0 / 1"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 "...1.." +
							 "...1.." + 
							 "...1.." +
							 "...1.." + 
							 "...1.." +
							 "...1.." +
							 "...1.." ) ,		"0 / 0 / 0 / 1"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 "....1." +
							 "....1." + 
							 "....1." +
							 "....1." + 
							 "....1." +
							 "....1." +
							 "....1." ) ,		"0 / 0 / 0 / 1"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 ".....1" +
							 ".....1" + 
							 ".....1" +
							 ".....1" + 
							 ".....1" +
							 ".....1" +
							 ".....1" ) ,		"0 / 0 / 0 / 1"))

		self.tipos.append(Tipo (self.cad_fm (
							 "......" +
							 "...1.." + 
							 "..11.." +
							 "...1.." + 
							 "...1.." +
							 "..111." +
							 "......" ) ,		"0 / 0 / 0 / 1"))	

	##############################################Dos
		self.tipos.append(Tipo (self.cad_fm (
							 "..11.." +
							 ".1..1." + 
							 "1....1" +
							 "....1." + 
							 "...1.." +
							 "..1..." +
							 "111111" ) ,		"0 / 0 / 1 / 0"))

		self.tipos.append(Tipo (self.cad_fm (
							 ".1111." +
							 "1....1" + 
							 ".....1" +
							 "..111." + 
							 ".1...." +
							 ".11111" +
							 "......" ) ,		"0 / 0 / 1 / 0"))

		self.tipos.append(Tipo (self.cad_fm (
							 "111111" +
							 ".....1" + 
							 ".....1" +
							 "111111" + 
							 "1....." +
							 "1....." +
							 "111111" ) ,		"0 / 0 / 1 / 0"))

		self.tipos.append(Tipo (self.cad_fm (
							 "......" +
							 "..11.." + 
							 ".1..1." +
							 "....1." + 
							 "...1.." +
							 "..1..." +
							 ".1111." ) ,		"0 / 0 / 1 / 0"))

		self.tipos.append(Tipo (self.cad_fm (
							 "......" +
							 ".1111." + 
							 "....1." +
							 ".1111." + 
							 ".1...." +
							 ".11111" +
							 "......" ) ,		"0 / 0 / 1 / 0"))

		self.tipos.append(Tipo (self.cad_fm (
							 "......" +
							 "..11.." + 
							 ".1..1." +
							 "...1.." + 
							 "..1..." +
							 ".1111." +
							 "......" ) ,		"0 / 0 / 1 / 0"))


							 
	##############################################Tres
		self.tipos.append(Tipo (self.cad_fm (
							 "111111" +
							 ".....1" + 
							 ".....1" +
							 "111111" + 
							 ".....1" +
							 ".....1" +
							 "111111" ) ,		"0 / 0 / 1 / 1"))

		self.tipos.append(Tipo (self.cad_fm (
							 ".1111." +
							 "1....1" + 
							 ".....1" +
							 "..111." + 
							 ".....1" +
							 "1....1" +
							 ".1111." ) ,		"0 / 0 / 1 / 1"))

		self.tipos.append(Tipo (self.cad_fm (
							 ".1111." +
							 "....1." + 
							 "....1." +
							 "..111." + 
							 "....1." +
							 "....1." +
							 ".1111." ) ,		"0 / 0 / 1 / 1"))

		self.tipos.append(Tipo (self.cad_fm (
							 "......" +
							 ".111.." + 
							 "....1." +
							 "..111." + 
							 "....1." +
							 ".111.." +
							 "......" ) ,		"0 / 0 / 1 / 1"))		
	##############################################Cuatro
		self.tipos.append(Tipo (self.cad_fm (
							 "1....1" +
							 "1....1" + 
							 "1....1" +
							 "111111" + 
							 ".....1" +
							 ".....1" +
							 ".....1" ) ,		"0 / 1 / 0 / 0"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 "....1." +
							 "...11." + 
							 "..1.1." +
							 ".1..1." + 
							 "111111" +
							 "....1." +
							 "....1." ) ,		"0 / 1 / 0 / 0"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 "....1." +
							 "...11." + 
							 "..1.1." +
							 ".1..1." + 
							 "11111." +
							 "....1." +
							 "....1." ) ,		"0 / 1 / 0 / 0"))

	##############################################Cinco
		self.tipos.append(Tipo (self.cad_fm (
							 "111111" +
							 "1....." + 
							 "1....." +
							 "111111" + 
							 ".....1" +
							 ".....1" +
							 "111111" ) ,		"0 / 1 / 0 / 1"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 ".1111." +
							 "1....." + 
							 "1....." +
							 "11111." + 
							 ".....1" +
							 ".....1" +
							 "11111." ) ,		"0 / 1 / 0 / 1"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 "......" +
							 ".1111." + 
							 ".1...." +
							 ".1111." + 
							 ".....1" +
							 ".1111." +
							 "......" ) ,		"0 / 1 / 0 / 1"))
	##############################################Seis
		self.tipos.append(Tipo (self.cad_fm (
							 "111111" +
							 "1....." + 
							 "1....." +
							 "111111" + 
							 "1....1" +
							 "1....1" +
							 "111111" ) ,		"0 / 1 / 1 / 0"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 ".1111." +
							 "1....1" + 
							 "1....." +
							 "11111." + 
							 "1....1" +
							 "1....1" +
							 ".1111." ) ,		"0 / 1 / 1 / 0"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 "......" +
							 ".1111." + 
							 ".1...." +
							 ".1111." + 
							 ".1..1." +
							 ".1111." +
							 "......" ) ,		"0 / 1 / 1 / 0"))
	##############################################Siete
		self.tipos.append(Tipo (self.cad_fm (
							 "111111" +
							 ".....1" + 
							 ".....1" +
							 ".....1" + 
							 ".....1" +
							 ".....1" +
							 ".....1" ) ,		"0 / 1 / 1 / 1"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 "111111" +
							 ".....1" + 
							 ".....1" +
							 "..1111" + 
							 ".....1" +
							 ".....1" +
							 ".....1" ) ,		"0 / 1 / 1 / 1"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 "111111" +
							 ".....1" + 
							 "....1." +
							 "...1.." + 
							 "..1..." +
							 ".1...." +
							 "1....." ) ,		"0 / 1 / 1 / 1"))

	##############################################Ocho
		self.tipos.append(Tipo (self.cad_fm (
							 "111111" +
							 "1....1" + 
							 "1....1" +
							 "111111" + 
							 "1....1" +
							 "1....1" +
							 "111111" ) ,		"1 / 0 / 0 / 0"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 ".1111." +
							 "1....1" + 
							 "1....1" +
							 ".1111." + 
							 "1....1" +
							 "1....1" +
							 ".1111." ) ,		"1 / 0 / 0 / 0"))

		self.tipos.append(Tipo (self.cad_fm (
							 "......" +
							 ".1111." + 
							 ".1..1." +
							 ".1111." + 
							 ".1..1." +
							 ".1111." +
							 "......" ) ,		"1 / 0 / 0 / 0"))

		self.tipos.append(Tipo (self.cad_fm (
							 "..11.." +
							 ".1..1." + 
							 ".1..1." +
							 "..11.." + 
							 ".1..1." +
							 ".1..1." +
							 "..11.." ) ,		"1 / 0 / 0 / 0"))

	##############################################Nueve
		self.tipos.append(Tipo (self.cad_fm (
							 "111111" +
							 "1....1" + 
							 "1....1" +
							 "111111" + 
							 ".....1" +
							 ".....1" +
							 "111111" ) ,		"1 / 0 / 0 / 1"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 "111111" +
							 "1....1" + 
							 "1....1" +
							 "111111" + 
							 ".....1" +
							 ".....1" +
							 ".....1" ) ,		"1 / 0 / 0 / 1"))
							 
		self.tipos.append(Tipo (self.cad_fm (
							 ".1111." +
							 "1....1" + 
							 "1....1" +
							 ".11111" + 
							 ".....1" +
							 "1....1" +
							 ".1111." ) ,		"1 / 0 / 0 / 1"))

		self.tipos.append(Tipo (self.cad_fm (
							 "......" +
							 ".1111." + 
							 ".1..1." +
							 ".1111." + 
							 "....1." +
							 "....1." +
							 "......" ) ,		"1 / 0 / 0 / 1"))

		archivo.close()
		return [self.w,self.b,self.tipos]

		
		
"""Prototipo
		self.tipos.append(Tipo (self.cad_fm (
							 "......" +
							 "......" + 
							 "......" +
							 "......" + 
							 "......" +
							 "......" +
							 "......" ) ,		"0 / 0 / 0 / 0"))
	"""		
		
		
		
		
		
		
		
