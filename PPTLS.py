from random import choice

ines = choice(["piedra", "papel", "tiejera", "lagarto", "spock"])
juan = choice(["piedra", "papel", "tiejera", "lagarto", "spock"])

print(f"ines ha sacado {ines}")
print(f"juan ha sacado {juan}")

if ines == juan:
    print("Empate")
elif (ines == "piedra" and juan == "tiejera") or (ines == "piedra" and juan == "spock"):
    print("gana ines")
elif (ines == "papel" and juan == "piedra") or(ines == "papel" and juan == "lagarto"):
    print("gana ines")
elif (ines == "tiejera" and juan == "papel") or (ines == "tiejera" and juan == "spock"):
    print("gana ines")
elif (ines == "lagarto" and juan == "piedra") or (ines == "lagarto" and juan == "tiejera"):
    print("gana ines")
elif (ines == "spock" and juan == "papel") or (ines == "spock" and juan == "lagarto"):
    print("gana ines")
else:
    print("gana juan")