# connect to database
import pymysql

host = "localhost"
port = 3306
user = "root"
passwd = "Batman#02"
db = "personal_bank_account"
charset = "utf8"

database = pymysql.Connect(host=host, port=port, user=user,
                           passwd=passwd, db=db, charset=charset)
cursor = database.cursor()
userInfo = {}
print("Connection established")

# cursor.execute("ALTER TABLE deposit AUTO_INCREMENT=0")
# database.commit()


def logIn():
    while True:
        username = input('username: ')
        if len(username) < 20:
            userInfo['username'] = username
            break
        else:
            print('username must be within 20 characters')

    sql = "SELECT username FROM user"
    cursor.execute(sql)
    result = cursor.fetchall()
    userExist = False
    for i in result:
        if userInfo["username"] == i[0]:
            userExist = True
    database.commit()

    if userExist == False:
        # sign up
        while True:
            password = input('password: ')
            if len(password) < 20:
                userInfo['password'] = password
                break
            else:
                print('password must be within 20 characters')
        sql = "INSERT INTO user(username, password) VALUES(%s, %s)"
        data = (userInfo["username"], userInfo["password"])
        cursor.execute(sql, data)
        database.commit()
        print('Congrats! Now you have an account!')
    else:
        # sign in
        login = False
        while not login:
            while True:
                password = input('password: ')
                if len(password) < 20:
                    userInfo['password'] = password
                    break
                else:
                    print('password must be within 20 characters')
            sql = "SELECT password FROM user WHERE username = %s"
            data = (userInfo["username"])
            cursor.execute(sql, data)
            result = cursor.fetchone()[0]
            if userInfo["password"] == result:
                login = True
                print('logging in...')
            else:
                login = False
                print('incorrect password')
        database.commit()


logIn()


def makeDeposit():
    while True:
        amount = input('Please select the amount of your current deposit: $')
        if int(amount) > 0 and int(amount) <= 100:
            break
        else:
            print('amount must be larger than 0 and smaller than 100')
    while True:
        reason = input('Please enter the reason of your current deposit: ')
        if reason:
            break
        else:
            print('You must provide with an reason')
    sql = "INSERT INTO deposit(username, amount, reason) VALUES(%s, %s, %s)"
    data = (userInfo["username"], amount, reason)
    cursor.execute(sql, data)
    database.commit()
    msg = 'Operation Saved'
    print(msg)


def makeWithdrawal():
    while True:
        amount = input(
            'Please select the amount of your current withdrawal: $')
        if int(amount) > 0 and int(amount) <= 100:
            break
        else:
            print('amount must be larger than 0 and smaller than 100')
    while True:
        reason = input('Please enter the reason of your current withdrawal: ')
        if reason:
            break
        else:
            print('You must provide with an reason')
    sql = "INSERT INTO withdrawal(username, amount, reason) VALUES(%s, %s, %s)"
    data = (userInfo["username"], amount, reason)
    cursor.execute(sql, data)
    database.commit()
    msg = 'Operation Saved'
    print(msg)


def checkBalance():
    # deposit
    allDeposit = 0
    sql = "SELECT amount FROM deposit WHERE username = %s"
    data = (userInfo["username"])
    cursor.execute(sql, data)
    deposits = cursor.fetchall()
    for deposit in deposits:
        allDeposit += deposit[0]
    database.commit()

    # withdrawal
    allWithdrawal = 0
    sql = "SELECT amount FROM withdrawal WHERE username = %s"
    data = (userInfo["username"])
    cursor.execute(sql, data)
    withdrawals = cursor.fetchall()
    for withdrawal in withdrawals:
        allWithdrawal += withdrawal[0]
    database.commit()

    balance = allDeposit - allWithdrawal
    print(f'Your current balance is ${balance}')
    if balance > 0:
        print('You are doing a really great job!')
    elif balance == 0:
        print('It is never too late to start anew.')
    else:
        print('You must change!')


def checkRecords():
    while True:
        typeSelect = input(
            'Please select the type of records that you want to check. A. deposit B. withdrawal\n')
        if typeSelect.lower() == 'a':
            type = 'deposit'
            break
        elif typeSelect.lower() == 'b':
            type = 'withdraw'
            break
        else:
            print('Please enter A(a) or B(b)')
    if type == 'deposit':
        sql = "SELECT * FROM deposit WHERE username = %s"
    else:
        sql = "SELECT * FROM withdrawal WHERE username = %s"
    data = (userInfo['username'])
    cursor.execute(sql, data)
    records = cursor.fetchall()
    for record in records:
        print(
            f'id: {record[0]} You {type}ed ${record[2]} for the reason that {record[3]}')
    database.commit()
    return type


def deleteTransaction():
    while True:
        type = checkRecords()
        answer = input(
            f'Do you want to delete a transaction in {type}? Y(y)/N(n)\n')
        if answer.lower() == 'y':
            break
        else:
            return

    if type == 'deposit':
        verifySql = "SELECT id FROM deposit WHERE username = %s"
    else:
        verifySql = "SELECT id FROM withdrawal WHERE username = %s"
    verifyData = (userInfo['username'])
    cursor.execute(verifySql, verifyData)
    ids = cursor.fetchall()

    idExist = False
    while not idExist:
        idSelect = input(
            'Please enter the id of the transaction that you want to delete: (press Q to quit)\n')
        if idSelect.lower() == 'q':
            return
        for id in ids:
            if int(idSelect) == id[0]:
                idExist = True
        if idExist == False:
            print('Invalid id')
    database.commit()

    if type == 'deposit':
        sql = "DELETE FROM deposit WHERE username = %s and id = %s"
    else:
        sql = "DELETE FROM withdrawal WHERE username = %s and id = %s"
    data = (userInfo['username'], int(idSelect))
    cursor.execute(sql, data)
    database.commit()
    msg = 'Operation Saved'
    print(msg)


def menu():
    print('Welcome to your personal bank account!\n--------------------------------------')
    prompt = 'A. check balance B. check records C. make a deposit D. make a withdrawal E. (caution!) delete transaction\n'
    while True:
        print('Please select the operation you want to make: ')
        userChoice = input(prompt).lower()
        if userChoice == 'a':
            checkBalance()
        elif userChoice == 'b':
            checkRecords()
        elif userChoice == 'c':
            makeDeposit()
        elif userChoice == 'd':
            makeWithdrawal()
        elif userChoice == 'e':
            deleteTransaction()
        else:
            break


menu()


# end database connection
cursor.close()
database.close()
print("Connection Closed")
