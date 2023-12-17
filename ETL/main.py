#%%
import pandas as pd
import os
import sys
from src import soporte_pair as so
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames
#%%
df_ventas=pd.read_csv("data/ventas.csv",index_col=0)
df_productos=pd.read_csv("data/productos.csv",on_bad_lines='skip',index_col=0)
df_clientes=pd.read_csv("data/clientes.csv",index_col=0)
# %%
# %%
so.exploracion_dataframe(df_ventas)
# %%
so.exploracion_dataframe(df_clientes)
# %%
so.exploracion_dataframe(df_productos)
# %%
df_productos=so.modificar_productos(df_productos)
# %%
df_clientes =so.organizacion_dataframe(df_clientes)
# %%
df_ventas= so.organizacion_dataframe(df_ventas)

df_final= so.integrar_datos(df_ventas, df_productos.df_clientes)
