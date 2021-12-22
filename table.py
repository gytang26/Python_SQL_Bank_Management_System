import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', password='tang1998', database='bank')
cur = conn.cursor()
cur.execute('create table customer_details(acc_no int primary key, acc_name varchar(25), phone_no bigint(25) check (phone_no > 11), address varchar(25), cr_amount float)')