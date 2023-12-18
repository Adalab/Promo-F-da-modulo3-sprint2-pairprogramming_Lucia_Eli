#%%
import pandas as pd

# %%
query_creacion_bbdd = "CREATE SCHEMA IF NOT EXISTS `Base de datos pair`;"
# %%
df=pd.read_csv("clientes.csv", index_col =0)
# %%
df= df.reset_index()
# %%

# %%
query_tabla_clientes = """CREATE TABLE IF NOT EXISTS `Base de datos pair`.`clientes` (
                            `id` VARCHAR(45) NOT NULL,
                            `first_name` VARCHAR(45) NOT NULL,
                            `last_name` VARCHAR(45) NOT NULL,
                            `email` VARCHAR(45) NULL,
                            `gender` VARCHAR(45) NULL,
                            `City` VARCHAR(45) NULL,
                            `Country` VARCHAR(45) NULL,
                            `Address` VARCHAR(45) NULL,
                            PRIMARY KEY (`id`));"""
 
# %%
query_insert_tabla_clientes = "INSERT INTO clientes (id, first_name, last_name, email, gender, City, Country, Address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"


