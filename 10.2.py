fname = raw_input("Enter file: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
mailtime = dict()
for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words)== 0 : continue
    if words[0] == 'From':
        if words[5].split(':')[0] not in mailtime:
            mailtime[words[5].split(':')[0]] = 1
        else:
            mailtime[words[5].split(':')[0]] += 1


temp = []
for k in sorted(mailtime):
    temp.append((k,mailtime[k]))
    print k, mailtime[k]