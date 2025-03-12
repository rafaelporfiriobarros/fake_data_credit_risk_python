# Projeto: fake_data_credit_risk_python

## Descrição
Este projeto gera um conjunto de dados sintéticos para análise de risco de crédito utilizando a linguagem Python. O script cria um dataset fictício de 5.000 registros com informações financeiras e de crédito de clientes, permitindo simulações e análises sem comprometer dados reais.

## Bibliotecas Utilizadas
- `pandas` - Para manipulação e armazenamento dos dados em DataFrame.
- `numpy` - Para gerar valores aleatórios e realizar cálculos numéricos.
- `Faker` - Para criação de identificadores únicos fictícios dos clientes.

## Geração dos Dados
Os seguintes atributos são gerados para cada cliente:
- `Customer_ID`: Identificador único (UUID4 gerado pelo Faker).
- `Age`: Idade do cliente (entre 18 e 75 anos).
- `Gender`: Gênero do cliente ("Male" ou "Female").
- `Annual_Income`: Renda anual do cliente (entre 20.000 e 150.000).
- `Loan_Amount`: Valor do empréstimo solicitado (entre 1.000 e 50.000).
- `Credit_Score`: Pontuação de crédito (entre 300 e 850).
- `Late_Payments`: Número de pagamentos atrasados (entre 0 e 10).
- `Loan_Term`: Prazo do empréstimo em meses (12, 24, 36, 48 ou 60).
- `Interest_Rate`: Taxa de juros (entre 3.5% e 25%).
- `Loan_Type`: Tipo de empréstimo ("Personal", "Mortgage", "Auto" ou "Education").

## Definição da Variável Alvo (`Default`)
A variável `Default` indica se o cliente é inadimplente (1) ou não (0). Um cliente é considerado inadimplente caso atenda simultaneamente a estas condições:
- `Credit_Score` inferior a 600.
- Mais de 3 pagamentos atrasados.
- Renda anual inferior a 40.000.

Caso contrário, o cliente é classificado como adimplente (`Default = 0`).

## Armazenamento dos Dados
Os dados gerados são convertidos em um DataFrame do `pandas` e exportados para um arquivo CSV denominado `synthetic_credit_risk.csv`.

## Uso
Para executar o script, basta rodá-lo em um ambiente Python com as bibliotecas mencionadas instaladas. O arquivo CSV resultante pode ser utilizado para análises estatísticas, treinamento de modelos de Machine Learning e outras aplicações relacionadas a risco de crédito.

