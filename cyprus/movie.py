import os
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
	
	def lookup(self):
		search_results = self.imdb.search_movie(self.splitname[0])
		self.result = search_results[0]
		self.imdb.update(self.result)
	
	def summarize(self):
		print self.result.summary()
