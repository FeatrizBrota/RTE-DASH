import mysql.connector

conexao_dev = mysql.connector.connect(
    host='rteop-dtb.econeteditora.com.br',
    port=3306,
    user='douglas_rangel',
    password='',
    database='rte')


conexao_hml = mysql.connector.connect(
    host='rteop-dtb.econeteditora.com.br',
    port=3307,
    user='douglas_rangel',
    password='',
    database='rte')


conexao_prod = mysql.connector.connect(
    host='database-tributacao.cluster-cgbav3shbm0x.sa-east-1.rds.amazonaws.com',
    port=3306,
    user='douglas_rangel',
    password='',
    database='rte')
