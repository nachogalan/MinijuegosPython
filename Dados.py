from random import randrange

#declaramos los cuatro dados que se van a utilizar con un rango del uno al 6 (todos utilizando la aleatoriedad).
dado1 = randrange(1, 7)
dado2 = randrange(1, 7)
dado3 = randrange(1, 7)
dado4 = randrange(1, 7)

#declaramos la variable la cual indica el numero más alto el cual han lanzado los jugadores
dado12 = max(dado1, dado2)
dado34 = max(dado3, dado4)

#Imprimimos por pantalla los resultados de los numeros aleatorios que ha sacado cada jugador
print(f"David ha sacado un {dado1} y un {dado2}.")
print(f"Carmen ha sacado un {dado3} y un {dado4}.")

#Comenzamos a valorar los distintos casos para saber quien ha ganado o si han empatado

if dado1 + dado2 > dado3 + dado4:
    print("Ha ganado David")
elif dado1 + dado2 < dado3 + dado4:
    print("Ha ganado Carmen")
elif dado12 > dado34:
    print("Ha ganado David")
elif dado12 < dado34:
    print("Ha ganado Carmen")
else:
    print("Los jugadores han empatado")