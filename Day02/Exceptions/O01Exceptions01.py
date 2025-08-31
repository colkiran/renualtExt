
import sys

num = int(input("Enter the number :"))
div = int(input("Enter the Divisor :"))

try:
    res = num / div
    print(f"res :{res}")
except:
    print("Exception caught.....")
    print(sys.exc_info()[0])            # class
    print(sys.exc_info()[1])            # message
