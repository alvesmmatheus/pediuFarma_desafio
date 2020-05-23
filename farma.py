import mysql.connector
from datetime import date   
import json

connection = mysql.connector.connect(host="127.0.0.1", user="root", passwd="", port="3308") 		#Inicia a conexão com o Banco de Dados

sql_select_Query = "SELECT barra, preco, promocao, quantidade, inipromo, fimpromo FROM sysfar.estoque"  #Comando para selecionar as colunas com os dados que serão utilizados
cursor = connection.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()

IndBarra = 0 		#Índice da coluna que contém o código de barras
IndPreco = 1 		#Índice da coluna que contém o preço cheio do item
IndPromocao = 2 	#Índice da coluna que contém o preço promocional do item
IndQuantidade = 3 	#Índice da coluna que contém o preço promocional do item
IndInipromo = 4 	#Índice da coluna que contém a data de início da promoção do item
IndFimpromo = 5 	#Índice da coluna que contém a data de término da promoção do item

today = date.today() # Carrega a data atual 
items = []

for row in records:
    if ((row[IndInipromo] is None) or (row[IndFimpromo] is None)): 					#Verifica se as datas de início e fim da promoção foram definidas
	items.append({'ean': row[IndBarra], 'preco': row[IndPreco], 'estoque':row[IndQuantidade]}) 	#Se não foram definidas,  o preço será o preço cheio

    elif (row[IndInipromo] <= today <= row[IndFimpromo]): 						#Verifica se a data atual está dentro do prazo da promoção do item
        items.append({'ean': row[IndBarra], 'preco': row[IndPromocao], 'estoque':row[IndQuantidade]}) 	#Se houver promoção, o preço promocional sobrepõe o preço cheio

    else:
        items.append({'ean': row[IndBarra], 'preco': row[IndPreco], 'estoque':row[IndQuantidade]}) 	#Se não houver promoção, segue com o preço cheio

farma = json.dumps(items, indent = 2, sort_keys = False) 						#Cria uma lista JSON no modelo: [ { "ean":789000000, "preco":1.99,"estoque":38},{ "ean":789000001, "preco":3.99,"estoque":18},...]

with open("pediuFarma.json", "w") as outfile:  								#Cria um arquivo .json com a lista json acima
    outfile.write(farma) 

cursor.close()
connection.close()
