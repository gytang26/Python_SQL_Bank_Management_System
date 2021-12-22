import mysql.connector as sql
import datetime as dt

conn = sql.connect(host='localhost', user='root', password='tang1998', database='bank')
cur = conn.cursor()

print("------------------------------------------WELCOME TO SQUID BANK------------------------------------------")

print(dt.datetime.now())
print('1.REGISTER')
print()
print('2.LOGIN')
print()

n = int(input('Enter your choice: '))
print()

if n == 1:
    name = input('Enter your username: ')
    print()
    password = int(input('Enter a 4 digits password: '))
    print()
    SQLInsert = "INSERT INTO user_table (password, username) values (" + str(password) + ", '" + name + "') "
    cur.execute(SQLInsert)
    conn.commit()
    print()
    print('USER created successfully')
    import menu

if n == 2:
    name = input('Enter your username: ')
    print()
    password = int(input('Enter a 4 digits password: '))
    print()
    SQLSelect = "select * from user_table where password='" + str(password) + "' and username= '" + name + "' "
    cur.execute(SQLSelect)
    if cur.fetchone() is None:
        print()
        print('Invalid username or password')

    else:
        print()
        import menu
