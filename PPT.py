from random import choice

ines = choice(["piedra", "papel", "tiejera"])
juan = choice(["piedra", "papel", "tiejera"])

print(f"ines ha sacado {ines}")
print(f"juan ha sacado {juan}")

if ines == juan:
    print("Empate")
elif ines == "piedra" and juan == "tiejera":
    print("gana ines")
elif ines == "papel" and juan == "piedra":
    print("gana ines")
elif ines == "tiejera" and juan == "papel":
    print("gana ines")
else:
    print("gana juan")