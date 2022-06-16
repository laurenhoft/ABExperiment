#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on June 14, 2022, at 14:16
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
expName = 'TestPsychoPy'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\User\\OneDrive\\Documents\\GitHub\\Test\\TestPsychoPy_lastrun.py',
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
    text='Instructions here',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
End_Instructions = keyboard.Keyboard()

# Initialize components for Routine "AB_Practice"
AB_PracticeClock = core.Clock()
# Set experiment start values for variable component curImage
curImage = ''
curImageContainer = []
#This is code
trialClock = core.Clock()
Practice_Text_1 = visual.TextStim(win=win, name='Practice_Text_1',
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

# Initialize components for Routine "Practice_T1_Response"
Practice_T1_ResponseClock = core.Clock()
T1_Response = visual.TextStim(win=win, name='T1_Response',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Practice_T2_Response"
Practice_T2_ResponseClock = core.Clock()
T2_Response = visual.TextStim(win=win, name='T2_Response',
    text='Did you see the blender',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

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
trials = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('C:/Users/User/OneDrive/Documents/GitHub/Test/Practice_Condition.xlsx'),
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
    
    # ------Prepare to start Routine "AB_Practice"-------
    continueRoutine = True
    # update component parameters for each repeat
    t = 0
    trialClock.reset()
    imageCount = 0
    #imgOnScreen = False
    Practice_Text_1.setText(cueWord)
    # keep track of which components have finished
    AB_PracticeComponents = [Practice_Text_1, Fixation_Cross, Rapid_Image_Present]
    for thisComponent in AB_PracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AB_PracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AB_Practice"-------
    while continueRoutine:
        # get current time
        t = AB_PracticeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AB_PracticeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        t = trialClock.getTime()
        
        
        
        curImage = "resources\\" + Img1
        imageCount = 1
        
        if t>StimLength + 1.5:
            curImage = "resources\\" + Img2
            imageCount = 2
        
        if t>StimLength*2 + 1.5:
            curImage = "resources\\" + Img3
            imageCount = 3
        
        if t>StimLength*3 + 1.5:
            curImage = "resources\\" + Img4
            imageCount = 4
        
        if t>StimLength*4 + 1.5:
            if Img5 == next_trial:
                continueRoutine = False
            else:
                curImage = "resources\\" + Img5
                imageCount = 5
        
        if t>StimLength*5 + 1.5:
            if Img6 == next_trial:
                continueRoutine = False
            else:
                curImage = "resources\\" + Img6
                imageCount = 6
        
        if t>StimLength*6 + 1.5:
            if Img7 == next_trial:
                continueRoutine = False
            else:
                curImage = "resources\\" + Img7
                imageCount = 7
        
        if t>StimLength*7 + 1.5:
            if Img8 == next_trial:
                continueRoutine = False
            else:
                curImage = "resources\\" + Img8
                imageCount = 8
        
        if t>StimLength*8 + 1.5:
            if Img9 == next_trial:
                continueRoutine = False
            else:
                curImage = "resources\\" + Img9
                imageCount = 9
        
        if t>StimLength*9 + 1.5:
            if Img10 == next_trial:
                continueRoutine = False
            else:
                curImage = "resources\\" + Img10
                imageCount = 10
        
        if t>StimLength*10 + 1.5:
            if Img11 == next_trial:
                continueRoutine = False
            else:
                curImage = "resources\\" + Img11
                imageCount = 11
        
        if t>StimLength*11 + 1.5:
            if Img12 == next_trial:
                continueRoutine = False
            else:
                curImage = "resources\\" + Img12
                imageCount = 12
        
        if t>StimLength*12 + 1.5:
            if Img13 == next_trial:
                continueRoutine = False
            else:
                curImage = "resources\\" + Img13
                imageCount = 13
        
        if t>StimLength*13 + 1.5:
            if Img14 == next_trial:
                continueRoutine = False
            else:
                curImage = "resources\\" + Img14
                imageCount = 14
        
        if t>StimLength*14 + 1.5:
            if Img15 == next_trial:
                continueRoutine = False
            else:
                curImage = "resources\\" + Img15
                imageCount = 15
        
        if t>StimLength*15 + 1.5:
            if Img16 == next_trial:
                continueRoutine = False
            else:
                curImage = "resources\\" + Img16
                imageCount = 16
        
        if t>StimLength*16 + 1.5:
            if Img17 == next_trial:
                continueRoutine = False
            else:
                curImage = "resources\\" + Img17
                imageCount = 17
        
        
            
            
        
        
        
        
        
        # *Practice_Text_1* updates
        if Practice_Text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Practice_Text_1.frameNStart = frameN  # exact frame index
            Practice_Text_1.tStart = t  # local t and not account for scr refresh
            Practice_Text_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Practice_Text_1, 'tStartRefresh')  # time at next scr refresh
            Practice_Text_1.setAutoDraw(True)
        if Practice_Text_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Practice_Text_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Practice_Text_1.tStop = t  # not accounting for scr refresh
                Practice_Text_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Practice_Text_1, 'tStopRefresh')  # time at next scr refresh
                Practice_Text_1.setAutoDraw(False)
        
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
        if Rapid_Image_Present.status == STARTED:  # only update if drawing
            Rapid_Image_Present.setImage(curImage, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AB_PracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AB_Practice"-------
    for thisComponent in AB_PracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Practice_Text_1.started', Practice_Text_1.tStartRefresh)
    trials.addData('Practice_Text_1.stopped', Practice_Text_1.tStopRefresh)
    trials.addData('Fixation_Cross.started', Fixation_Cross.tStartRefresh)
    trials.addData('Fixation_Cross.stopped', Fixation_Cross.tStopRefresh)
    trials.addData('Rapid_Image_Present.started', Rapid_Image_Present.tStartRefresh)
    trials.addData('Rapid_Image_Present.stopped', Rapid_Image_Present.tStopRefresh)
    # the Routine "AB_Practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Practice_T1_Response"-------
    continueRoutine = True
    # update component parameters for each repeat
    T1_Response.setText(T1cue)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    Practice_T1_ResponseComponents = [T1_Response, key_resp]
    for thisComponent in Practice_T1_ResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Practice_T1_ResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Practice_T1_Response"-------
    while continueRoutine:
        # get current time
        t = Practice_T1_ResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Practice_T1_ResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T1_Response* updates
        if T1_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1_Response.frameNStart = frameN  # exact frame index
            T1_Response.tStart = t  # local t and not account for scr refresh
            T1_Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1_Response, 'tStartRefresh')  # time at next scr refresh
            T1_Response.setAutoDraw(True)
        if T1_Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > T1_Response.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                T1_Response.tStop = t  # not accounting for scr refresh
                T1_Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(T1_Response, 'tStopRefresh')  # time at next scr refresh
                T1_Response.setAutoDraw(False)
        
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
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Practice_T1_ResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practice_T1_Response"-------
    for thisComponent in Practice_T1_ResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T1_Response.started', T1_Response.tStartRefresh)
    trials.addData('T1_Response.stopped', T1_Response.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "Practice_T1_Response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Practice_T2_Response"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    Practice_T2_ResponseComponents = [T2_Response, key_resp_2]
    for thisComponent in Practice_T2_ResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Practice_T2_ResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Practice_T2_Response"-------
    while continueRoutine:
        # get current time
        t = Practice_T2_ResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Practice_T2_ResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T2_Response* updates
        if T2_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2_Response.frameNStart = frameN  # exact frame index
            T2_Response.tStart = t  # local t and not account for scr refresh
            T2_Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2_Response, 'tStartRefresh')  # time at next scr refresh
            T2_Response.setAutoDraw(True)
        if T2_Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > T2_Response.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                T2_Response.tStop = t  # not accounting for scr refresh
                T2_Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(T2_Response, 'tStopRefresh')  # time at next scr refresh
                T2_Response.setAutoDraw(False)
        
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
        for thisComponent in Practice_T2_ResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practice_T2_Response"-------
    for thisComponent in Practice_T2_ResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T2_Response.started', T2_Response.tStartRefresh)
    trials.addData('T2_Response.stopped', T2_Response.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    trials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "Practice_T2_Response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'trials'


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
