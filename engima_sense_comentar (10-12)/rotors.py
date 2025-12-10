# es crea l'arxiu rotors.py - Serveix per gestionar la configuracio dels rotors

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def carregar_rotor(numero):
    """Carrega un rotor des d'un fitxer"""
    try:
        nom_fitxer = f"Rotor{numero}.txt"
        with open(nom_fitxer, "r", encoding='utf-8') as f:
            contingut = f.read().strip().splitlines()
        
        if len(contingut) == 0:
            print(f"[ERROR] Rotor{numero}.txt esta buit")
            return crear_rotor_per_defecte(numero)
        
        wiring = contingut[0].strip().upper()
        
        # Validar la permutació
        if len(wiring) != 26:
            print(f"[ERROR] Rotor{numero}.txt: permutacio incorrecta, calen 26 lletres uniques de A-Z")
            return crear_rotor_per_defecte(numero)
        
        # Comprovar que són totes lletres A-Z
        for lletra in wiring:
            if lletra not in alfabet:
                print(f"[ERROR] Rotor{numero}.txt: caracter '{lletra}' no es una lletra A-Z")
                return crear_rotor_per_defecte(numero)
        
        # Comprovar que no hi ha repetides
        if len(set(wiring)) != 26:
            print(f"[ERROR] Rotor{numero}.txt: hi ha lletres repetides")
            return crear_rotor_per_defecte(numero)
        
        if len(contingut) > 1:
            notch = contingut[1].strip().upper()
            if notch == "" or notch not in alfabet:
                notch = "Z"
        else:
            notch = "Z"
        
        return wiring, notch
        
    except FileNotFoundError:
        # Si no es troba el fitxer, fem un rotor per defecte
        print(f"[INFO] Rotor{numero}.txt no trobat. S'utilitzara la configuracio per defecte.")
        return crear_rotor_per_defecte(numero)

def crear_rotor_per_defecte(numero):
    """Crea un rotor per defecte"""
    # Rotors per defecte (simplificats)
    if numero == 1:
        return "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"
    elif numero == 2:
        return "AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"
    else:  # numero == 3
        return "BDFHJLCPRTXVZNYEIWGAKMSQUO", "V"

def editar_rotor():
    """Permet editar un rotor (versio simplificada)"""
    print("\n--- EDITAR ROTOR ---")
    
    try:
        num = int(input("Numero del rotor a editar (1-3): "))
        if num < 1 or num > 3:
            print("[ERROR] El numero ha de ser 1, 2 o 3")
            return
    except:
        print("[ERROR] Has d'escriure un numero")
        return
    
    print(f"\nEditant Rotor {num}")
    print("Posa 26 lletres diferents (A-Z) sense repetir")
    
    while True:
        wiring = input("Permutacio: ").upper()
        
        # Validar
        if len(wiring) != 26:
            print("[ERROR] Ha de tenir exactament 26 lletres")
            continue
        
        ok = True
        for lletra in wiring:
            if lletra not in alfabet:
                print(f"[ERROR] '{lletra}' no es una lletra A-Z valida")
                ok = False
                break
        
        if not ok:
            continue
        
        if len(set(wiring)) != 26:
            print("[ERROR] Hi ha lletres repetides")
            continue
        
        # Tot correcte
        break
    
    notch = input("Notch (ha de ser una sola lletra, ex: Q): ").upper()
    if notch == "" or notch not in alfabet:
        notch = "Z"
        print("[INFO] Notch per defecte: Z")
    
    # Guardar
    try:
        with open(f"Rotor{num}.txt", "w", encoding='utf-8') as f:
            f.write(wiring + "\n" + notch)
        print(f"[OK] Rotor {num} guardat correctament a Rotor{num}.txt")
    except Exception as e: #fet amb ia per poder guardar el rotor   
        print(f"[ERROR] No s'ha pogut guardar: {e}")