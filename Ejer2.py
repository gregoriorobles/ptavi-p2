fichero = open("/etc/passwd",'r')
Contador = 0;
Lineas = [fichero.readline()]
ListaUsuarioyShell = ["Usuarios -> Shell"]
ListaUsuarioyShell.append(" ")
print(" ")

for line in fichero:
	Lineas.append(fichero.readline())

for Linea in Lineas:
	Usuarios = Linea.split(":")[0] 

	Shell = Linea.split(":")[-1]
	ListaUsuarioyShell.append(Usuarios +" -> "+ Shell)

for UsuarioShell in ListaUsuarioyShell:
	print(UsuarioShell)
	
