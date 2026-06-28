class Bank:

    def __init__(self, account_number, name, phone, balance=0):
        self.account_number = account_number
        self.name = name
        self.phone = phone
        self.balance = balance


    def deposit(self, amount):
  
        if amount <= 0:
            print("Invalid Amount")
            return

        self.balance += amount
        print(f"Rupees {amount} deposited successfully.")
        print(f"Current Balance: {self.balance}")


    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid Amount")
            return

        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"Rupees {amount} debited from your account.")
            print(f"Current Balance: {self.balance}")


    def show_balance(self):
        print(f"Current Balance: {self.balance}")


    def show_info(self):
        print("\n------ Account Details ------")
        print(f"Name           : {self.name}")
        print(f"Account Number : {self.account_number}")
        print(f"Phone          : {self.phone}")
        print(f"Balance        : {self.balance}")
        print("-----------------------------")



accounts = []


while True:

    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Show All Accounts")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Exit")


    choice = int(input("Enter your choice: "))


    if choice == 1:

        account_number = int(input("Enter Account Number: "))
        name = input("Enter Name: ")
        phone = int(input("Enter Phone Number: "))

        account = Bank(account_number, name, phone)

        accounts.append(account)

        print("Account Created Successfully ✅")


    elif choice == 2:

        if len(accounts) == 0:
            print("No Accounts Found")

        else:
            for account in accounts:
                account.show_info()



    elif choice == 3:

        account_number = int(input("Enter Account Number: "))
        amount = int(input("Enter Deposit Amount: "))

        found = False

        for account in accounts:

            if account.account_number == account_number:
                account.deposit(amount)
                found = True
                break


        if found == False:
            print("Account Not Found")



    elif choice == 4:

        account_number = int(input("Enter Account Number: "))
        amount = int(input("Enter Withdrawal Amount: "))

        found = False

        for account in accounts:

            if account.account_number == account_number:
                account.withdraw(amount)
                found = True
                break


        if found == False:
            print("Account Not Found")



    elif choice == 5:

        account_number = int(input("Enter Account Number: "))

        found = False

        for account in accounts:

            if account.account_number == account_number:
                account.show_balance()
                found = True
                break


        if found == False:
            print("Account Not Found")



    elif choice == 6:

        print("Thank you for using Bank Management System 🏦")
        break



    else:
        print("Invalid Choice")


