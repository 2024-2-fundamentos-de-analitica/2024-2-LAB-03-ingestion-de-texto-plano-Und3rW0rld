"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    ruta = 'files/input/clusters_report.txt'
    with open(ruta, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    column_names = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
    data = []
    current_cluster = None
    
    for line in lines[4:]:
        line = line.strip()
        if not line:
            continue
        
        parts = re.split(r'\s{2,}', line)
        
        if parts[0].isdigit():
            if current_cluster:
                data.append(current_cluster)
            
            porcentaje = float(parts[2].replace('%', '').replace(',', '.').strip())
            current_cluster = [int(parts[0]), int(parts[1]), porcentaje, ' '.join(parts[3:]).strip()]
        else:
            current_cluster[3] += ' ' + ' '.join(parts).strip()
    
    if current_cluster:
        data.append(current_cluster)
    
    for row in data:
        row[3] = re.sub(r'\s*,\s*', ', ', row[3])
        row[3] = row[3].rstrip('.')
    
    df = pd.DataFrame(data, columns=column_names)
    return df