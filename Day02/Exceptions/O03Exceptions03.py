
"""
traceback
type error
message

interpreter will call sys.excepthook with three arguments
a. the exception class - typeerror
b. the exception value - unsupported operands....
c. traceback object = traceback
"""

import sys

def format_traceback(exc_type, exc_val, exc_traceback):
    print("Some thing went wrong.....")
    print(exc_type)
    print(exc_val)
    print(list(exc_traceback))
    # print(list(sys.excepthook))

sys.excepthook = format_traceback


def fun():
    print(1 + "abc")


fun()



