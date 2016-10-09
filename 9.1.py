fname = raw_input("Enter file: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
sender = dict()
for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words)== 0 : continue
    if words[0] == 'From':
        if words[1] not in sender:
            sender[words[1]] = 1
        else:
            sender[words[1]] += 1
maxname = None
sendmax = None
for name,values in sender.items():
    if sendmax is None or values > sendmax:
        sendmax = values
        maxname = name
print maxname,sendmax