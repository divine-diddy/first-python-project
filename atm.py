#Making an ATM machine
from datetime import datetime
import time

pin = 1234
balance = 100000
decoder_no = [234, 567, 890]
meter_no = [987, 654, 321]
account = [123456, 567890, 987654]

count = 0
limit = 3


while count < limit:
    password = int(input("insert pin "))
    count += 1
    if password != pin:
        print("Incorrect pin\nTry again")
        if count == 3:
            print("This card has been block!")
            break
    else:
        print("Welcome")  
        while True: 
            operation = int(input("1. Withdrawal\n2. Check Balance\n3. Make payment\n4. Quickteller\n5. Cancel\n Enter an operation "))
            def alt():
                ans = int(input("Will you like to perform another transaction?\n1. Yes\n2. No\n"))
                if ans == 1:
                    time.sleep(2)
                else:
                    print("Thank you for banking with us.\nTake your card.")
                    exit()
            if operation == 1:
                option = int(input("1. 1000\n2. 5000\n3. 10000\n4. 15000\n5. 20000\n6. Others\n"))
                if option == 1:
                    amount = 1000
                elif option == 2:
                    amount = 5000
                elif option == 3:
                    amount = 10000
                elif option == 4:
                    amount = 15000
                elif option == 5:
                    amount = 20000
                elif option == 6:
                    amount = int(input("Enter amount..."))
                if amount <= balance:
                    balance -= amount
                    print("Please wait while your transaction is being processed")
                    time.sleep(3)
                    print("Take your cash")
                    alt()
                else:
                    print("Insufficient fund")
                    alt()
            elif operation == 2:
                print("Please wait a moment while your transaction is being processed")
                time.sleep(3)
                print(f"Your balance is #{balance}")
                alt()
            elif operation == 3:
                print("Select biller")
                option2 = int(input("1. Dstv\n2. Gotv\n3. EEDC\n"))
                if option2 == 1:
                    decoder = int(input("Enter your decoder number\n"))
                    if decoder in decoder_no:
                        package = int(input("Select package\n1. Family\n2. Classic\n3. Classic plus\n4. Premium\n"))
                        if package == 1:
                            balance -= 4000
                        elif package ==2:
                            balance -= 5000
                        elif package == 3:
                            balance -= 6000
                        elif package == 4:
                            balance -= 7000
                        else:
                            print("Operation not available")
                            alt()
                        print("Please wait a moment while your transaction is being processed")
                        time.sleep(3)
                        if package > balance:
                            print("Insufficient fund")
                            alt()
                        else:
                            print("Thank you for paying via Diddy's ATM")
                            alt()
                    else:
                        time.sleep(3)
                        print("Sorry, decoder number not avaliable")
                        alt()
                elif option2 == 2:
                    decorder = int(input("Enter your decoder number\n"))
                    if decorder in decoder_no:
                        package = int(input("Select package\n1. Jolly\n2. Classic\n3. Plus\n4. Max\n"))
                        if package == 1:
                            balance -= 1000
                        elif package ==2:
                            balance -= 2000
                        elif package == 3:
                            balance -= 3000
                        elif package == 4:
                            balance -= 3500
                        else:
                            print("Operation not available")
                            alt()
                        print("Please wait a moment while your transaction is being processed")
                        time.sleep(3)
                        if package > balance:
                            print("Insufficient fund")
                        else:
                            print("Thank you for paying via Diddy's ATM")
                            alt()
                    else:
                        time.sleep(3)
                        print("Sorry, decoder number not avaliable")
                        alt()
                elif option2 == 3:
                    meter = int(input("Enter meter number\n"))
                    if meter in meter_no:
                        pay = int(input("Enter amount\n"))
                        balance -= pay
                        print("Please wait while your transaction is being processed")
                        time.sleep(3)
                        if pay > balance:
                            print("Insufficient fund")
                        else:
                            print("Thank you for paying via Diddy's ATM")
                            alt()
                    else:
                        time.sleep(3)
                        print("Sorry, meter number not avaliable")
                        alt()
                else:
                    alt()
            elif operation == 4:
                time.sleep(2)
                bank = int(input("Select bank\n1. First bank\n2. Access bank\n3. GT bank\n4. FCMB\n"))
                if bank in [1, 2, 3, 4]:
                    acc_type = int(input("1. Savings\n2. Current\n"))
                else:
                    time.sleep(1)
                    print("Operation not available")
                    alt()
                if acc_type == 1:
                    acc_no = int(input("Enter account number\n"))
                    if acc_no in account:
                        amt = int(input("Enter amount\n"))
                        if amt <= balance:
                            balance -= amt
                            print("Please wait a moment while your transaction is being processed")
                            time.sleep(3)
                            print("Transfer successful")
                            alt()
                        else:
                            time.sleep(3)
                            print("Insufficient fund")
                            alt()
                    else:
                        time.sleep(3)
                        print("Please confirm account number")
                        alt()
                else:
                    time.sleep(3)
                    acc_no = int(input("Enter account number\n"))
                    if acc_no in account:
                        amt = int(input("Enter amount\n"))
                        if amt <= balance:
                            balance -= amt
                            print("Please wait a moment while your transaction is being processed")
                            time.sleep(3)
                            print("Transfer successful")
                            alt()
                        else:
                            time.sleep(3)
                            print("Insufficient fund")
                            alt()
                    else:
                        time.sleep(3)
                        print("Please confirm account number")
                        alt()
            else:
                alt()
