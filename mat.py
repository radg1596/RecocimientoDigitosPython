from math import *
"""
Matriz
Módulo de matrices construido por nosotros, hecho según nuestras necesidades.
"""
"""
Clase Matriz
Está clase está diseñada para representar a cualquier matriz de orden NxM
Se definieron los siguientes atributos:
	-renglones: número de renglones
	-columnas: número de columnas
	-numeros: Es una lista que contiene los renglones de la matriz
	Por ejemplo:
		La matriz:
			1 0 2 
			3 8 2
		Tendría los siguientes atributos:
			renglones=2
			columnas=3
			numeros= [[1 0 2 ], [3 8 2]]
	
Se definieron los siguientes métodos:
	-imprimir
	-sum: Suma
	-rest: Resta
	-transponer: Matriz transpuesta
	-mult: Multiplicación
	-null: Comprobar sí la matriz contiene sólo ceros
	-hardlim: Obtiene el hardlim de la matriz
	
"""
class Matriz():
	"""
	Método init
	Se encarga de inicializar una matriz. 
	Recibe como parámetro una cadena en el siguiente formato:
		"0 1 2 / 2 3 4 / 9 0 4"
		cada símbolo "/" significa un salto de renglón, por ejemplo,
		la cadena anterior representa la matriz:
			0 1 2
			2 3 4
			9 0 4
	No retorna nada.
	"""
	def __init__(self, contenido):
		self.numeros=[]
		self.renglones=1
		self.columnas= len(contenido.split()) if contenido.find('/')<0 else contenido.split().index('/')
		aux=[]
		for elemento in contenido.split():
			if elemento=='/':
				self.numeros.append(aux)
				self.renglones=self.renglones+1
				aux=[]
			else:
				aux.append(elemento)
		if contenido!="":		
			self.numeros.append(aux)
	"""
	Método imprimir
	Se encarga de desplegar en pantalla una matriz.
	No recibe ningún parámetro. 
	Retorna la matriz como una cadena.
	"""
	def imprimir(self):
		if self.renglones==1 and self.columnas==1:
			aux=""+str(self.numeros[0][0])+"\n"
		else:
			aux="|"
			for renglon in self.numeros:
				for elemento in renglon:
					aux=aux+"  "+elemento
				aux=aux+"  | \n|"
			aux=aux[0:len(aux)-1]
		return aux
	"""
	Método sum
	Se encarga de hacer la suma de dos matrices (A y B) del mismo orden.
	Recibe como parámetro una matrizB
	Retorna una matrizC, la cuál es la suma de la instancia con la matrizB.
		matC=matA + matB
	"""
	def sum(self, matb):
		mat_c = Matriz("")
		if self.renglones==matb.renglones and self.columnas==matb.columnas:
			mat_c.renglones = self.renglones; mat_c.columnas = self.columnas
			for i in range(0,self.renglones):
					renglon = []
					for j in range(0,self.columnas):
						renglon.append( str (float(self.numeros[i][j])+float(matb.numeros[i][j])) )
					mat_c.numeros.append(renglon)
			#print(mat_c.imprimir())
			return mat_c
	"""
	Método rest
	Se encarga de hacer la resta de dos matrices (A y B) del mismo orden.
	Recibe como parámetro una matrizB
	Retorna una matrizC, la cuál es la resta de la instancia con la matrizB.
		matrizC= matrizA - matrizB
	"""			
	def rest(self, matb):
		return self.sum(matb.m_esc(-1))
	"""
	Método transponer
	No recibe ningún parámetro.
	Se encarga de transponer una matriz.
	Retorna la matriz transpuesta 
	"""	
	def transponer(self):
		mat_t = Matriz("")
		mat_t.columnas=self.renglones
		mat_t.renglones=self.columnas
		for i in range(0, mat_t.renglones):
			renglon = []
			for columna in self.numeros:
				renglon.append(columna[i])
			mat_t.numeros.append(renglon)
		return mat_t
	"""
	Método mult
	Se encarga de hacer la multiplicación de dos matrices de orden compatible
	Recibe como parametro una matrizB 
	Retorna una matrizC tal que
		matrizC = matrizA*matrizB
		(La matrizA es la instancia)
	"""	
	def mult(self, matb):
		mat_c = Matriz("") 
		mat_c.renglones = self.renglones ;mat_c.columnas = matb.columnas
		sum_temp=0
		if self.columnas==matb.renglones:
			mat_aux=matb.transponer()
			for renglon in self.numeros:
				r_temp = []
				for columna in mat_aux.numeros:
					for i in range (0, mat_aux.columnas):
						sum_temp=sum_temp+ (float(renglon[i]) * float(columna[i]))
					r_temp.append(str(sum_temp))
					sum_temp=0
				mat_c.numeros.append(r_temp)
			return mat_c
	"""
	Método null
	Se encarga de indicarnos si una matriz está llena de ceros.
	Retorna un valor entero dependiendo del resultado:
		1 si la matriz está llena de ceros
		0 sino lo está
	No recibe parámetros.
	"""	
	def null(self):
		nulo=1
		for renglon in self.numeros:
			for elemento in renglon:
				if float(elemento)!=0.0:
					nulo=0
					break
		return nulo
	"""	
	Método hardlim
	Obtiene el hardlim de una matriz
	No recibe parametro
	Retorna la matriz hardlim
	"""
	def hardlim(self):
		mat_h = Matriz("")
		mat_h.renglones = self.renglones ;mat_h.columnas = self.columnas
		for renglon in self.numeros:
			r_temp = []
			for elemento in renglon:
				if (float(elemento)>=0.0):
					r_temp.append("1")
				else:
					r_temp.append("0")
			mat_h.numeros.append(r_temp)
		return mat_h
	"""Método multiplicar por un escalar
	recibe una matriz como parámetro y un escalar
	retorna la matriz recibida multiplicada por el escalar
	"""	
	def m_esc(self, escalar):
		mat_e = Matriz("")
		mat_e.renglones = self.renglones ;mat_e.columnas = self.columnas
		for renglon in self.numeros:
			r_temp = []
			for elemento in renglon:
				r_temp.append( str(float(elemento)*escalar) )
			mat_e.numeros.append(r_temp)
		return mat_e












