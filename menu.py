import mysql.connector as sql
import datetime as dt
conn = sql.connect(host='localhost', user='root', password='tang1998', database='bank')
cur = conn.cursor()
conn.autocommit=True
c = 'y'

while c == 'y':
    print()
    print('1.CREATE BANK ACCOUNT')
    print()
    print('2.TRANSACTION')
    print()
    print('3.CUSTOMER DETAILS')
    print()
    print('4.TRANSACTION DETAILS')
    print()
    print('5.DELETE ACCOUNT')
    print()
    print('6.QUIT')

    print()
    n = int(input('Enter your choice: '))
    print()

    if n == 1:
        acc_no = int(input('Enter your account number: '))
        print()
        acc_name = input('Enter your account name: ')
        print()
        phone_no = int(input('Enter your phone number: '))
        print()
        add = input('Enter your location: ')
        print()
        total_credit = int(input('Enter your credit amount: '))

        SQLInsert = "INSERT INTO customer_details values(" + str(acc_no) + ",'" + acc_name + "'," + str(phone_no) + ",'" + add + "'," + str(total_credit) + ")"
        cur.execute(SQLInsert)
        print()
        print('Account Created Successfully!!')
        conn.commit()

    if n == 2:
        acc_no=int(input('Enter your account number: '))
        cur.execute('select * from customer_details where acc_no=' + str(acc_no))
        data = cur.fetchall()
        count = cur.rowcount
        conn.commit()

        if count == 0:
            print()
            print('Account number is invalid. Try again later. ')
            print()

        else:
            print()
            print('1.WITHDRAW AMOUNT')
            print()
            print('2.ADD AMOUNT')
            print()

            print()
            x = int(input('Enter your choice: '))
            print()
            if x == 1:
                amt = int(input('Enter withdrawal amount: '))
                cr_amt = 0
                cur.execute('update customer_details set cr_amount=cr_amount-' + str(amt) + ' where acc_no=' + str(acc_no))
                SQLInsert = "INSERT INTO transactions values ({}, '{}',{},{})".format(acc_no, dt.datetime.today(), amt, cr_amt)
                cur.execute(SQLInsert)
                conn.commit()
                print()
                print('Account updated successfully!')

            if x == 2:
                amt = int(input('Enter amount to be added: '))
                cr_amt = 0
                cur.execute('update customer_details set cr_amount=cr_amount+' + str(amt) + ' where acc_no=' + str(acc_no))
                SQLInsert = "INSERT INTO transactions values ({} , '{}' , {} , {} )".format(acc_no, dt.datetime.today(), cr_amt,
                                                                                     amt)
                cur.execute(SQLInsert)
                conn.commit()
                print()
                print('Account updated successfully!')

    if n == 3:
        acc_no=int(input('Enter your account number: '))
        SQLSelect = "select * from customer_details where acc_no= " + str(acc_no)
        cur.execute(SQLSelect)
        if cur.fetchone() is None:
            print()
            print('Invalid account number')

        else:
            cur.execute('select * from customer_details where acc_no=' + str(acc_no))
            data=cur.fetchall()
            for row in data:
                print('Account no: ', acc_no)
                print()
                print('Account name: ', row[1])
                print()
                print('Phone number: ', row[2])
                print()
                print('Address: ', row[3])
                print()
                print('Cr_amount: ', row[4])

    if n == 4:
        acc_no = int(input('Enter your account number: '))
        SQLSelect = "select * from customer_details where acc_no=" + str(acc_no)
        cur.execute(SQLSelect)
        if cur.fetchone() is None:
            print()
            print('Invalid account number')

        else:
            cur.execute('select * from transactions where acc_no=' + str(acc_no))
            data = cur.fetchall()
            for row in data:
                print('Account no: ', acc_no)
                print()
                print('Date: ', row[1])
                print()
                print('Withdrawal amount: ', row[2])
                print()
                print('Amount added: ', row[3])
                print()

    if n == 5:
        print('DELETE YOUR ACCOUNT')
        acc_no = int(input('Enter your account number: '))
        check = input('Are you sure to delete your account? Yes/No:  ')

        if check == 'Yes' or check == 'yes':
            cur.execute('delete from customer_details where acc_no=' + str(acc_no))
            print('Account Deleted Successfully!')

    if n == 6:
        print('Do you want to exit? Yes/No: ')
        c = input('Enter your choice: ')

else:
    print("Thank you! ")
    quit()
