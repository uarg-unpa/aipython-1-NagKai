print("Las máquinas me sorprenden con mucha frecuencia")
print()
print("Celeste")
print("23", 23)
print("Una computadora puede ser llamada \"inteligente\" si logra engañar a una persona haciéndole creer que es un humano")
print("Juan Martín", "Arenillas", "17",sep="_")
print("calle", "numero", "código postal", sep="\n")
print("Feliz", "\tprimavera", "\t\t\t2024", sep="\n")
print("Solo podemos ver poco del futuro", "pero lo suficiente para darnos cuenta de que hay mucho que hacer", sep=",")
print("     *")
print("    * *")
print("   *   *")
print("  *     *")
print(" ***   ***")
print("   *   *")
print("   *   *")
print("   *****")
nombre=("Juan Martín")
apellido=("Arenillas")
edad=(17)
altura=(1.70)
num_vuelo=("CLA 43")
temperatura=("22°C")
salario=(205000)
fin_juego=(True)
num_par=(False)
print(type(nombre))
print(type(apellido))
print(type(edad))
print(type(altura))
print(type(num_vuelo))
print(type(temperatura))
print(type(salario))
print(type(fin_juego))
print(type(num_par))
print("Nombre:",input("ingrese su nombre: "),input("ingrese su apellido: "),"| Edad:", int(input("ingrese su edad: ")), "| Status: desconocido")
num1=int(input("ingrese el primer número (debe ser entero): "))
num2=float(input("ingrese el segundo número (puede ser decimal): "))
print(f"{num1}+{num2} = {num1+num2}")
print(f"{num1}-{num2} = {num1-num2}")
print(f"{num1}*{num2} = {num1*num2}")
print(f"{num1}/{num2} = {num1/num2}")
print(f"{num1}//{num2} = {num1//num2}")
print(f"{num1}**{num2} = {num1**num2}")
base=float(input("ingrese el tamaño de la base del rectangulo: "))
height=float(input("ingrese el tamaño de la altura del rectangulo: "))
print("el perímetro del rectangulo es: ", (base*2+height*2))
print("el area del rectangulo es: ",(base*height),"metros cuadrados")
peso=float(input("ingrese su peso en Kg: "))
estatura=float(input("ingrese su estatura en metros: "))
ind_masa_corp=(peso/estatura**2)
print("Tu índice de masa corporal es: ", (ind_masa_corp))
