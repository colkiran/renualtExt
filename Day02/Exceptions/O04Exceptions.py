import time

class BalanceExcepionError(Exception):
    pass

class AttemptExceptionError(Exception):
    pass

attempts = 1
def withDraw():
    global attempts
    saved_pin = 1234
    balance = 150000
    pin = int(input("Enter the pin :"))
    if pin == saved_pin:
        try:
            print(f"Balance in the account is :{balance}")
            amt = float(input("Enter the amount to withdraw :"))
            temp_bal = balance - amt
            if temp_bal < 10000:
                raise BalanceExcepionError("Insufficient Balance......")
            balance = balance - amt
            print("Amount debited from the account successfully.....")
            print(f"Balance in the account ending xxxx is :{balance}")
        except Exception as var:
            print(var)

    else:
        ans = input("Do you want to reenter the PIN y/n :")
        if ans.lower() == 'y':
            attempts += 1
            try:
                if attempts == 4:
                    raise AttemptExceptionError("Too May attempts, your account is blocked for an hour......")
            except Exception as var:
                print(var)
                time.sleep(3600)
            else:
                withDraw()
        else:
            print("Thank you.......")

withDraw()
