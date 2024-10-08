import matplotlib.pyplot as plt

# Dados de exemplo
nomes_v = ['Candidato A', 'Candidato B', 'Candidato C', 'Candidato D']
votos_v = [150, 200, 300, 250]

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.title('Candidatos a Vereador', fontsize=14)
bars = plt.bar(nomes_v, votos_v, color='skyblue')

# Definir o tamanho da fonte para os rótulos dos eixos
plt.xticks(fontsize=8)  # Tamanho da fonte para os rótulos do eixo x
plt.yticks(fontsize=8)  # Tamanho da fonte para os rótulos do eixo y

# Adicionar rótulos aos eixos
plt.xlabel('Candidatos', fontsize=10)
plt.ylabel('Votos', fontsize=10)

# Exibir grade para facilitar a leitura
plt.grid(axis='y')

# Ajustar layout
plt.tight_layout()

# Mostrar o gráfico
plt.show()
