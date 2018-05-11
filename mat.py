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
		temp=""
		if self.renglones==matb.renglones and self.columnas==matb.columnas:
			for i in range(0,self.renglones):
					for j in range(0,self.columnas):
						temp=temp + str (float(self.numeros[i][j])+float(matb.numeros[i][j])) + " "
					temp=temp+"/ " if i!=self.renglones-1 else temp+" "
			return Matriz(temp)
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
		columnas=self.renglones
		renglones=self.columnas
		temp=""
		for i in range(0, renglones):
			for columna in self.numeros:
				temp=temp+ columna[i]+" "
			temp=temp+"/ " if i!=renglones-1 else temp+" "
		return Matriz(temp)
	"""
	Método mult
	Se encarga de hacer la multiplicación de dos matrices de orden compatible
	Recibe como parametro una matrizB 
	Retorna una matrizC tal que
		matrizC = matrizA*matrizB
		(La matrizA es la instancia)
	"""	
	def mult(self, matb):
		sum_temp=0; temp=""; contador=0
		if self.columnas==matb.renglones:
			mat_aux=matb.transponer()
			for renglon in self.numeros:
				for columna in mat_aux.numeros:
					for i in range (0, mat_aux.columnas):
						sum_temp=sum_temp+ (float(renglon[i]) * float(columna[i]))
					temp=temp+str(sum_temp)+" "
					sum_temp=0
				temp=temp+"/ " if contador!=len(self.numeros)-1 else temp+" "
				contador+=1
			return Matriz(temp)
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
		temp=""
		contador=0
		for renglon in self.numeros:
			for elemento in renglon:
				if (float(elemento)>=0.0):
					temp+="1 "
				else:
					temp+="0 "
			contador+=1
			temp=temp+"/ " if contador!=len(self.numeros) else temp+" "
		return Matriz(temp)
		
	def m_esc(self, escalar):
		temp=""
		contador=0
		for renglon in self.numeros:
			for elemento in renglon:
				temp+=str(float(elemento)*escalar)+" "
			contador+=1
			temp=temp+"/ " if contador!=len(self.numeros) else temp+" "
		return Matriz(temp)

















