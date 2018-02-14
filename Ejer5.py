
import os
lista=os.listdir('C:/windows/system32')
for i in list(lista):
   if i[-3:]=='exe'|| i[-3:]=='bat':
      print i