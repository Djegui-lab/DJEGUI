import streamlit as st
import pandas as pd
import sqlite3

# Connexion à la base de données SQLite distante
conn = sqlite3.connect('nex_data_assurance.db')

# Charger les données dans un DataFrame
df = pd.read_sql_query('SELECT * FROM nex_data_assurance', conn)

# Afficher les données dans l'interface utilisateur
st.dataframe(df)
st.dataframe(df.describe())

