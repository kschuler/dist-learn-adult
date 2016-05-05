#!/usr/bin/env python
"""
DISTRIBUTIONAL-LEARN-ADULT Paradigm
Updated Version: May 5, 2016, Kathryn Schuler
------------------------
"""
from psychopy import visual, core, event, data#, info,
#import datetime, os, sys, itertools

class DistLearnExperiment(object):
    def __init__(self):
        self.expInfo = {
    			'exp-id': 0000,											# experiment ID number (fixed value)
    			'subject': raw_input("enter subject no: "), 			# subject ID (requests user input)
    			'condition': raw_input("enter condition (A or B): ")   	# condition (requests user input)
		}
        self.expWindow = visual.Window(
			units = 'pix',
		 	winType = 'pyglet',
			screen = 0,
			color = 'black',
		 	size = [1440, 900],
			fullscr = True,
			allowGUI = False
		)
        self.expMouse = event.Mouse(
		 	win = self.expWindow,
		 	visible = False
		)
        self.instructions = visual.TextStim(
			win = self.expWindow,
			pos = [0, 300],
			color = 'white',
			height = 20,
			font = 'Helvetica',
			wrapWidth = 800
		)
        self.progBarOutline = visual.Rect(
			win = self.expWindow,
			pos = [0, 350],
			width = 680,
			height = 23,
			lineColor =  'white'
		)
        self.progBar = visual.Rect(
			win = self.expWindow,
			pos = [0, 350],
			width = 680,
			height = 20,
			fillColor = 'gray',
			opacity = 0.8
		)
        self.ratingScale = visual.RatingScale(
			win = self.expWindow,
			pos = [0, -300],
			low = 1,
			high = 5,
			precision = 1,
			textColor = 'white',
			marker = 'triangle',
			size = 0.60,
			stretch = 1.0,
			lineColor = 'white',
			markerColor = 'blue',
			scale = None
		)
    def runExperiment(self):
        self.displayInstructions('Do this first')
        self.displayInstructions('Then do this.')


    def displayInstructions(self, theseInstructs):
        self.instructions.setText(theseInstructs)
        self.instructions.draw()
        self.expWindow.flip()
        event.waitKeys('space')

    def exposurePhase(self, thisFile, numReps = 1):
        self.conditionsFile = data.importConditions('conditions/'+thisFile)
		self.trials = data.TrialHandler(self.conditionsFile, method = 'sequential', nReps = numReps, extraInfo = self.expInfo)
		for trial in self.trials :
            thisSequence = [trial.A, trial.B, trial.C]
            filter('None', thisSequence)

        # play the sounds, with required silence

    def testPhase(self, conditionFile):
        # make the sentence
        # play the sounds
        # wait for rating



exp = DistLearnExperiment()
exp.runExperiment()
