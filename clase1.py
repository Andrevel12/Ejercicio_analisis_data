import pandas as pd
list_unidades =[120, 150, 90, 200]
list_indices=["semana 1","semana 2","semana 3","semana 4"]
nombres_series = pd.Series(data=list_unidades,index=list_indices)
print(nombres_series)

#ventas totales
ventas_totales=nombres_series.sum()
print("ventas totales", ventas_totales)

#promedio de ventas
prom_ventas= int(nombres_series.mean())
print("promedio venta", prom_ventas)

#mayor venta y la menor venta
mayor_venta=nombres_series.max()
menor_venta=nombres_series.min()
print("mayor venta", mayor_venta, ": menor venta",menor_venta)

#semanas mayor ventas y menor ventas
semana_mayor=nombres_series.idxmax()
semana_min=nombres_series.idxmin()
print("semana mayor venta:",semana_mayor, ": semana menor venta", semana_min)

#incrementar el 10 %
serie_aumentada= (nombres_series * 1.1).astype(int)
print("serie aumentada")
print(serie_aumentada)