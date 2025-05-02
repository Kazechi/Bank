import time
#default input user value
users = {
    "ahjin": {"pin": "1234", "balance_usd": 5000},
    "ajin": {"pin": "5678", "balance_usd": 3000}
}

information = {""}

def progress_bar(total):
    for x in range(total + 1):
        percent = (x / total) * 100
        bar = '█' * int(percent / 5) + '-' * (20 - int(percent / 5))
        print(f"\rLoading: |{bar}| {percent:.0f}%", end='')
        time.sleep(0.1)

def listOfAccounts():
    return information

def registerLogin():
    print("----------Do you want to Register or Login----------")
    user = input("Input 'R', if you want to register, and 'L', if you want to login: ").upper()

    if user == "R":
        return register()
    elif user == "L":
        return login()
    else:
        print("Invalid Input. Please try again!")
        return None



def register():
    print("----------Register----------")
    username = input("Enter your name: ")
    #this will notify the user that the username had already been taken
    if username in listOfAccounts():
        print("Username already exists. Please log in.")
        return None
    
    #using try except
    #this approach will be able to return the output of the user without receiving it as error
    #this will make the code transparent towards letters
    try:
        pin = input("Enter your pin: ")
    except ValueError:
        print("Pin must be a NUMBER!")
        return None

    confirmation = input("Is the information correct? Input Y if 'Yes' or N if 'No': ").upper()
    if confirmation == "Y":
        users[username] = {"pin": pin, "balance_usd": 0}
        information.add(username) == username
        information.add(pin) == pin
        print("Registration successful!\n")
        print("---Getting ready your account---")
        progress_bar(30)
        return login()
    elif confirmation == "N":
        print("Registration cancelled.\n")
        return None
    # This will redirectly the admin towards its users
    elif confirmation == "ML":
        viewer()
    else:
        print("Invalid input! Please enter Y or N.\n")
        return None
    

def login():
    print("\n----------Login----------")
    username = input("Enter your username: ")
    #using try except
    #this approach will be able to return the output of the user without receiving it as error
    #this will make the code transparent towards letters
    try:
        pin = input("Enter your pin: ")
    except ValueError:
        print("Pin must be a NUMBER!")
        return None

    if username in users and users[username]["pin"] == pin:
        print(f"Welcome, {username}!\n")
        return username
    else:
        print("Invalid username or pin. Please try again!")
        return None






# This function will show only to the admin
def viewer():
    rName = input("Enter Root Name: ")
    pNumber = input("Enter Pin Number: ")
    #check
    if rName == "JavaRice" and pNumber == "2023":
        viewUsers()

#check the currency around asia
#variable name - Intended code - rate per country
currency_rates = {
    "Philippines": {"code": "PHP", "rate": 56.0},
    "Japan": {"code": "JPY", "rate": 150.0},
    "South Korea": {"code": "KRW", "rate": 1300.0},
    "China": {"code": "CNY", "rate": 7.2},
    "India": {"code": "INR", "rate": 83.0},
    "Indonesia": {"code": "IDR", "rate": 16000.0},
    "Thailand": {"code": "THB", "rate": 36.0},
    "Malaysia": {"code": "MYR", "rate": 4.7},
    "Vietnam": {"code": "VND", "rate": 24500.0},
    "Singapore": {"code": "SGD", "rate": 1.35}
}
    
#showing all available country inside the list
def select_country():
    print("Select your current country:")
    for i, country in enumerate(currency_rates.keys(), 1):
        print(f"{i}. {country}")
    try:
        choice = int(input("Enter number: ")) - 1
        country = list(currency_rates.keys())[choice]
        return country
    except:
        print("Invalid selection.")
        return "Singapore"

def convert_to_local(usd, rate):
    return usd * rate

def convert_to_usd(local, rate):
    return local / rate

def get_amount(currency_code, rate, to_usd=True):
    amt = float(input(f"Enter amount in {currency_code}: "))
    return convert_to_usd(amt, rate) if to_usd else convert_to_local(amt, rate)

# getting the money from the current value inside the bank
def withdraw(user, rate, currency_code):
    #create a choice to determine the user wants regarding the currency that the user will need
    choice = input(f"Withdraw in USD or {currency_code}? (USD/{currency_code}): ").upper()
    if choice == "USD":
        amount = float(input("Enter amount in USD: "))
    elif choice == currency_code:
        amount = get_amount(currency_code, rate, to_usd=True)
    else:
        print("Invalid currency.")
        return
    #calculating the current balance of the user
    #this will print if the transaction is succesful
    if users[user]["balance_usd"] >= amount:
        users[user]["balance_usd"] -= amount
        print(f"Withdrawn successfully. New balance in USD: ${users[user]['balance_usd']:.2f}")
    else:
        print("Insufficient funds.")

# putting the money inside the bank
def deposit(user, rate, currency_code):
    #create a choice to determine the user wants regarding the currency that the user will need
    choice = input(f"Deposit in USD or {currency_code}? (USD/{currency_code}): ").upper()
    if choice == "USD":
        amount = float(input("Enter amount in USD: "))
    elif choice == currency_code:
        amount = get_amount(currency_code, rate, to_usd=True)
    else:
        print("Invalid currency.")
        return
    #calculating the current money inside the bank of the user
    #this will print the amount of money currently inside the bank of the user
    users[user]["balance_usd"] += amount
    print(f"Deposit successful. New balance in USD: ${users[user]['balance_usd']:.2f}")


# transferring money in the default users
# note this can be changeable accordingly if the user will be default or by having a user input from external sources
def transfer(user):
    recipient = input("Enter recipient username: ")
    #will check whether the inputted recipient is available at the user
    if recipient not in users:
        #return this statement if the user is not found
        print("Recipient not found.")
        return
    # the user will only be able to put amount base on the standard currency which is 'USD'
    amount = float(input("Enter amount to transfer (USD only): "))
    if users[user]["balance_usd"] >= amount:
        users[user]["balance_usd"] -= amount
        users[recipient]["balance_usd"] += amount
        # display the name of the recipient as well as the transferred money
        # this will only display if the transfer was succesful
        print(f"Transferred ${amount:.2f} to {recipient}.")
    else:
        print("Insufficient funds.")
# the user will be able to pay the bills in this system
def pay_bills(user, rate, currency_code):
    # will identify what type of bills the user will pay
    bill_type = input("Enter bill type: ")
    # will create choices whether the user want to pay using 'USD' or the currency the user currently in
    choice = input(f"Pay in USD or {currency_code}? (USD/{currency_code}): ").upper()
    # will display if the user has chosen 'USD' as payment currency
    if choice == "USD":
        amount = float(input("Enter bill amount in USD: "))
    # if the user inputted different currency, 
    # this line will get the current value of "USD" from the country that the user had chosen 
    elif choice == currency_code:
        amount = get_amount(currency_code, rate, to_usd=True)
    else:
    # this will print if the current amount of money inside the user is less than that needs to be paid
        print("Invalid Currency")
        return
    # will reduce the current value of the user inside the bank account
    if users[user]["balance_usd"] >= amount:
        users[user]["balance_usd"] -= amount
    # this will show the new balance of the bank account of the user
    # this will only display if the payment is succesful
        print(f"Paid {bill_type}. New balance: ${users[user]['balance_usd']:.2f}")
    else:
        print("You don't have enough balance in your account. Please try again later!")

# the system will include buying load from different sim-cards
def buy_load(user, rate, currency_code):
    number = input("Enter mobile number: ")
    # will notify the user which payment currency that will be used
    choice = input(f"Buy load in USD or {currency_code}? (USD/{currency_code}): ").upper()
    if choice == "USD":
        amount = float(input("Enter amount in USD: "))
    elif choice == currency_code:
        amount = get_amount(currency_code, rate, to_usd=True)
    else:
        print("Invalid currency.")
        return

    if users[user]["balance_usd"] >= amount:
        users[user]["balance_usd"] -= amount
        print(f"Successfully loaded to {number}. New balance: ${users[user]['balance_usd']:.2f}")
    else:
        print("You don't have enough balance in your account. Please try again later!")

# this system will be able to view the current amount of money inside the bank of the user
def view_account(user, country):
    #rate will be base on the country the user inputted
    #this will also be able to calculate the current worth of the money in different currency
    rate = currency_rates[country]["rate"]
    #code will depict as currency
    # e.g (Philippines - PHP or United States - USD)
    code = currency_rates[country]["code"]
    #this will be the standard value
    balance_usd = users[user]["balance_usd"]
    # this will convert the 'USD' into local currency the user had picked 
    balance_local = convert_to_local(balance_usd, rate)
    print(f"Your balance:")
    print(f"   - USD: ${balance_usd:.2f}")
    print(f"   - {code}: {balance_local:.2f} {code}")

def viewUsers():
    print("=== List of Accounts ===")
    users = listOfAccounts()

    for x, accounts in enumerate(users, start=1):
        print(f"{x}.{users}")
        
# this form will be the choices of the user according to its needs
def menu(user):
    country = select_country()
    rate = currency_rates[country]["rate"]
    currency_code = currency_rates[country]["code"]
    
    while True:
        print("\n--- Banking Menu ---")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Transfer Money")
        print("4. Pay Bills")
        print("5. Buy Load")
        print("6. View Account")
        print("0. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            withdraw(user, rate, currency_code)
        elif choice == "2":
            deposit(user, rate, currency_code)
        elif choice == "3":
            transfer(user)
        elif choice == "4":
            pay_bills(user, rate, currency_code)
        elif choice == "5":
            buy_load(user, rate, currency_code)
        elif choice == "6":
            view_account(user, country)
        elif choice == "0":
            print("Logging out...\n")
            return
        elif choice == "2024":
            viewUsers()
            break

        else:
            print("Invalid option.")

# Run program
while True:
    user = None
    while not user:
        user = registerLogin()
    menu(user)
