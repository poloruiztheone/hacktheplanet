import numpy
import math
import time 

#numpy.random.seed(time.time())


id = 0

class Tupla(object):
	"""docstring for Tupla"""
	def __init__(self, longitudGenoma):
		super(Tupla, self).__init__()
		self.idOrden = "" #Para saber cuales y cuanto pagar
 		self.indicador = setIndicador() #1 o 0
		self.disponible = setDisponible() #monto a cambiar
		self.cambio = setCambio() #tipo de cambio
		self.genotipo = setGenotipo(longitudGenoma) #genotipo
		self.horas = 48 #entero del 0 al 48
		self.cantUsada = "" #fitness

def setGenotipo (longitudGenoma):
	
	genotipo = ""

	for i in range(longitudGenoma):
		if numpy.random.random() < 0.5:
			genotipo += "0"
		else:
			genotipo += "1"
	
	return genotipo

def setIndicador():
	rand = numpy.random.random()

	if rand > 0.5:
		indicador = 0
	else:
		indicador = 1

	return indicador

def setDisponible ():

	return numpy.random.random() * 10000

def setCambio ():
	if numpy.random.random() > 0.5:
		cambio = 0.061 + (numpy.random.random()/1000)
	else: 
		cambio = 0.061 - (numpy.random.random()/1000)
	return cambio

def generaTupla(longitudGenoma):
	
	return Tupla(longitudGenoma)

def combinacionesIniciales(numCombinaciones, numOrdenes, longitudGenoma):
	
	combinaciones = []

	ordenes = []

	for x in range(numOrdenes):
		ordenes.append(generaTupla(longitudGenoma))

	for y in range(numCombinaciones):
		combinaciones.append(ordenes)

	return combinaciones

def poblacion(numIndividuos, numTuplas, longitudGenoma):
	
	poblacion = []
	
	for i in range(numIndividuos):
	
		fila = []
	
		for j in range(numTuplas):
	
			fila.append(generaTupla(longitudGenoma))
	
		poblacion.append(fila)
	
	return poblacion

def calcularFenotipo(genoma):
	fenotipo = 0.0
	for i in range(len(genoma)):
		if genoma[i] == '1':
			fenotipo += math.pow(2, len(genoma) - i - 1)
	return fenotipo

def fitnessDeOrden(individuo):
	loQuePonemos = 0
	for i in range(len(individuo)):
		if individuo[i].disponible >= individuo[i].cantUsada:
			fitness = 0
			if individuo[i].indicador == 1: #dolares a pesos
				fitness += individuo[i].disponible * (individuo[i].cambio - 0.0001)
			else:
				fitness += individuo[i].disponible * (individuo[i].cambio + 0.0001)
			loQuePonemos += fitness
			fitness += (individuo[i].horas / 48) + ((1 - individuo[i].cantUsada) / individuo.disponible)
		else:
			return 1000000000

	return fitness + loQuePonemos

def evaluaOrdenes(poblacion, probCruzamiento):
	for i in range(len(poblacion)):
		fitnessDeOrden(poblacion[i])
	poblacion.sort(key=lambda tup: tup[1]) #suponemos que los ordena del menor al mayor
	arrayAux = poblacion
	poblacion = []
	poblacion.extend(arrayAux[0:len(arrayAux)/2])
	poblacion.extend(arrayAux[0:len(arrayAux)/2])	
	return poblacion

def cruzaTuplas(individuos, probCruzamiento):

	mitad = int(len(individuos)/2)

	print "MITAD: " + str(mitad) 

	for i in range(mitad):

		rand = numpy.random.random()

		if probCruzamiento > rand:

			n_i = len(individuos) - 1 - i
			p = int((numpy.random.random() * len(individuos[i].genotipo)) % ((len(individuos[i].genotipo)/2) - 1))

			print "P: " + str(p)

			individuoI = individuos[i].genotipo
			individuoN_I = individuos[n_i].genotipo

			individuos[i].genotipo = individuoI[0:p] + individuoN_I[p:p + len(individuoI)/2] + individuoI[p + len(individuoI)/2:] 
			individuos[n_i].genotipo = individuoN_I[0:p] + individuoI[p:p + len(individuoI)/2] +  individuoN_I[p + len(individuoI)/2:] 

			print "ORIGINAL_I: " + str(individuoI)
			print "ORIGINAL_N_I: " + str(individuoN_I)

			print "I: " + str(individuos[i].genotipo)
			print "N_I: " + str(individuos[n_i].genotipo)

			print ""

	return individuos

def cruzaIndividuos(ordenes, probCruzamiento):
	
	mitad = int(len(ordenes)/2)

	for i in range(mitad):

		rand = numpy.random.random()

		if probCruzamiento > rand:

			n_i = len(ordenes) - 1 - i
			p = int((numpy.random.random() * 100000) % ((len(ordenes[i])/2) - 1))

			ordenI = ordenes[i]
			ordenN_I = ordenes[n_i]

			ordenes[i] = ordenI[0:p] + ordenN_I[p:p + (len(ordenN_I)/2)] + ordenI[p + (len(ordenN_I)/2):]
			ordenes[n_i] = ordenN_I[0:p] + ordenI[p:p + (len(ordenN_I)/2)] + ordenN_I[p + (len(ordenN_I)/2):]
			
		return ordenes

def duplicaArreglo(conjunto):
	for i in range(len(conjunto)):
		conjunto.append(conjunto[i])

	return conjunto

def selecciona(combinaciones, fitness):
	for i in range(len(combinaciones)):
		
		mejorFitness = fitness[i]
		mejorIndex = i

		for j in range(i+1,len(combinaciones)):
			if fitness[j] < mejorFitness:
				mejorFitness = fitness[j]
				mejorIndex = j

		if mejorIndex != i:
			auxString = combinaciones[i]
			combinaciones[i] = combinaciones[mejorIndex]
			combinaciones[mejorIndex] = auxString

			auxFitness = fitness[i]
			fitness[i] = fitness[mejorIndex]
			fitness[mejorIndex] = auxFitness

	ans = [combinaciones, fitness]

	return ans

def evaluaIndividuos(individuos):

	fitness = 0.0
	for i in range(len(individuos)):
		
		if individuos[i].indicador == 1: #dolares a pesos
			fitness += individuos[i].disponible * (individuos[i].cambio - 0.0001)
		else:
			fitness += (individuos[i].disponible * (individuos[i].cambio + 0.0001)) * (-1)

		#fitness += (individuo[i].horas / 48) + ((1 - individuo[i].cantUsada) / individuo.disponible)

	return fitness

def mutar(individuos, bitsAMutar):

	for i in range(0,bitsAMutar):

		individuoSeleccionado = int(numpy.random.random() * len(individuos))
		bitSeleccionado = int(numpy.random.random() * len(individuos))

		mutado = ""

		for i in range(len(individuos[individuoSeleccionado])):
			if i != bitSeleccionado:
				mutado += individuos[individuoSeleccionado][i]
			else:
				if individuos[individuoSeleccionado][bitSeleccionado] == '1':
					mutado += '0'
				else:
					mutado += '1'

		individuos[individuoSeleccionado] = mutado

		print "INDEX: " + str(individuoSeleccionado)

	return individuos		

def evaluarCombinaciones(combinaciones):
	fitness = []
	for x in range(len(combinaciones)):
		fitness.append(evaluarOrdenes(combinaciones[x]))
	return fitness

def evaluarOrdenes (ordenes):
	fitness = 0.0
	for x in range(len(ordenes)):
		if ordenes[x].disponible >= calcularFenotipo(ordenes[x].genotipo):
			if ordenes[x].indicador == 1:
				fitness += ordenes[x].disponible * (ordenes[x].cambio - 0.0001)
			else:
				fitness += (ordenes[x].disponible * (ordenes[x].cambio + 0.0001)) * (-1)
		else:
			fitness = 1000000000000000000000
	return fitness

def nuevosGenotipos (ordenes, longitudGenoma):
	for orden in range(len(ordenes)):
		ordenes[orden].genotipo = setGenotipo(longitudGenoma)
	return ordenes

def inicializaCombinaciones(combinaciones, longitudGenoma):
	for combinacion in range(len(combinaciones)):
		combinaciones[combinacion] = nuevosGenotipos(combinaciones[combinacion], longitudGenoma)
	return combinaciones

def curzaCombinaciones(combinaciones, probCruzamiento):
	
	mitad = int(len(combinaciones)/2)

	for i in range(mitad):
		rand = numpy.random.random()

		if probCruzamiento > rand:

			n_i = (len(combinaciones)/2) - 1 - i
			p = int((numpy.random.random() * (len(combinaciones)/2)) % (((len(combinaciones)/2)/2) - 1))

			ordenI = combinaciones[i]
			ordenN_I = combinaciones[n_i]

			combinaciones[i] = ordenI[0:len(ordenI)/3] + ordenN_I[len(ordenI)/3:len(2*ordenI)/3] + ordenI[len(2*ordenI)/3:]
			combinaciones[n_i] = ordenN_I[0:len(ordenI)/3] + ordenI[len(ordenI)/3:len(2*ordenI)/3] + ordenN_I[len(2*ordenI)/3:]

	return combinaciones

def mutarCombinaciones(combinaciones, bitsAMutar):

	for i in range(bitsAMutar):

		individuoSeleccionado = int(numpy.random.random() * len(combinaciones))
		bitSeleccionado = int(numpy.random.random() * len(combinaciones[0][0].genotipo))
        
		combinaciones[individuoSeleccionado][bitSeleccionado].genotipo = setGenotipo(len(combinaciones[0][0].genotipo))

	return combinaciones


try:
		
	#PARAMETROS
	probCruzamiento = 1
	numGeneraciones = 10;
	bitsAMutar = 5;

	#Inicializa las Combinaciones
	combinaciones = combinacionesIniciales(10, 9, 8)

	#Evalua la primer vez
	fitness = evaluarCombinaciones(combinaciones)

	try:
		#Generaciones
		for x in range(numGeneraciones):

		#	Duplica
			combinaciones = duplicaArreglo(combinaciones)
			fitness = duplicaArreglo(fitness)

		#	Cruza
			for combinacion in range(len(combinaciones)):
				combinaciones[combinacion] = curzaCombinaciones(combinaciones, probCruzamiento)

		#	Muta
			combinaciones = mutarCombinaciones(combinaciones, bitsAMutar)

		#	Evalua
			fitness = evaluarCombinaciones(combinaciones)

		#	Selecciona
			seleccionados = selecciona(combinaciones, fitness)
			combinaciones = seleccionados[0]
			fitness = seleccionados[1]

	except Exception, e:

		print ""
		print "=====================Algoritmo evolutivo=========================="
		print ""
		print "MEJOR COMBINACION: " + str(fitness[0])
		print ""
		print "/////////////////////////////Inicio/////////////////////////////"
		print ""
		print "PARA VER LOS DATO DESCOMENTE LAS LINEAS SIGUIENTES"

		tiempo = 0

		usd_mxn = []
		total_cartera_dolares = 0.0

		mxn_usd = []
		total_cartera_peso = 0.0

		pib = 0.0001

		lote = 100

		ganancias_usd = 0.0

		rand = numpy.random.random()
		limteUSD_MXN = int(rand*lote)

		for x in range(limteUSD_MXN):
			tupla = generaTupla(0)
			#print "DATOS DE LA TRANSACCION: " + str(tupla.idOrden)
			#print "CANTIDAD DE LA ORDEN: " + str("%.4f" % tupla.disponible)
			#print "TIEMPO RESTANTE: " + str(tupla.horas - (0.3 * x))
			#print "TIPO DE CAMBIO: " + str(tupla.cambio)
			#print ""
			usd_mxn.append(tupla)
			
		rand = numpy.random.random()
		limteMXN_USD = int(rand*lote)

		for x in range(limteMXN_USD):
			tupla = generaTupla(0)
			#print "DATOS DE LA TRANSACCION: " + str(tupla.idOrden)
			#print "CANTIDAD DE LA ORDEN: " + str("%.4f" % tupla.disponible / tupla.cambio)
			#print "TIEMPO RESTANTE: " + str(tupla.horas - (0.3 * x))
			#print "TIPO DE CAMBIO: " + str(1/tupla.cambio)
			#print ""
			mxn_usd.append(tupla)

		total_cartera_dolares = sum(c.disponible for c in usd_mxn)
		total_cartera_peso = sum(c.disponible for c in mxn_usd)
		total_cartera_peso_en_pesos = sum(c.disponible/c.cambio for c in mxn_usd)

		print ""
		print ""
		print "**********************************Inicio**********************************"
		print ""
		print "CUENTA EN USD:"
		print "Disponible: " + str("%.4f" % total_cartera_dolares) + " USD"
		print ""
		print "CUENTA EN MXN:"
		print "Disponible: " + str("%.4f" % total_cartera_peso_en_pesos) + " MXN => CANTIDAD EN USD: " + str("%.4f" %  total_cartera_peso)
		print ""
		print "=============================Despues de Pagar============================="
		print ""

		ordenes_pagadas_usd_mxn = []
		ordenes_pagadas_mxn_usd = []

		sig1 = usd_mxn[0]
		sig2 = mxn_usd[0]

		while len(usd_mxn) != 0 and len(mxn_usd) != 0:

			if sig1.disponible < sig2.disponible:
				ordenes_pagadas_usd_mxn.append(usd_mxn[0])
				del usd_mxn[0]
				if len(usd_mxn) != 0:
					sig2.disponible -= sig1.disponible 
					ganancias_usd += sig1.disponible * pib
					sig1 = usd_mxn[0]
			else:
				ordenes_pagadas_mxn_usd.append(mxn_usd[0])
				del mxn_usd[0]
				if len(mxn_usd) != 0:
					sig1.disponible -= sig2.disponible 
					ganancias_usd += sig2.disponible * pib
					sig2 = mxn_usd[0]

		total_cartera_dolares = sum(c.disponible for c in usd_mxn)
		total_cartera_peso = sum(c.disponible for c in mxn_usd)
		total_cartera_peso_en_pesos = sum(c.disponible/c.cambio for c in mxn_usd)

		print "CUENTA EN USD:"
		print "Disponible: " + str("%.4f" %  total_cartera_dolares) + " USD"
		print ""
		print "CUENTA EN MXN:"
		print "Disponible: " + str("%.4f" %  total_cartera_peso_en_pesos)  + " MXN => CANTIDAD EN USD: " + str("%.4f" %  total_cartera_peso)
		print ""
		print "=================================Ganancias================================="
		print ""
		print "GANANCIA: " + str(ganancias_usd)
		print ""
		print ""
		print ""
		
except Exception, e:
	pass