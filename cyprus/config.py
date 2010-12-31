import ConfigParser
import os

configfile = '~/.cyprus/config'
configfile = os.path.expanduser(configfile)

config = ConfigParser.ConfigParser()

(path, filename) = os.path.split(configfile)
if not os.path.exists(path):
	os.makedirs(path)

if not os.path.exists(configfile):
	config.add_section('basic')
	config.set('basic', 'library', '~/CyprusLib')
	configsocket = open(configfile, 'wb')
	config.write(configsocket)

config.read(configfile)
librarydir = os.path.expanduser(config.get('basic', 'library'))
if not os.path.exists(librarydir):
	os.makedirs(librarydir)
