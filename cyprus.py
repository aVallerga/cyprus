#!/usr/bin/python

import imdb
import sys

ia = imdb.IMDb()

s_result = ia.search_movie(sys.argv[1])

for item in s_result:
		print item['long imdb canonical title'], item.movieID
