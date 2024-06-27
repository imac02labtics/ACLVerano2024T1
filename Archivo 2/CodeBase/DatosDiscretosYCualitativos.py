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