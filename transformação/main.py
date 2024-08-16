import pandas as pd
import sqlite3
from datetime import datetime

# carregando o dataframe do json
df = pd.read_json('../data/data.jsonl', lines=True)

#criando novas colunas
df['source'] = 'https://lista.mercadolivre.com.br/tenis-corrida-masculino'
df['_data_coleta'] = datetime.now()

# tratando os numeros como float
df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['old_price_centavos'] = df['old_price_centavos'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['new_price_centavos'] = df['new_price_centavos'].fillna(0).astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)

# Tirando os parenteses do amount
df['reviews_amount'] = df['reviews_amount'].str.replace('[\(\)]', '', regex=True)
df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)

# juntando os reais com os centavos
df['old_price'] = df['old_price_reais'] + df['old_price_centavos'] / 100
df['new_price'] = df['new_price_reais'] + df['new_price_centavos'] / 100

# removendo as colunas de preços antigas
df.drop(columns=['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_centavos'], inplace=True)

# conectando ao banco de dados sql
conn = sqlite3.connect('../data/data.db')

# salvar o df no banco de dados
df.to_sql('mercadolivre_itens', conn, if_exists='replace', index=False)

# fechar a conexão
conn.close()