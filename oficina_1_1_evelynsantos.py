# -*- coding: utf-8 -*-
"""Oficina_1_1_evelynsantos.ipynb

O consumo excessivo de álcool é um problema grave de saúde pública, você não acha? Imagine que você é um cientista de dados trabalhando em uma equipe da Organização Mundial da Saúde (OMS), cujo objetivo é desenvolver relatórios sobre o consumo de álcool no mundo.

Foram coletados dados de diferentes países, indicando o consumo de cerveja (beer), licor (spirit) e vinho (wine), e o consumo de litros de álcool por pessoa do país no ano de 2010. Seu trabalho, então, é responder a algumas perguntas sobre os dados que irão ajudar a compor o relatório.

1.   Qual a média e desvio padrão do consumo de cerveja, licor, vinho e total de álcool?
1.   Qual o consumo de licor na França?
1.   Quais os 5 países nos quais se consome mais vinho?
1.   Quais os países nos quais o consumo de cerveja está acima da média?
1.   Quais países nos quais o consumo total de álcool está acima do Brasil, em ordem do menor para o maior?

Para responder a essas questões, você deve usar os dados disponibilizados nesta página:
[
dados.](https://d11s0xq1vqg039.cloudfront.net/videos_conteudo/visual/micro01/oficina/arquivos/dadosoficina01.txt)

Baixe o conjunto de dados, selecionando o link e clicando com o botão direito do mouse ou usando a tecla Aplicação. Então, escolha a opção “Salvar como…”, e salve o arquivo com o nome drinks.txt. Na mesma pasta em que você salvou os dados, crie um Jupyter Notebook, importe a biblioteca pandas e carregue os dados com os comandos abaixo.
"""

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/evelynsantos/data/589ff087bc8f69677fc20c6e6efe99ded01d0c95/alcohol-consumption/drinks.csv')
msg=("\n")

df.head(10)

#Question 1
print('''A média do consumo de cerveja, licor, vinho e total de álcool é consecutivamente
\n{}\n\nO desvio padrão é \n{}'''.format(df.mean(), df.std()))

#Question 2
df_spirit_fr = df[df['country'] == 'France']
print('O consumo de licor na França é de {} l/ano'.format(df_spirit_fr['spirit_servings'].values))

#Question 3
print('Os 5 países que mais consomem vinho são')
df.sort_values(by='wine_servings', ascending = False).head(5)

#Question 4
mean_beer = df['beer_servings'].mean()
print(f'Os países que tem consumo acima da média({mean_beer:.2f}) são \n ')
df[df['beer_servings'] > mean_beer].sort_values(by='beer_servings', ascending=False).country

br

#Question 5

df_br_alcohol = df[df['country'] == 'Brazil']
df[df['total_litres_of_pure_alcohol'] > df_br_alcohol['total_litres_of_pure_alcohol'].mean()].sort_values(by='total_litres_of_pure_alcohol', ascending = True)
