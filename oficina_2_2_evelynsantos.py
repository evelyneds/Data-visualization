# -*- coding: utf-8 -*-
"""Oficina_2_2_evelynsantos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-XaJFCqFKnRYpr3jVrkwanVBykLOSZrX

# Oficina Aula 2.2
Durante a aula, você aprendeu a utilizar gráficos de pizza e gráficos de barra para visualizar proporções entre categorias, permitindo comparar partes com o todo. Agora, é hora de exercitar o que você aprendeu!

Nesta oficina, você deve continuar a analisar os dados de vendas de videogames. Portanto, crie um Jupyter Notebook e responda cada questão com código em uma célula.

1.   Importe as bibliotecas pandas e matplotlib, usando a palavra mágica inline para exibir as visualizações no notebook; e carregue os dados, que estão disponibilizados neste link:dados, em um DataFrame. Assim, você pode carregar os dados pela URI ou salvar em sua máquina e carregá-los localmente;
1.   Crie uma visualização que mostre a proporção de vendas global entre gêneros de jogos da empresa Nintendo;
1.   Crie uma visualização que mostre a proporção de quantidade de jogos por plataforma a partir do ano de 2015

# 1  Importe as bibliotecas pandas/ Carregue os dados em um DataFrame
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

data_games = pd.read_csv('https://raw.githubusercontent.com/evelynsantos/Data-visualization/main/dadosoficina04.txt')
data_games.head()

"""# 2 visualização com proporção de vendas global do dataset"""

global_sales_nintendo = data_games[data_games['Publisher'] == 'Nintendo']
generos_nintendo = global_sales_nintendo.groupby(by='Genre').sum()
global_sales_nintendo.head()

global_nintendo_sort= generos_nintendo.sort_values(by='Global_Sales', ascending=False)
porcentagens = global_nintendo_sort['Global_Sales']*100.0/global_nintendo_sort['Global_Sales'].sum()
plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(15,5))
plt.bar(global_nintendo_sort.index, porcentagens, color='C1')
plt.title('Proporção de vendas de jogos por gênero')
plt.show()

plt.figure(figsize=(8, 10))
plt.pie(x=generos_nintendo['Global_Sales'], labels = generos_nintendo.index, autopct='%1.1f%%',startangle=90, pctdistance=0.90)
my_circle=plt.Circle((0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.show()

"""# 3 visualização da proporção de quantidade de jogos"""

gender_period = data_games.query('Year > 2014')
gender_period = gender_period.groupby(by='Platform').sum()
gender_period

gender_period_sort = gender_period.sort_values(by='Global_Sales', ascending=False)
porcentagens = gender_period_sort['Global_Sales']*100.0/gender_period_sort['Global_Sales'].sum()
plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(15,5))
plt.bar(gender_period_sort.index, porcentagens, color='C1')
plt.title('Proporção de vendas de jogos por gênero')
plt.show()