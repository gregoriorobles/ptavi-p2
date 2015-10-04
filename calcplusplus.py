import calcplus
import sys
def main():
    pass


if __name__ == '__main__':
	Calculadora = calcplus.CalculadoraPlus();
	NombreFichero = sys.argv[1];
	Calculadora.leerfichero(NombreFichero);
	for line in Calculadora.fichero:
		print(line[:-1])
		Operacion = line.split(",")[0] 

		if Operacion == "sumar" or Operacion == "suma":
			OperacionTotal = 0;
			for next in line.split(",") :
				if next != "sumar" and next != "suma":
					Calculadora.introAgmt(OperacionTotal,next,Operacion)
					OperacionTotal = Calculadora.sumar()			
	
		if Operacion == "restar" or Operacion == "resta":
			Entrar = True
			OperacionTotal = 0;
			for next in line.split(",") :
				if next != "restar" and next != "resta":
					Siguiente = next
					Primero = line.split(",")[1];
					if next == Primero and Entrar:
						Siguiente = -int(next)
						Entrar = False;
					Siguiente = int(Siguiente);
					Calculadora.introAgmt(OperacionTotal,Siguiente,Operacion)
					OperacionTotal = Calculadora.restar()

		if Operacion == "multiplicar" or Operacion == "multiplica":
			OperacionTotal = 1;
			for next in line.split(",") :
				if next != "multiplicar" and next != "multiplica":
					Calculadora.introAgmt(OperacionTotal,next,Operacion)
					OperacionTotal = Calculadora.multiplicar()
		if Operacion == "dividir" or Operacion == "divide":
			OperacionTotal = 1;
			for next in line.split(",") :
				if next != "dividir" and next != "divide":
					Siguiente = next
					Primero = line.split(",")[1];
					if next == Primero:
						OperacionTotal = Siguiente
						Siguiente = 1 
					Siguiente = int(Siguiente);
					Calculadora.introAgmt(OperacionTotal,Siguiente,Operacion)
					OperacionTotal = Calculadora.dividir()
		if line != line[-1]:
			print(OperacionTotal)

		
		
		


