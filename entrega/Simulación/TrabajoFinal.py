#Elegir la cantidad de dados a lanzar
#Especificar el número de caras de cada dado
#Realizar múltiples lanzamientos
#Obtener resultados individuales y totales
#Ver estadísticas básicas de los lanzamientos
import random
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
cant_caras=int(input("ingrese la cantidad de caras que deban tener los dados: "))
cant_lanzamientos=int(input("ingrese la cantidad de lanzamientos que quiere hacer: "))
lista_valor_dados=[]
lista_promedios=[]
lista_sumas=[]
for l in range(0, cant_lanzamientos):
     suma_dados=0
     promedio_actual=0
     print(f"Lanzamiento ", l+1,":",sep="")
     print(" ")
     for i in range(0,cant_dados):
          valor=(lanzar_dado(cant_caras))
          lista_valor_dados.append(valor)
          print(f"El valor del dado ",i+1, "es: ",valor)
          suma_dados=suma_dados+valor
     print(f"La suma de todos los dados lanzados es: ", suma_dados)
     promedio_actual=suma_dados/cant_dados
     print(f"El resultado promedio de todos los dados lanzados es: ", promedio_actual)
     print()
     lista_sumas.append(suma_dados)
     lista_promedios.append(promedio_actual)
print("ESTADISTICAS:")
print("")
print(f"Cantidad de lanzamientos: ",cant_lanzamientos)
print(f"Cantidad de dados por lanzamiento: ",cant_dados)
print(f"Cantidad de caras de los dados: ",cant_caras)
print("")
print("SUMA DE CADA LANZAMIENTO:")
for s in range(0,cant_lanzamientos):
     print(f"Lanzamiento ", s+1,": ",lista_sumas[s],sep="")
print("PROMEDIO DE CADA LANZAMIENTO:")
for p in range(0,cant_lanzamientos):
     print(f"Lanzamiento ", p+1,": ",lista_promedios[p],sep="")