# enigma.py - Conte les funcions per xifrar i desxifrar
import rotors               # Importa el modul extern que conte la configuracio dels rotors

# Defineix l'alfabet constant que s'utilitzara per a les conversions
alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def netejar_text(text):
    net = ""                # Inicialitza la variable on guardarem el text netejat
    for lletra in text:     # Recorre cada caracter del text original
        # Comprova si el caracter es una lletra entre A i Z 
        if 'A' <= lletra.upper() <= 'Z':
            net += lletra.upper()  # Afegeix la lletra convertida a majuscula
    return net  

def formatar_grups(text):
    grups = []              # Llista per emmagatzemar els blocs de 5 lletres
    for i in range(0, len(text), 5):  
        grups.append(text[i:i+5])  # Afegeix el fragment de text actual a la llista
    return ' '.join(grups)  # Uneix tots els grups amb un espai entre ells i ho retorna

def avancar_rotor(posicio, notch):
    nova_pos = (posicio + 1) % 26  # Incrementa la posicio i torna a 0 si arriba a 26 
    ha_saltat = (alfabet[posicio] == notch)  # Comprova si la posició actual es el punt de salt 
    return nova_pos, ha_saltat  

def xifrar_lletra(lletra, rotors_info, posicions):
    if lletra not in alfabet:      # Si el caracter no esta a l'alfabet
        return lletra              # El retorna sense fer cap canvi   
    index = alfabet.index(lletra)  # Converteix la lletra en el seu index numeric, com es fa per xifrar lletres en ciber
    for i in range(3):  
        wiring = rotors_info[i][0]  # Obte el cablejat del rotor actual
        desp = posicions[i]         # Obte el desplaçament actual d'aquest rotor
        # Calcula la nova lletra aplicant el desplaçament i buscant al cablejat del rotor
        index = alfabet.index(wiring[(index + desp) % 26])
    
    return alfabet[index]  # Converteix l'index final resultant en lletra

def desxifrar_lletra(lletra, rotors_info, posicions):
    if lletra not in alfabet:  # Comprovacio de seguretat
        return lletra
    
    index = alfabet.index(lletra)  # Converteix lletra a número  
    # Passar pels 3 rotors (endarrere)
    for i in range(2, -1, -1):      # Va del ultim al primer
        wiring = rotors_info[i][0]  # Obte el cablejat del rotor
        desp = posicions[i]         # Obte el desplaçament actual
        lletra_anterior = wiring.index(alfabet[index])  # Busca quina lletra entrava per obtenir la sortida actual (inversa)
        index = (lletra_anterior - desp) % 26  # Resta el desplaçament per obtenir l'index original relatiu
   
    return alfabet[index]  # Retorna la lletra original desxifrada

def xifrar():
    print("\n--- XIFRAR MISSATGE ---")   
    missatge = input("Escriu el missatge: ")    #Solicita l'input a l'usuari
    missatge_net = netejar_text(missatge)       #Neteja el text (nomes majuscules)
    print(f"[INFO] Missatge netejat: {len(missatge_net)} lletres")   
    r1 = rotors.carregar_rotor(1)       #Carreguem la configuracio (cablejat i notch) del Rotor 1
    r2 = rotors.carregar_rotor(2)       #Carreguem la configuracio (cablejat i notch) del Rotor 2
    r3 = rotors.carregar_rotor(3)       #Carreguem la configuracio (cablejat i notch) del Rotor 3
    
    while True:  # Bucle infinit fins que l'usuari introdueixi dades valides
        pos_str = input("Posicio inicial (3 lletres, ex: ABC): ").upper()  #Input convertit a majuscules
        if len(pos_str) == 3 and pos_str.isalpha():                        # Valida que siguin exactament 3 lletres
            break  # Surt del bucle si es valid
        print("[ERROR] Has d'escriure exactament 3 lletres A-Z")           #Imprmim el missatge avisant del error
    # Converteix les lletres inicials a indexs numerics
    p1 = alfabet.index(pos_str[0])          #Posicio inicial numerica del Rotor 1
    p2 = alfabet.index(pos_str[1])          #Posicio inicial numerica del Rotor 2
    p3 = alfabet.index(pos_str[2])          #Posicio inicial numerica del Rotor 3
    print(f"[INFO] Posicio inicial: {pos_str}")
    
    resultat = ""                   #Variable on guardarem el missatge final
    for lletra in missatge_net:     #Processa lletra per lletra el missatge
        # Per avançar rotors
        p1, salt1 = avancar_rotor(p1, r1[1])        #Mecanisme per a fer avançar els rotors per a cada lletra
        if salt1:                                   #Si el rotor 1 ha arribat al seu notch 
            p2, salt2 = avancar_rotor(p2, r2[1])    #Mou el rotor 2
            if salt2:                               #Si el rotor 2 ha arribat al seu notch 
                p3, _ = avancar_rotor(p3, r3[1])    #Mou el rotor 3
        
        # Xifrar la lletra actual amb les posicions actualitzades
        resultat += xifrar_lletra(lletra, [r1, r2, r3], [p1, p2, p3])
        
    resultat_formatat = formatar_grups(resultat)  
    # Calcula quants grups han sortit 
    num_grups = len(resultat) // 5 + (1 if len(resultat) % 5 > 0 else 0)   
    print(f"\n[OK] Missatge xifrat: {resultat_formatat}")                   #Imprimim el missatge xifrat
    print(f"[OK] Guardat a xifrat.txt ({len(resultat)} lletres, {num_grups} grups de 5)")       #Avisem a l'usuari de la ubicacio del arxiu
    
    with open("xifrat.txt", "w") as f:  #Obrim el fitxer xifrat.txt per guardar
        f.write(resultat_formatat)      #Guardem el text amb els grups de 5 lletres
    
    return resultat 

def desxifrar():
    print("\n--- DESXIFRAR MISSATGE ---")   #Imprimim aquest missatge per a informar el que estem fent i millorar l'estetica
    
    # Llegir missatge xifrat
    try:
        with open("xifrat.txt", "r") as f:  #Intentem llegir el missatge xifrat del fitxer 
            contingut = f.read() 
            missatge = contingut.replace(" ", "").replace("\n", "")         #Eliminem espais  i salts de linea (ja que aquests no els xifrarem)
            print(f"[INFO] Llegit de xifrat.txt: {len(missatge)} lletres")  #Imprimim el missatge per a informar a l'usuari

    except FileNotFoundError: #Si no trobem el fitxer:
        print("[ERROR] No s'ha trobat xifrat.txt")              #Imprimim el missatge per a avisar que no hem trobat el fitxer
        contingut = input("Pega el missatge xifrat aqui: ")     #Demana entrada manual del text
        missatge = netejar_text(contingut)                      #Netejem el text manual per a garantir que nomes hi hagi majuscules
        print(f"[INFO] Missatge netejat: {len(missatge)} lletres")  #Tornem a avisar a l'usuari dels canvis
    
    # Carregar rotors
    r1 = rotors.carregar_rotor(1)       #Carreguem la configuracio del Rotor 1
    r2 = rotors.carregar_rotor(2)       #Carreguem la configuracio del Rotor 2
    r3 = rotors.carregar_rotor(3)       #Carreguem la configuracio del Rotor 3
    
    # Demanem la posicio inicial
    while True:                         #Bucle per assegurar que l'usuari posa 3 lletres
        pos_str = input("Posicio inicial (IMPORTANT!! ha de ser la mateixa que per xifrar, ex: ABC): ").upper()  #Demanem la posicio inicial i li remarquem que ha de ser la mateixa (i afegim el .upper per a evitar errors de comprensio de text)
        if len(pos_str) == 3 and pos_str.isalpha():         #S'HA UTILITZAT IA EN AQUESTA LINEA PER A LA COHESIO DEL CODI
            break
        print("[ERROR] Has d'escriure exactament 3 lletres A-Z")    #Salta l'error i imprimim el missatge per a avisar a l'usuari
    
    # Conversio de la posicio inicial a indexs
    p1 = alfabet.index(pos_str[0])      #Convertim la lletra del Rotor 1 a un numero (0-25)
    p2 = alfabet.index(pos_str[1])      #Convertim la lletra del Rotor 2 a un numero (0-25)
    p3 = alfabet.index(pos_str[2])      #Convertim la lletra del Rotor 3 a un numero (0-25)
    print(f"[INFO] Posicio inicial: {pos_str}")
    
    # Per desxifrar
    resultat = ""               #Variable per a guardar el text desxifrat
    for lletra in missatge:     #Llegeix cada lletra del missatge una per una 
        # Avançar rotors 
        p1, salt1 = avancar_rotor(p1, r1[1])        #Mecanisme per a fer avançar els rotors per a cada lletra 
        if salt1:                                   #Si el rotor 1 ha arribat al seu notch 
            p2, salt2 = avancar_rotor(p2, r2[1])    #Mou el rotor 2
            if salt2:                               #Si el rotor 2 ha arribat al seu notch
                p3, _ = avancar_rotor(p3, r3[1])    #Mou el rotor 3
        
        # Desxifrem utilitzant la funcio inversa
        resultat += desxifrar_lletra(lletra, [r1, r2, r3], [p1, p2, p3])        #Aplica el proces invers (anant del rotor 3 al rotor 1)
    
    # Mostrar resultat
    resultat_formatat = formatar_grups(resultat)  
    print(f"\n[OK] Missatge desxifrat: {resultat_formatat}")            #Imprimim el missatge desxifrat
    print(f"[OK] Guardat a desxifrat.txt ({len(resultat)} lletres)")    #Avisem a l'usuari de la ubicacio del missatge desxifrat 
    
    # Guardar a fitxer
    with open("desxifrat.txt", "w") as f:   #Obrim el fitxer desxifrat.txt
        f.write(resultat)   #Guardem el resultat final
    print("[INFO] Recorda que desxifrat.txt nomes te lletres majuscules sense signes ni espais")    #Finalment imprimim el missatge avisant que el document esta desxifrat sense majuscules ni signes ni espais
