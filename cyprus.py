#!/usr/bin/python

import sys

try:
	import imdb
except ImportError:
	print "Please install the IMDbPY package. python-imdbpy in Ubuntu."
	sys.exit(1)

# check for one argument
if len(sys.argv) != 2:
	print "Only one argument is required:"
	print "   %s 'movie title'" % sys.argv[0]
	sys.exit(2)

ia = imdb.IMDb()

searchterm = sys.argv[1]

try:
	# try searching for list of results
	s_result = ia.search_movie(searchterm)
except imdb.IMDbError, e:
	print "You probably have no internet connection. Complete error report: "
	print e
	sys.exit(3)

if not s_result:
	print "No matches for %s, sorry." % searchterm 
	sys.exit(0)

first_result = s_result[0]
ia.update(first_result)

print "\nBest match: "
print first_result.summary()
