# Análise de Vendas com Python e Power BI

Projeto de análise comercial que demonstra um fluxo completo de dados, desde o tratamento da base com Python até a construção de um dashboard interativo no Power BI.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-ETL-blue)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![DAX](https://img.shields.io/badge/DAX-Medidas-orange)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

## Problema de negócio

Empresas precisam acompanhar seus resultados comerciais de forma clara para identificar produtos, vendedores, categorias e regiões com melhor desempenho.

Este projeto simula um cenário empresarial no qual uma base de vendas é tratada com Python e transformada em indicadores gerenciais no Power BI.

## Objetivo

Construir uma solução de análise comercial capaz de:

- tratar e validar uma base de vendas;
- calcular custos, lucro e margem;
- analisar o desempenho de produtos e vendedores;
- acompanhar indicadores comerciais;
- disponibilizar os registros detalhados;
- facilitar a tomada de decisão por meio de um dashboard interativo.

## Arquitetura do projeto

```mermaid
flowchart LR
    A[Base Excel bruta] --> B[ETL com Python e Pandas]
    B --> C[Base de vendas tratada]
    C --> D[Power BI]
    D --> E[Power Query e Modelagem]
    E --> F[Medidas DAX]
    F --> G[Dashboard Comercial]
```

## Dashboard

### Página 1 — Visão geral

![Página 1 do dashboard](images/dashboard_pagina_1.png)

### Página 2 — Análise comercial

![Página 2 do dashboard](images/dashboard_pagina_2.png)

### Página 3 — Detalhamento dos dados

![Página 3 do dashboard](images/dashboard_pagina_3.png)

## Indicadores desenvolvidos

### Receita total

Apresenta o valor total gerado pelas vendas dentro do período e dos filtros selecionados.

### Lucro

Demonstra o resultado obtido após a dedução dos custos simulados.

### Margem de lucro

Indica qual percentual da receita foi convertido em lucro.

### Ticket médio

Ajuda a acompanhar o valor médio movimentado pelas vendas.

### Quantidade de vendas

Mostra o volume de registros comerciais realizados.

## Análises disponíveis

- Receita por categoria;
- desempenho por produto;
- ranking de vendedores;
- análise por cidade;
- evolução das vendas ao longo do tempo;
- produtos com maior lucro;
- detalhamento dos registros;
- filtros por período, produto, categoria, vendedor e localização.

## Processo de ETL

O script `src/tratamento.py` realiza:

1. leitura da base de vendas em Excel;
2. análise da estrutura dos dados;
3. verificação de valores nulos;
4. remoção de registros duplicados;
5. conversão e validação das datas;
6. criação das colunas de ano, mês, trimestre, dia e dia da semana;
7. cálculo do valor médio por item;
8. simulação dos custos;
9. cálculo do lucro;
10. cálculo da margem percentual;
11. classificação das vendas por faixa de valor;
12. exportação da base tratada.

## Tecnologias utilizadas

- Python;
- Pandas;
- Excel;
- Power BI;
- Power Query;
- DAX;
- HTML para visuais personalizados;
- Git e GitHub.

## Estrutura do projeto

```text
analise-vendas-power-bi/
├── dashboard/
│   └── dashboard_vendas.pbix
├── data/
│   ├── base_vendas_ficticia.xlsx
│   └── base_vendas_tratada.xlsx
├── images/
│   ├── dashboard_pagina_1.png
│   ├── dashboard_pagina_2.png
│   └── dashboard_pagina_3.png
├── src/
│   └── tratamento.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/pedrombz/analise-vendas-power-bi.git
```

### 2. Entre na pasta do projeto

```bash
cd analise-vendas-power-bi
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o tratamento

```bash
python src/tratamento.py
```

A base tratada será gerada dentro da pasta `data`.

## Principais aprendizados

Durante o desenvolvimento, foram aplicados conhecimentos de:

- ETL com Python;
- manipulação de dados com Pandas;
- validação e limpeza de dados;
- criação de métricas comerciais;
- modelagem de dados no Power BI;
- desenvolvimento de medidas em DAX;
- criação de visuais personalizados com HTML;
- organização e documentação de projetos no GitHub.

## Próximas melhorias

- separar os dados em pastas `raw` e `processed`;
- criar logs de execução do ETL;
- adicionar testes automatizados;
- utilizar banco de dados SQL como fonte;
- automatizar a atualização dos dados;
- desenvolver análises preditivas.

## Autor

**Pedro Davi Monteiro**

Estudante de Ciência de Dados com interesse em análise de dados, Business Intelligence, automação e desenvolvimento de soluções orientadas a dados.