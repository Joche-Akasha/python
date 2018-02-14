def imprimir():
	print 'HOLA'

	
	
def funcion():
	return "Hola Mundo"

# Funcion PAR/IMPAR
def typenum(num):
	if num%2==0:
		return "El Numero " +str(num)+" es PAR"
	else:
		return "El Numero " +str(num)+" es IMPAR"

# Funcion PAR/IMPAR con Operador Ternario

def ter_typenum(num):
	return "El Numero " +str(num)+" es PAR"  if (num % 2 == 0) else "El Numero " +str(num)+" es IMPAR"

# Funcion Alta cliente
def alta_cliente(dni,nombre,*apellidos):
	print 'DNI: ' +str(dni)
	print 'Nombre: ' +str(nombre)
	for N in apellidos:
		print 'Apellido: ' +str(N)

# Funcion Inciales
def iniciales(nombre,*apellidos):
	ini=nombre[0]+'.'
	for N in apellidos:
		ini=ini+N[0]+'.'
	return ini