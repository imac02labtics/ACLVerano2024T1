{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "97409acc-21a2-427e-94e3-729191b6ac25",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Imprimir tabla usando pandas\n",
    "import pandas as pd\n",
    "def printTable(encabezados, contenido):\n",
    "    if len(encabezados) == len(contenido):\n",
    "        data = dict(zip(encabezados, contenido))\n",
    "        df = pd.DataFrame(data)\n",
    "        # Imprimir el DataFrame sin los índices\n",
    "        print(df.to_string(index=False))\n",
    "    else:\n",
    "        print(\"La longitud de encabezados y contenido no coincide\")\n",
    "\n",
    "# Crear tabla HTML\n",
    "from IPython.display import HTML, display\n",
    "def printHTMLTable(encabezados, contenido):\n",
    "    if len(encabezados) == len(contenido):\n",
    "        html = \"<center><table>\"\n",
    "        html += \"<tr>\"\n",
    "        for header in encabezados:\n",
    "            html += f\"<th style='border: 1px #ccc solid; text-align: center;'>{header}</th>\"\n",
    "        html += \"</tr>\"\n",
    "        rowsNum = len(contenido[0])\n",
    "        for row in range(rowsNum):\n",
    "            html += \"<tr>\"\n",
    "            for col in contenido:\n",
    "                html += f\"<td style='border: 1px #ccc solid; text-align: center;'>{col[row]}</td>\"\n",
    "            html += \"</tr>\"\n",
    "        html += \"</table></center>\"\n",
    "        \n",
    "        display(HTML(html))\n",
    "    else:\n",
    "        print(\"Verificar longitud de encabezados y contenido\")\n",
    "\n",
    "def datosStrPorcentaje(fr, frAc):\n",
    "    frStr, frAcStr = [], []\n",
    "    for i in range(len(fr)):\n",
    "        frStr.append(str(fr[i]) + \"%\")\n",
    "    for i in range(len(frAc)):\n",
    "        frAcStr.append(str(frAc[i]) + \"%\")\n",
    "    return frStr, frAcStr"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

