# Assignment Chapter 11
import re

fname = raw_input("Enter file: ")
fh = open(fname)

numlist = list()

for line in fh:
    line = line.rstrip()
    y = re.findall('[0-9]+', line)

    for i in y:
        numlist.append(int(i))

print "The sum of all the numbers in the file :", sum(numlist)
