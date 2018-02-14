
import os,sys

letra=raw_input('Introduce Cadena : ')
lista=os.listdir('C:/windows/system32')
t=0
for i in lista:
	if i.count(letra)> 0:
		print i
		t=1+t

print 'Total de Ficheros con la letra ' +str(letra)+' : ' +str(t)+ ' Ficheros'