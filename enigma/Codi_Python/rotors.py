# Es crea el fitxer rotors.py - Per gestionar la configuracio dels rotors

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"                      #Definim l'alfabet

def carregar_rotor(numero):                                 #Generem una funcio carregar_rotor que carrega un rotor des d'un fitxer
  
    try:                                                    #Intentem obrir i llegir el fitxer
        nom_fitxer = f"Rotor{numero}.txt"                   #Es busca el nom del fitxer
        with open(nom_fitxer, "r", encoding='utf-8') as f:
            contingut = f.read().strip().splitlines()       #Llegim les dues linies (permutacio i notch)
        
        if len(contingut) == 0:                             #Si l'arxiu esta buit len(contingut) sera 0 imprimirem per pantalla que no hi ha res al fitxer
            print(f"[ERROR] Rotor{numero}.txt esta buit")
            return crear_rotor_per_defecte(numero)          #Tornem a la configuracio base
        
        wiring = contingut[0].strip().upper()               #La primera linia fa referencia al wiring (cablejat)
        
        # Validem la permutacio
        if len(wiring) != 26:                               #Comprovem que hi hagi exactament 26 lletres, si no hi ha 26 s'executara aquest if
            print(f"[ERROR] Rotor{numero}.txt: permutacio incorrecta - calen 26 lletres uniques A-Z")   #Com que no hi ha 26 lletres, imprimim el seguent missatge avisant que la permutacio es incorrecta
            return crear_rotor_per_defecte(numero)          #Tornem a la configuracio base
        
        # Comprovem que son totes lletres A-Z
        for lletra in wiring:                               #Revisem lletra per lletra el wiring per a comprovar que tot son lletres A-Z
            if lletra not in alfabet:                       #Si hi ha algun simbol extrany o algo que no sigui A-Z
                print(f"[ERROR] Rotor{numero}.txt: caracter '{lletra}' no es una lletra A-Z")       #Imprimim i avisem de l'error
                return crear_rotor_per_defecte(numero)      #Tornem a la configuracio base
        
        # Comprovem que no hi ha repetides
        if len(set(wiring)) != 26:                          #Mirem si hi ha cap lletra repetida
            print(f"[ERROR] Rotor{numero}.txt: hi ha lletres repetides")        #En cas de que hi hagi cap lletra repetida imprimirem el seguent missatge avisant de l'error
            return crear_rotor_per_defecte(numero)          #Tornem a la configuracio base
        
        if len(contingut) > 1:                              #Mirem si hi ha una segona linia (sera el notch)
            notch = contingut[1].strip().upper()            #Aquesta linia es el notch, que s'encarrega de moure el seguent rotor
            if notch == "" or notch not in alfabet:         #Si el notch es incorrecte li assignarem un valor predefinit, notch = Z
                notch = "Z"
        else:
            notch = "Z"                                     #D'altra manera tambe li donarem un valor predefinit, notch = Z
        
        return wiring, notch                                #Finalment fem un return del cablejat i de notch
        
    except FileNotFoundError:                               #Si el fitxer no existeix
        print(f"[INFO] Rotor{numero}.txt no trobat. Utilitzant configuracio per defecte.")      #Imprimim el missatge avisant que no s'ha trobat el fitxer i utilitzem la configuracio per defecte
        return crear_rotor_per_defecte(numero)              #Tornem a la configuracio base

def crear_rotor_per_defecte(numero):                        #Definim una funcio que crea un rotor per defecte
   
    if numero == 1:
        return "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"            #S’ha agafat tant el cablejat o switch com el notch del document de simulacio basica del enigma
    elif numero == 2:
        return "AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"            #Tant el cablejat o switch com el notch han estat generats amb IA
    else:  # numero == 3
        return "BDFHJLCPRTXVZNYEIWGAKMSQUO", "V"            #Tant el cablejat o switch, com el notch han estat generats amb IA

def editar_rotor():                                         #Creem una funcio que permeti a l'usuari canviar i guardar la configuracio del rotor escollit
    print("\n--- EDITAR ROTOR ---")                         #Imprimim un titol per a millorar l'estetica del programa
    
    try:                                                        #Provem a demanar a l'usuari quin rotor vol editar
        num = int(input("Numero del rotor a editar (1-3): "))
        if num < 1 or num > 3:                                  #Si el numero que ens dona no es 1, 2, 3 saltara error
            print("[ERROR] El numero ha de ser 1, 2 o 3")       #Imprimim un missatge avisant a l'usuari que el numero a escollir es 1, 2 o 3
            return
    except:                                                     #Si l'usuari introdueix algo que no sigui un numero salta l'error
        print("[ERROR] Has d'escriure un numero")
        return
    
    print(f"\nEditant Rotor {num}")
    print("Posa 26 lletres diferents (A-Z) sense repetir")
    
    while True:                                         #Bucle per a demanar una permutacio fins que aquesta sigui valida
        wiring = input("Permutacio: ").upper()
        
        # Validem la permutacio
        if len(wiring) != 26:                           #Comprovem que tingui exactament 26 lletres, sino salta l'error
            print("[ERROR] Ha de tenir exactament 26 lletres")
            continue
        
        ok = True
        for lletra in wiring:                           #Utilitzem un for per a validar lletra per lletra que totes aquestes estiguin en el alfabet (A-Z)
            if lletra not in alfabet:                   #Si la lletra no esta en el alfabet salta l'error
                print(f"[ERROR] '{lletra}' no es una lletra A-Z valida")
                ok = False
                break               #Al acabar d'imprimir el missatge de l'error el programa llegeix el break i para
        
        if not ok:
            continue
        
        if len(set(wiring)) != 26:              #Comprovem que no hi hagi lletres repetides, i si hi ha fem saltar l'error
            print("[ERROR] Hi ha lletres repetides")    #En cas de que hi hagi lletres repetides imprimim el missatge corresponent
            continue
        
        # Si tot esta correcte:
        break
    
    notch = input("Notch (una sola lletra, ex: Q): ").upper()           #Demanem la lletra de 'notch' (A mes utilitzem el .upper per a evitar errors de lectura de text)
    if notch == "" or notch not in alfabet:                         #Si no s'introdueix un valor valid utilitzarem el valor per defecte "Z"
        notch = "Z"
        print("[INFO] Notch per defecte: Z")                        #Imprimim el missatge avisant que utilitzarem el valor per defecte
    
    # Guardar
    try:
        with open(f"Rotor{num}.txt", "w", encoding='utf-8') as f:       #Intentem obrir el fitxer per escriure
            f.write(wiring + "\n" + notch)                              #Escrivim el cablejat i el notch
        print(f"[OK] Rotor {num} guardat correctament a Rotor{num}.txt")        #Imprimim un missatge avisant que tot ha sortit correctament
    except Exception as e:                                                  #S'HA UTILITZAT IA PER A SOLIDIFICAR EL CODI EN AQUESTA LINEA
        print(f"[ERROR] No s'ha pogut guardar: {e}")    #En cas d'error imprimim un missatge per avisar que no s'ha pogut guardar correctament
