import pymysql
connection = pymysql.connect(host='db', user='root', password='test', db='test')
connection.commit()
cursor = connection.cursor()
%config SqlMgci.autopandas = True
%config SqlMagic.feedback = False
%load_ext sql

%%sql mysql+pymysql://root:test@db/test

show databases
