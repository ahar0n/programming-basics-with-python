# calificaciones.py muestra concepto asociado a la nota
nota = float(input('Ingrese su nota: '))

if nota >= 4.0:
	if nota <= 4.9:
		concepto = 'Aprobado por unanimidad'
	elif nota < 5.7:
		concepto = 'Aprobado por distincion'
	else:
		concepto = 'Aprobado por distincion maxima'
else:
    concepto = 'Reprobado'
    
print(concepto)

# Verificación del problema
# test1: input: 3.9, output: Reprobado
# test2: input: 4.5, output: Aprob. x unanimidad
# test3: input: 5.1, output: Apro. x distinción
# test4: input: 5.8, output: Apro. x distin. mñaxima

# Mejorar el algoritmo para evaluar  nota < 1 and nota > 7 => 'Nota fuera de rango'?