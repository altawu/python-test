#import modules
from sys import argv

#unpack args
script, filename = argv

#open a file
txt = open(filename)

#print the name of the opend file
print "Here's your file %r:" % filename
#print the content of file
print txt.read()




txt.close()


