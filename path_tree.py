import os
import json
import sys

globalJSON = {}

def recursePath(curPath, parentPath):

	children = os.listdir(curPath)

	global globalJSON
	globalJSON[curPath] = {"parent" : parentPath, "children": children}

	for i in range(0, len(children)):
		if os.path.isdir(curPath + "/" + children[i]):
			recursePath(curPath + "/" + children[i], curPath)

def writePathToFile(path):
	recursePath(path, None)
	global globalJSON
	s = json.dumps(globalJSON, indent=4)
	# print s

	f1=open('./info.json', 'w+')
	f1.write(s)

def parseArgs():
	if len(sys.argv) is not 2:
		print "FAILED: takes only 1 path"
		return

	print "following " + sys.argv[1]
	writePathToFile(sys.argv[1])

parseArgs()
