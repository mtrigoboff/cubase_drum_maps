# Code written by Michael Trigoboff, http://spot.pcc.edu/~mtrigobo

import xml.etree.ElementTree as et, os.path, sys

def buildNoteNumbers():
	noteNames = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
	noteNameIndex = 0
	octaveIndex = 0
	noteNumbers = {}
	for noteNumber in range(24, 97):
		noteNumbers[noteNames[noteNameIndex] + str(octaveIndex)] = noteNumber
		noteNameIndex += 1
		if (noteNameIndex > 11):
			noteNameIndex = 0
			octaveIndex += 1
	return noteNumbers

def createDrumMap(fileName):
	noteNumbers = buildNoteNumbers()
	tree = et.parse('empty.drm')
	root = tree.getroot()

	dk = open(fileName, "r")
	lines = [line.rstrip() for line in dk.readlines()]
	dk.close()

	root[0].set('value', lines[0])		# drum map name

	# set Name [9] in Map [2]
	map = root[2]
	for line in lines[1:]:
		lineSplit = line.split()
		noteNumber = noteNumbers[lineSplit[0]]
		noteName = ' '.join(lineSplit[2:])
		map[noteNumber][9].set('value', noteName)

	# configure Order [3] so that items with names come first
	order = root[3]
	firstNoteNumber = noteNumbers[lines[1].split()[0]]
	lastNoteNumber =  noteNumbers[lines[-1].split()[0]]
	item = 0
	for noteNumber in range(firstNoteNumber, lastNoteNumber + 1):
		order[item].set('value', str(noteNumber))
		item += 1
	for noteNumber in range(0, firstNoteNumber):
		order[item].set('value', str(noteNumber))
		item += 1
	for noteNumber in range(lastNoteNumber + 1, 128):
		order[item].set('value', str(noteNumber))
		item += 1

	tree.write(os.path.splitext(fileName)[0] + '.drm')
