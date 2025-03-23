run = True
vidas = 100
dinero = 25

puntuacionPartida = vidas * dinero

print (puntuacionPartida)

if vidas <= 0:
    print ("Goku ha caido")
elif vidas == 0:
    print("Goku ha caido")
else:
    print("Infernape puede seguir")

while run:
    print("El combate ha comenzado")
    run = False

for i in range(7):
    print(f"faltan {i} minutos")
