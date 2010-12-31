import sys
import movie
import config
import os
"""
Main class which handles user input sanitization
"""
class Main:
	def __init__(self):
		self.argv = sys.argv
		self.config = config.Config()
		self.config.check_config()
	
	def read_input(self):
		if len(self.argv) != 2:
			print 'Only one argument is required:'
			print '     %s "movie filename"' % self.argv[0]
			sys.exit(2)
		elif not os.path.exists(sys.argv[1]):
			print 'File %s does not exist' % self.argv[1]
		else:
			mov = movie.Movie(sys.argv[1])
			print "Looking up movie %s" % sys.argv[1]
			mov.lookup()
			mov.print_metadata()
			#mov.summarize()
