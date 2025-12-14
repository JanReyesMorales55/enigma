# Es crea el fitxer menu.py - El qual controla el menu principal
import enigma
import rotors

def mostrar_menu():     
    while True:
        print("\n" + "=" * 25)
        print("SIMULADOR ENIGMA")               #Titol
        print ("Jan Reyes, Marc Fernandez")     #Creadors
        print ("ENTI - UB")                     #Entitat
        print("=" * 25)
        print("1. Xifrar missatge")             # 1a opcio
        print("2. Desxifrar missatge")          # 2a opcio
        print("3. Veure/Editar rotors")         # 3a opcio
        print("4. Sortir")                      # 4a opcio        
        opcio = input("\nTria una opcio (1-4): ")       #En funcio de l'opcio escollida el programa dura a terme diferents funcionalitats       
        if opcio == "1":                        # Si l'usuari escull la opcio 1 s'executara enigma.xifrar()
            enigma.xifrar()
        elif opcio == "2":                      # Si l'usuari escull la opcio 2 s'executara enigma.desxifrar()
            enigma.desxifrar()
        elif opcio == "3":                      # Si l'usuari escull la opcio 3 s'executara mostrar_menu_rotors()
            mostrar_menu_rotors()               
        elif opcio == "4":                      # Si l'usuari escull la opcio 4 es desplegara un missatge final i el programa finalitzara
            print("\n[INFO] Esperem que t'hagi estat util.")
            print("[INFO] S'han generat els seguents fitxers: xifrat.txt, desxifrat.txt")
            break
        else:
            print("[ERROR] Opcio incorrecta. Tria del 1 al 4.")             #Si l'usuari no escull cap de les opcions i introdueix un valor que no es valid el programa li donara error i li demanara un altre cop que introdueixi un valor valid (1,2,3,4)

def mostrar_menu_rotors():                  #Menu per gestionar rotors
    while True:
        print("\n" + "=" * 16)
        print("GESTIO DE ROTORS")                       #Despleguem totes les opcions possibles per a que l'usuari trii que vol fer dintre del menu de rotors
        print("=" * 16)
        print("1. Veure configuracio actual")           #Despleguem la 1a opcio
        print("2. Editar rotor")                        #Despleguem la 2a opcio
        print("3. Tornar al menu principal")            #Despleguem la 3a opcio     
        opcio = input("\nTria una opcio (1-3): ")       #Tornem a preguntar a l'usuari que vol fer dintre de l'apartat de rotors        
        if opcio == "1":                                #Si l'usuari escull la opcio 1 s'executara mostrar_rotors()
            mostrar_rotors()
        elif opcio == "2":                              #Si l'usuari escull la opcio 2 s'executara rotors.editar_rotor()
            rotors.editar_rotor()
        elif opcio == "3":                              #Si l'usuari escull la opcio 3 el codi llegira el break i finalitzara aquest proces
            break
        else:
            print("[ERROR] Opcio incorrecta")           #Si l'usuari introdueix cualsevol valor no acceptat, salta un error

def mostrar_rotors():                                   #Mostra la informacio dels rotors
    print("\n--- CONFIGURACIO DELS ROTORS ---")
    for i in range(1, 4):                               # Iterem pels 3 rotors: Rotor 1, Rotor 2 i Rotor 3
        try:
            wiring, notch = rotors.carregar_rotor(i)             #En funcio dels valors de "wiring" i "notch", el rotor defineix la seva funcio criptografica:
            print(f"\nRotor {i}:")                          # Mostrem quin rotor s'esta processant
            print(f"  Notch: {notch}")                      # Informem de la lletra de 'notch' que activa el salt del seguent rotor
            print(f"  Permutacio: {wiring}")                # Mostrem la permutacio completa (el cablejat intern)
            print(f"  Longitud: {len(wiring)} lletres")     # Mostrem la longitud de la permutacio (hauria de ser 26)
            if len(set(wiring)) != 26:                      #Comprovem si hi ha lletres repetides (ha de tenir 26 elements)
                print(f"  [AVIS] Hi ha lletres repetides!") #En cas de que hi hagi lletres repetides ho notifiquem
            if len(wiring) != 26:                           #Comprovem si hi ha exactament 26 elements
                print(f"  [ERROR] Longitud incorrecta!")    # Notifiquem l'error de longitud i que la permutacio no es valida
        except Exception as e:                                        #S'HA UTILITZAT IA PER A SOLIDIFICAR EL CODI EN AQUESTA LINEA
            print(f"\nRotor {i}: Error carregant - {e}")    ## Informem l'usuari que la carrega del rotor ha fallat i mostrem el motiu
