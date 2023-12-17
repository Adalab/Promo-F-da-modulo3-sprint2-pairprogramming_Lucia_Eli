#%%
import pandas as pd
import os
import sys

pd.set_option('display.max_columns', None)
#%%

df_ventas=pd.read_csv("data/ventas.csv",index_col=0)
df_productos=pd.read_csv("data/productos.csv",on_bad_lines='skip',index_col=0)
df_clientes=pd.read_csv("data/clientes.csv",index_col=0)


#%%
def exploracion_dataframe(dataframe):

    print(f"Los duplicados que tenemos en el conjunto de datos son: {dataframe.duplicated().sum()}")
    print("\n ..................... \n")
    
    
    # generamos un DataFrame para los valores nulos
    print("Los nulos que tenemos en el conjunto de datos son:")
    df_nulos = pd.DataFrame(dataframe.isnull().sum() / dataframe.shape[0] * 100, columns = ["%_nulos"])
    display(df_nulos[df_nulos["%_nulos"] > 0])
    null_columns = dataframe.columns[dataframe.isnull().any()].tolist()
    print(null_columns)
    
    print("\n ..................... \n")
    print(f"Los tipos de las columnas son:")
    display(pd.DataFrame(dataframe.dtypes, columns = ["tipo_dato"]))
    
    
    print("\n ..................... \n")
    print("Los valores que tenemos para las columnas categóricas son: ")
    dataframe_categoricas = dataframe.select_dtypes(include = "O")
    
    for col in dataframe_categoricas.columns:
        print(f"La columna {col.upper()} tiene las siguientes valore únicos:")
        display(pd.DataFrame(dataframe[col].value_counts()).head()) 

    return null_columns
    
    
# %%
exploracion_dataframe(df_ventas)
# %%
exploracion_dataframe(df_clientes)
# %%
exploracion_dataframe(df_productos)
# %%
def nulos(df):
    null_columns = df.columns[df.isnull().any()].tolist()
    df[null_columns] = df[null_columns].fillna("Unknown")
    
    return df

# %%
nulos(df_clientes)

# %%

def modificar_productos(df):
    df = df.reset_index()
    null_columns = df.columns[df.isnull().any()].tolist()
    df[null_columns] = df[null_columns].fillna("Unknown")
    nuevos_nombres = ['ID', 'Nombre_Producto', 'Categoría', 'Precio', 'Origen', 'Descripción', 'ingredientes']
    df.columns = nuevos_nombres
    return df


# %%
def organizacion_dataframe(df):
    df= df.reset_index()
    return df

# %%
df_ventas= organizacion_dataframe(df_ventas)

# %%
df_clientes =organizacion_dataframe(df_clientes)

# %%
def integrar_datos(df1, df2, df3):
    # Unir df_clientes y df_ventas por el ID_Cliente
    df_intermedio = pd.merge(df1, df2, left_on='ID_Cliente', right_on='id', how='inner')

    # Unir el resultado anterior con df_productos por el ID_Producto
    tabla_final = pd.merge(df_intermedio, df3, left_on='ID_Producto', right_on='ID', how='inner')

    return tabla_final
# %%
integrar_datos(df_ventas, df_productos, df_clientes)


