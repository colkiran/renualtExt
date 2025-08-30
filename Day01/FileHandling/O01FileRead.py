
import re
# "C:\\Training\\PycharmProjects\\renualtExt\\Day01\\FileHandling\\data.txt"
"""
read    -   will read the entire content of the file
readline - will read one line
readlines - will read all the lines and store it like a list
"""

FL = open("data.txt", "r")

# st = FL.read(100)

# st = FL.readline(500)  # read one line
# print(st)
#
# st = FL.readlines(865)
# print(st)

for line in FL.readlines():
    res = re.search(r"(\A\w{2})", line)
    if res:
        print(res.group(0))


FL.close()