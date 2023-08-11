import random, time

def tiro():
  return random.randint(0,36)

ganaRojo = False
ganaNegro = False
ganaPar = False
ganaImpar = False
ganaRojo = False
ganaPasa = False
ganaFalta = False
ganaDocena1 = False
ganaDocena12 = False
ganaDocena2 = False
ganaDocena23 = False
ganaDocena3 = False
ganaColumna1 = False
ganaColumna12 = False
ganaColumna2 = False
ganaColumna23 = False
ganaColumna3 = False
ganaSeisena = False
ganaCuadro = False
ganaTransversal = False
ganaCaballo = False
ganaPleno = False

print("girando....")
time.sleep(1)
ganador = tiro()
#ganador = 0
print(f"\nGanador {ganador} !")

rojos=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
negros=[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]

if ganador in rojos:
  print("\nRojos ganan, paga al 1x1")
else:
  print("\nRojos pierden")

if ganador in negros:
  print("\nNegros ganan, paga al 1x1")
else:
  print("\nNegros pierden")

if ganador == 0:
  print("\nPares pierden\n\nNones pierden")
elif (ganador % 2) == 0:
  print("\nPares ganan, paga al 1x1\n\nNones pierden")
else:
  print("\nPares pierden\n\nNones ganan, paga al 1x1")

if ganador > 0 and ganador <19:
  print("\nFalta ganan, paga al 1x1\n\nPasa pierden")
elif ganador > 18 and ganador <37:
  print("\nFalta pierden\n\nPasa ganan, paga al 1x1")
  
