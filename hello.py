fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    sen = line.split()
    for word in sen:
        if word not in lst:
           lst.append(word)
lst.sort()
print lst