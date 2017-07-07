fp=open("myfile.txt", "r")
full_length=0
lines=fp.readlines()
for line in lines:
    full_length=full_length + int((line.strip()))
print ("\nThe sum of all these numbers is " + str(full_length) + ".")