fichero = open("/etc/passwd",'r')
Contador = 0;
Lineas = [fichero.readline()]
ListaUsuarioyShell = ["Usuarios -> Shell"]
Diccionario={"Usuario":"Shell"}
print(" ")

for line in fichero:
	Lineas.append(fichero.readline())

for Linea in Lineas:
	Diccionario[Linea.split(":")[0]] = Linea.split(":")[-1]
	
try:
	print(Diccionario['root'])
	print(Diccionario['Imaginario'])
except:
	print ("Usuario incorrecto")
