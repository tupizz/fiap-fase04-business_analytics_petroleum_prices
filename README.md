### Iniciar Projeto

```bash
poetry new poetry-demo
poetry add matplotlib seaborn
poetry add pandas
poetry add numpy
```


### Iniciar banco de dados

```bash
docker compose up -d
```


```sql
CREATE TABLE public.preco_combustivel(
    regiao VARCHAR(255),
    estado VARCHAR(255),
    municipio VARCHAR(255),
    revenda VARCHAR(255),
    cnpj VARCHAR(255),
    nome_rua VARCHAR(255),
    numero_rua VARCHAR(255),
    complemento VARCHAR(255),
    bairro VARCHAR(255),
    cep VARCHAR(255),
    produto VARCHAR(255),
    data_coleta DATE,
    valor_venda FLOAT,
    unidade_medida VARCHAR(255),
    bandeira VARCHAR(255)
);
```

### Load data to database (option 1) ✅ choosed

```bash
poetry run python ./business_analytics_fase04/01_load_pg_data.py
```

```python
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
```

### Load data to database (option 2)

- Here we're going to load the data from the CSV file to the database.
- We're going to use KNIME to do this.
- We're going to use the `DB Writer` node to write the data to the database.
- We're going to use the `DB Reader` node to read the data from the CSV file.
- We're going to use the `CSV Reader` node to read the data from the CSV file.
- We're going to use the `DB Connection Table Reader` node to read the data from the database.
