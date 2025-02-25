#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on Tue Feb 18 12:34:52 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'imensa_vc'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [2560, 1440]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/byeolkim/Dartmouth College Dropbox/Kim Byeol/Dartmouth/research/2022_Lux_IMENSA/experiment/continuous rater/imensa_vc/imensa_vc_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='norm',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'norm'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_consent1') is None:
        # initialise key_consent1
        key_consent1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_consent1',
        )
    if deviceManager.getDevice('key_consent2') is None:
        # initialise key_consent2
        key_consent2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_consent2',
        )
    if deviceManager.getDevice('key_intro') is None:
        # initialise key_intro
        key_intro = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_intro',
        )
    if deviceManager.getDevice('key_demo') is None:
        # initialise key_demo
        key_demo = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_demo',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Consent1" ---
    consent_1 = visual.ImageStim(
        win=win,
        name='consent_1', 
        image='consent1.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1.7,1.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_consent1 = keyboard.Keyboard(deviceName='key_consent1')
    
    # --- Initialize components for Routine "Consent2" ---
    consent_2 = visual.ImageStim(
        win=win,
        name='consent_2', 
        image='consent2.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1.7,1.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_consent2 = keyboard.Keyboard(deviceName='key_consent2')
    
    # --- Initialize components for Routine "Intro" ---
    # Run 'Begin Experiment' code from code_intro
    import random
    # Shuffle the seed (optional but adds more randomness)
    random.seed(random.randint(0, 10000))
    
    # List of emotions
    emotion_texts = [
        "How strongly are you feeling joyful right now?",
        "How strongly are you feeling warm and tender right now?",
        "How strongly are you feeling inspired or uplifted right now?",
        "How strongly are you feeling sadness right now?",
        "How strongly are you feeling ashamed right now?",
        "How strongly are you feeling horrified right now?",
        "How strongly are you feeling disgusted right now?",
        "How strongly are you feeling a sense of relevance to yourself right now?",
        "How strongly are you feeling surprised right now?",
        "How strongly are you feeling angry right now?",
        "How strongly are you feeling happy right now?"
    ]
    
    # Generate a random number (0~10, to match the list index)
    emo_index = random.randint(0, len(emotion_texts) - 1)
    
    # Assign the selected emotion text to a variable
    cont_emotion_que = emotion_texts[emo_index]
    text_intro = visual.TextStim(win=win, name='text_intro',
        text='In this task, you will watch nine short videos, each lasting 2–3 minutes. While watching, you will provide continuous ratings related to the video and answer a series of follow-up questions after each clip.\n\nDuring the video, you will rate the extent of your feelings by moving the red rating circle along the continuous rating bar using your mouse. The position of the circle represents the intensity of your emotions and will be recorded continuously. Please adjust the circle’s position whenever you notice a change in your emotions throughout the video. \n\nA demonstration of the continuous rating will be provided on the next page. Please adjust volume, if needed.\n\nTo proceed to the next page, please press the spacebar. ',
        font='Arial',
        units='norm', pos=(0, 0), draggable=False, height=0.07, wrapWidth=1.3, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_intro = keyboard.Keyboard(deviceName='key_intro')
    
    # --- Initialize components for Routine "demo" ---
    # Run 'Begin Experiment' code from code_demo
    slider_decimals = 1
    slideSpeed = 12
    oldRating = 50
    slider_width = 1
    slider_height = .05
    slider_orientation = 0
    #Failing to set ticks or labels in code
    slider_granularity = .1
    
    ###############
    # there seems to be a sampling mismatch between the audio playing device and the audio
    # the sound is sampling weird
    # but wait to see whether the online study went well
    ###############
    
    demo_text = (
        f'{cont_emotion_que}\n'
        f'Adjust the red circle to reflect your emotion in real-time.'
    )
    mouse_demo = event.Mouse(win=win)
    x, y = [None, None]
    mouse_demo.mouseClock = core.Clock()
    slider_shape_demo = visual.Rect(
        win=win, name='slider_shape_demo',
        width=(1.5, 0.15)[0], height=(1.5, 0.15)[1],
        ori=0.0, pos=(0, -0.67), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=0.0, depth=-2.0, interpolate=True)
    continuousSlider_demo = visual.Slider(win=win, name='continuousSlider_demo',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.67), units='norm',
        labels=["Barely at all", "", "Strongest\nimaginable"], ticks=(0, 50, 100), granularity=0.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[1, 1, 1], markerColor=[0.6078, -0.2784, -0.2784], lineColor='White', colorSpace='rgb',
        font='Arial', labelHeight=0.06,
        flip=False, ori=0.0, depth=-3, readOnly=False)
    questionText_demo = visual.TextStim(win=win, name='questionText_demo',
        text='',
        font='Arial',
        pos=(0, 0.7), draggable=False, height=0.08, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    movie_demo = visual.MovieStim(
        win, name='movie_demo',
        filename='stimuli/testvideo_4s.mp4', movieLib='ffpyplayer',
        loop=False, volume=1.0, noAudio=False,
        pos=(0, 0), size=(1,1), units=win.units,
        ori=0.0, anchor='center',opacity=None, contrast=1.0,
        depth=-5
    )
    
    # --- Initialize components for Routine "confirm" ---
    demo_confirm = visual.TextStim(win=win, name='demo_confirm',
        text='If you’d like to practice rating again, press “b.”\n\nIf the instructions are clear and you’re ready to begin the task, press the spacebar to proceed.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.07, wrapWidth=1.2, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_demo = keyboard.Keyboard(deviceName='key_demo')
    
    # --- Initialize components for Routine "begintrial" ---
    text_begintrial = visual.TextStim(win=win, name='text_begintrial',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.07, wrapWidth=1.3, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "clip" ---
    mouse_clip = event.Mouse(win=win)
    x, y = [None, None]
    mouse_clip.mouseClock = core.Clock()
    slider_shape_clip = visual.Rect(
        win=win, name='slider_shape_clip',units='norm', 
        width=(1.5, 0.15)[0], height=(1.5, 0.15)[1],
        ori=0.0, pos=(0, -0.67), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=0.0, depth=-2.0, interpolate=True)
    continuousSlider_clip = visual.Slider(win=win, name='continuousSlider_clip',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.67), units='norm',
        labels=["Barely at all", "", "Strongest\nimaginable"], ticks=(0, 50, 100), granularity=0.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=(1,1,1), markerColor=[0.6078, -0.2784, -0.2784], lineColor='White', colorSpace='rgb',
        font='Arial', labelHeight=0.06,
        flip=False, ori=0.0, depth=-3, readOnly=False)
    questionText_clip = visual.TextStim(win=win, name='questionText_clip',
        text='',
        font='Arial',
        pos=(0, 0.7), draggable=False, height=0.1, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    movie_clip = visual.MovieStim(
        win, name='movie_clip',
        filename=None, movieLib='ffpyplayer',
        loop=False, volume=1.0, noAudio=False,
        pos=(0, 0), size=(1, 1), units=win.units,
        ori=0.0, anchor='center',opacity=None, contrast=1.0,
        depth=-5
    )
    
    # --- Initialize components for Routine "attention" ---
    mouse_atten = event.Mouse(win=win)
    x, y = [None, None]
    mouse_atten.mouseClock = core.Clock()
    text_atten = visual.TextStim(win=win, name='text_atten',
        text='',
        font='Arial',
        pos=(0, 0.2), draggable=False, height=0.06, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    button_A_atten = visual.ButtonStim(win, 
        text='A', font='Arial',
        pos=(-0.4, -0.6),
        letterHeight=0.05,
        size=(0.2, 0.2), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_A_atten',
        depth=-3
    )
    button_A_atten.buttonClock = core.Clock()
    button_B_atten = visual.ButtonStim(win, 
        text='B', font='Arial',
        pos=(-0.2, -0.6),
        letterHeight=0.05,
        size=(0.2, 0.2), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_B_atten',
        depth=-4
    )
    button_B_atten.buttonClock = core.Clock()
    button_C_atten = visual.ButtonStim(win, 
        text='C', font='Arial',
        pos=(0, -0.6),
        letterHeight=0.05,
        size=(0.2, 0.2), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_C_atten',
        depth=-5
    )
    button_C_atten.buttonClock = core.Clock()
    button_D_atten = visual.ButtonStim(win, 
        text='D', font='Arial',
        pos=(0.2, -0.6),
        letterHeight=0.05,
        size=(0.2, 0.2), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_D_atten',
        depth=-6
    )
    button_D_atten.buttonClock = core.Clock()
    button_E_atten = visual.ButtonStim(win, 
        text='E', font='Arial',
        pos=(0.4, -0.6),
        letterHeight=0.05,
        size=(0.2, 0.2), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_E_atten',
        depth=-7
    )
    button_E_atten.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "ratings" ---
    text_rating_intro = visual.TextStim(win=win, name='text_rating_intro',
        text='Please respond to the following questions about the previous video clip by selecting a point on the bar.',
        font='Arial',
        pos=(0, .6), draggable=False, height=0.09, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    mouse_ratings = event.Mouse(win=win)
    x, y = [None, None]
    mouse_ratings.mouseClock = core.Clock()
    text_emo_ratings = visual.TextStim(win=win, name='text_emo_ratings',
        text='',
        font='Arial',
        pos=(0, 0.2), draggable=False, height=0.08, wrapWidth=1.2, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    continuousSlider_ratings = visual.Slider(win=win, name='continuousSlider_ratings',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.3), units='norm',
        labels=["Barely at all", "", "Strongest\nimaginable"], ticks=(0,50,100), granularity=0.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[1.0000, 1.0000, 1.0000], markerColor=[0.6078, -0.2784, -0.2784], lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.06,
        flip=False, ori=0.0, depth=-4, readOnly=False)
    
    # --- Initialize components for Routine "quiz" ---
    mouse_quiz = event.Mouse(win=win)
    x, y = [None, None]
    mouse_quiz.mouseClock = core.Clock()
    text_quiz = visual.TextStim(win=win, name='text_quiz',
        text='',
        font='Arial',
        pos=(0, 0.2), draggable=False, height=0.06, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    button_A_quiz = visual.ButtonStim(win, 
        text='A', font='Arial',
        pos=(-0.4, -0.6),
        letterHeight=0.05,
        size=(0.2, 0.2), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_A_quiz',
        depth=-3
    )
    button_A_quiz.buttonClock = core.Clock()
    button_B_quiz = visual.ButtonStim(win, 
        text='B', font='Arial',
        pos=(-0.2, -0.6),
        letterHeight=0.05,
        size=(0.2, 0.2), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_B_quiz',
        depth=-4
    )
    button_B_quiz.buttonClock = core.Clock()
    button_C_quiz = visual.ButtonStim(win, 
        text='C', font='Arial',
        pos=(0, -0.6),
        letterHeight=0.05,
        size=(0.2, 0.2), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_C_quiz',
        depth=-5
    )
    button_C_quiz.buttonClock = core.Clock()
    button_D_quiz = visual.ButtonStim(win, 
        text='D', font='Arial',
        pos=(0.2, -0.6),
        letterHeight=0.05,
        size=(0.2, 0.2), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_D_quiz',
        depth=-6
    )
    button_D_quiz.buttonClock = core.Clock()
    button_E_quiz = visual.ButtonStim(win, 
        text='E', font='Arial',
        pos=(0.4, -0.6),
        letterHeight=0.05,
        size=(0.2, 0.2), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_E_quiz',
        depth=-7
    )
    button_E_quiz.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "real" ---
    mouse_real = event.Mouse(win=win)
    x, y = [None, None]
    mouse_real.mouseClock = core.Clock()
    text_real = visual.TextStim(win=win, name='text_real',
        text='',
        font='Arial',
        pos=(0, 0.2), draggable=False, height=0.07, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    real_answer = visual.Slider(win=win, name='real_answer',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.3), units=win.units,
        labels=["Strongly\ndisagree", "Disagree", "Neutral", "Ågree", "Strongly\nagree"], ticks=(0, 25, 50, 75, 100), granularity=0.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='White', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Arial', labelHeight=0.05,
        flip=False, ori=0.0, depth=-2, readOnly=False)
    
    # --- Initialize components for Routine "End" ---
    text_ending = visual.TextStim(win=win, name='text_ending',
        text='The experiment is now complete. \nThank you for your participation.\nThis window will close shortly.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.07, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # set up handler to look after randomisation of conditions etc
    consentLoop = data.TrialHandler2(
        name='consentLoop',
        nReps=5.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(consentLoop)  # add the loop to the experiment
    thisConsentLoop = consentLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisConsentLoop.rgb)
    if thisConsentLoop != None:
        for paramName in thisConsentLoop:
            globals()[paramName] = thisConsentLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisConsentLoop in consentLoop:
        currentLoop = consentLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisConsentLoop.rgb)
        if thisConsentLoop != None:
            for paramName in thisConsentLoop:
                globals()[paramName] = thisConsentLoop[paramName]
        
        # --- Prepare to start Routine "Consent1" ---
        # create an object to store info about Routine Consent1
        Consent1 = data.Routine(
            name='Consent1',
            components=[consent_1, key_consent1],
        )
        Consent1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_consent1
        key_consent1.keys = []
        key_consent1.rt = []
        _key_consent1_allKeys = []
        # store start times for Consent1
        Consent1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Consent1.tStart = globalClock.getTime(format='float')
        Consent1.status = STARTED
        thisExp.addData('Consent1.started', Consent1.tStart)
        Consent1.maxDuration = None
        # keep track of which components have finished
        Consent1Components = Consent1.components
        for thisComponent in Consent1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Consent1" ---
        # if trial has changed, end Routine now
        if isinstance(consentLoop, data.TrialHandler2) and thisConsentLoop.thisN != consentLoop.thisTrial.thisN:
            continueRoutine = False
        Consent1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *consent_1* updates
            
            # if consent_1 is starting this frame...
            if consent_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                consent_1.frameNStart = frameN  # exact frame index
                consent_1.tStart = t  # local t and not account for scr refresh
                consent_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(consent_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                consent_1.status = STARTED
                consent_1.setAutoDraw(True)
            
            # if consent_1 is active this frame...
            if consent_1.status == STARTED:
                # update params
                pass
            
            # *key_consent1* updates
            waitOnFlip = False
            
            # if key_consent1 is starting this frame...
            if key_consent1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_consent1.frameNStart = frameN  # exact frame index
                key_consent1.tStart = t  # local t and not account for scr refresh
                key_consent1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_consent1, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_consent1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_consent1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_consent1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_consent1.status == STARTED and not waitOnFlip:
                theseKeys = key_consent1.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_consent1_allKeys.extend(theseKeys)
                if len(_key_consent1_allKeys):
                    key_consent1.keys = _key_consent1_allKeys[-1].name  # just the last key pressed
                    key_consent1.rt = _key_consent1_allKeys[-1].rt
                    key_consent1.duration = _key_consent1_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Consent1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Consent1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Consent1" ---
        for thisComponent in Consent1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Consent1
        Consent1.tStop = globalClock.getTime(format='float')
        Consent1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Consent1.stopped', Consent1.tStop)
        # the Routine "Consent1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Consent2" ---
        # create an object to store info about Routine Consent2
        Consent2 = data.Routine(
            name='Consent2',
            components=[consent_2, key_consent2],
        )
        Consent2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_consent2
        key_consent2.keys = []
        key_consent2.rt = []
        _key_consent2_allKeys = []
        # store start times for Consent2
        Consent2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Consent2.tStart = globalClock.getTime(format='float')
        Consent2.status = STARTED
        thisExp.addData('Consent2.started', Consent2.tStart)
        Consent2.maxDuration = None
        # keep track of which components have finished
        Consent2Components = Consent2.components
        for thisComponent in Consent2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Consent2" ---
        # if trial has changed, end Routine now
        if isinstance(consentLoop, data.TrialHandler2) and thisConsentLoop.thisN != consentLoop.thisTrial.thisN:
            continueRoutine = False
        Consent2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *consent_2* updates
            
            # if consent_2 is starting this frame...
            if consent_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                consent_2.frameNStart = frameN  # exact frame index
                consent_2.tStart = t  # local t and not account for scr refresh
                consent_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(consent_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                consent_2.status = STARTED
                consent_2.setAutoDraw(True)
            
            # if consent_2 is active this frame...
            if consent_2.status == STARTED:
                # update params
                pass
            
            # *key_consent2* updates
            waitOnFlip = False
            
            # if key_consent2 is starting this frame...
            if key_consent2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_consent2.frameNStart = frameN  # exact frame index
                key_consent2.tStart = t  # local t and not account for scr refresh
                key_consent2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_consent2, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_consent2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_consent2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_consent2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_consent2.status == STARTED and not waitOnFlip:
                theseKeys = key_consent2.getKeys(keyList=['space','b'], ignoreKeys=["escape"], waitRelease=False)
                _key_consent2_allKeys.extend(theseKeys)
                if len(_key_consent2_allKeys):
                    key_consent2.keys = _key_consent2_allKeys[-1].name  # just the last key pressed
                    key_consent2.rt = _key_consent2_allKeys[-1].rt
                    key_consent2.duration = _key_consent2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Consent2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Consent2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Consent2" ---
        for thisComponent in Consent2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Consent2
        Consent2.tStop = globalClock.getTime(format='float')
        Consent2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Consent2.stopped', Consent2.tStop)
        # Run 'End Routine' code from code_consent
        if key_consent2.keys == 'space':
             consentLoop.finished = True
        # the Routine "Consent2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 5.0 repeats of 'consentLoop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "Intro" ---
    # create an object to store info about Routine Intro
    Intro = data.Routine(
        name='Intro',
        components=[text_intro, key_intro],
    )
    Intro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_intro
    key_intro.keys = []
    key_intro.rt = []
    _key_intro_allKeys = []
    # store start times for Intro
    Intro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Intro.tStart = globalClock.getTime(format='float')
    Intro.status = STARTED
    thisExp.addData('Intro.started', Intro.tStart)
    Intro.maxDuration = None
    # keep track of which components have finished
    IntroComponents = Intro.components
    for thisComponent in Intro.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Intro" ---
    Intro.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_intro* updates
        
        # if text_intro is starting this frame...
        if text_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_intro.frameNStart = frameN  # exact frame index
            text_intro.tStart = t  # local t and not account for scr refresh
            text_intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_intro, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_intro.status = STARTED
            text_intro.setAutoDraw(True)
        
        # if text_intro is active this frame...
        if text_intro.status == STARTED:
            # update params
            pass
        
        # *key_intro* updates
        waitOnFlip = False
        
        # if key_intro is starting this frame...
        if key_intro.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_intro.frameNStart = frameN  # exact frame index
            key_intro.tStart = t  # local t and not account for scr refresh
            key_intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_intro, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_intro.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_intro.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_intro.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_intro.status == STARTED and not waitOnFlip:
            theseKeys = key_intro.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_intro_allKeys.extend(theseKeys)
            if len(_key_intro_allKeys):
                key_intro.keys = _key_intro_allKeys[-1].name  # just the last key pressed
                key_intro.rt = _key_intro_allKeys[-1].rt
                key_intro.duration = _key_intro_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Intro.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Intro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Intro" ---
    for thisComponent in Intro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Intro
    Intro.tStop = globalClock.getTime(format='float')
    Intro.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Intro.stopped', Intro.tStop)
    # Run 'End Routine' code from code_intro
    thisExp.addData('continuous_emotion_type',emo_index)
    thisExp.nextEntry()
    # the Routine "Intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    demoLoop = data.TrialHandler2(
        name='demoLoop',
        nReps=10.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(demoLoop)  # add the loop to the experiment
    thisDemoLoop = demoLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDemoLoop.rgb)
    if thisDemoLoop != None:
        for paramName in thisDemoLoop:
            globals()[paramName] = thisDemoLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisDemoLoop in demoLoop:
        currentLoop = demoLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisDemoLoop.rgb)
        if thisDemoLoop != None:
            for paramName in thisDemoLoop:
                globals()[paramName] = thisDemoLoop[paramName]
        
        # --- Prepare to start Routine "demo" ---
        # create an object to store info about Routine demo
        demo = data.Routine(
            name='demo',
            components=[mouse_demo, slider_shape_demo, continuousSlider_demo, questionText_demo, movie_demo],
        )
        demo.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_demo
        # frame counter
        thisFrame = 0
        
        # create an empty list to store data
        slider_data=[]
        
        # record the current position of the mouse
        mouseRec=mouse_demo.getPos()
        
        # a boolean value to make sure we only store one time point of the audio to stopping
        audioStopped = False
        
        # a boolean value to indicate whether there has been valid slider data
        mouseInSlider = False
        # setup some python lists for storing info about the mouse_demo
        gotValidClick = False  # until a click is received
        continuousSlider_demo.reset()
        questionText_demo.setText(demo_text)
        # store start times for demo
        demo.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        demo.tStart = globalClock.getTime(format='float')
        demo.status = STARTED
        thisExp.addData('demo.started', demo.tStart)
        demo.maxDuration = None
        # keep track of which components have finished
        demoComponents = demo.components
        for thisComponent in demo.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "demo" ---
        # if trial has changed, end Routine now
        if isinstance(demoLoop, data.TrialHandler2) and thisDemoLoop.thisN != demoLoop.thisTrial.thisN:
            continueRoutine = False
        demo.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_demo
            if slider_shape_demo.contains(mouse_demo) and (not mouseInSlider):
                mouseInSlider = True
                
            if slider_shape_demo.contains(mouse_demo) and mouseInSlider:
                if mouse_demo.getPos()[slider_orientation] != mouseRec[slider_orientation]:
                    mouseRec = mouse_demo.getPos()
                    continuousSlider_demo.markerPos = mouseRec[slider_orientation]/slider_width*100+100/2
                    # update oldRatings if 
                if continuousSlider_demo.markerPos:
                    if oldRating != continuousSlider_demo.markerPos:
                        oldRating = continuousSlider_demo.markerPos
                if continuousSlider_demo.markerPos and thisFrame%slideSpeed==0:
                    slider_data.append([round(oldRating,slider_decimals),int(t*1000)])
            
            thisFrame = thisFrame + 1
            # *mouse_demo* updates
            
            # if mouse_demo is starting this frame...
            if mouse_demo.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_demo.frameNStart = frameN  # exact frame index
                mouse_demo.tStart = t  # local t and not account for scr refresh
                mouse_demo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_demo, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_demo.status = STARTED
                mouse_demo.mouseClock.reset()
                prevButtonState = mouse_demo.getPressed()  # if button is down already this ISN'T a new click
            
            # *slider_shape_demo* updates
            
            # if slider_shape_demo is starting this frame...
            if slider_shape_demo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_shape_demo.frameNStart = frameN  # exact frame index
                slider_shape_demo.tStart = t  # local t and not account for scr refresh
                slider_shape_demo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_shape_demo, 'tStartRefresh')  # time at next scr refresh
                # update status
                slider_shape_demo.status = STARTED
                slider_shape_demo.setAutoDraw(True)
            
            # if slider_shape_demo is active this frame...
            if slider_shape_demo.status == STARTED:
                # update params
                pass
            
            # *continuousSlider_demo* updates
            
            # if continuousSlider_demo is starting this frame...
            if continuousSlider_demo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                continuousSlider_demo.frameNStart = frameN  # exact frame index
                continuousSlider_demo.tStart = t  # local t and not account for scr refresh
                continuousSlider_demo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(continuousSlider_demo, 'tStartRefresh')  # time at next scr refresh
                # update status
                continuousSlider_demo.status = STARTED
                continuousSlider_demo.setAutoDraw(True)
            
            # if continuousSlider_demo is active this frame...
            if continuousSlider_demo.status == STARTED:
                # update params
                pass
            
            # *questionText_demo* updates
            
            # if questionText_demo is starting this frame...
            if questionText_demo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                questionText_demo.frameNStart = frameN  # exact frame index
                questionText_demo.tStart = t  # local t and not account for scr refresh
                questionText_demo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(questionText_demo, 'tStartRefresh')  # time at next scr refresh
                # update status
                questionText_demo.status = STARTED
                questionText_demo.setAutoDraw(True)
            
            # if questionText_demo is active this frame...
            if questionText_demo.status == STARTED:
                # update params
                pass
            
            # *movie_demo* updates
            
            # if movie_demo is starting this frame...
            if movie_demo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                movie_demo.frameNStart = frameN  # exact frame index
                movie_demo.tStart = t  # local t and not account for scr refresh
                movie_demo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(movie_demo, 'tStartRefresh')  # time at next scr refresh
                # update status
                movie_demo.status = STARTED
                movie_demo.setAutoDraw(True)
                movie_demo.play()
            
            # if movie_demo is stopping this frame...
            if movie_demo.status == STARTED:
                if bool(False) or movie_demo.isFinished:
                    # keep track of stop time/frame for later
                    movie_demo.tStop = t  # not accounting for scr refresh
                    movie_demo.tStopRefresh = tThisFlipGlobal  # on global time
                    movie_demo.frameNStop = frameN  # exact frame index
                    # update status
                    movie_demo.status = FINISHED
                    movie_demo.setAutoDraw(False)
                    movie_demo.stop()
            if movie_demo.isFinished:  # force-end the Routine
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[movie_demo]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                demo.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in demo.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "demo" ---
        for thisComponent in demo.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for demo
        demo.tStop = globalClock.getTime(format='float')
        demo.tStopRefresh = tThisFlipGlobal
        thisExp.addData('demo.stopped', demo.tStop)
        # Run 'End Routine' code from code_demo
        thisExp.addData('continuousrating_demo',slider_data)
        # store data for demoLoop (TrialHandler)
        movie_demo.stop()  # ensure movie has stopped at end of Routine
        # the Routine "demo" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "confirm" ---
        # create an object to store info about Routine confirm
        confirm = data.Routine(
            name='confirm',
            components=[demo_confirm, key_demo],
        )
        confirm.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_demo
        key_demo.keys = []
        key_demo.rt = []
        _key_demo_allKeys = []
        # store start times for confirm
        confirm.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        confirm.tStart = globalClock.getTime(format='float')
        confirm.status = STARTED
        thisExp.addData('confirm.started', confirm.tStart)
        confirm.maxDuration = None
        # keep track of which components have finished
        confirmComponents = confirm.components
        for thisComponent in confirm.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "confirm" ---
        # if trial has changed, end Routine now
        if isinstance(demoLoop, data.TrialHandler2) and thisDemoLoop.thisN != demoLoop.thisTrial.thisN:
            continueRoutine = False
        confirm.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *demo_confirm* updates
            
            # if demo_confirm is starting this frame...
            if demo_confirm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                demo_confirm.frameNStart = frameN  # exact frame index
                demo_confirm.tStart = t  # local t and not account for scr refresh
                demo_confirm.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(demo_confirm, 'tStartRefresh')  # time at next scr refresh
                # update status
                demo_confirm.status = STARTED
                demo_confirm.setAutoDraw(True)
            
            # if demo_confirm is active this frame...
            if demo_confirm.status == STARTED:
                # update params
                pass
            
            # *key_demo* updates
            waitOnFlip = False
            
            # if key_demo is starting this frame...
            if key_demo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_demo.frameNStart = frameN  # exact frame index
                key_demo.tStart = t  # local t and not account for scr refresh
                key_demo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_demo, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_demo.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_demo.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_demo.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_demo.status == STARTED and not waitOnFlip:
                theseKeys = key_demo.getKeys(keyList=['space','b'], ignoreKeys=["escape"], waitRelease=False)
                _key_demo_allKeys.extend(theseKeys)
                if len(_key_demo_allKeys):
                    key_demo.keys = _key_demo_allKeys[-1].name  # just the last key pressed
                    key_demo.rt = _key_demo_allKeys[-1].rt
                    key_demo.duration = _key_demo_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                confirm.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in confirm.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "confirm" ---
        for thisComponent in confirm.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for confirm
        confirm.tStop = globalClock.getTime(format='float')
        confirm.tStopRefresh = tThisFlipGlobal
        thisExp.addData('confirm.stopped', confirm.tStop)
        # Run 'End Routine' code from code_confirm
        if key_demo.keys == 'space':
             demoLoop.finished = True
        # the Routine "confirm" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 10.0 repeats of 'demoLoop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # set up handler to look after randomisation of conditions etc
    trialLoop = data.TrialHandler2(
        name='trialLoop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('stim_positive.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trialLoop)  # add the loop to the experiment
    thisTrialLoop = trialLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop.rgb)
    if thisTrialLoop != None:
        for paramName in thisTrialLoop:
            globals()[paramName] = thisTrialLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrialLoop in trialLoop:
        currentLoop = trialLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop.rgb)
        if thisTrialLoop != None:
            for paramName in thisTrialLoop:
                globals()[paramName] = thisTrialLoop[paramName]
        
        # --- Prepare to start Routine "begintrial" ---
        # create an object to store info about Routine begintrial
        begintrial = data.Routine(
            name='begintrial',
            components=[text_begintrial, key_resp],
        )
        begintrial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_begintrial
        trial_start_text = (
            f"Movie clip {TrialN} of 9 is about to start.\n\n"
            f"During the movie, you will answer the\nquestion with the continuous rating:\n"
            f'"{cont_emotion_que}"\n\n'
            f"If you need a break before the next video,\nplease take a moment now.\n" 
            f"Pay close attention to the video and the \ncontinuous rating as the movie plays.\n\n"
            f"When you're ready, press the spacebar to begin."
        )
        
        
        text_begintrial.setText(trial_start_text)
        # create starting attributes for key_resp
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # store start times for begintrial
        begintrial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        begintrial.tStart = globalClock.getTime(format='float')
        begintrial.status = STARTED
        thisExp.addData('begintrial.started', begintrial.tStart)
        begintrial.maxDuration = None
        # keep track of which components have finished
        begintrialComponents = begintrial.components
        for thisComponent in begintrial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "begintrial" ---
        # if trial has changed, end Routine now
        if isinstance(trialLoop, data.TrialHandler2) and thisTrialLoop.thisN != trialLoop.thisTrial.thisN:
            continueRoutine = False
        begintrial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_begintrial* updates
            
            # if text_begintrial is starting this frame...
            if text_begintrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_begintrial.frameNStart = frameN  # exact frame index
                text_begintrial.tStart = t  # local t and not account for scr refresh
                text_begintrial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_begintrial, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_begintrial.status = STARTED
                text_begintrial.setAutoDraw(True)
            
            # if text_begintrial is active this frame...
            if text_begintrial.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                begintrial.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in begintrial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "begintrial" ---
        for thisComponent in begintrial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for begintrial
        begintrial.tStop = globalClock.getTime(format='float')
        begintrial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('begintrial.stopped', begintrial.tStop)
        # the Routine "begintrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "clip" ---
        # create an object to store info about Routine clip
        clip = data.Routine(
            name='clip',
            components=[mouse_clip, slider_shape_clip, continuousSlider_clip, questionText_clip, movie_clip],
        )
        clip.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_clip
        # frame counter
        thisFrame = 0
        
        # create an empty list to store data
        slider_data=[]
        
        # record the current position of the mouse
        mouseRec=mouse_clip.getPos()
        
        # a boolean value to make sure we only store one time point of the audio to stopping
        audioStopped = False
        
        # a boolean value to indicate whether there has been valid slider data
        mouseInSlider = False
        # setup some python lists for storing info about the mouse_clip
        mouse_clip.x = []
        mouse_clip.y = []
        mouse_clip.leftButton = []
        mouse_clip.midButton = []
        mouse_clip.rightButton = []
        mouse_clip.time = []
        gotValidClick = False  # until a click is received
        continuousSlider_clip.reset()
        questionText_clip.setText(cont_emotion_que)
        movie_clip.setMovie(clip_stim)
        # store start times for clip
        clip.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        clip.tStart = globalClock.getTime(format='float')
        clip.status = STARTED
        thisExp.addData('clip.started', clip.tStart)
        clip.maxDuration = None
        # keep track of which components have finished
        clipComponents = clip.components
        for thisComponent in clip.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "clip" ---
        # if trial has changed, end Routine now
        if isinstance(trialLoop, data.TrialHandler2) and thisTrialLoop.thisN != trialLoop.thisTrial.thisN:
            continueRoutine = False
        clip.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_clip
            if slider_shape_clip.contains(mouse_clip) and (not mouseInSlider):
                mouseInSlider = True
                
            if slider_shape_clip.contains(mouse_clip) and mouseInSlider:
                if mouse_clip.getPos()[slider_orientation] != mouseRec[slider_orientation]:
                    mouseRec = mouse_clip.getPos()
                    continuousSlider_clip.markerPos = mouseRec[slider_orientation]/slider_width*100+100/2
                    # update oldRatings if 
                if continuousSlider_clip.markerPos:
                    if oldRating != continuousSlider_clip.markerPos:
                        oldRating = continuousSlider_clip.markerPos
                if continuousSlider_clip.markerPos and thisFrame%slideSpeed==0:
                    slider_data.append([round(oldRating,slider_decimals),int(t*1000)])
            
            thisFrame = thisFrame + 1
            # *mouse_clip* updates
            
            # if mouse_clip is starting this frame...
            if mouse_clip.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_clip.frameNStart = frameN  # exact frame index
                mouse_clip.tStart = t  # local t and not account for scr refresh
                mouse_clip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_clip, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_clip.status = STARTED
                mouse_clip.mouseClock.reset()
                prevButtonState = mouse_clip.getPressed()  # if button is down already this ISN'T a new click
            if mouse_clip.status == STARTED:  # only update if started and not finished!
                buttons = mouse_clip.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        pass
                        x, y = mouse_clip.getPos()
                        mouse_clip.x.append(x)
                        mouse_clip.y.append(y)
                        buttons = mouse_clip.getPressed()
                        mouse_clip.leftButton.append(buttons[0])
                        mouse_clip.midButton.append(buttons[1])
                        mouse_clip.rightButton.append(buttons[2])
                        mouse_clip.time.append(mouse_clip.mouseClock.getTime())
            
            # *slider_shape_clip* updates
            
            # if slider_shape_clip is starting this frame...
            if slider_shape_clip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_shape_clip.frameNStart = frameN  # exact frame index
                slider_shape_clip.tStart = t  # local t and not account for scr refresh
                slider_shape_clip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_shape_clip, 'tStartRefresh')  # time at next scr refresh
                # update status
                slider_shape_clip.status = STARTED
                slider_shape_clip.setAutoDraw(True)
            
            # if slider_shape_clip is active this frame...
            if slider_shape_clip.status == STARTED:
                # update params
                pass
            
            # *continuousSlider_clip* updates
            
            # if continuousSlider_clip is starting this frame...
            if continuousSlider_clip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                continuousSlider_clip.frameNStart = frameN  # exact frame index
                continuousSlider_clip.tStart = t  # local t and not account for scr refresh
                continuousSlider_clip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(continuousSlider_clip, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continuousSlider_clip.started')
                # update status
                continuousSlider_clip.status = STARTED
                continuousSlider_clip.setAutoDraw(True)
            
            # if continuousSlider_clip is active this frame...
            if continuousSlider_clip.status == STARTED:
                # update params
                pass
            
            # *questionText_clip* updates
            
            # if questionText_clip is starting this frame...
            if questionText_clip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                questionText_clip.frameNStart = frameN  # exact frame index
                questionText_clip.tStart = t  # local t and not account for scr refresh
                questionText_clip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(questionText_clip, 'tStartRefresh')  # time at next scr refresh
                # update status
                questionText_clip.status = STARTED
                questionText_clip.setAutoDraw(True)
            
            # if questionText_clip is active this frame...
            if questionText_clip.status == STARTED:
                # update params
                pass
            
            # *movie_clip* updates
            
            # if movie_clip is starting this frame...
            if movie_clip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                movie_clip.frameNStart = frameN  # exact frame index
                movie_clip.tStart = t  # local t and not account for scr refresh
                movie_clip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(movie_clip, 'tStartRefresh')  # time at next scr refresh
                # update status
                movie_clip.status = STARTED
                movie_clip.setAutoDraw(True)
                movie_clip.play()
            
            # if movie_clip is stopping this frame...
            if movie_clip.status == STARTED:
                if bool(False) or movie_clip.isFinished:
                    # keep track of stop time/frame for later
                    movie_clip.tStop = t  # not accounting for scr refresh
                    movie_clip.tStopRefresh = tThisFlipGlobal  # on global time
                    movie_clip.frameNStop = frameN  # exact frame index
                    # update status
                    movie_clip.status = FINISHED
                    movie_clip.setAutoDraw(False)
                    movie_clip.stop()
            if movie_clip.isFinished:  # force-end the Routine
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[movie_clip]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                clip.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in clip.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "clip" ---
        for thisComponent in clip.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for clip
        clip.tStop = globalClock.getTime(format='float')
        clip.tStopRefresh = tThisFlipGlobal
        thisExp.addData('clip.stopped', clip.tStop)
        # Run 'End Routine' code from code_clip
        thisExp.addData('continuousrating',slider_data)
        # store data for trialLoop (TrialHandler)
        trialLoop.addData('mouse_clip.x', mouse_clip.x)
        trialLoop.addData('mouse_clip.y', mouse_clip.y)
        trialLoop.addData('mouse_clip.leftButton', mouse_clip.leftButton)
        trialLoop.addData('mouse_clip.midButton', mouse_clip.midButton)
        trialLoop.addData('mouse_clip.rightButton', mouse_clip.rightButton)
        trialLoop.addData('mouse_clip.time', mouse_clip.time)
        trialLoop.addData('continuousSlider_clip.response', continuousSlider_clip.getRating())
        trialLoop.addData('continuousSlider_clip.rt', continuousSlider_clip.getRT())
        movie_clip.stop()  # ensure movie has stopped at end of Routine
        # the Routine "clip" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "attention" ---
        # create an object to store info about Routine attention
        attention = data.Routine(
            name='attention',
            components=[mouse_atten, text_atten, button_A_atten, button_B_atten, button_C_atten, button_D_atten, button_E_atten],
        )
        attention.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_atten
        button_atten = 0
        text_atten.alignText = 'left'
        # setup some python lists for storing info about the mouse_atten
        gotValidClick = False  # until a click is received
        text_atten.setText(attention_ques)
        # reset button_A_atten to account for continued clicks & clear times on/off
        button_A_atten.reset()
        # reset button_B_atten to account for continued clicks & clear times on/off
        button_B_atten.reset()
        # reset button_C_atten to account for continued clicks & clear times on/off
        button_C_atten.reset()
        # reset button_D_atten to account for continued clicks & clear times on/off
        button_D_atten.reset()
        # reset button_E_atten to account for continued clicks & clear times on/off
        button_E_atten.reset()
        # store start times for attention
        attention.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        attention.tStart = globalClock.getTime(format='float')
        attention.status = STARTED
        thisExp.addData('attention.started', attention.tStart)
        attention.maxDuration = None
        # keep track of which components have finished
        attentionComponents = attention.components
        for thisComponent in attention.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "attention" ---
        # if trial has changed, end Routine now
        if isinstance(trialLoop, data.TrialHandler2) and thisTrialLoop.thisN != trialLoop.thisTrial.thisN:
            continueRoutine = False
        attention.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *mouse_atten* updates
            
            # if mouse_atten is starting this frame...
            if mouse_atten.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_atten.frameNStart = frameN  # exact frame index
                mouse_atten.tStart = t  # local t and not account for scr refresh
                mouse_atten.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_atten, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_atten.status = STARTED
                mouse_atten.mouseClock.reset()
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            
            # *text_atten* updates
            
            # if text_atten is starting this frame...
            if text_atten.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_atten.frameNStart = frameN  # exact frame index
                text_atten.tStart = t  # local t and not account for scr refresh
                text_atten.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_atten, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_atten.status = STARTED
                text_atten.setAutoDraw(True)
            
            # if text_atten is active this frame...
            if text_atten.status == STARTED:
                # update params
                pass
            # *button_A_atten* updates
            
            # if button_A_atten is starting this frame...
            if button_A_atten.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_A_atten.frameNStart = frameN  # exact frame index
                button_A_atten.tStart = t  # local t and not account for scr refresh
                button_A_atten.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_A_atten, 'tStartRefresh')  # time at next scr refresh
                # update status
                button_A_atten.status = STARTED
                win.callOnFlip(button_A_atten.buttonClock.reset)
                button_A_atten.setAutoDraw(True)
            
            # if button_A_atten is active this frame...
            if button_A_atten.status == STARTED:
                # update params
                pass
                # check whether button_A_atten has been pressed
                if button_A_atten.isClicked:
                    if not button_A_atten.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_A_atten.timesOn.append(routineTimer.getTime())
                        button_A_atten.timesOff.append(routineTimer.getTime())
                    elif len(button_A_atten.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_A_atten.timesOff[-1] = routineTimer.getTime()
                    if not button_A_atten.wasClicked:
                        # end routine when button_A_atten is clicked
                        continueRoutine = False
                    if not button_A_atten.wasClicked:
                        # run callback code when button_A_atten is clicked
                        button_atten = 1
            # take note of whether button_A_atten was clicked, so that next frame we know if clicks are new
            button_A_atten.wasClicked = button_A_atten.isClicked and button_A_atten.status == STARTED
            # *button_B_atten* updates
            
            # if button_B_atten is starting this frame...
            if button_B_atten.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_B_atten.frameNStart = frameN  # exact frame index
                button_B_atten.tStart = t  # local t and not account for scr refresh
                button_B_atten.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_B_atten, 'tStartRefresh')  # time at next scr refresh
                # update status
                button_B_atten.status = STARTED
                win.callOnFlip(button_B_atten.buttonClock.reset)
                button_B_atten.setAutoDraw(True)
            
            # if button_B_atten is active this frame...
            if button_B_atten.status == STARTED:
                # update params
                pass
                # check whether button_B_atten has been pressed
                if button_B_atten.isClicked:
                    if not button_B_atten.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_B_atten.timesOn.append(button_B_atten.buttonClock.getTime())
                        button_B_atten.timesOff.append(button_B_atten.buttonClock.getTime())
                    elif len(button_B_atten.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_B_atten.timesOff[-1] = button_B_atten.buttonClock.getTime()
                    if not button_B_atten.wasClicked:
                        # end routine when button_B_atten is clicked
                        continueRoutine = False
                    if not button_B_atten.wasClicked:
                        # run callback code when button_B_atten is clicked
                        button_atten = 2
            # take note of whether button_B_atten was clicked, so that next frame we know if clicks are new
            button_B_atten.wasClicked = button_B_atten.isClicked and button_B_atten.status == STARTED
            # *button_C_atten* updates
            
            # if button_C_atten is starting this frame...
            if button_C_atten.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_C_atten.frameNStart = frameN  # exact frame index
                button_C_atten.tStart = t  # local t and not account for scr refresh
                button_C_atten.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_C_atten, 'tStartRefresh')  # time at next scr refresh
                # update status
                button_C_atten.status = STARTED
                win.callOnFlip(button_C_atten.buttonClock.reset)
                button_C_atten.setAutoDraw(True)
            
            # if button_C_atten is active this frame...
            if button_C_atten.status == STARTED:
                # update params
                pass
                # check whether button_C_atten has been pressed
                if button_C_atten.isClicked:
                    if not button_C_atten.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_C_atten.timesOn.append(button_C_atten.buttonClock.getTime())
                        button_C_atten.timesOff.append(button_C_atten.buttonClock.getTime())
                    elif len(button_C_atten.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_C_atten.timesOff[-1] = button_C_atten.buttonClock.getTime()
                    if not button_C_atten.wasClicked:
                        # end routine when button_C_atten is clicked
                        continueRoutine = False
                    if not button_C_atten.wasClicked:
                        # run callback code when button_C_atten is clicked
                        button_atten = 3
            # take note of whether button_C_atten was clicked, so that next frame we know if clicks are new
            button_C_atten.wasClicked = button_C_atten.isClicked and button_C_atten.status == STARTED
            # *button_D_atten* updates
            
            # if button_D_atten is starting this frame...
            if button_D_atten.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_D_atten.frameNStart = frameN  # exact frame index
                button_D_atten.tStart = t  # local t and not account for scr refresh
                button_D_atten.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_D_atten, 'tStartRefresh')  # time at next scr refresh
                # update status
                button_D_atten.status = STARTED
                win.callOnFlip(button_D_atten.buttonClock.reset)
                button_D_atten.setAutoDraw(True)
            
            # if button_D_atten is active this frame...
            if button_D_atten.status == STARTED:
                # update params
                pass
                # check whether button_D_atten has been pressed
                if button_D_atten.isClicked:
                    if not button_D_atten.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_D_atten.timesOn.append(button_D_atten.buttonClock.getTime())
                        button_D_atten.timesOff.append(button_D_atten.buttonClock.getTime())
                    elif len(button_D_atten.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_D_atten.timesOff[-1] = button_D_atten.buttonClock.getTime()
                    if not button_D_atten.wasClicked:
                        # end routine when button_D_atten is clicked
                        continueRoutine = False
                    if not button_D_atten.wasClicked:
                        # run callback code when button_D_atten is clicked
                        button_atten = 4
            # take note of whether button_D_atten was clicked, so that next frame we know if clicks are new
            button_D_atten.wasClicked = button_D_atten.isClicked and button_D_atten.status == STARTED
            # *button_E_atten* updates
            
            # if button_E_atten is starting this frame...
            if button_E_atten.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_E_atten.frameNStart = frameN  # exact frame index
                button_E_atten.tStart = t  # local t and not account for scr refresh
                button_E_atten.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_E_atten, 'tStartRefresh')  # time at next scr refresh
                # update status
                button_E_atten.status = STARTED
                win.callOnFlip(button_E_atten.buttonClock.reset)
                button_E_atten.setAutoDraw(True)
            
            # if button_E_atten is active this frame...
            if button_E_atten.status == STARTED:
                # update params
                pass
                # check whether button_E_atten has been pressed
                if button_E_atten.isClicked:
                    if not button_E_atten.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_E_atten.timesOn.append(button_E_atten.buttonClock.getTime())
                        button_E_atten.timesOff.append(button_E_atten.buttonClock.getTime())
                    elif len(button_E_atten.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_E_atten.timesOff[-1] = button_E_atten.buttonClock.getTime()
                    if not button_E_atten.wasClicked:
                        # end routine when button_E_atten is clicked
                        continueRoutine = False
                    if not button_E_atten.wasClicked:
                        # run callback code when button_E_atten is clicked
                        button_atten = 5
            # take note of whether button_E_atten was clicked, so that next frame we know if clicks are new
            button_E_atten.wasClicked = button_E_atten.isClicked and button_E_atten.status == STARTED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                attention.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in attention.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "attention" ---
        for thisComponent in attention.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for attention
        attention.tStop = globalClock.getTime(format='float')
        attention.tStopRefresh = tThisFlipGlobal
        thisExp.addData('attention.stopped', attention.tStop)
        # Run 'End Routine' code from code_atten
        if button_atten == atten_answer:
           rightorwrong = True
        else:
           rightorwrong = False
        thisExp.addData('atten_button_response',button_atten)
        thisExp.addData('atten_pass',rightorwrong)
        # store data for trialLoop (TrialHandler)
        # the Routine "attention" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        ratingLoop = data.TrialHandler2(
            name='ratingLoop',
            nReps=1.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('rating_questions.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(ratingLoop)  # add the loop to the experiment
        thisRatingLoop = ratingLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisRatingLoop.rgb)
        if thisRatingLoop != None:
            for paramName in thisRatingLoop:
                globals()[paramName] = thisRatingLoop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisRatingLoop in ratingLoop:
            currentLoop = ratingLoop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisRatingLoop.rgb)
            if thisRatingLoop != None:
                for paramName in thisRatingLoop:
                    globals()[paramName] = thisRatingLoop[paramName]
            
            # --- Prepare to start Routine "ratings" ---
            # create an object to store info about Routine ratings
            ratings = data.Routine(
                name='ratings',
                components=[text_rating_intro, mouse_ratings, text_emo_ratings, continuousSlider_ratings],
            )
            ratings.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # setup some python lists for storing info about the mouse_ratings
            gotValidClick = False  # until a click is received
            mouse_ratings.mouseClock.reset()
            text_emo_ratings.setText(rating_ques)
            continuousSlider_ratings.reset()
            # store start times for ratings
            ratings.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            ratings.tStart = globalClock.getTime(format='float')
            ratings.status = STARTED
            thisExp.addData('ratings.started', ratings.tStart)
            ratings.maxDuration = None
            # keep track of which components have finished
            ratingsComponents = ratings.components
            for thisComponent in ratings.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ratings" ---
            # if trial has changed, end Routine now
            if isinstance(ratingLoop, data.TrialHandler2) and thisRatingLoop.thisN != ratingLoop.thisTrial.thisN:
                continueRoutine = False
            ratings.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_rating_intro* updates
                
                # if text_rating_intro is starting this frame...
                if text_rating_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_rating_intro.frameNStart = frameN  # exact frame index
                    text_rating_intro.tStart = t  # local t and not account for scr refresh
                    text_rating_intro.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_rating_intro, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    text_rating_intro.status = STARTED
                    text_rating_intro.setAutoDraw(True)
                
                # if text_rating_intro is active this frame...
                if text_rating_intro.status == STARTED:
                    # update params
                    pass
                # *mouse_ratings* updates
                
                # if mouse_ratings is starting this frame...
                if mouse_ratings.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_ratings.frameNStart = frameN  # exact frame index
                    mouse_ratings.tStart = t  # local t and not account for scr refresh
                    mouse_ratings.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_ratings, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    mouse_ratings.status = STARTED
                    prevButtonState = mouse_ratings.getPressed()  # if button is down already this ISN'T a new click
                
                # *text_emo_ratings* updates
                
                # if text_emo_ratings is starting this frame...
                if text_emo_ratings.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                    # keep track of start time/frame for later
                    text_emo_ratings.frameNStart = frameN  # exact frame index
                    text_emo_ratings.tStart = t  # local t and not account for scr refresh
                    text_emo_ratings.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_emo_ratings, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    text_emo_ratings.status = STARTED
                    text_emo_ratings.setAutoDraw(True)
                
                # if text_emo_ratings is active this frame...
                if text_emo_ratings.status == STARTED:
                    # update params
                    pass
                
                # *continuousSlider_ratings* updates
                
                # if continuousSlider_ratings is starting this frame...
                if continuousSlider_ratings.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                    # keep track of start time/frame for later
                    continuousSlider_ratings.frameNStart = frameN  # exact frame index
                    continuousSlider_ratings.tStart = t  # local t and not account for scr refresh
                    continuousSlider_ratings.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(continuousSlider_ratings, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    continuousSlider_ratings.status = STARTED
                    continuousSlider_ratings.setAutoDraw(True)
                
                # if continuousSlider_ratings is active this frame...
                if continuousSlider_ratings.status == STARTED:
                    # update params
                    pass
                
                # Check continuousSlider_ratings for response to end Routine
                if continuousSlider_ratings.getRating() is not None and continuousSlider_ratings.status == STARTED:
                    continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    ratings.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ratings.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ratings" ---
            for thisComponent in ratings.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for ratings
            ratings.tStop = globalClock.getTime(format='float')
            ratings.tStopRefresh = tThisFlipGlobal
            thisExp.addData('ratings.stopped', ratings.tStop)
            # store data for ratingLoop (TrialHandler)
            ratingLoop.addData('continuousSlider_ratings.response', continuousSlider_ratings.getRating())
            ratingLoop.addData('continuousSlider_ratings.rt', continuousSlider_ratings.getRT())
            # the Routine "ratings" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'ratingLoop'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "quiz" ---
        # create an object to store info about Routine quiz
        quiz = data.Routine(
            name='quiz',
            components=[mouse_quiz, text_quiz, button_A_quiz, button_B_quiz, button_C_quiz, button_D_quiz, button_E_quiz],
        )
        quiz.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_quiz
        button = 0
        text_quiz.alignText = 'left'
        # setup some python lists for storing info about the mouse_quiz
        gotValidClick = False  # until a click is received
        mouse_quiz.mouseClock.reset()
        text_quiz.setText(compre_ques)
        # reset button_A_quiz to account for continued clicks & clear times on/off
        button_A_quiz.reset()
        # reset button_B_quiz to account for continued clicks & clear times on/off
        button_B_quiz.reset()
        # reset button_C_quiz to account for continued clicks & clear times on/off
        button_C_quiz.reset()
        # reset button_D_quiz to account for continued clicks & clear times on/off
        button_D_quiz.reset()
        # reset button_E_quiz to account for continued clicks & clear times on/off
        button_E_quiz.reset()
        # store start times for quiz
        quiz.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        quiz.tStart = globalClock.getTime(format='float')
        quiz.status = STARTED
        thisExp.addData('quiz.started', quiz.tStart)
        quiz.maxDuration = None
        # keep track of which components have finished
        quizComponents = quiz.components
        for thisComponent in quiz.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "quiz" ---
        # if trial has changed, end Routine now
        if isinstance(trialLoop, data.TrialHandler2) and thisTrialLoop.thisN != trialLoop.thisTrial.thisN:
            continueRoutine = False
        quiz.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *mouse_quiz* updates
            
            # if mouse_quiz is starting this frame...
            if mouse_quiz.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_quiz.frameNStart = frameN  # exact frame index
                mouse_quiz.tStart = t  # local t and not account for scr refresh
                mouse_quiz.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_quiz, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_quiz.status = STARTED
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            
            # *text_quiz* updates
            
            # if text_quiz is starting this frame...
            if text_quiz.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_quiz.frameNStart = frameN  # exact frame index
                text_quiz.tStart = t  # local t and not account for scr refresh
                text_quiz.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_quiz, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_quiz.status = STARTED
                text_quiz.setAutoDraw(True)
            
            # if text_quiz is active this frame...
            if text_quiz.status == STARTED:
                # update params
                pass
            # *button_A_quiz* updates
            
            # if button_A_quiz is starting this frame...
            if button_A_quiz.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_A_quiz.frameNStart = frameN  # exact frame index
                button_A_quiz.tStart = t  # local t and not account for scr refresh
                button_A_quiz.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_A_quiz, 'tStartRefresh')  # time at next scr refresh
                # update status
                button_A_quiz.status = STARTED
                win.callOnFlip(button_A_quiz.buttonClock.reset)
                button_A_quiz.setAutoDraw(True)
            
            # if button_A_quiz is active this frame...
            if button_A_quiz.status == STARTED:
                # update params
                pass
                # check whether button_A_quiz has been pressed
                if button_A_quiz.isClicked:
                    if not button_A_quiz.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_A_quiz.timesOn.append(routineTimer.getTime())
                        button_A_quiz.timesOff.append(routineTimer.getTime())
                    elif len(button_A_quiz.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_A_quiz.timesOff[-1] = routineTimer.getTime()
                    if not button_A_quiz.wasClicked:
                        # end routine when button_A_quiz is clicked
                        continueRoutine = False
                    if not button_A_quiz.wasClicked:
                        # run callback code when button_A_quiz is clicked
                        button = 1
            # take note of whether button_A_quiz was clicked, so that next frame we know if clicks are new
            button_A_quiz.wasClicked = button_A_quiz.isClicked and button_A_quiz.status == STARTED
            # *button_B_quiz* updates
            
            # if button_B_quiz is starting this frame...
            if button_B_quiz.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_B_quiz.frameNStart = frameN  # exact frame index
                button_B_quiz.tStart = t  # local t and not account for scr refresh
                button_B_quiz.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_B_quiz, 'tStartRefresh')  # time at next scr refresh
                # update status
                button_B_quiz.status = STARTED
                win.callOnFlip(button_B_quiz.buttonClock.reset)
                button_B_quiz.setAutoDraw(True)
            
            # if button_B_quiz is active this frame...
            if button_B_quiz.status == STARTED:
                # update params
                pass
                # check whether button_B_quiz has been pressed
                if button_B_quiz.isClicked:
                    if not button_B_quiz.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_B_quiz.timesOn.append(button_B_quiz.buttonClock.getTime())
                        button_B_quiz.timesOff.append(button_B_quiz.buttonClock.getTime())
                    elif len(button_B_quiz.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_B_quiz.timesOff[-1] = button_B_quiz.buttonClock.getTime()
                    if not button_B_quiz.wasClicked:
                        # end routine when button_B_quiz is clicked
                        continueRoutine = False
                    if not button_B_quiz.wasClicked:
                        # run callback code when button_B_quiz is clicked
                        button = 2
            # take note of whether button_B_quiz was clicked, so that next frame we know if clicks are new
            button_B_quiz.wasClicked = button_B_quiz.isClicked and button_B_quiz.status == STARTED
            # *button_C_quiz* updates
            
            # if button_C_quiz is starting this frame...
            if button_C_quiz.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_C_quiz.frameNStart = frameN  # exact frame index
                button_C_quiz.tStart = t  # local t and not account for scr refresh
                button_C_quiz.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_C_quiz, 'tStartRefresh')  # time at next scr refresh
                # update status
                button_C_quiz.status = STARTED
                win.callOnFlip(button_C_quiz.buttonClock.reset)
                button_C_quiz.setAutoDraw(True)
            
            # if button_C_quiz is active this frame...
            if button_C_quiz.status == STARTED:
                # update params
                pass
                # check whether button_C_quiz has been pressed
                if button_C_quiz.isClicked:
                    if not button_C_quiz.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_C_quiz.timesOn.append(button_C_quiz.buttonClock.getTime())
                        button_C_quiz.timesOff.append(button_C_quiz.buttonClock.getTime())
                    elif len(button_C_quiz.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_C_quiz.timesOff[-1] = button_C_quiz.buttonClock.getTime()
                    if not button_C_quiz.wasClicked:
                        # end routine when button_C_quiz is clicked
                        continueRoutine = False
                    if not button_C_quiz.wasClicked:
                        # run callback code when button_C_quiz is clicked
                        button = 3
            # take note of whether button_C_quiz was clicked, so that next frame we know if clicks are new
            button_C_quiz.wasClicked = button_C_quiz.isClicked and button_C_quiz.status == STARTED
            # *button_D_quiz* updates
            
            # if button_D_quiz is starting this frame...
            if button_D_quiz.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_D_quiz.frameNStart = frameN  # exact frame index
                button_D_quiz.tStart = t  # local t and not account for scr refresh
                button_D_quiz.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_D_quiz, 'tStartRefresh')  # time at next scr refresh
                # update status
                button_D_quiz.status = STARTED
                win.callOnFlip(button_D_quiz.buttonClock.reset)
                button_D_quiz.setAutoDraw(True)
            
            # if button_D_quiz is active this frame...
            if button_D_quiz.status == STARTED:
                # update params
                pass
                # check whether button_D_quiz has been pressed
                if button_D_quiz.isClicked:
                    if not button_D_quiz.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_D_quiz.timesOn.append(button_D_quiz.buttonClock.getTime())
                        button_D_quiz.timesOff.append(button_D_quiz.buttonClock.getTime())
                    elif len(button_D_quiz.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_D_quiz.timesOff[-1] = button_D_quiz.buttonClock.getTime()
                    if not button_D_quiz.wasClicked:
                        # end routine when button_D_quiz is clicked
                        continueRoutine = False
                    if not button_D_quiz.wasClicked:
                        # run callback code when button_D_quiz is clicked
                        button = 4
            # take note of whether button_D_quiz was clicked, so that next frame we know if clicks are new
            button_D_quiz.wasClicked = button_D_quiz.isClicked and button_D_quiz.status == STARTED
            # *button_E_quiz* updates
            
            # if button_E_quiz is starting this frame...
            if button_E_quiz.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_E_quiz.frameNStart = frameN  # exact frame index
                button_E_quiz.tStart = t  # local t and not account for scr refresh
                button_E_quiz.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_E_quiz, 'tStartRefresh')  # time at next scr refresh
                # update status
                button_E_quiz.status = STARTED
                win.callOnFlip(button_E_quiz.buttonClock.reset)
                button_E_quiz.setAutoDraw(True)
            
            # if button_E_quiz is active this frame...
            if button_E_quiz.status == STARTED:
                # update params
                pass
                # check whether button_E_quiz has been pressed
                if button_E_quiz.isClicked:
                    if not button_E_quiz.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_E_quiz.timesOn.append(button_E_quiz.buttonClock.getTime())
                        button_E_quiz.timesOff.append(button_E_quiz.buttonClock.getTime())
                    elif len(button_E_quiz.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_E_quiz.timesOff[-1] = button_E_quiz.buttonClock.getTime()
                    if not button_E_quiz.wasClicked:
                        # end routine when button_E_quiz is clicked
                        continueRoutine = False
                    if not button_E_quiz.wasClicked:
                        # run callback code when button_E_quiz is clicked
                        button = 5
            # take note of whether button_E_quiz was clicked, so that next frame we know if clicks are new
            button_E_quiz.wasClicked = button_E_quiz.isClicked and button_E_quiz.status == STARTED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                quiz.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in quiz.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "quiz" ---
        for thisComponent in quiz.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for quiz
        quiz.tStop = globalClock.getTime(format='float')
        quiz.tStopRefresh = tThisFlipGlobal
        thisExp.addData('quiz.stopped', quiz.tStop)
        # Run 'End Routine' code from code_quiz
        if button == que_answer:
           rightorwrong = True
        else:
           rightorwrong = False
        thisExp.addData('button_response',button)
        thisExp.addData('quiz_answer',rightorwrong)
        # store data for trialLoop (TrialHandler)
        # the Routine "quiz" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trialLoop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "real" ---
    # create an object to store info about Routine real
    real = data.Routine(
        name='real',
        components=[mouse_real, text_real, real_answer],
    )
    real.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_real
    gotValidClick = False  # until a click is received
    mouse_real.mouseClock.reset()
    text_real.setText('This question will not affect your payment.\nWe simply ask for your honest response. \n\nDid you pay sufficient attention during the study, and do you believe that your data should be included in the final dataset?\n\nClick anywhere on the bar to submit your response.\n\n')
    real_answer.reset()
    # store start times for real
    real.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    real.tStart = globalClock.getTime(format='float')
    real.status = STARTED
    thisExp.addData('real.started', real.tStart)
    real.maxDuration = None
    # keep track of which components have finished
    realComponents = real.components
    for thisComponent in real.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "real" ---
    real.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse_real* updates
        
        # if mouse_real is starting this frame...
        if mouse_real.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_real.frameNStart = frameN  # exact frame index
            mouse_real.tStart = t  # local t and not account for scr refresh
            mouse_real.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_real, 'tStartRefresh')  # time at next scr refresh
            # update status
            mouse_real.status = STARTED
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        
        # *text_real* updates
        
        # if text_real is starting this frame...
        if text_real.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_real.frameNStart = frameN  # exact frame index
            text_real.tStart = t  # local t and not account for scr refresh
            text_real.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_real, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_real.status = STARTED
            text_real.setAutoDraw(True)
        
        # if text_real is active this frame...
        if text_real.status == STARTED:
            # update params
            pass
        
        # *real_answer* updates
        
        # if real_answer is starting this frame...
        if real_answer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            real_answer.frameNStart = frameN  # exact frame index
            real_answer.tStart = t  # local t and not account for scr refresh
            real_answer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(real_answer, 'tStartRefresh')  # time at next scr refresh
            # update status
            real_answer.status = STARTED
            real_answer.setAutoDraw(True)
        
        # if real_answer is active this frame...
        if real_answer.status == STARTED:
            # update params
            pass
        
        # Check real_answer for response to end Routine
        if real_answer.getRating() is not None and real_answer.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            real.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in real.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "real" ---
    for thisComponent in real.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for real
    real.tStop = globalClock.getTime(format='float')
    real.tStopRefresh = tThisFlipGlobal
    thisExp.addData('real.stopped', real.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('real_answer.response', real_answer.getRating())
    thisExp.addData('real_answer.rt', real_answer.getRT())
    thisExp.nextEntry()
    # the Routine "real" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "End" ---
    # create an object to store info about Routine End
    End = data.Routine(
        name='End',
        components=[text_ending],
    )
    End.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for End
    End.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    End.tStart = globalClock.getTime(format='float')
    End.status = STARTED
    thisExp.addData('End.started', End.tStart)
    End.maxDuration = None
    # keep track of which components have finished
    EndComponents = End.components
    for thisComponent in End.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "End" ---
    End.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_ending* updates
        
        # if text_ending is starting this frame...
        if text_ending.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_ending.frameNStart = frameN  # exact frame index
            text_ending.tStart = t  # local t and not account for scr refresh
            text_ending.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_ending, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_ending.status = STARTED
            text_ending.setAutoDraw(True)
        
        # if text_ending is active this frame...
        if text_ending.status == STARTED:
            # update params
            pass
        
        # if text_ending is stopping this frame...
        if text_ending.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_ending.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_ending.tStop = t  # not accounting for scr refresh
                text_ending.tStopRefresh = tThisFlipGlobal  # on global time
                text_ending.frameNStop = frameN  # exact frame index
                # update status
                text_ending.status = FINISHED
                text_ending.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            End.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "End" ---
    for thisComponent in End.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for End
    End.tStop = globalClock.getTime(format='float')
    End.tStopRefresh = tThisFlipGlobal
    thisExp.addData('End.stopped', End.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if End.maxDurationReached:
        routineTimer.addTime(-End.maxDuration)
    elif End.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
