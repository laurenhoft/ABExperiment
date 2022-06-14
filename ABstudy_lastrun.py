#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on June 14, 2022, at 19:42
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
    originPath='C:\\Users\\User\\OneDrive\\Documents\\GitHub\\ABExperiment\\ABstudy_lastrun.py',
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

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Any text\n\nincluding line breaks',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "AB_Test"
AB_TestClock = core.Clock()
# Set experiment start values for variable component curImage
curImage = ''
curImageContainer = []
trialClock = core.Clock()
text_1 = visual.TextStim(win=win, name='text_1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Fixation_Cross = visual.TextStim(win=win, name='Fixation_Cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Rapid_Image_Present = visual.ImageStim(
    win=win,
    name='Rapid_Image_Present', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

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

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
InstructionsComponents = [text, key_resp]
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
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
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
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Condition_Spreadsheet.xlsx'),
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
    
    # ------Prepare to start Routine "AB_Test"-------
    continueRoutine = True
    # update component parameters for each repeat
    t = 0
    trialClock.reset()
    imageCount = 0
    #imgOnScreen = False
    text_1.setText(cueWord)
    # keep track of which components have finished
    AB_TestComponents = [text_1, Fixation_Cross, Rapid_Image_Present]
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
        
        # *text_1* updates
        if text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_1.frameNStart = frameN  # exact frame index
            text_1.tStart = t  # local t and not account for scr refresh
            text_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
            text_1.setAutoDraw(True)
        if text_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_1.tStop = t  # not accounting for scr refresh
                text_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_1, 'tStopRefresh')  # time at next scr refresh
                text_1.setAutoDraw(False)
        
        # *Fixation_Cross* updates
        if Fixation_Cross.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation_Cross.frameNStart = frameN  # exact frame index
            Fixation_Cross.tStart = t  # local t and not account for scr refresh
            Fixation_Cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation_Cross, 'tStartRefresh')  # time at next scr refresh
            Fixation_Cross.setAutoDraw(True)
        if Fixation_Cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation_Cross.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                Fixation_Cross.tStop = t  # not accounting for scr refresh
                Fixation_Cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation_Cross, 'tStopRefresh')  # time at next scr refresh
                Fixation_Cross.setAutoDraw(False)
        
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
            if tThisFlipGlobal > Rapid_Image_Present.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Rapid_Image_Present.tStop = t  # not accounting for scr refresh
                Rapid_Image_Present.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Rapid_Image_Present, 'tStopRefresh')  # time at next scr refresh
                Rapid_Image_Present.setAutoDraw(False)
        if Rapid_Image_Present.status == STARTED:  # only update if drawing
            Rapid_Image_Present.setImage(curImage, log=False)
        
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
    trials.addData('text_1.started', text_1.tStartRefresh)
    trials.addData('text_1.stopped', text_1.tStopRefresh)
    trials.addData('Fixation_Cross.started', Fixation_Cross.tStartRefresh)
    trials.addData('Fixation_Cross.stopped', Fixation_Cross.tStopRefresh)
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
