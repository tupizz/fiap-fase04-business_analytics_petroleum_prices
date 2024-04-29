import pandas as pd
from sqlalchemy import create_engine
import os
import chardet

database_url = "postgresql+psycopg2://postgres:123456@localhost:5432/postgres"

# create a SQLALchemy engine
engine = create_engine(database_url)

path_to_csv = "/Users/tupizz/Desktop/fiap/business-analytics-fase04/data"

csv_files = [f for f in os.listdir(path_to_csv) if f.endswith('.csv')]


# Function to detect file encoding
def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        # Read enough of the file to make a good guess
        rawdata = file.read(50000)
    return chardet.detect(rawdata)['encoding']


# Define transformations and data loading
def transform_and_load(file_path: str):
    encoding = detect_encoding(file_path)
    print(f"Detected encoding: {encoding}")

    print(f"Loading data from {os.path.basename(file_path)}...")
    # Load CSV into DataFrame
    df = pd.read_csv(file_path, encoding=encoding, delimiter=';', quotechar='"', header=0, on_bad_lines='skip')

    # Rename columns as necessary (adjust according to your needs)
    df.rename(columns={
        'Regiao - Sigla': 'regiao',
        'Estado - Sigla': 'estado',
        'Municipio': 'municipio',
        'Revenda': 'revenda',
        'CNPJ da Revenda': 'cnpj',
        'Nome da Rua': 'nome_rua',
        'Numero Rua': 'numero_rua',
        'Complemento': 'complemento',
        'Bairro': 'bairro',
        'Cep': 'cep',
        'Produto': 'produto',
        'Data da Coleta': 'data_coleta',
        'Valor de Venda': 'valor_venda',
        'Unidade de Medida': 'unidade_medida',
        'Bandeira': 'bandeira'
    }, inplace=True)

    df.drop(['Valor de Compra'], axis=1, inplace=True)

    # Convert data types
    df['data_coleta'] = pd.to_datetime(df['data_coleta'], format='%d/%m/%Y')
    df['valor_venda'] = df['valor_venda'].str.replace(',', '.').astype(float)

    # Handle missing values
    df['complemento'] = df['complemento'].fillna('')  # Assuming empty string for missing complemento

    print(df.info())

    # # Load DataFrame into PostgreSQL table
    df.to_sql('preco_combustivel', con=engine, if_exists='append', index=False)
    print(f"Data from {os.path.basename(file_path)} loaded successfully.")


# Process each file
for file_name in csv_files:
    file_path = os.path.join(path_to_csv, file_name)
    transform_and_load(file_path)
