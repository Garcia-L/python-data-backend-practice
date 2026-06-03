# Proyecto 2 — Analizador de datos (Data Analyst)

# instala pandas desde el cmd 
# py -m pip install pandas

# import pandas as pd
import pandas as pd 

# Leer un CSV y:
csv = pd.read_csv(r'C:\Users\Luisg\OneDrive\Documentos\4. Practica Python\python basic\proyectos\mymoviedb.csv', sep=",", quotechar='"', engine="python")

# Mostrar promedio
data = csv["Popularity"]
average = data.mean()
print(f'Promedio: {average}')

# Filtrar datos
csv["Vote_Average"] = pd.to_numeric(csv["Vote_Average"], errors="coerce")

filtro = csv[ csv["Vote_Average"] > 9]

print("\nFiltro")
print(filtro[ ["Title", "Vote_Average"] ])

# Ordenar
ordenados = filtro.sort_values(by="Vote_Average", ascending=False)

print("\nOrdenados")
print(ordenados[ ["Title", "Vote_Average"] ])
