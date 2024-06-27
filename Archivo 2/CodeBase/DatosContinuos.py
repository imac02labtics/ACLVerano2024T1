# Menor a Mayor
def menorMayor(lista):
    l = len(lista)
    for i in range(0,l):
        elemento = i
        for j in range(i + 1, l):
            if lista[j] < lista[elemento]: # <>
                elemento = j
        lista[i], lista[elemento] = lista[elemento], lista[i]

    return lista

# Odenar clases por frecuencia de mayor a menor
def mayorMenorFrec(listaClases, listaFrec):
    l = len(listaClases)
    for i in range(0,l):
        elemento = i
        for j in range(i + 1, l):
            if listaFrec[j] < listaFrec[elemento]: # <>
                elemento = j
        listaClases[i], listaClases[elemento] = listaClases[elemento], listaClases[i]
        listaFrec[i], listaFrec[elemento] = listaFrec[elemento], listaFrec[i]

    return listaClases, listaFrec

# FORMATEAR DATOS
def formatData(dataArray):
    dataArraySorted = []
    for element in dataArray:
        if isinstance(element, str):
            element = element.strip()
            element = element.lower()
            dataArraySorted.append(element)
        else:
            element = round(element, 3)
            dataArraySorted.append(element)
    
    return dataArraySorted;

# OBTENER DATOS PARA LA TABLA DE FRECUENCIAS
def generateDiscreteData(lstDatos):
    lstDatos = menorMayor(lstDatos)
    lstDatos = formatData(lstDatos)
    clase, frecAbs = [], []
    for element in lstDatos:
        if(element not in clase):
            clase.append(element)
            frecAbs.append(1)
        else:
            frecAbs[clase.index(element)] += 1
        
    frecAbsAc, frecRel, frecRelAc = [], [], []
    frecAbsT = sum(frecAbs)
    ultFa = 0
    ultFr = 0
    for fa in frecAbs:
        fr = 100 / frecAbsT * fa
        frecRel.append(round(fr, 3))
        frecRelAc.append(round(fr+ultFr, 3))
        frecAbsAc.append(fa+ultFa)
        ultFr += fr
        ultFa += fa
    return clase, frecAbs, frecAbsAc, frecRel, frecRelAc

# OBTENER DATOS PARA LA TABLA DE FRECUENCIAS
def generateQualitativeData(lstDatos):
    lstDatos = formatData(lstDatos)
    clase, frecAbs = [], []
    for element in lstDatos:
        if(element not in clase):
            clase.append(element)
            frecAbs.append(1)
        else:
            frecAbs[clase.index(element)] += 1
            
    clase, frecAbs = mayorMenorFrec(clase, frecAbs)
    
    frecAbsAc, frecRel, frecRelAc = [], [], []
    frecAbsT = sum(frecAbs)
    ultFa = 0
    ultFr = 0
    for fa in frecAbs:
        fr = 100 / frecAbsT * fa
        frecRel.append(round(fr, 3))
        frecRelAc.append(round(fr+ultFr, 3))
        frecAbsAc.append(fa+ultFa)
        ultFr += fr
        ultFa += fa
    return clase, frecAbs, frecAbsAc, frecRel, frecRelAc

    
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