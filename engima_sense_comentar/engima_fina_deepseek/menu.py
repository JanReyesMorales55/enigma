# menu.py - Controla el menu principal
import enigma
import rotors

def mostrar_menu():
    """Mostra el menu d'opcions"""
    
    while True:
        print("\n" + "=" * 40)
        print("ENIGMA MACHINE SIMULATOR - ESTUDIANTS")
        print("=" * 40)
        print("1. Xifrar missatge")
        print("2. Desxifrar missatge")
        print("3. Veure/Editar rotors")
        print("4. Sortir")
        
        opcio = input("\nTria una opcio (1-4): ")
        
        if opcio == "1":
            enigma.xifrar()
        elif opcio == "2":
            enigma.desxifrar()
        elif opcio == "3":
            mostrar_menu_rotors()
        elif opcio == "4":
            print("\n[INFO] Gracies per utilitzar l'Enigma!")
            print("[INFO] Fitxers generats: xifrat.txt, desxifrat.txt")
            break
        else:
            print("[ERROR] Opcio incorrecta. Tria del 1 al 4.")

def mostrar_menu_rotors():
    """Menu per gestionar rotors"""
    while True:
        print("\n" + "-" * 30)
        print("GESTIO DE ROTORS")
        print("-" * 30)
        print("1. Veure configuracio actual")
        print("2. Editar rotor")
        print("3. Tornar al menu principal")
        
        opcio = input("\nTria una opcio (1-3): ")
        
        if opcio == "1":
            mostrar_rotors()
        elif opcio == "2":
            rotors.editar_rotor()
        elif opcio == "3":
            break
        else:
            print("[ERROR] Opcio incorrecta")

def mostrar_rotors():
    """Mostra la informacio dels rotors"""
    print("\n--- CONFIGURACIO DELS ROTORS ---")
    
    for i in range(1, 4):
        try:
            wiring, notch = rotors.carregar_rotor(i)
            print(f"\nRotor {i}:")
            print(f"  Notch: {notch}")
            print(f"  Permutacio: {wiring}")
            print(f"  Longitud: {len(wiring)} lletres")
            
            # Validació addicional
            if len(set(wiring)) != 26:
                print(f"  [AVIS] Hi ha lletres repetides!")
            if len(wiring) != 26:
                print(f"  [ERROR] Longitud incorrecta!")
        except Exception as e: #generat amb ia per poder guardar el rotor
            print(f"\nRotor {i}: Error carregant - {e}")