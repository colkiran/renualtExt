
FL = open("employee.csv", "r")

# st = FL.read()
# print(st)

for line in FL.readlines():
    print(line)

FL.close()