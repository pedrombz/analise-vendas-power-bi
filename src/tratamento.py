# ==========================================
# ETL - Tratamento da Base de Vendas
# ==========================================

from pathlib import Path

import pandas as pd


# ------------------------------------------
# Configuração dos caminhos
# ------------------------------------------

PASTA_PROJETO = Path(__file__).resolve().parent.parent
ARQUIVO_ENTRADA = (
    PASTA_PROJETO
    / "data"
    / "raw"
    / "base_vendas_ficticia.xlsx"
)

ARQUIVO_SAIDA = (
    PASTA_PROJETO
    / "data"
    / "processed"
    / "base_vendas_tratada.xlsx"
)

# ------------------------------------------
# Importando a base
# ------------------------------------------

print("Lendo a base de dados...")

if not ARQUIVO_ENTRADA.exists():
    raise FileNotFoundError(
        f"Arquivo não encontrado: {ARQUIVO_ENTRADA}"
    )

df = pd.read_excel(ARQUIVO_ENTRADA)

print("Base carregada com sucesso!\n")


# ------------------------------------------
# Pegando informações da base
# ------------------------------------------

print("=" * 60)
print("INFORMAÇÕES DA BASE")
print("=" * 60)

df.info()

print("\nQuantidade de registros e colunas:")
print(df.shape)

print("\nValores nulos:")
print(df.isnull().sum())


# ------------------------------------------
# Remoção de registros duplicados
# ------------------------------------------

registros_antes = len(df)

df.drop_duplicates(inplace=True)

registros_depois = len(df)

print(
    f"\nRegistros duplicados removidos: "
    f"{registros_antes - registros_depois}"
)


# ------------------------------------------
# Conversão da coluna de data
# ------------------------------------------

df["data"] = pd.to_datetime(
    df["data"],
    errors="coerce"
)

datas_invalidas = df["data"].isna().sum()

print(f"Datas inválidas encontradas: {datas_invalidas}")

df.dropna(
    subset=["data", "quantidade", "valor_total"],
    inplace=True
)


# ------------------------------------------
# Criação de novas colunas de data
# ------------------------------------------

meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro",
}

dias = {
    "Monday": "Segunda-feira",
    "Tuesday": "Terça-feira",
    "Wednesday": "Quarta-feira",
    "Thursday": "Quinta-feira",
    "Friday": "Sexta-feira",
    "Saturday": "Sábado",
    "Sunday": "Domingo",
}

df["ano"] = df["data"].dt.year
df["mes"] = df["data"].dt.month
df["nome_mes"] = df["mes"].map(meses)
df["trimestre"] = df["data"].dt.quarter
df["dia"] = df["data"].dt.day
df["dia_semana"] = df["data"].dt.day_name().map(dias)


# ------------------------------------------
# Criação de métricas de vendas
# ------------------------------------------

df["ticket_medio"] = (
    df["valor_total"]
    .div(df["quantidade"].replace(0, pd.NA))
    .round(2)
)

df["custo_total"] = (
    df["valor_total"] * 0.68
).round(2)

df["lucro"] = (
    df["valor_total"] - df["custo_total"]
).round(2)

df["margem_%"] = (
    df["lucro"]
    .div(df["valor_total"].replace(0, pd.NA))
    .mul(100)
    .round(2)
)


# ------------------------------------------
# Classificação das vendas
# ------------------------------------------

def classificar_venda(valor):
    if valor < 500:
        return "Baixa"

    if valor < 2000:
        return "Média"

    return "Alta"


df["faixa_venda"] = df["valor_total"].apply(
    classificar_venda
)


# ------------------------------------------
# Validação dos dados
# ------------------------------------------

print("\n" + "=" * 60)
print("VALIDAÇÃO")
print("=" * 60)

print(f"Total de vendas: {len(df)}")

print(
    f"Valor total vendido: "
    f"R$ {df['valor_total'].sum():,.2f}"
)

print(
    f"Ticket médio por item: "
    f"R$ {df['ticket_medio'].mean():,.2f}"
)

print(
    f"Lucro total: "
    f"R$ {df['lucro'].sum():,.2f}"
)


# ------------------------------------------
# Exportando a base tratada
# ------------------------------------------

df.to_excel(
    ARQUIVO_SAIDA,
    index=False
)

print(
    "\nBase tratada exportada com sucesso em:"
)

print(ARQUIVO_SAIDA)

print("\nPrimeiros registros:")

print(df.head())