import sys
import movie

"""
Main class which handles user input sanitization
"""
class Main:
	def __init__(self):
		self.argv = sys.argv
	
	def read_input(self):
		if len(self.argv) != 2:
			print 'Only one argument is required:'
			print '     %s "movie title"' % self.argv[0]
			sys.exit(2)
		else:
			mov = movie.Movie(sys.argv[1])
			print "Looking up movie %s" % sys.argv[1]
			mov.lookup()
			mov.print_metadata()
			#mov.summarize()
