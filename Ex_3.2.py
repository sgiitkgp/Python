numb = raw_input("Please Enter a number between 0 & 10")
try:
    numb = int(numb)
except ValueError:
    print 'Entry should be an integer between 0 & 10 !!'
    quit()
if numb > 10:
    print 'Number not in range!!'
    quit()
if numb >= 8:
    print 'Cool'
elif numb >= 6:
    print 'Good'
elif numb >= 4:
    print 'Meh'
elif numb >= 2:
    print 'Never Mind'
elif numb == 0:
    print 'Ouch'
quit()