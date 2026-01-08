import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------
# Criar pasta de saída
# -----------------------------
os.makedirs('outputs/figures', exist_ok=True)

# -----------------------------
# Carregar dados
# -----------------------------
df = pd.read_csv(
    'data/dados_doenca_mental_2019_2025.csv',
    sep=';',
    encoding='latin1',
    skiprows=6,
    header=None
)

df.columns = [
    'Ano',
    'Norte',
    'Nordeste',
    'Sudeste',
    'Sul',
    'Centro_Oeste',
    'Total'
]

# -----------------------------
# Gráfico 1 - Evolução total
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(df['Ano'], df['Total'], marker='o')
plt.title('Evolução dos Casos de Doenças Mentais no Brasil (2019–2025)')
plt.xlabel('Ano')
plt.ylabel('Número de casos')
plt.grid(True)
plt.tight_layout()
plt.savefig('outputs/figures/evolucao_total.png')
plt.close()

# -----------------------------
# Gráfico 2 - Total por região
# -----------------------------
totais_regiao = df[['Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro_Oeste']].sum()

plt.figure(figsize=(8,5))
totais_regiao.plot(kind='bar')
plt.title('Casos Totais por Região (2019–2025)')
plt.xlabel('Região')
plt.ylabel('Número de casos')
plt.tight_layout()
plt.savefig('outputs/figures/total_por_regiao.png')
plt.close()

# -----------------------------
# Gráfico 3 - Evolução por região
# -----------------------------
plt.figure(figsize=(8,5))
for regiao in ['Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro_Oeste']:
    plt.plot(df['Ano'], df[regiao], label=regiao)

plt.title('Evolução dos Casos por Região')
plt.xlabel('Ano')
plt.ylabel('Número de casos')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('outputs/figures/evolucao_por_regiao.png')
plt.close()

# -----------------------------
# Insight numérico
# -----------------------------
crescimento_total = (
    (df['Total'].iloc[-1] - df['Total'].iloc[0])
    / df['Total'].iloc[0]
) * 100

print(f'Crescimento total no período: {crescimento_total:.2f}%')
