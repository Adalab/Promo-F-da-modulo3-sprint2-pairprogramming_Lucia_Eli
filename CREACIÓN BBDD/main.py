#%%
import pandas as pd
import os
from src import query_creacion_soporte as que
from src import BBDD_soporte as BD
#%%
BD.creacion_bbdd_tablas(que.query_creacion_bbdd, "AlumnaAdalab", "Base de datos pair")
print("Creación del esquema de la base datos")
#%%
df=pd.read_csv("clientes.csv", index_col =0)
# %%
df= df.reset_index()
#%%
BD.creacion_bbdd_tablas(que.query_tabla_clientes, "AlumnaAdalab")
#%% 
data_tablaclientes = list((zip(df["id"].values, df["first_name"].values, df["email"].values, df["gender"].values,df["City"].values, df["Country"].values, df["Address"].values)))
#%% 
BD.convertir_float(data_tablaclientes)
#%%
data_tabla_clientes=BD.convertir_float(data_tablaclientes)
#%%
print(data_tabla_clientes)
#%%
BD.insert_data(que.query_insert_tabla_clientes, "AlumnaAdalab", "Base de datos pair", data_tabla_clientes)
# %%
