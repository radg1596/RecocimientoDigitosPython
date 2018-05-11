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
	def entrenar(self,lista):
		ite=1; e_cero=0; w=lista[0]; b=lista[1]; tipos=lista[2]
		while e_cero!=len(tipos) and ite<39999:
			for tipo in tipos:
				if e_cero==len(tipos) or ite>40000:
					break
				else:
					print("Iteracion "+ str(ite) + ": ")
					a=w.mult(tipo.p).sum(b).hardlim()
					e=tipo.t.rest(a)
					if e.null()==1:
						e_cero+=1
					else:
						e_cero=0
						w=w.sum( e.mult(tipo.p.transponer()) )
						b=b.sum(e)
					#self.__imprimir_aux(e, w, b, ite)
					ite+=1
		self.w=w; self.b=b;
	"""
	Se encarga de imprimir W, b y e de cada iteración.
	Recibe como parametro W, b y e
	No devuelve nada.
	"""	
	def __imprimir_aux(self, e, w, b, ite):
		print("\ne("+str(ite)+") = \n"+ e.imprimir())
		print("\nW("+str(ite)+") = \n"+ w.imprimir())
		print("\nb("+str(ite)+") = \n"+ b.imprimir())
	"""
	Se encarga de reconocer un vector de entrada.
	Recibe una matriz de entrada
	Devuelve f(wp+b), es decir a
	"""	
	def reconocer(self, entrada):
		a=self.w.mult(entrada).sum(self.b).hardlim()
		print(a.imprimir())
		return a
"""
Es la función principal
Se encarga de elegir qué datos cargarle a la red,
la entrena y después solicita entradas para reconocer
"""
def main():
	red=Red()
	datos=Datos()
	datos.cargar()
	red.entrenar([datos.w,datos.b,datos.tipos])	
	print("***********Se ha entrenado a la red************")
	while True:
		print("Introduce un vector para reconocerlo: ")
		cad=input()
		if cad=="salir":
			break
		else:
			rec = red.reconocer(Matriz(cad))
				
main()