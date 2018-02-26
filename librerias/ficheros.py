import os
import sys


def version():
	return 'version 1.0 Joche'

def creadir(directorio):
        if os.access(directorio,1):
                return "Imposible ya Existe"
        else:
                os.mkdir(directorio)
		return "Directorio: "+directorio+"creado"


def entorno():
	for clave,valor in os.environ.iteritems():
		if clave=='USER' or clave=='PATH' or clave=='SHELL':
			print valor

def gordo(directorio,size):
	for x in os.listdir(directorio):
	    path_size=0
	    if os.path.isfile(x):
		path_size = os.path.getsize(x)
		if path_size > size:
			print x+' Su tama en bytes: ' +str(path_size)

def visualizar(nombre):
    f=open(nombre,r)
	while True:
	   linea=f.readline()
	   if not linea:break
	   print linea

