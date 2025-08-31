
try:
    num = int(input("Enter the number :"))
    div = int(input("Enter the Divisor :"))

    res = num / div
    print(f"res :{res}")

except ZeroDivisionError as z:
    print("Exception caught.....")
    print(z)

except ValueError as v:
    print("Exception caught.....")
    print(v)

except Exception as e:
# exception is the base class of all exceptions
    print("Exception caught(exception class),.....")
    print(e)

finally:
    print("Division of number completed sucessfully....")

