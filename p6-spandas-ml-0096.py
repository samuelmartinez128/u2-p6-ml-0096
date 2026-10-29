import pandas as pd 
import numpy as np
## Samuel Martinez NC 0096
serie_amigos=["Pedro", "Morgan","Farfan","El Adrian","Jesse","Nava","Mario"]
print("--- Serie listado de amigos NC 0096")
amigos=pd.Series(serie_amigos)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
print("--- Serie listado de billetes MX NC 0096")
billetes=pd.Series(serie_billetes)
print(billetes)

serie_billetes=[20,50,100,200,500,1000]
serie_bletras=("veinte","cincuenta","cien","doscientos","quinientos","mil")
print("--- Serie listado nombre y valor de billetes MX NC 0096")
tablabilletes=pd.Series(serie_billetes,serie_bletras)
print(tablabilletes)
# Diccionario frame
# Diccionario de valor monedas y nombre
print("Datos de diccionario a DataFrame en pandas")
dic_monedas={
   "serie_billetes":[20,50,100,200,500,1000],
   "serie_bletras":("veinte","cincuenta","cien","doscientos","quinientos","mil")
}

tablabilletes=pd.DataFrame(dic_monedas,index=["A","B","C","D","E","F"])
print(tablabilletes)

print("Casa de cambio de Samuel Martinez NC 0096")