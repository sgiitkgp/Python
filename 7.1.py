fname =raw_input('Enter the file name:')
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:',fname
    exit()

data = fhand.read()
data = data.rstrip()
print data.upper()