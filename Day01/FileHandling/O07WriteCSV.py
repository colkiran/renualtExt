
import csv
data = [
        [101, "JAN", "m", "MGR", 'HR', 1000],
        [102, 'FEB', 'f', 'PL', 'ADMIN', 1500],
        [103, 'MAR', 'f', 'PM', 'FINANCE', 2000],
        [104, 'APR', 'm', 'TL', 'PROCUREMENT', 2500],
        [105, 'MAY', 'm', 'ADMIN', 'IT', 3000]
    ]

with open("employee.csv", "w", newline="") as CSVW:
    writer = csv.writer(CSVW)

    writer.writerow(['empid', 'empname', 'gender', 'desig', 'dept', 'salary'])

    for row in data:
        writer.writerow(row)

