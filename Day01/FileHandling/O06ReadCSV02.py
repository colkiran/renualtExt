
import csv

gender = {}
dept = []
desig = []
sal = 0
sal1 = 0

with open("EMP.csv", "r") as CSVR:
    reader = csv.reader(CSVR)

    for row in reader:
        # print(row)
        dg = row[2]
        if dg not in gender:
            gender[dg] = 1
        else:
            gender[dg] += 1

        dp = row[3]
        if dp not in dept:
            dept.append(dp)

        ds = row[4]
        if ds not in desig:
            desig.append(ds)

        sal += int(row[5])

print(gender)
print("-" * 60)
print(dept)
print("-" * 60)
print(desig)
print("-" * 60)
print(sal)
