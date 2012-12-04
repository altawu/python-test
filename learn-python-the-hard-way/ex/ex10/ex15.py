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

#get the file name from raw_input
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()


