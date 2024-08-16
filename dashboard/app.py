import pandas as pd
import streamlit as st
import sqlite3

# conectar ao banco de dados
conn = sqlite3.connect('../data/data.db')

# Carregar os dados da tabela em um dataframe pandas
df = pd.read_sql_query("SELECT * FROM mercadolivre_itens", conn)

# Fechar conexão banco de dados
conn.close()

# Titulo da aplicação
st.title('Pesquisa de Mercado - Tenis Esportivos no Mercado Livre')

# Melhorar layout com colunas KPI
st.subheader('KPIs principais do sistema')
col1, col2, col3 = st.columns(3)

# KPI1 numero total de  itens
total_itens = df.shape[0]
col1.metric(label='Numero Total de Itens', value=total_itens)

# KPI2 numero de marcas unicas
unique_brands = df['brand'].nunique()
col2.metric(label='Numero de Marcas', value=unique_brands)

# KPI3 preço novo médio
average_new_price = df['new_price'].mean()
col3.metric(label='Preo Médio (R$)', value=f'{average_new_price:.2f}')

# Quais marcas são mais encontradas até a página 10
st.subheader('Marcas mais Encontradas até a página 10')
col1, col2 = st.columns([4,2])
top_10_pages_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_pages_brands)
col2.write(top_10_pages_brands)

# Qual preço médio por marca
st.subheader('Preço Médio por Marca')
col1, col2 = st.columns([4,2])
df_non_zero_price = df[df['new_price']>0]
average_price_by_brand = df_non_zero_price.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

# Qual satisfação média por marca

st.subheader('Satisfação Média por Marca')
col1, col2 = st.columns([4,2])
df_non_zero_satisfaction = df[df['reviews_rating_number']>0]
satisfaction = df_non_zero_satisfaction.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction)
col2.write(satisfaction)