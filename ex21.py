def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print"MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DEVIDE %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(780, 4)
weight = multiply(9, 2)
iq = divide(100, 2)

print ("Age: %d, Height: %d, Weight: %d, IQ: %d") % (age, height, weight, iq)

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

def mixing(b, c):
	print "We have %d part of %d grams of sugar." % (b, c)
	return float(b) / c

chemExperiment = mixing(100, 34)
print "Result of chemical is: %.5f " % chemExperiment