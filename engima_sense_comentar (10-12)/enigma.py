# es crea l'arxiu enigma.py. Aquest conte les funcions per xifrar i desxifrar
import rotors

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def netejar_text(text):
    """Deixa nomes lletres majuscules"""
    net = ""
    for lletra in text:
        if 'A' <= lletra.upper() <= 'Z':
            net += lletra.upper()
    return net

def formatar_grups(text):
    """Formata el text en grups de 5 lletres"""
    grups = []
    for i in range(0, len(text), 5):
        grups.append(text[i:i+5])
    return ' '.join(grups)

def avancar_rotor(posicio, notch):
    """Avanca un rotor una posicio"""
    nova_pos = (posicio + 1) % 26
    ha_saltat = (alfabet[posicio] == notch)
    return nova_pos, ha_saltat

def xifrar_lletra(lletra, rotors_info, posicions):
    """Xifra una sola lletra"""
    if lletra not in alfabet:
        return lletra
    
    index = alfabet.index(lletra)
    
    # Passar pels 3 rotors (endavant)
    for i in range(3):
        wiring = rotors_info[i][0]
        desp = posicions[i]
        index = alfabet.index(wiring[(index + desp) % 26])
    
    return alfabet[index]

def desxifrar_lletra(lletra, rotors_info, posicions):
    """Desxifra una sola lletra"""
    if lletra not in alfabet:
        return lletra
    
    index = alfabet.index(lletra)
    
    # Passar pels 3 rotors (endarrere)
    for i in range(2, -1, -1):  # 2, 1, 0
        wiring = rotors_info[i][0]
        desp = posicions[i]
        lletra_anterior = wiring.index(alfabet[index])
        index = (lletra_anterior - desp) % 26
    
    return alfabet[index]

def xifrar():
    """Xifra un missatge complet"""
    print("\n---XIFRAR MISSATGE---")
    
    # 1. Demanar missatge
    missatge = input("Escriu el missatge: ")
    missatge_net = netejar_text(missatge)
    print(f"[INFO] Missatge netejat: {len(missatge_net)} lletres")
    
    # 2. Carregar rotors
    r1 = rotors.carregar_rotor(1)
    r2 = rotors.carregar_rotor(2)
    r3 = rotors.carregar_rotor(3)
    
    # 3. Demanar posicio inicial
    while True:
        pos_str = input("Posicio inicial (3 lletres, ex: ABC): ").upper()
        if len(pos_str) == 3 and pos_str.isalpha():
            break
        print("[ERROR] Has d'escriure exactament 3 lletres A-Z")
    
    p1 = alfabet.index(pos_str[0])
    p2 = alfabet.index(pos_str[1])
    p3 = alfabet.index(pos_str[2])
    print(f"[INFO] Posicio inicial: {pos_str}")
    
    # 4. Xifrar
    resultat = ""
    for lletra in missatge_net:
        # Avancar rotors
        p1, salt1 = avancar_rotor(p1, r1[1])
        if salt1:
            p2, salt2 = avancar_rotor(p2, r2[1])
            if salt2:
                p3, _ = avancar_rotor(p3, r3[1])
        
        # Xifrar
        resultat += xifrar_lletra(lletra, [r1, r2, r3], [p1, p2, p3])
    
    # 5. Formatar i mostrar resultat
    resultat_formatat = formatar_grups(resultat)
    num_grups = len(resultat) // 5 + (1 if len(resultat) % 5 > 0 else 0)
    
    print(f"\n[OK] Missatge xifrat: {resultat_formatat}")
    print(f"[OK] Guardat a xifrat.txt ({len(resultat)} lletres, {num_grups} grups de 5)")
    
    # 6. Guardar
    with open("xifrat.txt", "w") as f:
        f.write(resultat_formatat)
    
    return resultat

def desxifrar():
    """Desxifra un missatge"""
    print("\n---DESXIFRAR MISSATGE---")
    
    # 1. Llegir missatge xifrat
    try:
        with open("xifrat.txt", "r") as f:
            contingut = f.read()
            # Eliminar espais per obtenir el text net
            missatge = contingut.replace(" ", "").replace("\n", "")
            print(f"[INFO] Llegit de xifrat.txt: {len(missatge)} lletres")
    except FileNotFoundError:
        print("[ERROR] No s'ha trobat xifrat.txt")
        contingut = input("Pega el missatge xifrat aqui: ")
        missatge = netejar_text(contingut)
        print(f"[INFO] Missatge netejat: {len(missatge)} lletres")
    
    # 2. Carregar rotors
    r1 = rotors.carregar_rotor(1)
    r2 = rotors.carregar_rotor(2)
    r3 = rotors.carregar_rotor(3)
    
    # 3. Demanar posicio inicial (HA DE SER LA MATEIXA!)
    while True:
        pos_str = input("Posicio inicial (es la mateixa que has utilitzat per xifrar, ex: ABC): ").upper()
        if len(pos_str) == 3 and pos_str.isalpha():
            break
        print("[ERROR] Has d'escriure exactament 3 lletres de a A-Z")
    
    p1 = alfabet.index(pos_str[0])
    p2 = alfabet.index(pos_str[1])
    p3 = alfabet.index(pos_str[2])
    print(f"[INFO] Posicio inicial: {pos_str}")
    
    # 4. Desxifrar
    resultat = ""
    for lletra in missatge:
        # Avancar rotors (IGUAL que en xifrar)
        p1, salt1 = avancar_rotor(p1, r1[1])
        if salt1:
            p2, salt2 = avancar_rotor(p2, r2[1])
            if salt2:
                p3, _ = avancar_rotor(p3, r3[1])
        
        # Desxifrar
        resultat += desxifrar_lletra(lletra, [r1, r2, r3], [p1, p2, p3])
    
    # 5. Mostrar resultat
    resultat_formatat = formatar_grups(resultat)
    print(f"\n[OK] Missatge desxifrat: {resultat_formatat}")
    print(f"[OK] Guardat a desxifrat.txt ({len(resultat)} lletres)")
    
    # 6. Guardar
    with open("desxifrat.txt", "w") as f:
        f.write(resultat)
    print("[INFO] Recorda que desxifrat.txt nomes te lletres majuscules sense signes ni espais")