# programa que al introducir nombre, lea tu nombre, cuantas letras tiene, que letras estan presentes y cuantas veces aparece cada una.
nombre=input('ingrese su nombre:\n')
contador=0
for i in nombre:
	contador=contador+1
print(f'su nombre:\n {nombre.upper()}, tiene {contador} letras ')