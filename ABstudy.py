#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on June 15, 2022, at 10:55
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'ABstudy'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\User\\OneDrive\\Documents\\GitHub\\ABExperiment\\ABstudy.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "Practice_Instructions"
Practice_InstructionsClock = core.Clock()
Practice_Ins = visual.TextStim(win=win, name='Practice_Ins',
    text='Practice trials instructions here',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
End_Prac_Ins = keyboard.Keyboard()

# Initialize components for Routine "Practice_AB_Test"
Practice_AB_TestClock = core.Clock()
# Set experiment start values for variable component Prac_curImage
Prac_curImage = ''
Prac_curImageContainer = []
trialClock = core.Clock()
from os.path import exists 
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Fixation_Cross_2 = visual.TextStim(win=win, name='Fixation_Cross_2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Rapid_Image_Present_2 = visual.ImageStim(
    win=win,
    name='Rapid_Image_Present_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Initialize components for Routine "Practice_T1"
Practice_T1Clock = core.Clock()
key_resp = keyboard.Keyboard()
T1Response_2 = visual.TextStim(win=win, name='T1Response_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Practice_T2"
Practice_T2Clock = core.Clock()
T2Response_2 = visual.TextStim(win=win, name='T2Response_2',
    text='Did you see the blender?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Instructions here',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
End_Instructions = keyboard.Keyboard()

# Initialize components for Routine "textFix"
textFixClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "AB_Test"
AB_TestClock = core.Clock()
# Set experiment start values for variable component curImage
curImage = ''
curImageContainer = []
trialClock = core.Clock()

Rapid_Image_Present = visual.ImageStim(
    win=win,
    name='Rapid_Image_Present', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "T1_Response"
T1_ResponseClock = core.Clock()
T1Response = visual.TextStim(win=win, name='T1Response',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "T2_Response"
T2_ResponseClock = core.Clock()
T2Response = visual.TextStim(win=win, name='T2Response',
    text='Did you see the blender?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Practice_Instructions"-------
continueRoutine = True
# update component parameters for each repeat
End_Prac_Ins.keys = []
End_Prac_Ins.rt = []
_End_Prac_Ins_allKeys = []
# keep track of which components have finished
Practice_InstructionsComponents = [Practice_Ins, End_Prac_Ins]
for thisComponent in Practice_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Practice_InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Practice_Instructions"-------
while continueRoutine:
    # get current time
    t = Practice_InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Practice_InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Practice_Ins* updates
    if Practice_Ins.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Practice_Ins.frameNStart = frameN  # exact frame index
        Practice_Ins.tStart = t  # local t and not account for scr refresh
        Practice_Ins.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Practice_Ins, 'tStartRefresh')  # time at next scr refresh
        Practice_Ins.setAutoDraw(True)
    if Practice_Ins.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Practice_Ins.tStartRefresh + 10000-frameTolerance:
            # keep track of stop time/frame for later
            Practice_Ins.tStop = t  # not accounting for scr refresh
            Practice_Ins.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Practice_Ins, 'tStopRefresh')  # time at next scr refresh
            Practice_Ins.setAutoDraw(False)
    
    # *End_Prac_Ins* updates
    waitOnFlip = False
    if End_Prac_Ins.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        End_Prac_Ins.frameNStart = frameN  # exact frame index
        End_Prac_Ins.tStart = t  # local t and not account for scr refresh
        End_Prac_Ins.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(End_Prac_Ins, 'tStartRefresh')  # time at next scr refresh
        End_Prac_Ins.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(End_Prac_Ins.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(End_Prac_Ins.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if End_Prac_Ins.status == STARTED and not waitOnFlip:
        theseKeys = End_Prac_Ins.getKeys(keyList=['space'], waitRelease=False)
        _End_Prac_Ins_allKeys.extend(theseKeys)
        if len(_End_Prac_Ins_allKeys):
            End_Prac_Ins.keys = _End_Prac_Ins_allKeys[-1].name  # just the last key pressed
            End_Prac_Ins.rt = _End_Prac_Ins_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Practice_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Practice_Instructions"-------
for thisComponent in Practice_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Practice_Ins.started', Practice_Ins.tStartRefresh)
thisExp.addData('Practice_Ins.stopped', Practice_Ins.tStopRefresh)
# check responses
if End_Prac_Ins.keys in ['', [], None]:  # No response was made
    End_Prac_Ins.keys = None
thisExp.addData('End_Prac_Ins.keys',End_Prac_Ins.keys)
if End_Prac_Ins.keys != None:  # we had a response
    thisExp.addData('End_Prac_Ins.rt', End_Prac_Ins.rt)
thisExp.addData('End_Prac_Ins.started', End_Prac_Ins.tStartRefresh)
thisExp.addData('End_Prac_Ins.stopped', End_Prac_Ins.tStopRefresh)
thisExp.nextEntry()
# the Routine "Practice_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Practice_Trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('C:/Users/User/OneDrive/Documents/GitHub/Test/Practice_Condition_2.xlsx'),
    seed=None, name='Practice_Trials')
thisExp.addLoop(Practice_Trials)  # add the loop to the experiment
thisPractice_Trial = Practice_Trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_Trial.rgb)
if thisPractice_Trial != None:
    for paramName in thisPractice_Trial:
        exec('{} = thisPractice_Trial[paramName]'.format(paramName))

for thisPractice_Trial in Practice_Trials:
    currentLoop = Practice_Trials
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_Trial.rgb)
    if thisPractice_Trial != None:
        for paramName in thisPractice_Trial:
            exec('{} = thisPractice_Trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Practice_AB_Test"-------
    continueRoutine = True
    # update component parameters for each repeat
    t = 0
    trialClock.reset()
    imageCount = 0
    #imgOnScreen = False
    text_2.setText(cueWord)
    # keep track of which components have finished
    Practice_AB_TestComponents = [text_2, Fixation_Cross_2, Rapid_Image_Present_2]
    for thisComponent in Practice_AB_TestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Practice_AB_TestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Practice_AB_Test"-------
    while continueRoutine:
        # get current time
        t = Practice_AB_TestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Practice_AB_TestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        t = trialClock.getTime()
        
        curImage = "resources\\JPG\\" + Img1
        imageCount = 1
        
        if t>StimLength + 1.5:
            curImage = "resources\\JPG\\" + Img2
            imageCount = 2
        
        if t>StimLength*2 + 1.5:
            curImage = "resources\\JPG\\" + Img3
            imageCount = 3
        
        if t>StimLength*3 + 1.5:
            curImage = "resources\\JPG\\" + Img4
            imageCount = 4
        
        if t>StimLength*4 + 1.5:
            if Img5 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img5
                imageCount = 5
        
        if t>StimLength*5 + 1.5:
            if Img6 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img6
                imageCount = 6
        
        if t>StimLength*6 + 1.5:
            if Img7 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img7
                imageCount = 7
        
        if t>StimLength*7 + 1.5:
            if Img8 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img8
                imageCount = 8
        
        if t>StimLength*8 + 1.5:
            if Img9 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img9
                imageCount = 9
        
        if t>StimLength*9 + 1.5:
            if Img10 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img10
                imageCount = 10
        
        if t>StimLength*10 + 1.5:
            if Img11 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img11
                imageCount = 11
        
        if t>StimLength*11 + 1.5:
            if Img12 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img12
                imageCount = 12
        
        if t>StimLength*12 + 1.5:
            if Img13 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img13
                imageCount = 13
        
        if t>StimLength*13 + 1.5:
            if Img14 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img14
                imageCount = 14
        
        if t>StimLength*14 + 1.5:
            if Img15 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img15
                imageCount = 15
        
        if t>StimLength*15 + 1.5:
            if Img16 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img16
                imageCount = 16
        
        if t>StimLength*16 + 1.5:
            if Img17 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img17
                imageCount = 17
        
        curImage = curImage + ".jpg"
        
        #if !exists(curImage):
        #    Practice_Trials.addData('ErrorImage', curImage)
         #   curImage = "resources\\JPG\\" + "blender.jpg"
            
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *Fixation_Cross_2* updates
        if Fixation_Cross_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation_Cross_2.frameNStart = frameN  # exact frame index
            Fixation_Cross_2.tStart = t  # local t and not account for scr refresh
            Fixation_Cross_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation_Cross_2, 'tStartRefresh')  # time at next scr refresh
            Fixation_Cross_2.setAutoDraw(True)
        if Fixation_Cross_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation_Cross_2.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                Fixation_Cross_2.tStop = t  # not accounting for scr refresh
                Fixation_Cross_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation_Cross_2, 'tStopRefresh')  # time at next scr refresh
                Fixation_Cross_2.setAutoDraw(False)
        
        # *Rapid_Image_Present_2* updates
        if Rapid_Image_Present_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            Rapid_Image_Present_2.frameNStart = frameN  # exact frame index
            Rapid_Image_Present_2.tStart = t  # local t and not account for scr refresh
            Rapid_Image_Present_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Rapid_Image_Present_2, 'tStartRefresh')  # time at next scr refresh
            Rapid_Image_Present_2.setAutoDraw(True)
        if Rapid_Image_Present_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Rapid_Image_Present_2.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                Rapid_Image_Present_2.tStop = t  # not accounting for scr refresh
                Rapid_Image_Present_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Rapid_Image_Present_2, 'tStopRefresh')  # time at next scr refresh
                Rapid_Image_Present_2.setAutoDraw(False)
        if Rapid_Image_Present_2.status == STARTED:  # only update if drawing
            try:
                Rapid_Image_Present_2.setImage(curImage, log=False)
            except:
                Rapid_Image_Present_2.setImage("C:\\Users\\User\\OneDrive\\Documents\\GitHub\\ABExperiment\\resources\\JPG\\blender.jpg", log=False)
                Practice_Trials.addData('errorImage', curImage)
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Practice_AB_TestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practice_AB_Test"-------
    for thisComponent in Practice_AB_TestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice_Trials.addData('text_2.started', text_2.tStartRefresh)
    Practice_Trials.addData('text_2.stopped', text_2.tStopRefresh)
    Practice_Trials.addData('Fixation_Cross_2.started', Fixation_Cross_2.tStartRefresh)
    Practice_Trials.addData('Fixation_Cross_2.stopped', Fixation_Cross_2.tStopRefresh)
    Practice_Trials.addData('Rapid_Image_Present_2.started', Rapid_Image_Present_2.tStartRefresh)
    Practice_Trials.addData('Rapid_Image_Present_2.stopped', Rapid_Image_Present_2.tStopRefresh)
    # the Routine "Practice_AB_Test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Practice_T1"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    T1Response_2.setText(T1cue)
    # keep track of which components have finished
    Practice_T1Components = [key_resp, T1Response_2]
    for thisComponent in Practice_T1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Practice_T1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Practice_T1"-------
    while continueRoutine:
        # get current time
        t = Practice_T1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Practice_T1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left','right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *T1Response_2* updates
        if T1Response_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1Response_2.frameNStart = frameN  # exact frame index
            T1Response_2.tStart = t  # local t and not account for scr refresh
            T1Response_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1Response_2, 'tStartRefresh')  # time at next scr refresh
            T1Response_2.setAutoDraw(True)
        if T1Response_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > T1Response_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                T1Response_2.tStop = t  # not accounting for scr refresh
                T1Response_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(T1Response_2, 'tStopRefresh')  # time at next scr refresh
                T1Response_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Practice_T1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practice_T1"-------
    for thisComponent in Practice_T1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    Practice_Trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        Practice_Trials.addData('key_resp.rt', key_resp.rt)
    Practice_Trials.addData('key_resp.started', key_resp.tStartRefresh)
    Practice_Trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    Practice_Trials.addData('T1Response_2.started', T1Response_2.tStartRefresh)
    Practice_Trials.addData('T1Response_2.stopped', T1Response_2.tStopRefresh)
    # the Routine "Practice_T1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Practice_T2"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    Practice_T2Components = [T2Response_2, key_resp_4]
    for thisComponent in Practice_T2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Practice_T2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Practice_T2"-------
    while continueRoutine:
        # get current time
        t = Practice_T2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Practice_T2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T2Response_2* updates
        if T2Response_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2Response_2.frameNStart = frameN  # exact frame index
            T2Response_2.tStart = t  # local t and not account for scr refresh
            T2Response_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2Response_2, 'tStartRefresh')  # time at next scr refresh
            T2Response_2.setAutoDraw(True)
        if T2Response_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > T2Response_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                T2Response_2.tStop = t  # not accounting for scr refresh
                T2Response_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(T2Response_2, 'tStopRefresh')  # time at next scr refresh
                T2Response_2.setAutoDraw(False)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['left','right'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Practice_T2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practice_T2"-------
    for thisComponent in Practice_T2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice_Trials.addData('T2Response_2.started', T2Response_2.tStartRefresh)
    Practice_Trials.addData('T2Response_2.stopped', T2Response_2.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    Practice_Trials.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        Practice_Trials.addData('key_resp_4.rt', key_resp_4.rt)
    Practice_Trials.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    Practice_Trials.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "Practice_T2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Practice_Trials'


# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
End_Instructions.keys = []
End_Instructions.rt = []
_End_Instructions_allKeys = []
# keep track of which components have finished
InstructionsComponents = [text, End_Instructions]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 10000-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # *End_Instructions* updates
    waitOnFlip = False
    if End_Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        End_Instructions.frameNStart = frameN  # exact frame index
        End_Instructions.tStart = t  # local t and not account for scr refresh
        End_Instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(End_Instructions, 'tStartRefresh')  # time at next scr refresh
        End_Instructions.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(End_Instructions.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(End_Instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if End_Instructions.status == STARTED and not waitOnFlip:
        theseKeys = End_Instructions.getKeys(keyList=['space'], waitRelease=False)
        _End_Instructions_allKeys.extend(theseKeys)
        if len(_End_Instructions_allKeys):
            End_Instructions.keys = _End_Instructions_allKeys[-1].name  # just the last key pressed
            End_Instructions.rt = _End_Instructions_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if End_Instructions.keys in ['', [], None]:  # No response was made
    End_Instructions.keys = None
thisExp.addData('End_Instructions.keys',End_Instructions.keys)
if End_Instructions.keys != None:  # we had a response
    thisExp.addData('End_Instructions.rt', End_Instructions.rt)
thisExp.addData('End_Instructions.started', End_Instructions.tStartRefresh)
thisExp.addData('End_Instructions.stopped', End_Instructions.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('C:/Users/User/OneDrive/Documents/GitHub/Test/Practice_Condition_3.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "textFix"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    text_3.setText(cueWord)
    # keep track of which components have finished
    textFixComponents = [text_3, text_4]
    for thisComponent in textFixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    textFixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "textFix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = textFixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=textFixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in textFixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "textFix"-------
    for thisComponent in textFixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_3.started', text_3.tStartRefresh)
    trials.addData('text_3.stopped', text_3.tStopRefresh)
    trials.addData('text_4.started', text_4.tStartRefresh)
    trials.addData('text_4.stopped', text_4.tStopRefresh)
    
    # ------Prepare to start Routine "AB_Test"-------
    continueRoutine = True
    # update component parameters for each repeat
    t = 0
    trialClock.reset()
    imageCount = 0
    frame = 0
    #imgOnScreen = False
    # keep track of which components have finished
    AB_TestComponents = [Rapid_Image_Present]
    for thisComponent in AB_TestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AB_TestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AB_Test"-------
    while continueRoutine:
        # get current time
        t = AB_TestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AB_TestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        t = trialClock.getTime()
        frame = t
        curImage = "resources\\JPG\\" + Img1
        imageCount = 1
        
        if t>StimLength:
            curImage = "resources\\JPG\\" + Img2
            imageCount = 2
        if t>StimLength*2:
            curImage = "resources\\JPG\\" + Img3
            imageCount = 3
        if frame>StimLength*3:
            curImage = "resources\\JPG\\" + Img4
            imageCount = 4
        if frame>StimLength*4:
            if Img5 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img5
                imageCount = 5
        if frame>StimLength*5:
            if Img6 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img6
                imageCount = 6
        if frame>StimLength*6:
            if Img7 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img7
                imageCount = 7
        if frame>StimLength*7:
            if Img8 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img8
                imageCount = 8
        if frame>StimLength*8:
            if Img9 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img9
                imageCount = 9
        if frame>StimLength*9:
            if Img10 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img10
                imageCount = 10
        
        if frame>StimLength*10:
            if Img11 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img11
                imageCount = 11
        
        if frame>StimLength*11:
            if Img12 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img12
                imageCount = 12
        
        if frame>StimLength*12:
            if Img13 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img13
                imageCount = 13
        
        if frame>StimLength*13:
            if Img14 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img14
                imageCount = 14
        
        if frame>StimLength*14:
            if Img15 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img15
                imageCount = 15
        
        if frame>StimLength*15:
            if Img16 == "blankImage":
                continueRoutine = False
            else:
                curImage = "resources\\JPG\\" + Img16
                imageCount = 16
        else:
            continueRoutine = False
           
        
        curImage = curImage + ".jpg"
        
            
        
        # *Rapid_Image_Present* updates
        if Rapid_Image_Present.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            Rapid_Image_Present.frameNStart = frameN  # exact frame index
            Rapid_Image_Present.tStart = t  # local t and not account for scr refresh
            Rapid_Image_Present.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Rapid_Image_Present, 'tStartRefresh')  # time at next scr refresh
            Rapid_Image_Present.setAutoDraw(True)
        if Rapid_Image_Present.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Rapid_Image_Present.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                Rapid_Image_Present.tStop = t  # not accounting for scr refresh
                Rapid_Image_Present.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Rapid_Image_Present, 'tStopRefresh')  # time at next scr refresh
                Rapid_Image_Present.setAutoDraw(False)
        if Rapid_Image_Present.status == STARTED:  # only update if drawing
            try:
                Rapid_Image_Present.setImage(curImage, log=False)
            except:
                Rapid_Image_Present.setImage("C:\\Users\\User\\OneDrive\\Documents\\GitHub\\ABExperiment\\resources\\JPG\\blender.jpg", log=False)
                trials.addData('errorImage', curImage)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AB_TestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AB_Test"-------
    for thisComponent in AB_TestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Rapid_Image_Present.started', Rapid_Image_Present.tStartRefresh)
    trials.addData('Rapid_Image_Present.stopped', Rapid_Image_Present.tStopRefresh)
    # the Routine "AB_Test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T1_Response"-------
    continueRoutine = True
    # update component parameters for each repeat
    T1Response.setText(T1cue)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    T1_ResponseComponents = [T1Response, key_resp_2]
    for thisComponent in T1_ResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T1_ResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T1_Response"-------
    while continueRoutine:
        # get current time
        t = T1_ResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T1_ResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T1Response* updates
        if T1Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1Response.frameNStart = frameN  # exact frame index
            T1Response.tStart = t  # local t and not account for scr refresh
            T1Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1Response, 'tStartRefresh')  # time at next scr refresh
            T1Response.setAutoDraw(True)
        if T1Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > T1Response.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                T1Response.tStop = t  # not accounting for scr refresh
                T1Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(T1Response, 'tStopRefresh')  # time at next scr refresh
                T1Response.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['left','right'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T1_ResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T1_Response"-------
    for thisComponent in T1_ResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T1Response.started', T1Response.tStartRefresh)
    trials.addData('T1Response.stopped', T1Response.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    trials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "T1_Response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T2_Response"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    T2_ResponseComponents = [T2Response, key_resp_3]
    for thisComponent in T2_ResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T2_ResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T2_Response"-------
    while continueRoutine:
        # get current time
        t = T2_ResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T2_ResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T2Response* updates
        if T2Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2Response.frameNStart = frameN  # exact frame index
            T2Response.tStart = t  # local t and not account for scr refresh
            T2Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2Response, 'tStartRefresh')  # time at next scr refresh
            T2Response.setAutoDraw(True)
        if T2Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > T2Response.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                T2Response.tStop = t  # not accounting for scr refresh
                T2Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(T2Response, 'tStopRefresh')  # time at next scr refresh
                T2Response.setAutoDraw(False)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['left','right'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T2_ResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T2_Response"-------
    for thisComponent in T2_ResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T2Response.started', T2Response.tStartRefresh)
    trials.addData('T2Response.stopped', T2Response.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials.addData('key_resp_3.rt', key_resp_3.rt)
    trials.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    trials.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # the Routine "T2_Response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
