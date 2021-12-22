import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', password='tang1998', database='bank')
cur = conn.cursor()
cur.execute('create table transactions(acc_no int(20), date date, withdrawal_amount bigint(20), amount_added bigint(20))')
