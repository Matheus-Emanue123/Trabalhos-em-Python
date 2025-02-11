import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
n_medicoes = 100

latencia_r1 = np.random.normal(loc=10, scale=2, size=n_medicoes)
latencia_r2 = np.random.normal(loc=15, scale=3, size=n_medicoes)
latencia_r3 = np.random.normal(loc=20, scale=4, size=n_medicoes)
latencia_r4 = np.random.normal(loc=25, scale=5, size=n_medicoes)

df = pd.DataFrame({
    'Roteador 1': latencia_r1,
    'Roteador 2': latencia_r2,
    'Roteador 3': latencia_r3,
    'Roteador 4': latencia_r4
})

print("Primeiras linhas do DataFrame:")
print(df.head())

plt.figure(figsize=(10, 6))
sns.boxplot(data=df)
plt.title('Boxplot das Latências dos Roteadores')
plt.ylabel('Latência (ms)')
plt.xlabel('Roteadores')
plt.show()

percentual_acima_18 = {}
for coluna in df.columns:
    contagem = (df[coluna] > 18).sum()
    percentual = (contagem / n_medicoes) * 100
    percentual_acima_18[coluna] = percentual

print("\nPorcentagem de medições com latência acima de 18 ms:")
for roteador, perc in percentual_acima_18.items():
    print(f"{roteador}: {perc:.2f}%")

plt.figure(figsize=(10, 6))
bins = np.linspace(df.min().min(), df.max().max(), 20)
plt.hist(df['Roteador 1'], bins=bins, alpha=0.5, label='Roteador 1', density=True)
plt.hist(df['Roteador 2'], bins=bins, alpha=0.5, label='Roteador 2', density=True)
plt.hist(df['Roteador 3'], bins=bins, alpha=0.5, label='Roteador 3', density=True)
plt.hist(df['Roteador 4'], bins=bins, alpha=0.5, label='Roteador 4', density=True)
plt.xlabel('Latência (ms)')
plt.ylabel('Densidade')
plt.title('Distribuição das Latências dos Roteadores')
plt.legend()
plt.show()
