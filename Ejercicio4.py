import librerias.ficheros as l
import sys

if len(sys.argv) <> 2:
	print "Error, necesito directorio"
else:
	l.creadir(sys.argv[1])
