import pandas as pd

data={
"Nombre":["jonier", "juan", "sebastian", "luis"],
"edad":[32,28,15,20],
"ciudad":["Bogota", "pereira","cali","Medellin"],
}

df = pd.DataFrame(data)
print(df)