#!/usr/bin/env python
"""
DISTRIBUTIONAL-LEARN-ADULT Paradigm
Updated Version: May 5, 2016, Kathryn Schuler
------------------------
"""
from psychopy import prefs
prefs.general['audioLib'] = ['pygame']
from psychopy import visual, core, event, data, sound#, info,
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
        self.exposurePhase('Z-exposure.xlsx')
        self.testPhase('Z-exposure.xlsx')

    def displayInstructions(self, theseInstructs):
        self.instructions.setText(theseInstructs)
        self.instructions.draw()
        self.expWindow.flip()
        event.waitKeys('space')

    def exposurePhase(self, thisFile, numReps = 1):
        self.expWindow.flip()
        self.conditionsFile = data.importConditions('conditions/'+thisFile)
        self.trials = data.TrialHandler(self.conditionsFile, method = 'sequential', nReps = numReps, extraInfo = self.expInfo)
        for trial in self.trials :
            thisSequence = filter(None, [trial.A, trial.B, trial.C])
            for item in thisSequence:
                self.playSound(whichSound='sounds/'+str(item)+'.wav', ISI = 0.50)
        self.trials.saveAsWideText('edatafile.csv', delim=",")

    def testPhase(self, thisFile, numReps = 1):
        self.expWindow.flip()
        self.conditionsFile = data.importConditions('conditions/'+thisFile)
        self.trials = data.TrialHandler(self.conditionsFile, method = 'sequential', nReps = numReps, extraInfo = self.expInfo)
        for trial in self.trials :
            thisSequence = filter(None, [trial.A, trial.B, trial.C])
            for item in thisSequence:
                self.playSound(whichSound='sounds/'+str(item)+'.wav', ISI = 0.50)
            self.collectRating()
            if event.getKeys(['escape']): core.quit()
        self.trials.saveAsWideText('edatafile.csv', delim=",")

    def playSound(self, whichSound, waitDur = True, ISI = 0.0, whatVolume = 1.0):
        thisSound = sound.Sound(whichSound)
        thisSound.setVolume(whatVolume)
        thisSound.play()
        dur = thisSound.getDuration()
        if waitDur :
            core.wait(dur)
        core.wait(ISI)

    def collectRating(self):
        self.ratingScale.reset()
        while self.ratingScale.noResponse:
            self.ratingScale.draw()
            self.expWindow.flip()
            if event.getKeys(['escape']): core.quit()
        rating = self.ratingScale.getRating()
        self.expWindow.flip()

exp = DistLearnExperiment()
exp.runExperiment()
