# A biblioteca cx_Oracle irá se comunicar com as bibliotecas do cliente Oracle

# Para esse teste, foi baixado o Instant Client Package - Basic Light v12.1.0.2.0 e descompactado em C:\instantclient
# Por último, foi adicionado o caminho do driver (C:\instantclient\instantclient_12_2) na variável PATH do ambiente

import cx_Oracle

#MODO 1: Conexão diretamente pelo python
host = '192.168.x.x'
port = '1521'
service_name = 'SERVICE_NAME_123'
username = 'user'
password = 'pass'

connection = cx_Oracle.connect(f"{username}/{password}@{host}:{port}/{service_name}")

#MODO 2: Conexão através do TNSNAMES.ORA
#Para esse modo funcionar, deve-se colocar o TNSNAMES em: C:\instantclient\instantclient_12_2\network\admin
username = 'user'
password = 'pass'
service = 'SERVICE_123'

connection = cx_Oracle.connect(username, password, service)

#------------------------------------------[EXEMPLO DE QUERY]------------------------------------

#Definido o cursor
cursor = connection.cursor()
#Feito uma query qualquer
cursor.execute("SELECT * FROM TABLE_123")

#Iteração no cursor para retornar as linhas da consulta
for row in cursor:
    print(row)
    
    