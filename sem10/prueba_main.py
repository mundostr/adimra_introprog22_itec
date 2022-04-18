def main():
	pass

# def calcular(val: float, coef: float) -> float:
def calcular(val, coef):
	calculo = val * coef
	
	return calculo


def mostrar(texto):
	print("****************")
	print()
	print(texto)
	print("________________")
	print()


# Flujo principal
if (__name__ == "__main__"):
	valor = 16
	coeficiente = 3.14

	resultado = calcular(valor, coeficiente)
	mostrar("El resultado es " + str(resultado))
	mostrar("El resultado * 2 es " + str(resultado * 2))
