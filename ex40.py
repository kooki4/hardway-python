class song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = song(["Happy birthday to you",
				   "I Don't want to get sued",
				   "So I'll stop right there"])

bulls_on_parade = song(["They rally around the family",
						"With pockets full of shells"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# a much better example of classes and objects
# source: http://www.tutorialspoint.com/python/python_classes_objects.htm
