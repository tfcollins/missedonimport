
"""
This plugin creates a separate log of files that are ignored when on import and a separate log is created
for them
"""


from beets.plugins import BeetsPlugin
import os
import socket
from beets import config
from beets.ui import Subcommand

missedLogFile = '/home/travis/Apps/BeetsPlugin/beetsplug/missed.txt'

importMissedAlbums = Subcommand('importmissed', help='Import the album listed in the "missed" file')
def reImportMissed(lib, opts, args):
	print "Reimported files/albums we missed the first time"
	with open(missedLogFile) as f:
		albums = f.readlines()	
	

importMissedAlbums.func = reImportMissedAlbums


class MissedOnImport(BeetsPlugin):
	def __init__(self):
		print 'Init of new plugin!!'



@MissedOnImport.listen('import_task_choice')
def importmissed(session,task):
	albumpath = task.paths
	print task.choice_flag.name
	if task.choice_flag.name!='APPLY':
		with open(missedLogFile, "a") as myfile:
			myfile.write(albumpath[0]+'\n')
	print task['path']
	pass



