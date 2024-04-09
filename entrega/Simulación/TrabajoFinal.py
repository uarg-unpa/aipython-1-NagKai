#Elegir la cantidad de dados a lanzar
#Especificar el número de caras de cada dado
#Realizar múltiples lanzamientos
#Obtener resultados individuales y totales
#Ver estadísticas básicas de los lanzamientos
import random
#def cant_dados (dados=1):
#    dados=int(input("ingrese la cantidad de dados que quiere tirar: "))
#def cara_dados (caras=6):
#    caras=int(input("ingrese la cantidad de caras que deban tener los dados: "))
#def cant_lanzamientos (lanzamientos=1):
#    lanzamientos=int(input("ingrese la cantidad de lanzamientos que quiere hacer: "))
def lanzar_dado(cant_caras):
     return random.randint(1, cant_caras)

#plan: tengo que realizar una lista con tamaño igual a la cantidad de dados. Para esto, se usa append con una lista, la cantidad de dados que se van a lanzar
#se genera un número aleatorio entre 1 y la cantidad de caras. dicho número se guarda en la lista previamente creada
#se dan los resultados de cada dado, y el total sumado
#los 2 previos puntos se encuentran dentro de un bucle, que se repite por la cantidad de lanzamientos

#estructura:
#definir variables
#Se indican la cantidad de dados y caras
#[se generan los valores y se muestran, luego se muestra a la suma] se repite por la cantidad de lanzamientos
#se guardan el promedio y la suma de cada lanzamiento, y se muestran como "estadísticas" después de terminar los lanzamientos

cant_dados=int(input("ingrese la cantidad de dados que va a lanzar: "))
cant_caras=int(input("ingrese la  cantidad de caras que deban tener los dados: "))
cant_lanzamientos=int(input("ingrese la cantidad de lanzamientos que quiere hacer: "))
lista_valor_dados=[]
for i in range(1,cant_dados):
    valor=(lanzar_dado) #no está funcionando
    lista_valor_dados.append(valor)
    print(lista_valor_dados[i-1])
    print(f"El valor del dado ",i, "es: ",valor)
