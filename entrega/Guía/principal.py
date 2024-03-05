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