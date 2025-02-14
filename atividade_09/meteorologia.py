import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#colunas do arquivo csv Data,Temp. Inst (C),Umidade (%),Precipitacao (mm)

#carregando o arquivo csv (encoding=ISO-8859-1)

df = pd.read_csv('atividade_09/dados_meteorologicos.csv')

#média, max e min por mes

df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)
df['Ano'] = df['Data'].dt.year
df['Mes'] = df['Data'].dt.month

df_medias = df.groupby(['Ano', 'Mes']).mean()

df_max = df.groupby(['Ano', 'Mes']).max()

df_min = df.groupby(['Ano', 'Mes']).min()

print(df_medias)

print(df_max)

print(df_min)

#grafico de barras precipitação por mes

df_precipitacao = df.groupby('Mes')['Precipitacao (mm)'].sum()

df_precipitacao.plot(kind='bar', title='Precipitação por mês', xlabel='Mês', ylabel='Precipitação (mm)')
plt.grid()
plt.show()

#filtrando e identificando os 10 dias mais quentes e os 10 mais frios

df_max = df.sort_values(by='Temp. Inst (C)', ascending=False).head(10)

df_min = df.sort_values(by='Temp. Inst (C)', ascending=True).head(10)

print(df_max)

print(df_min)

#gerando uma nova coluna
#se prep.> 5mm, coluna = 'Chuvoso', se prep. = 0 'Seco', senão 'Neutro'

df['Condicao'] = np.where(df['Precipitacao (mm)'] > 5, 'Chuvoso', np.where(df['Precipitacao (mm)'] == 0, 'Seco', 'Neutro'))
print(df)

#salvando o arquivo csv

df.to_csv('dados_meteorologicos_novo.csv', index=False)




