import math

Edad=19
altura=1.65
Complejo=1+1

#4
(Base)= int (input('Ingresa la base del triangulo'))
(Altura)= int (input('Ingresa la altura del traingulo'))
area=(0.5*Base*Altura)
print('La area del traingulo es: ', area)

#5
lado1=int (input('Ingresa la longitud de un lado'))
lado2=int (input(('Ingresa el segundo lasdo')))
lado3=int (input('Ingresa el tercer lado'))


#6
lado2= int (input('Ingresa la b ase del rectangulo'))
Area=lado1*lado2
Perimetro =2*(lado1+lado2)
print('La area del rectangulo es: ', area)
print('El perimetro del rectangulo es de :',Perimetro)

#7
Radio=int (input ('Ingresa  el radio del circulo'))
Pi=3.14
Area=Pi *Radio*Radio 
Circunferencia=2*Pi*Radio 
print('La area del circulo es: ', area)
print('El perimetro del circulo  es de :',Perimetro)

#8   
#z =2q - q =x z=y
q1,z1,q2,z2,=2,2,6,10
Frist_slope=(z2-z1)/(q2-q1)
print('La pediente es:', Frist_slope)


#9
x1,y1,x2,y2=2,2,6,10
Second_slope=(y2-y1 )/(x1-x2)
print('La segunda pendiente es:', Second_slope)
distancia_ecudiliana= math.sqrt((x2-x1)) **2+(y2-y1)**2
print('La distancia ecudilina es:',distancia_ecudiliana)

#10 
if(Frist_slope==Second_slope):
     print('Son iguales')
else:print('No son iguales ,estas mal')

#11
x=int(input('Ingresar el valor de x'))
y=int(x^2+6*x+9)
print('El valor de y es',y)

#12
Palabra1=len('Phyton')
Palabra2=len( 'Dragon')
if(Palabra1==Palabra2):
     print('Las palabras son iguales')
else:print('Las palabras son diferentes')

#13
print('Ejercicio 13')
if'on'in 'Dragon'and 'on' in 'Phyton':
  print('Si esta en las palabras')
else:print ('Si se encuentra')
 
 #14
print('ejercicio14')
if 'Jragon'in'I hope this course is not full of jargon':
    print('Si se encuentra la palabra en la oracion')
else: 
    print('no se encuentra en la oracion')

#15
print('ejercicio15')
if 'on'in'Phyton'and 'Dragon':
    print('La palabra si se encuentra ')
else: 
    print('La palabra no se encuentra')

#16
flotam=float (len('Phtyon'))
print('Ejercicio16 ')
print (len('Phyton'))
print (str('Phyton'))
print(flotam)

#17
print('ejercicio 17')
num=int (input())
if num%2:
   print('El numero es par')
else:print('el numero no es par')

#18
print('Ejercicio 18')
division=7/3
resultado=2.7
if division == resultado:
     print ('Si es igual')
else: print ('No es igual a 2.7, es igual a :',division)

#19
print('ejercicio19')
comparar=type(10)
if comparar==10:
   print('si es igual a 10')
else:print('no es igual a 10')

#20
print('ejercicio 20')
valor=int(9.8)
 
if valor==10:
  print('el valor de 9.8 si es igual a 10')

else :('el valor de 9.8 no es igual a 10')

#21
print('ejercicio 21')
Horas= int(input('ingresa las horas laborales'))
Pago_por_horas = int(input('ingresa su suledo por hora'))
Sueldo_total = Horas*Pago_por_horas
print('Su sueldo total es de ',Sueldo_total)

#22
print('ejercicio 22')
años=int (input ('Ingrese sus años vividos'))
Total=años*360*24*365
print('El total de sus años  vividos son',Total)

#23
print('ejercicio 23')

for i in range (1,6):
 print(i,1,i**2, 1**2,i**3)