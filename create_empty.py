# create empty drum map starting with a non-empty one

import xml.etree.ElementTree as et, sys

def main(fileName):
	tree = et.parse(fileName)
	root = tree.getroot()

	root[0].set('value', 'Empty')		# drum map name

	note = 0
	for elmt in root[2]:				# Map
		noteStr = str(note)
		elmt[0].set('value', noteStr)	# INote
		elmt[1].set('value', noteStr)	# ONote
		elmt[2].set('value', '-1')		# Channel == Any
		elmt[3].set('value', str(200))	# Length, as seen in GM.drm
		elmt[4].set('value', '0')		# Mute off
		elmt[5].set('value', noteStr)	# DisplayNote
		elmt[9].set('value', '---')		# Name
		elmt[10].set('value', '0')		# QuantizeIndex
		note += 1
	
	order = 0
	for elmt in root[3]:				# Order
		elmt.set('value', str(order))
		order += 1

	tree.write('empty.drm')

# when invoked from the command line
if __name__ == '__main__':
	main(sys.argv[1])
