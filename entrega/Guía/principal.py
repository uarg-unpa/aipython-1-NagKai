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
    num=int(input("ingresar número: "))
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
# LISTAS
#Creación listas vacías
nombres=[]
#Valores iniciales
nombres=['franco','fernanda','fabiana']
#mostrar lista
print(nombres)
#iterar sobre las listas usando índices
for Q in range(len(nombres)):
    print(nombres[Q])
#accedemos a los elementos
primer_elemento=nombres[0]
print(f"el primer elemento es {primer_elemento}")
#creación de listas usando metodos
#nombres=list()
#nombres=list('gaston','eva','lautaro')
#Append agrega un elemento al final de la lista
nombres.append('sandra')
#insert
nombres.insert(0,'victoria')
#utilizar el operador in
for nombre in nombres:
    print(nombre)
#mutabilidad
nombres[4]='Lorenza'
for nombre in nombres:
    print(nombres)