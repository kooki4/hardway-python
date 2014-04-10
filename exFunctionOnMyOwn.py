def talking_time(alexTimeSpeaking, stefanTimeSpeaking):
	print "Now I am going to show you how much time each of theme is loosing in pointless \nspeaking:\nPress Enter to continue or CRTL+C"
	raw_input()
	print "Alex is speaking %d minutes" % alexTimeSpeaking
	print "Stefan is speaking %d minutes" % stefanTimeSpeaking
	print "Combined they took %d minutes of our working time" % ( alexTimeSpeaking + stefanTimeSpeaking)
talking_time( input("Alex time:"), input("Stefan time: ") )
