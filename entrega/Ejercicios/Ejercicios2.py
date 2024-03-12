Edad=int(input("Ingrese su edad: "))
if Edad >= 18:
    print("tiene edad para conducir")
else:
    print("no tiene edad para conducir")
#
edad=int(input("Ingrese su edad: "))
mi_edad=int(input("Ingrese mi edad: "))
if edad==mi_edad:
    print("yayy, tenemos la misma edad!")
else:
    if edad<mi_edad:
        if edad==mi_edad-1:
            print("Usted es menor por 1 año")
        else:
            print(f"Usted es menor que yo por {mi_edad-edad} años")
    else:
        if edad==mi_edad+1:
            print("Usted es mayor por 1 año")
        else:
            print(f"Usted es mayor que yo por {edad-mi_edad} años")
#
Saved_Contra=("SALSA")
contraseña=input("ingrese su contraseña: ")
contraseña=(contraseña.upper)
if Saved_Contra==contraseña:
    print("la contraseña coincide con la contraseña guardada")
else:
    print("la contraseña no coincide con la contraseña guardada")
#
numA=float(input("ingrese el número A: "))
numB=float(input("ingrese el número B: "))
if numA==numB:
    print("A es igual a B")
elif numA>numB:
    print("A es mayor a B")
else:
    print("A es menor a B")
#
num=int(input("Ingrese el número: "))
if num%2!=0:
    print("el número es impar")
else:
    print("el número es par")
#
dia=int(input("ingrese un número del 1 al 7"))
if dia<1 or dia>7:
    print("error, ese número no está entre 1 y 7")
elif dia==1:
    print(f"el número {dia} corresponde al día Lunes")
elif dia==2:
    print(f"el número {dia} corresponde al día Martes")
elif dia==3:
    print(f"el número {dia} corresponde al día Miércoles")
elif dia==4:
    print(f"el número {dia} corresponde al día Jueves")
elif dia==5:
    print(f"el número {dia} corresponde al día Viernes")
elif dia==6:
    print(f"el número {dia} corresponde al día Sabado")
elif dia==7:
    print(f"el número {dia} corresponde al día Domingo")
#
puntuacion=int(input("Ingrese la puntuacion del alumno"))
if puntuacion>=90:
    print("A")
elif puntuacion>=80:
    print("B")
elif puntuacion>=60:
    print("C")
elif puntuacion>=50:
    print("D")
else:
    print("F")
#

#
userage=int(input("ingrese su edad"))
ing_men=int(input("ingrese sus ingresos mensuales"))
if userage >= 18:
    if ing_men >=100000:
        print("usted debe pagar el impuesto")
else:
    print("usted no debe pagar el impuesto")