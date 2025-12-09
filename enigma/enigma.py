import rotors

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"




def netejar_missatge(txt):
    t = ""
    for c in txt.upper():
        if c in alfabet:
            t += c
    return t




def carregar_tot():
    r1 = rotors.carregar_rotor(1)
    r2 = rotors.carregar_rotor(2)
    r3 = rotors.carregar_rotor(3)
    return r1, r2, r3




def avancar(pos, notch):
    nova = (pos + 1) % 26
    salt = False
    if alfabet[pos] == notch:
        salt = True
    return nova, salt

def xifrar_lletra(c, r1, r2, r3, p1, p2, p3):
    i = alfabet.index(c)
    i = alfabet.index(r1[0][(i + p1) % 26])
    i = alfabet.index(r2[0][(i + p2) % 26])
    i = alfabet.index(r3[0][(i + p3) % 26])
    return alfabet[i]

def desxifrar_lletra(c, r1, r2, r3, p1, p2, p3):
    i = alfabet.index(c)
    i = (r3[0].index(alfabet[i]) - p3) % 26
    i = (r2[0].index(alfabet[i]) - p2) % 26
    i = (r1[0].index(alfabet[i]) - p1) % 26
    return alfabet[i]




def xifrar():
    txt = input("Escriu el missatge: ")
    txt = netejar_missatge(txt)
    r1, r2, r3 = carregar_tot()


    w = input("Posicio inicial (ex ABC): ").upper()
    p1 = alfabet.index(w[0])
    p2 = alfabet.index(w[1])
    p3 = alfabet.index(w[2])


    res = ""
    count = 0


    for c in txt:
        p1, salt1 = avancar(p1, r1[1])
        if salt1:
            p2, salt2 = avancar(p2, r2[1])
            if salt2:
                p3, _ = avancar(p3, r3[1])


        x = xifrar_lletra(c, r1, r2, r3, p1, p2, p3)
        res += x
        count += 1
        if count == 5:
            res += " "
            count = 0


    f = open("Xifrat.txt", "w")
    f.write(res)
    f.close()
    print("Missatge xifrat a Xifrat.txt")




def desxifrar():
    try:
        f = open("Xifrat.txt", "r")
        txt = f.read().replace(" ", "")
        f.close()
    except:
        print("No s'ha trobat Xifrat.txt")
        return


    r1, r2, r3 = carregar_tot()


    w = input("Posicio inicial (ex ABC): ").upper()
    p1 = alfabet.index(w[0])
    p2 = alfabet.index(w[1])
    p3 = alfabet.index(w[2])


    res = ""


    for c in txt:
        p1, salt1 = avancar(p1, r1[1])
        if salt1:
            p2, salt2 = avancar(p2, r2[1])
            if salt2:
                p3, _ = avancar(p3, r3[1])


        d = desxifrar_lletra(c, r1, r2, r3, p1, p2, p3)
        res += d


    f = open("Desxifrat.txt", "w")
    f.write(res)
    f.close()
    print("Missatge desxifrat a Desxifrat.txt")
