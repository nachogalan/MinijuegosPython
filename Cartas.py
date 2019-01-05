from random import randrange

#declaramos los cuatro dados que se van a utilizar con un rango del uno al 6 (todos utilizando la aleatoriedad).
carta1 = randrange(1, 11)
carta2 = randrange(1, 11)
carta3 = randrange(1, 11)
carta4 = randrange(1, 11)
carta5 = randrange(1, 11)
carta6 = randrange(1, 11)


#Imprimimos por pantalla los resultados de los numeros aleatorios que ha sacado cada jugador
print(f"Gloria ha sacado un {carta1}, {carta2} y {carta3}.")
print(f"Hector ha sacado un {carta4}, {carta5} y {carta6}.")

#Comenzamos a valorar los distintos casos para saber quien ha ganado o si han empatado

if carta1 + carta2 + carta3 > 15 and carta4 + carta5 + carta6 > 15:
    print("No ha ganado nadie")
elif carta1 + carta2 + carta3 > carta4 + carta5 + carta6 and carta1 + carta2 + carta3 <= 15:
    print("ha ganado gloria")
elif carta1 + carta2 + carta3 < carta4 + carta5 + carta6 and carta4 + carta5 + carta6 <= 15:
    print("ha ganado hector")
elif carta1 + carta2 + carta3 <= 15 and carta4 + carta5 + carta6 > 15:
    print("ha ganado gloria")
elif carta1 + carta2 + carta3 > 15 and carta4 + carta5 + carta6 <= 15:
    print("ha ganado hector")
else:
    print("han empatado")