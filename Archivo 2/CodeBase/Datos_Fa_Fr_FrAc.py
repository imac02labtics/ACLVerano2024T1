# Frecuencia absoluta
def frecAbs(lstDatos):
    clase, frecAbs = [], []
    for element in lstDatos:
        if(element not in clase):
            clase.append(element)
            frecAbs.append(1)
        else:
            frecAbs[clase.index(element)] += 1
    return clase, frecAbs

# Odenar clases y frecuencias
def mayorMenorFrec(listaClases, listaFrec):
    l = len(listaClases)
    for i in range(0,l):
        elemento = i
        for j in range(i + 1, l):
            if listaClases[j] < listaClases[elemento]: # <>
                elemento = j
        listaClases[i], listaClases[elemento] = listaClases[elemento], listaClases[i]
        listaFrec[i], listaFrec[elemento] = listaFrec[elemento], listaFrec[i]

    return listaClases, listaFrec

# Frecuencia Relativa
def frecRel(frecAbs):
    frecRel = []
    frecAbsT = sum(frecAbs)
    for element in frecAbs:
        fr = 100 / frecAbsT * element
        fr = round(fr, 3)
        frecRel.append(fr)
    return frecRel

# Frecuencia Acumulada
def frecAc(frec):
    frecAc = []
    ultVal = 0
    for element in frec:
        fAc = element
        frecAc.append(fAc+ultVal)
        ultVal += fAc
    return frecAc

def calcularFaFrFrAc(datos):
    clases, fa = frecAbs(datos)
    clasesSorted, faSorted = mayorMenorFrec(clases, fa)
    fr = frecRel(faSorted)
    frAc = frecAc(fr)

    return clasesSorted, faSorted, fr, frAc