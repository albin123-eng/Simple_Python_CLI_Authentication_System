print("Welcome To ATM")
log = {}
balance = 0
def add_login():
    username = input("Enter your username: ")
    password = input('Enter your password: ')
    log[username] = password
    return log
def login():
    attemp = 0
    while attemp < 3:
        username = input("Enter your username: ")
        password = input('Enter your password: ')
        if username in log and password == log[username]:
            print('You are logged in successfully')
        else:
            attemp += 1
def withdraw(balance):
    amount =int(input('Enter your amount to withdraw: '))
    if amount < balance:
        balance = balance - amount
        return balance
    else:
        print('You cannot withdraw more money than you have')
def deposit(balance):
    amount = int(input('Enter your amount to deposit: '))
    balance = balance + amount
    return balance




