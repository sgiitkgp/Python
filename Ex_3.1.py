age = raw_input("Please Enter Your Age")
try:
    age = int(age)
except:
    print 'Invalid Entry'
    quit()
print 'Your age is ' + str(age)

