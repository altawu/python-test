# -- coding: utf-8 --
name = '吴陈旭'
age = 25
height = 170 #cm
weight = 60 #kg
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." %  name
print "He's %d cm tall." %  height
print "He's %d kilograms heavy." %  weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % ( eyes,  hair)
print "His teeth are usually %s depending on the coffee." % ( teeth)

#this line is tricky, try to get it exactly right
print "If I add %d, %d ,and %d I get %d." % (
                age,  height,  weight,  age +  height +  weight)
