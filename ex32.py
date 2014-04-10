the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first of for-loop goes throught a list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "This is count %d" % number

#also we can go trough mixed lists too
#notice we have to use %r since we don't know hwat's in it
for i in change:
	print "I got %r" %i

#we can also build lists, first start with an empty one
elements = []
print "elements = %r" % elements
# then use the range function to do 9 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
elements = range(0,6)
print "elements = %r" % elements

#now we can print them out too
for i in elements:
	print "Element was: %r" % i