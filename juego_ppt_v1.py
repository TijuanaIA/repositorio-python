# Juego de Piedra, Papel o Tijera
# Desarrollado por Oscar como ejercicio de práctica

#Importar módulos
import random   
import time

#Declaración de variables y diccionario
opciones = ['piedra', 'papel', 'tijera']
mapa = {"1": "piedra", "2":"papel","3":"tijera"}
puntos_usuario = 0
puntos_compu = 0



while True:
#Solicitar la elección del jugador   
   print("\nSelecciona un número:")
   print(" (1) 🪨 Piedra")
   print(" (2) 📄 Papel")
   print(" (3) ✂️ Tijera")
   print(" (4)  SALIR\n")
   usuario = input()
 
   if usuario not in ['1', '2', '3', '4']:
     print("\nEntrada no válida. Por favor selecciona 1, 2 o 3.")
     continue
   if usuario == '4':
      break 

   #Generar una elección aleatoria para la computadora
   print("\nLa computadora está pensando...")
   time.sleep(1)  #Simula que está "pensando" para dar suspenso
   computadora = random.choice(opciones)

   #Comparar resultados y declarar al ganador 
   usuario = mapa.get(usuario)
   resultado = ""
   if(usuario == 'piedra' and computadora == 'tijera') or \
     (usuario == 'papel' and computadora == 'piedra') or \
     (usuario == 'tijera' and computadora == 'papel'):
     resultado = 'Ganaste'
     puntos_usuario += 1
   elif(usuario==computadora):
     resultado = 'Empate'
   else:
     resultado = 'Perdiste'
     puntos_compu += 1
   
   #Imprimir en pantalla resultado y mencionar al ganador. 
   print(f"\n🧑 Tú elegiste: {usuario} \n💻 La computadora eligió: {computadora}")
   print(f"\n🎯 Resultado: {resultado}")
   print (f"\nTus Puntos: {puntos_usuario}\nPuntos de la computadora: {puntos_compu}")   
