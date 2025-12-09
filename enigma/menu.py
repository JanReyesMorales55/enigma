import enigma
import rotors


def mostrar_menu():
    print("--- PROGRAMA ENIGMA INICIAT ---")
    while True:
        print("ENIGMA:")
        print("1. Xifrar missatge")
        print("2. Desxifrar missatge")
        print("3. Editar rotors")
        print("4. Sortir")
        op = input("Opcio: ")


        if op == "1":
            enigma.xifrar()
        elif op == "2":
            enigma.desxifrar()
        elif op == "3":
            rotors.editar_rotor()
        elif op == "4":
            break
        else:
            print("Opcio incorrecta")