import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregamento dos dados
valor_usd = pd.read_csv(r"C:\Users\jlnsa\OneDrive\Documentos\FACUL\MATEMATICA COMPUTACIONAL\ESTUDO DE CASO (BITCOIN)\MANIPULAÇÃO\dados_usd_formatados.csv")
var_btc = pd.read_csv(r"C:\Users\jlnsa\OneDrive\Documentos\FACUL\MATEMATICA COMPUTACIONAL\ESTUDO DE CASO (BITCOIN)\MANIPULAÇÃO\DADOS FORMATADOS\dados_btc_formatados.csv")
var_nasdaq = pd.read_csv(r"C:\Users\jlnsa\OneDrive\Documentos\FACUL\MATEMATICA COMPUTACIONAL\ESTUDO DE CASO (BITCOIN)\MANIPULAÇÃO\dados_nasdaq_formatados.csv")
var_sp500 = pd.read_csv(r"C:\Users\jlnsa\OneDrive\Documentos\FACUL\MATEMATICA COMPUTACIONAL\ESTUDO DE CASO (BITCOIN)\MANIPULAÇÃO\DADOS FORMATADOS\dados_s&p500_formatados.csv")

# Seleção das colunas
valor_usd = valor_usd["Abertura"].reset_index(drop=True)
var_btc = var_btc["Var%"].reset_index(drop=True)
var_nasdaq = var_nasdaq["Var%"].reset_index(drop=True)
var_sp500 = var_sp500["Var%"].reset_index(drop=True)

# Unificação dos dados
dados_unificados = pd.DataFrame({
    "Var_BTC": var_btc,
    "USD_BRL": valor_usd
})
dados_unificados_nasdaq = pd.DataFrame({
    "Var_NASDAQ": var_nasdaq,
    "USD_BRL": valor_usd
})
dados_unificados_sp500 = pd.DataFrame({
    "Var_SP500": var_sp500,
    "USD_BRL": valor_usd
})

#  Ajuste para ordem cronológica (do passado para o presente)
dados_unificados = dados_unificados.iloc[::-1].reset_index(drop=True)
dados_unificados_nasdaq = dados_unificados_nasdaq.iloc[::-1].reset_index(drop=True)
dados_unificados_sp500 = dados_unificados_sp500.iloc[::-1].reset_index(drop=True)

print("\n🔍 Dados organizados:")
print(dados_unificados.head(), dados_unificados_sp500.head(), dados_unificados_nasdaq.head())

escolha = input("Escolha qual simulação deseja efetuar digitando o numero referente a cada um -- (Bitcoin - 1), (Nasdaq - 2), (S&P 500 - 3), (S&P 500 e Nasdaq - 4) --: ")

#   Entradas do usuário
if escolha == "1":
    investimento_inicial_reais = float(input("\n💰 Insira o valor inicial do investimento em Bitcoin (em R$): "))
    aporte_mensal_reais = float(input("💵 Digite o valor do aporte mensal em R$: "))

    #  Conversão inicial para dólar utilizando o câmbio do primeiro mês
    valor_dolar_inicial = dados_unificados.loc[0, "USD_BRL"]
    investimento_atual_dolar = investimento_inicial_reais / valor_dolar_inicial

    #  Loop de simulação mês a mês
    for i, linha in dados_unificados.iterrows():
        variacao = linha["Var_BTC"]
        cambio_dolar_mes = linha["USD_BRL"]

        fator_valorizacao = 1 + variacao

        # Conversão do aporte mensal para dólar no câmbio do mês atual
        aporte_mensal_dolar = aporte_mensal_reais / cambio_dolar_mes

        # Aplicação da valorização e do aporte
        investimento_atual_dolar = (investimento_atual_dolar + aporte_mensal_dolar) * fator_valorizacao
        print(f"Mês {i+1}: Variação BTC: {variacao:.4f}, Câmbio USD: {cambio_dolar_mes:.2f}, "
          f"Investimento (USD): {investimento_atual_dolar:.2f}")
    #  Conversão final de dólares para reais, utilizando o câmbio do último mês
    valor_dolar_final = dados_unificados.iloc[-1]["USD_BRL"]
    investimento_atual_reais = investimento_atual_dolar * valor_dolar_final

    #  Resultado final
    print("\n📊 Resultado Final:")
    print(f"Valor final estimado do investimento: R$ {investimento_atual_reais:.2f}")
elif escolha == "2":
    investimento_inicial_reais = float(input("\n💰 Insira o valor inicial do investimento em Nasdaq (em R$): "))
    aporte_mensal_reais = float(input("💵 Digite o valor do aporte mensal em R$: "))

    #  Conversão inicial para dólar utilizando o câmbio do primeiro mês
    valor_dolar_inicial = dados_unificados_nasdaq.loc[0, "USD_BRL"]
    investimento_atual_dolar = investimento_inicial_reais / valor_dolar_inicial

    #  Loop de simulação mês a mês
    for i, linha in dados_unificados_nasdaq.iterrows():
        variacao = linha["Var_NASDAQ"]
        cambio_dolar_mes = linha["USD_BRL"]

        fator_valorizacao = 1 + variacao

        # Conversão do aporte mensal para dólar no câmbio do mês atual
        aporte_mensal_dolar = aporte_mensal_reais / cambio_dolar_mes

        # Aplicação da valorização e do aporte
        investimento_atual_dolar = (investimento_atual_dolar + aporte_mensal_dolar) * fator_valorizacao
        print(f"Mês {i+1}: Variação Nasdaq: {variacao:.4f}, Câmbio USD: {cambio_dolar_mes:.2f}, "
        f"Investimento (USD): {investimento_atual_dolar:.2f}")

    #  Conversão final de dólares para reais, utilizando o câmbio do último mês
    valor_dolar_final = dados_unificados_nasdaq.iloc[-1]["USD_BRL"]
    investimento_atual_reais = investimento_atual_dolar * valor_dolar_final
    print("\n📊 Resultado Final:")
    print(f"Valor final estimado do investimento: R$ {investimento_atual_reais:.2f}")
elif escolha == "3":
    investimento_inicial_reais = float(input("\n💰 Insira o valor inicial do investimento em S&P500 (em R$): "))
    aporte_mensal_reais = float(input("💵 Digite o valor do aporte mensal em R$: "))

    #  Conversão inicial para dólar utilizando o câmbio do primeiro mês
    valor_dolar_inicial = dados_unificados_sp500.loc[0, "USD_BRL"]
    investimento_atual_dolar = investimento_inicial_reais / valor_dolar_inicial
    for i, linha in dados_unificados_sp500.iterrows():
        variacao = linha["Var_SP500"]
        cambio_dolar_mes = linha["USD_BRL"]

        fator_valorizacao = 1 + variacao

        # Conversão do aporte mensal para dólar no câmbio do mês atual
        aporte_mensal_dolar = aporte_mensal_reais / cambio_dolar_mes

        # Aplicação da valorização e do aporte
        investimento_atual_dolar = (investimento_atual_dolar + aporte_mensal_dolar) * fator_valorizacao

        print(f"Mês {i+1}: Variação S&P 500: {variacao:.4f}, Câmbio USD: {cambio_dolar_mes:.2f}, "
            f"Investimento (USD): {investimento_atual_dolar:.2f}")

    #  Conversão final de dólares para reais, utilizando o câmbio do último mês
    valor_dolar_final = dados_unificados_sp500.iloc[-1]["USD_BRL"]
    investimento_atual_reais = investimento_atual_dolar * valor_dolar_final
    print("\n📊 Resultado Final:")
    print(f"Valor final estimado do investimento: R$ {investimento_atual_reais:.2f}")
elif escolha == "4":
    investimento_inicial_reais = float(input("\n💰 Insira o valor inicial do investimento (em R$): "))
    aporte_mensal_reais = float(input("💵 Digite o valor do aporte mensal (em R$): "))

    #  Dividir igualmente o investimento inicial
    investimento_inicial_reais_dividido = investimento_inicial_reais / 2

    # Inicialização dos investimentos convertidos para dólar
    invest_nasdaq = investimento_inicial_reais_dividido / valor_usd.loc[0]
    invest_sp500 = investimento_inicial_reais_dividido / valor_usd.loc[0]

    #  Loop de simulação mês a mês
    for i in range(len(valor_usd)):
        cambio = valor_usd.loc[i]

        # Fatores de valorização
        fator_nasdaq = 1 + var_nasdaq.loc[i]
        fator_sp500 = 1 + var_sp500.loc[i]

        # Aportes convertidos no câmbio do mês
        aporte_mensal_dolar = (aporte_mensal_reais / cambio) / 2

        # Atualização de cada investimento
        invest_nasdaq = (invest_nasdaq + aporte_mensal_dolar) * fator_nasdaq
        invest_sp500 = (invest_sp500 + aporte_mensal_dolar) * fator_sp500

        # Print mensal (opcional)
        print(f"\nMês {i+1}:")
        print(f"NASDAQ: {invest_nasdaq:.2f} USD | S&P 500: {invest_sp500:.2f} USD")

    #  Conversão final para reais (usando câmbio do último mês)
    valor_final_nasdaq = invest_nasdaq * valor_usd.iloc[0]
    valor_final_sp500 = invest_sp500 * valor_usd.iloc[0]

    #  Valor total do portfólio diversificado
    valor_total_reais = valor_final_nasdaq + valor_final_sp500

    #  Resultado final
    print("\n📊 Resultado Final do Portfólio Diversificado:")
    print(f"NASDAQ: R$ {valor_final_nasdaq:.2f}")
    print(f"S&P 500: R$ {valor_final_sp500:.2f}")
    print(f"🪙 Total Final: R$ {valor_total_reais:.2f}")
else:
    print("Escolha um valor válido!!")