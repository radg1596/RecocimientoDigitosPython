from datos import *
"""
Abstración de la red neuronal como un objeto.
Puede entrenarse a partir de un conjunto de datos mediante
	el algoritmo de aprendizaje de perceptrón.
Después de entrenarse estará lista para reconocer vectores
	de entrada.
"""
class Red():
	"""
	Entrena a la red
	Recibe un W y una b iniciales. Así como una lista de tipos	
		con su t y p.
	Guarda la configuración final de W y b cuando converge el algoritmo.
	"""
	def entrenar(self, lista):
		ite=1; e_cero=0; w=lista[0]; b=lista[1]; tipos=lista[2]
		while e_cero!=len(tipos) and ite<99999999:
			for tipo in tipos:
				if e_cero==len(tipos) or ite>100000000:
					break
				else:
					print("Iteracion "+ str(ite) + ": " + str(e_cero))
					a = ( (w*tipo.p)+b ).hardlim()
					e = tipo.t-a
					if e.null()==True:
						e_cero+=1
					else:
						e_cero=0
						w = w + ( e*(tipo.p.transponer()) )
						b = b+e
					ite+=1
		archivo=open("wb.txt", "w+")
		self.w=w; self.b=b
		archivo.write(self.w.to_s() + "\n" + self.b.to_s())
		archivo.close()
		print("***********Se ha entrenado a la red************")
	"""

	"""	
	def __imprimir_aux(self, e, w, b, ite):
		print("\ne("+str(ite)+") = \n"+ e)
		print("\nW("+str(ite)+") = \n"+ w)
		print("\nb("+str(ite)+") = \n"+ b)
	"""
	Se encarga de reconocer un vector de entrada.
	Recibe una matriz de entrada
	Devuelve f(wp+b), es decir a
	"""	 
	def reconocer(self, entrada):
		a=( (self.w*entrada)+(self.b) ).hardlim()
		return a.transponer()