#!/usr/bin/python

import imdb
import sys

ia = imdb.IMDb()

s_result = ia.search_movie(sys.argv[1])

print "Search results: "
i = 1
for item in s_result:
		print i,
		print item['long imdb canonical title'], item.movieID
		i = i + 1
		
first_result = s_result[0]
ia.update(first_result)

print "\nBest match: "
print first_result.summary()
