import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('memory_usage.csv')

# Convertendo o Timestamp para o tipo datetime para melhor manipulação
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%H:%M:%S')

# Plotando os gráficos
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotando o uso de memória
ax1.plot(df['Timestamp'], df['MemUsed'], color='tab:blue', label='Memória Usada (MB)')
ax1.set_xlabel('Timestamp')
ax1.set_ylabel('Memória Usada (MB)', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Criando um eixo y compartilhado para o uso de swap
ax2 = ax1.twinx()
ax2.plot(df['Timestamp'], df['SwapUsed'], color='tab:red', label='Swap Usada (MB)')
ax2.set_ylabel('Swap Usada (MB)', color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Adicionando título
plt.title('Uso de Memória e Swap Durante o Teste')

# Exibindo o gráfico
fig.tight_layout()
plt.show()
