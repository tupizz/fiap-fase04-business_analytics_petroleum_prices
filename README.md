### Iniciar Projeto

```bash
poetry new poetry-demo
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

```

### Load data to database (option 2)

- Here we're going to load the data from the CSV file to the database.
- We're going to use KNIME to do this.
- We're going to use the `DB Writer` node to write the data to the database.
- We're going to use the `DB Reader` node to read the data from the CSV file.
- We're going to use the `CSV Reader` node to read the data from the CSV file.
- We're going to use the `DB Connection Table Reader` node to read the data from the database.
