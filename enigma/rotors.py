alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def carregar_rotor(num):
    try:
        nom = "Rotor" + str(num) + ".txt"
        f = open(nom, "r") 
        linies = f.read().splitlines()
        f.close()
        wiring = linies[0]
        notch = "Z"
        if len(linies) > 1:
            notch = linies[1]
            return wiring, notch
    except FileNotFoundError:
        print(f"[ERROR] Fitxer Rotor{num}.txt no trobat. Utilitzant configuració per defecte.", file=sys.stderr)
        return alfabet, "Z"
    except Exception as e:
        print(f"[ERROR] Error carregant rotor {num}: {e}", file=sys.stderr)
        return alfabet, "Z"


def guardar_rotor(num, wiring, notch):
    try:
        nom = "Rotor" + str(num) + ".txt"
        f = open(nom, "w")
        f.write(wiring + "\n" + notch)
        f.close()
        print("Rotor guardat")
    except:
        print("Error guardant rotor")




def validar_permutacio(w):
    if len(w) != 26:
        return False
    for c in w:
        if c not in alfabet:
            return False
    if len(set(w)) != 26:
        return False
    return True




def editar_rotor():
    num = input("Quin rotor vols editar (1-3): ")
    try:
        num = int(num)
    except:
        print("Introdueix un valor numeric")
        return


    if num < 1 or num > 3:
        print("Introdueix un numero entre 1 i 3")
        return


    wiring = input("Nova permutacio (26 lletres): ").upper()
    if validar_permutacio(wiring):
        notch = input("Notch (lletra): ").upper()
        if notch == "":
            notch = "Z"
        guardar_rotor(num, wiring, notch)
    else:
        print("Permutacio incorrecta")