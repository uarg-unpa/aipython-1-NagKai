print("Taller de AIPython P1 E2")
print()
print("hola","soy","Juan")
print("ya", "estoy","en","casa", sep="*",end=".")
print("Dim")
print("yogurt")
print("usando la función print ()"*3)
print(10, 3.14, "cadena", True)
edad=int(input("ingrese su edad: "))
print("su edad es ", edad)
print("su edad es "+str(edad))
print(f"su edad es: {edad}")

num1=4
num2=6
print(f"{num1}+{num2} = {num1+num2}")
suma=f"{num1}+{num2} = {num1+num2}"
print(f"{num1}-{num2} = {num1-num2}")
print(f"{num1}*{num2} = {num1*num2}")
print(f"{num1}/{num2} = {num1/num2}")
print(f"{num1}//{num2} = {num1//num2}")
print(f"{num1}**{num2} = {num1**num2}")
print("suma", suma)
#
texto="EsTo eS uN texTo MeZclAdO"
#title
print(texto)
print(texto.title())
texto=texto.title()
print(texto)
#upper lower
print(texto.upper())
print(texto.lower())
#replace
print(texto.replace(" ","-"))
print(len(texto))
print(len('AIPython'))
#while
num=int(input("ingresar número"))
positivo=0
negativo=0
while(num!=0):
    if num>0:
        positivo=positivo+1
    else:
        negativo=negativo+1
    num=int(input("ingresar número"))
print(f"la cantidad de números positivos es {positivo} y la cantidad de npumeros negativos es {negativo}")
#
#for
cadena=("AIPYTHON")
for letra in cadena:
    print(letra)
#range
for number in range(11):
    print(number)
#imprimir AIPYTHON 10 veces
for _ in range(10):
    print("AIPYTHON")