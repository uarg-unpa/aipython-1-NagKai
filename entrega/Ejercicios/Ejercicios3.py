#1 y 2
for num in range(0,101):
    print (num,end=",")
print("")
#3
X=11
while X !=0:
    print(X-1)
    X=X-1
for Y in range (0,11):
    print(Y)
#4
N1=int(input("ingrese el primer número: "))
N2=int(input("ingrese el segundo número: "))
for inbetween in range(N1+1,N2):
    print(inbetween)
#5
iteracion=0
while iteracion !=8:
    iteracion=iteracion+1
    for i in range(1,iteracion):
        print("*",end="")
    print("")
#6
iteration=0
while iteration !=8:
    iteration=iteration+1
    for i in range(1,9):
        print("#",end="")
    print("")
#7
name=input("ingrese su nombre: ")
num_name=int(input("ingrese un número: "))
for i in range(0,num_name):
    print(name,end=",")
print("")
#8
#numero no puede ser divisible por 2,3 o 5, a menos que el número sea uno de dichos números
#numero debe aumentar hasta llegar al numero ingresado
num_ing=int(input("ingrese un número mayor a 3: "))
if num_ing >=3:
    for W in range(1,num_ing):
        if W%2 !=0:
            if W%3 !=0:
                if W%5 !=0 or W==5:
                    print(W)
else:
    print("error: el número no es mayor a 3")
#9
for patron in range(0,11):
    print(f"{patron} x {patron} = {patron*patron}")
