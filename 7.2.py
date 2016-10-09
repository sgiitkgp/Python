fname =raw_input('Enter the file name:')
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:',fname
    exit()

for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):continue
    print line
print 'Done'

# # Use the file name mbox-short.txt as the file name
# fname = raw_input("Enter file name: ")
# fh = open(fname)
# cvalue = 0
# count = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"): continue
#     linevalue = float(line[len(line) - 6:len(line)])
#     cvalue = cvalue + linevalue
#     count = count + 1
#
# average = cvalue / count
# print "Average spam confidence:", average
