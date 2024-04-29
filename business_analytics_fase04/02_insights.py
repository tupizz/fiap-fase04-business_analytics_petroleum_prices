import pandas as pd
from sqlalchemy import create_engine

database_url = "postgresql+psycopg2://postgres:123456@localhost:5432/postgres"

# create a SQLALchemy engine
engine = create_engine(database_url)

with engine.connect() as connection:
    print("Connection successful!")
    print("Reading data from the database...")

    df = pd.read_sql_query("""
        SELECT * FROM public.preco_combustivel;
    """, connection)

    df['data_coleta'] = pd.to_datetime(df['data_coleta'])
    df_anp = df[['data_coleta', 'regiao', 'estado', 'municipio','bandeira', 'produto', 'valor_venda' ]]
    df_anp['ano'] = df_anp['data_coleta'].dt.year
    df_anp['mes'] = df_anp['data_coleta'].dt.month
    print(df_anp.head())

    # Estatísticas basica
    print(df_anp.describe().round(2))

    # Quais são os tipos de produtos que estão sendo comercializados?
    print(f"Tipos de produtos: {df_anp['produto'].unique()}\n\n")

    # Quais são as bandeiras que estão presentes na base de dados?
    print(f"Bandeiras: {df_anp['bandeira'].unique()}\n\n")

    # Qual a média de preço de combustível por estado?
    print("Média de preço de combustível por estado: ")
    print(df_anp.groupby('estado')['valor_venda'].mean().round(2))
    print("\n\n")

    df_anp_valor = df_anp[['ano', 'produto', 'valor_venda']]

    # Quais os minimos e maximos de preço de combustível por ano?
    print("Mínimos e máximos de preço de combustível por ano: ")
    print(df_anp_valor.groupby(['produto', 'ano']).agg(['min', 'max', 'mean']).round(2))
    print("\n\n")


    df_anp_valor_estado = df_anp[['ano', 'produto', 'estado', 'valor_venda']]

    # Quais os minimos e maximos de preço de combustível por estado e por ano?
    print("Mínimos e máximos de preço de combustível por estado e por ano: ")
    print(df_anp_valor_estado.groupby(['produto', 'ano', 'estado']).agg(['min', 'max', 'mean']).round(2))
    print("\n\n")

