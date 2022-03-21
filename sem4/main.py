"""
BREVE REPASO OPERADORES

= asignación (creación variable o cte, o modificación de variable)
== comparación (if, SI ES IGUAL)
!= comparación (if, SI NO ES IGUAL)

+, -, *, /

and (y, una condición Y la otra)
or (o, una condición O la otra)
"""

# Definición de 2 VARIABLES p/ los nros
# nro1 = 3
# nro2 = 21
# nro3 = 2
mult = 1

# Definición de CONSTANTES
PI = 3.141592654

for ciclo1 in range(2):
	nro = input("Ingresar nro: ")
	nro = int(nro)
	if (nro > 0):
		mult = mult * nro * PI # Esto es un acumulador
	else:
		print("error")

print()
print(mult)