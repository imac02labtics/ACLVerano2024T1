# Frecuencia Relativa
def frecRel(frecAbs):
    frecRel = []
    frecAbsT = sum(frecAbs)
    for element in frecAbs:
        fr = 100 / frecAbsT * element
        frecRel.append(round(fr, 3))
    return frecRel

# Frecuencia Acumulada
def frecAc(frec):
    frecAc = []
    ultVal = 0
    for element in frec:
        fAc = element
        frecAc.append(round(fAc+ultVal, 3))
        ultVal += fAc
    return frecAc

import math
def clases_groped(datos, noClases=0):
    datos.sort()
    minVal = datos[0]
    maxVal = datos[0]
    
    for num in datos:
        if num > maxVal:
            maxVal = num
        if num < minVal:
            minVal = num
    
    rango = maxVal - minVal
    #print(rango, maxVal, minVal)
    
    if noClases == 0:
        numClases = 1 + 3.3 * math.log10(len(datos))
    else: 
        numClases = noClases
    numClases = int(numClases)
    anchoClase = rango / numClases
    #print(anchoClase, rango, numClases)
    
    limsInf = []
    limsSup = []
    mrksClases = []
    limInf = minVal
    limSup = minVal+anchoClase
    for i in range(1,numClases+1):
        mrkClase = (limSup + limInf)/2
        limsSup.append(round(limSup, 3))
        limsInf.append(round(limInf, 3))
        mrksClases.append(round(mrkClase, 3))
        limInf = limSup
        limSup = limInf+anchoClase
    clases = list(range(1,numClases+1))
    return clases, limsInf, limsSup, mrksClases


def faGrouped(limSup, limInf, datos, forma=1):
    fa = [0] * len(limInf)
    for dato in datos:
        for j in range(0, len(limInf)):
            if forma == 1:
                if j == len(limInf)-1:
                    if limInf[j] <= dato <= limSup[j]:
                        fa[j] += 1
                        break
                else:
                    if limInf[j] <= dato < limSup[j]:
                        fa[j] += 1
                        break
            else:
                if j == 0:
                    if limInf[j] <= dato <= limSup[j]:
                        fa[j] += 1
                        break
                else:
                    if limInf[j] < dato <= limSup[j]:
                        fa[j] += 1
                        break
    return fa
    
def generateGroupedData(datos, forma=1, noClases=0):
    clases, limsInf, limsSup, mrksClases = clases_groped(datos, noClases)
    fa = faGrouped(limsSup, limsInf, datos, forma)
    fr = frecRel(fa)
    frAc = frecAc(fr)

    return clases, limsInf, limsSup, mrksClases, fa, fr, frAc