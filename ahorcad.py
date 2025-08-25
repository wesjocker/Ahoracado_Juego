#modulo random permite obtener de forma aleatoria un palabra del array
import random 

#Funcion para obetner palabra
def obtener_palabra():
    lista_palabras=["perro","gato","comida","video","ahorcado"]
    palabra_aleatoria=random.choice(lista_palabras)
    return palabra_aleatoria

#Funcion para palabra secreta, para msotar el estado actual del juego
def mostrar_palabra(palabra_secreta, letras_adivinadas):
    palabra=""
    for letra in palabra_secreta:
        if letra in letras_adivinadas: #compara si esta dentro de letras adivinadas
            palabra+=letra #aumento contador
        else:
            palabra+="_" #aumento un guion bajo en la palabra
    print(palabra)
    

#funcion para jugar ahorcado
def jugar_ahorcado():
    palabra_secreta=obtener_palabra()
    letras_adivinadas=[] #incia en cero
    intentos_restantes=6
    
    while intentos_restantes>0:
        mostrar_palabra(palabra_secreta, letras_adivinadas)
        letra=input("Introduce una letra: ").lower() #la transformor a miniscula
        
        if letra in letras_adivinadas:
            print(f"Letra ya ingresada, ingrese una letra")
            continue #me salto todos los demas pasos y regreso al inicio de while
        
        if letra in palabra_secreta:
            letras_adivinadas.append(letra) #agrego la letra a ese array
            if set(letras_adivinadas)==set(palabra_secreta): #set permite crear un conjutno de elemento unicos, es decir elmina los du
                print("Gano el Jugador")
                break
        else:
            intentos_restantes-=1
            print(f"Letra incorrecta. Te quedan {intentos_restantes}")
    
    if intentos_restantes==0:
        print(f"has pertido el juego, la palabra secreta era: {palabra_secreta} ")
        
jugar_ahorcado()