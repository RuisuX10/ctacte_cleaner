import pandas as pd

# Cargar el DataFrame
df = pd.read_excel("cta_cte.xlsx", sheet_name="Sheet1")

# Obtener el nombre de la segunda columna
columna_b = df.columns[1]

# Buscar la fila donde se encuentra "Saldo Anterior" en la segunda columna
saldo_anterior_index = df[df[columna_b] == 'Saldo Anterior'].index

# Verificar si la fila debajo de "Saldo Anterior" está vacía
for idx in saldo_anterior_index:
    if pd.isna(df.loc[idx + 1, columna_b]):  # Si la celda debajo está vacía
        # Eliminar la fila de "Saldo Anterior", las 4 superiores y las 2 inferiores
        df.drop(df.index[idx-4:idx+2], inplace=True)

# Guardar el DataFrame modificado si es necesario
df.to_excel("cta_cte_modificado.xlsx", index=False)
