import pandas as pd


df = pd.read_csv('sdw2026.csv')
print("Dados extraídos com sucesso!")


def gerar_mensagem(nome):
    return f"Olá {nome}, o Santander quer te ajudar a investir. Confira as ofertas para o seu cartão!"

df['Mensagem'] = df['Nome'].apply(gerar_mensagem)
print("Mensagens geradas com sucesso!")


df.to_csv('sdw2026_com_mensagens.csv', index=False)
print("Arquivo 'sdw2026_com_mensagens.csv' criado com sucesso!")

print("\n--- Resultado Final ---")
print(df)