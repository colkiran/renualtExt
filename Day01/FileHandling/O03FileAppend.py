
FA = open("myfile.txt", "a")

st = input("Enter the file contents :")

FA.write(st + '\n')

FA.close()