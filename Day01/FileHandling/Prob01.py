
FL = open("EMP.csv", "r")

gender = {}     # empty dictionary
dept = []       # empty list
desig = []
sal = 0
sal1 = 0

for line in FL.readlines():
    gen = line.split(",")[2]
    dp = line.split(",")[4]
    ds = line.split(",")[3]

    # looking for key in a dictionary
    if gen not in gender:
        gender[gen] = 1
    else:
        gender[gen] += 1

    if dp not in dept:
        dept.append(dp)

    if ds not in desig:
        desig.append(ds)

    sal += int(line.split(",")[5])

    if gen == 'f' and ds == 'HR':
        sal1 += int(line.split(",")[5])


print(f"Gender      :{gender}")
print("-" * 60)
print(f"Department  :{dept}")
print("-" * 60)
print(f"Designations :{desig}")
print("-" * 60)
print(f"Total Salary :{sal}")
print("-" * 60)
print(f"HR Female Salary :{sal1}")

FL.close()