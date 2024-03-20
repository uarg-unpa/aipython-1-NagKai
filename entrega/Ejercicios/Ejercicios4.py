#1 y 2
def multi(num1=1,num2=1):
    print(f"{num1} * {num2} = {num1*num2}")
#llamado de función
multi(5,8)
#3
def name(nom="amigo"):
    print(f"hola {nom}, espero que te hays portado bien hoy!")
#llamado de función
name()
#4
def tabla(tabla_num=1):
    for i in range(0,11):
        print(f"{tabla_num} x {i} = {tabla_num*i}")
#llamado de función
tabla(8)
#5
def par_impar(num=0):
    if num%2!=0:
        print("el número es impar")
    else:
        print("el número es par")
#llamado de función
par_impar(140)
#6
def factorial(number=1):
    fact=1
    for f in range(1,number+1):
        fact=fact*f
    print(fact)
#llamado de función
factorial(7)
#7
def max_de_tres(n1=1,n2=2,n3=3):
    print(max(n1,n2,n3))
#llamado de función
max_de_tres(4,10,15)
#8
def gnirts(palabra="palabra"):
    for p in range(len(palabra)-1,-1,-1):
        print(palabra[p],end="")
    print()
#llamado de función
gnirts()
#9

#10
def far_cel(temp_far=0):
    print(f"su temperatura de fahrenheit en celsius es {(temp_far-32)*0.5556}°C")
#llamado de función
far_cel()