tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "0\' 1\" 2\a 3\b 4\e 5\000 6\n 7\v 8\t 9\f 10\r 11"
while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" %i,
        print "%s\r" %i,
        print "%s\r" %i,
        print "%s\r" %i,
        print "%s\r" %i,
        print "%s\r" %i,
        print "%s\r" %i,
        print "%s\r" %i,
        print "%s\r" %i,

