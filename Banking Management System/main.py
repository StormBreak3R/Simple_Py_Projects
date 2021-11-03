"""
Banking management system
Group Project Done By:
Ahsanul Haque - 1820182078
Tanvir Ahmed - 1820182074
"""

import random
import pickle
import os
import pathlib
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)


class Account:
    def __init__(self):
        self.accNo = 0
        self.f_name = ''
        self.l_name = ''
        self.name = ''
        self.deposit = 0
        self.type = ''


    def newemployeeacc(self):
        self.name = input("Enter Your Name: ")
        self.accNo = random.randint(1000, 9999)
        input("Enter reference Name: ")
        print("\n\n")
        print(Fore.RED + "New Employee account created . . . .")
        print(f"Your Employee Tag: {self.accNo}")
        print(Fore.RED + Style.BRIGHT + "[PLEASE, REMEMBER YOUR  TAG NUMBER!]")

    def createaccount(self):
        self.f_name = input("Enter Your First Name: ")
        self.l_name = input("Enter Your Last Name: ")
        self.name = self.f_name + " " + self.l_name
        self.accNo = random.randint(10000000, 99999999)
        self.type = input("Enter the type of account [C/S] : ")
        self.deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current: "))
        print("\n\n")
        print(Style.BRIGHT + "Account Created Successfully . . . .")
        print(Style.BRIGHT + f"Your Account Number: {self.accNo}")
        print(Fore.RED + Style.BRIGHT + "[PLEASE DON'T FORGET YOUR ACCOUNT NUMBER!]")
        print()

    def showAccount(self):
        print("Account Number : ", self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account", self.type)
        print("Balance : ", self.deposit)

    def modifyAccount(self):
        print("Account Number : ", self.accNo)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify type of Account :")
        self.deposit = int(input("Modify Balance :"))

    def depositAmount(self, amount):
        self.deposit += amount

    def withdrawAmount(self, amount):
        self.deposit -= amount

    def report(self):
        print(self.accNo, " ", self.name, " ", self.type, " ", self.deposit)

    def getAccountNo(self):
        return self.accNo

    def getAcccountHolderName(self):
        return self.name

    def getAccountType(self):
        return self.type

    def getDeposit(self):
        return self.deposit

    def datainformation(self):
        pass


def EmoloyeeRecord():
    print(Fore.MAGENTA + Style.BRIGHT + "---- Employee Record ----")
    print(Fore.MAGENTA + Style.BRIGHT + "-------------------------")
    print()
    print(Fore.GREEN + "    1. New Employee")
    print(Fore.GREEN + "    2. Delete Employee")
    print(Fore.GREEN + "    3. Employee List")
    ch2 = input(Style.BRIGHT + "    Enter Your choice: ")
    employee = Account()
    if ch2 == "1":
        employee.newemployeeacc()
        employeeAccFile(employee)
    elif ch2 == "2":
        tag = int(input(Style.BRIGHT + "    Enter The employee Tag: "))
        deleteEmployee(tag)
    elif ch2 == "3":
        emplist()


def transactions():
    print(Fore.MAGENTA + Style.BRIGHT + "---- Transactions ----")
    print(Fore.MAGENTA + Style.BRIGHT + "----------------------")
    print()
    print(Fore.RED + "     1. Deposit")
    print(Fore.RED + "     2. Withdraw")
    print(Fore.RED + "     3. Balance Enquiry")
    print(Fore.RED + "     0. Back")
    ch3 = input(Style.BRIGHT + "Enter your choice: ")
    if ch3 == "1":
        num = int(input(Style.BRIGHT + "    Enter The account No. : "))
        depositAndWithdraw(num, 1)
    elif ch3 == "2":
        num = int(input(Style.BRIGHT + "    Enter The account No. : "))
        depositAndWithdraw(num, 2)
    elif ch3 == "3":
        num = int(input(Style.BRIGHT + "    Enter The account No. : "))
        displaySp(num)




def accountdetails():
    print(Fore.MAGENTA + Style.BRIGHT + "---- Account Details ----")
    print(Fore.MAGENTA + Style.BRIGHT + "--------------------------")
    print()
    print(Fore.GREEN + "     1. Open Account")
    print(Fore.GREEN + "     2. Modify Account")
    print(Fore.GREEN + "     3. Delete Account")
    print(Fore.GREEN + "     4. Data Information")
    print(Fore.GREEN + "     0. Back")
    ch1 = input(Style.BRIGHT + "    Enter Your Choice: ")
    account = Account()
    if ch1 == "1":
        account.createaccount()
        writeAccountsFile(account)
    elif ch1 == "2":
        num = int(input(Style.BRIGHT + "    Enter The account No. : "))
        modifyAccount(num)
    elif ch1 == "3":
        num = int(input(Style.BRIGHT + "    Enter The account No. : "))
        deleteAccount(num)
    elif ch1 == "4":
        datainfo()


def emplist():
    file = pathlib.Path("employee.data")
    if file.exists():
        infile = open('employee.data', 'rb')
        mylist = pickle.load(infile)
        for item in mylist:
            print(item.name, " ", item.accNo, " ")
        infile.close()
    else:
        print(Fore.RED + Style.BRIGHT + "No records to display")
    print()

def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        for item in mylist:
            print(item.accNo, " ", item.name, " ", item.type, " ", item.deposit)
        infile.close()
        print()
    else:
        print(Fore.RED + Style.BRIGHT + "No records to display")


def displaySp(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist:
            if item.accNo == num:
                print(Style.BRIGHT + "Your account Balance is = ", item.deposit)
                print()
                found = True
    else:
        print(Fore.RED + Style.BRIGHT + "No records to Search")
    if not found:
        print("No existing record with this number")


def depositAndWithdraw(num1, num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist:
            if item.accNo == num1:
                if num2 == 1:
                    amount = int(input(Fore.GREEN + "Enter the amount to deposit : "))
                    item.deposit += amount
                    print(Fore.RED + Style.BRIGHT + "Your account has been updated!")
                elif num2 == 2:
                    amount = int(input(Fore.GREEN + "Enter the amount to withdraw: "))
                    if amount <= item.deposit:
                        item.deposit -= amount
                        print(Fore.RED + Style.BRIGHT + "Your account has been updated!")
                    else:
                        print(Fore.RED + "You Cannot Withdraw Big amount")

    else:
        print(Fore.RED + "No records to Search")
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist:
            if item.accNo != num:
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
        print(Fore.RED + "    Your Account Has been deleted!")


def deleteEmployee(tag):
    file = pathlib.Path("employee.data")
    if file.exists():
        infile = open('employee.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist:
            if item.accNo != tag:
                newlist.append(item)
        os.remove('employee.data')
        outfile = open('newemployee.data', 'wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newemployee.data', 'employee.data')
        print(Fore.RED + "Employee Record Deleted!")
        print()

def aboutus():
    print(Fore.YELLOW + Style.BRIGHT + """    Bank PB aka Bank Peaky Blinders is a multi functional, technology based modern Bank.
    JUST DEPOSIT AND FORGET. :33
    Our goal is to To be the best performing bank in the world""")

def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist:
            if item.accNo == num:
                item.name = input("Enter the account holder name : ")
                item.type = input("Enter the account Type : ")
                item.deposit = int(input("Enter the Amount : "))

        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


def datainfo():
    print("""Dear Client,
    We always provide the best support for our clients. Its our duty to keep your data
    safe and secure. So, stay free and Thanks for staying with Bank PB""")


def writeAccountsFile(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else:
        oldlist = [account]
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


def employeeAccFile(employee):
    file = pathlib.Path("employee.data")
    if file.exists():
        infile = open('employee.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(employee)
        infile.close()
        os.remove('employee.data')
    else:
        oldlist = [employee]
    outfile = open('newemployee.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newemployee.data', 'employee.data')


ch = ''
ch4 = ''
num = 0

print(Fore.MAGENTA + Style.BRIGHT + "----WELCOME TO BANK PB----")
print(Fore.MAGENTA + Style.BRIGHT + "--------------------------")
print(Fore.GREEN + "    1. Customer")
print(Fore.GREEN + "    2. Employee")
print(Fore.GREEN + "    0. Exit")
role = input(Style.BRIGHT + "Enter Your Role: ")

if role == "1":
    while ch != 0:
        print(Fore.MAGENTA + Style.BRIGHT + "----Customer Options----")
        print(Fore.MAGENTA + Style.BRIGHT + "------------------------")
        print()
        print(Fore.GREEN + "    1. Account Details")
        print(Fore.GREEN + "    2. Transactions")
        print(Fore.GREEN + "    3. About US")
        print(Fore.GREEN + "    0. Exit")
        ch = input(Style.BRIGHT + "Please Enter your choice: ")
        if ch == '1':
            accountdetails()
        elif ch == "2":
            transactions()
        elif ch == "3":
            aboutus()
        elif ch == '0':
            print(Style.BRIGHT + "Thanks for using our service!".upper())
            break
        else:
            print(Fore.RED + Style.BRIGHT + "Invalid Choice")
            print()

elif role == "2":
    while ch4 != 0:
        print(Fore.MAGENTA + Style.BRIGHT + "----Employee Options----")
        print(Fore.MAGENTA + Style.BRIGHT + "------------------------")
        print(Fore.GREEN + "    1. Employee Record")
        print(Fore.GREEN + "    2. Account Holders List")
        print(Fore.GREEN + "    0. Exit")
        ch4 = input(Style.BRIGHT + "Enter Your Choice: ")
        if ch4 == "1":
            EmoloyeeRecord()
        elif ch4 == "2":
            displayAll()
        elif ch4 == '0':
            print(Style.BRIGHT + "Thanks for using our service!".upper())
            break
        else:
            print(Fore.RED + Style.BRIGHT + "Invalid Choice")
            print()


















