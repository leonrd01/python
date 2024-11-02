import pandas as pd 
import matplotlib.pyplot as plt

# Carregar o arquivo CSV com pandas
dados = pd.read_csv("vendas.csv")

# Calcular o total de vendas (Quantidade * Preço Unitário) para cada produto
dados["Total_Vendas"] = dados["Quantidade"] * dados["Preço_Unitario"]

# Exibir a tabela com os totais de vendas
print(dados)

# Visualizar os dados em um gráfico de barras
plt.bar(dados["Produto"], dados["Total_Vendas"], color="blue")
plt.xlabel("Produto")
plt.ylabel("Total de Vendas (R$)")
plt.title("Vendas por Produto")
plt.show()