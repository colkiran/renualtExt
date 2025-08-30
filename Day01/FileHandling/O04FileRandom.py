"""
seek - used to move the file handle from one location to another and seek returns the position of the file handle

tell - will return the position of the file handle
"""

FL = open("data.txt", "rb")

pos = FL.tell()
print(f"pos :{pos}")

pos = FL.seek(150, 0)
print(f"pos :{pos}")

pos = FL.seek(-65, 1)
print(f"pos :{pos}")

pos = FL.seek(50, 2)
print(f"pos :{pos}")

# FL.seek(-10, 0)

FL.close()