import os
import config
try:
	import imdb
except:
	print 'You must install the IMDbPY package.'
	sys.exit(1)

"""
Movie object, holds file information and metadata, is responsible for
low level moving and writing metadata
"""
class Movie:
	def __init__(self, fullpath):
		self.fullpath = fullpath
		(self.path, self.filename) = os.path.split(fullpath)
		self.splitname = self.filename.split('.')
		self.imdb = imdb.IMDb()
		self.result = None
		self.title = None
	
	def lookup(self):
		try:
			search_results = self.imdb.search_movie(self.splitname[0])
		except imdb.IMDbError, e:
			print "Probably no connection to the internet. Full error follows:"
			print e
			sys.exit(3)
			
		self.result = search_results[0]
		self.imdb.update(self.result)
		self.title = self.result['long imdb canonical title']
	
	def print_metadata(self):
		print "Title: ", self.title
		print config.librarydir

	def summarize(self):
		print self.result.summary()
