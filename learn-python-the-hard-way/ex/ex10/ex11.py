#input and output 
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy" % (age, height, weight)
'''
#input string
nID = ''
while True:
    nID = raw_input("Input your id plz")
    if len(nID) != len("32062319880101****"):
        print "wrong length of id, input again"
    else:
        break

print "you id is %s" % (nID)



#input integer
nAge = int(raw_input("input your age plz:"))
if nAge > 0 and nAge < 120:
    print "thanks!"
else:
    print "bad age"

print "your age is %d" % nAge
'''

#my quesetion
testId = int(raw_input("input the test id:"))
print "the testId is %r" % testId

