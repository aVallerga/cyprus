import os
import config
import shutil
import urllib
try:
	import imdb
except:
	print 'You must install the IMDbPY package.'
	sys.exit(1)

"""
Movie class, holds file information and metadata, is responsible for
low level moving and writing metadata
"""
class Movie:
	def __init__(self, fullpath):
		self.fullpath = fullpath
		(self.path, self.filename) = os.path.split(fullpath)
		self.splitname = self.filename.split('.')
		self.config = config.Config()
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

	def move_to_library(self):
		path = self.config.get_librarydir() + '/' + self.title
		if not os.path.exists(path):
			os.makedirs(path)
		filename = path + '/' + self.title + '.' + self.splitname[-1]
		shutil.copy(self.fullpath, filename) 
		coverurl = self.result['full-size cover url']
		urllib.urlretrieve(coverurl, path + '/' + self.title + '.tbn')
	
	def print_metadata(self):
		print "Title: ", self.title
		print "Filetype: ", self.splitname[-1]
		print self.config.get_librarydir()

	def summarize(self):
		print self.result.summary()
