import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', password='tang1998', database='bank')
cur = conn.cursor()
cur.execute('create table user_table(username varchar(25) primary key, password varchar(25) not null)')
