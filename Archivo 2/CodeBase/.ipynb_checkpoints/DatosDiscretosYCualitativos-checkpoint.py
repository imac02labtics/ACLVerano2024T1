# Imprimir tabla usando pandas
import pandas as pd
def printTable(encabezados, contenido):
    if len(encabezados) == len(contenido):
        data = dict(zip(encabezados, contenido))
        df = pd.DataFrame(data)
        # Imprimir el DataFrame sin los índices
        print(df.to_string(index=False))
    else:
        print("La longitud de encabezados y contenido no coincide")

# Crear tabla HTML
from IPython.display import HTML, display
def printHTMLTable(encabezados, contenido):
    if len(encabezados) == len(contenido):
        html = "<center><table>"
        html += "<tr>"
        for header in encabezados:
            html += f"<th style='border: 1px #ccc solid; text-align: center;'>{header}</th>"
        html += "</tr>"
        rowsNum = len(contenido[0])
        for row in range(rowsNum):
            html += "<tr>"
            for col in contenido:
                html += f"<td style='border: 1px #ccc solid; text-align: center;'>{col[row]}</td>"
            html += "</tr>"
        html += "</table></center>"
        
        display(HTML(html))
    else:
        print("Verificar longitud de encabezados y contenido")

def datosStrPorcentaje(fr, frAc):
    frStr, frAcStr = [], []
    for i in range(len(fr)):
        frStr.append(str(fr[i]) + "%")
    for i in range(len(frAc)):
        frAcStr.append(str(frAc[i]) + "%")
    return frStr, frAcStr