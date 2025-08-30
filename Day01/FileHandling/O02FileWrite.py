
FW = open("myfile.txt", "w")

# st = input("Enter the file contents :")
#
# # will write one line
# FW.write(st)

line1 = "This is the first line.\n"
line2 = "This is the second line.\n"
line3 = "This is the third line.\n"

FW.writelines([line1, line2, line3])

FW.close()