/****************** 
 * Imensa_Vc *
 ******************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'imensa_vc';  // from the Builder filename that created this script
let expInfo = {
    // 'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'PROLIFIC_PID': '', // Prolific option
  };

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'norm',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const consentLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(consentLoopLoopBegin(consentLoopLoopScheduler));
flowScheduler.add(consentLoopLoopScheduler);
flowScheduler.add(consentLoopLoopEnd);



flowScheduler.add(IntroRoutineBegin());
flowScheduler.add(IntroRoutineEachFrame());
flowScheduler.add(IntroRoutineEnd());
const demoLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(demoLoopLoopBegin(demoLoopLoopScheduler));
flowScheduler.add(demoLoopLoopScheduler);
flowScheduler.add(demoLoopLoopEnd);



const trialLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialLoopLoopBegin(trialLoopLoopScheduler));
flowScheduler.add(trialLoopLoopScheduler);
flowScheduler.add(trialLoopLoopEnd);








flowScheduler.add(realRoutineBegin());
flowScheduler.add(realRoutineEachFrame());
flowScheduler.add(realRoutineEnd());
flowScheduler.add(EndRoutineBegin());
flowScheduler.add(EndRoutineEachFrame());
flowScheduler.add(EndRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'stim_positive.xlsx', 'path': 'stim_positive.xlsx'},
    {'name': 'rating_questions.xlsx', 'path': 'rating_questions.xlsx'},
    {'name': 'consent1.png', 'path': 'consent1.png'},
    {'name': 'consent2.png', 'path': 'consent2.png'},
    {'name': 'stimuli/testvideo_4s.mp4', 'path': 'stimuli/testvideo_4s.mp4'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  psychoJS.setRedirectUrls('https://app.prolific.com/submissions/complete?cc=YOURCODE', '');  // Prolific option. Change the URL accordingly
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["PROLIFIC_PID"]}_${expName}`);
    
  // psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var Consent1Clock;
var consent_1;
var key_consent1;
var Consent2Clock;
var consent_2;
var key_consent2;
var IntroClock;
var text_intro;
var key_intro;
var demoClock;
var slider_decimals;
var slideSpeed;
var oldRating;
var slider_width;
var slider_height;
var slider_orientation;
var slider_granularity;
var mouse_demo;
var slider_shape_demo;
var continuousSlider_demo;
var questionText_demo;
var movie_demo;
var confirmClock;
var demo_confirm;
var key_demo;
var begintrialClock;
var text_begintrial;
var key_resp;
var clipClock;
var mouse_clip;
var slider_shape_clip;
var continuousSlider_clip;
var questionText_clip;
var movie_clip;
var attentionClock;
var mouse_atten;
var text_atten;
var button_A_atten;
var button_B_atten;
var button_C_atten;
var button_D_atten;
var button_E_atten;
var ratingsClock;
var text_rating_intro;
var mouse_ratings;
var text_emo_ratings;
var continuousSlider_ratings;
var quizClock;
var mouse_quiz;
var text_quiz;
var button_A_quiz;
var button_B_quiz;
var button_C_quiz;
var button_D_quiz;
var button_E_quiz;
var realClock;
var mouse_real;
var text_real;
var real_answer;
var EndClock;
var text_ending;
var globalClock;
var routineTimer;

var emotionTexts;
var emoIndex;
var cont_emotion_que;
var demo_text;
var trial_start_text;
var isAnswerCorrect

async function experimentInit() {
  // Initialize components for Routine "Consent1"
  Consent1Clock = new util.Clock();
  consent_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'consent_1', units : undefined, 
    image : 'consent1.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    // size : [screenHeight * (1.8*1300/930)/screenWidth, 1.8],
    size : [(10/16) * (1300/930) * 1.8, 1.8],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_consent1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Consent2"
  Consent2Clock = new util.Clock();
  consent_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'consent_2', units : undefined, 
    image : 'consent2.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [(10/16) * (1300/930) * 1.8, 1.8],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  key_consent2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Intro"
  IntroClock = new util.Clock();
  text_intro = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_intro',
    text: 'In this task, you will watch nine short videos, each lasting 2–3 minutes. While watching, you will provide continuous ratings related to the video and answer a series of follow-up questions after each clip.\n\nDuring the video, you will rate the extent of your feelings by moving the red rating circle along the continuous rating bar using your mouse. The position of the circle represents the intensity of your emotions and will be recorded continuously. Please adjust the circle’s position whenever you notice a change in your emotions throughout the video. \n\nA demonstration of the continuous rating will be provided on the next page. Please adjust volume, if needed.\n\nTo proceed to the next page, please press the spacebar. ',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], draggable: false, height: 0.07,  wrapWidth: 1.3, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });


  // List of emotions
  emotionTexts = [
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
];

// Generate a random number (0~10, to match the list index)
emoIndex = getRandomInt(0, 10);
psychoJS.experiment.addData('continuous_emotion_type', emoIndex);

// Assign the selected emotion text to a variable
cont_emotion_que = emotionTexts[emoIndex];

// console.log(cont_emotion_que);
demo_text = cont_emotion_que + "\nAdjust the red circle to reflect your emotion in real-time.";

  
  key_intro = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "demo"
  demoClock = new util.Clock();
  // Run 'Begin Experiment' code from code_demo
  slider_decimals = 1;
  // slideSpeed = 12;
  if (frameDur <= 0.0833) {
    // to make the sampling rate relatively consistent across participants (83.3 ms per sample, for 60, 120, and 144 Hz frame rate)
    slideSpeed = Math.round(0.0833/frameDur);    
  } else {
    // if the frame rate is less than 12 Hz, then sample at every frame
    slideSpeed = 1
  }
    oldRating = 50;
  slider_width = 1;
  slider_height = 0.05;
  slider_orientation = 0;
  slider_granularity = 0.1;
  
  mouse_demo = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_demo.mouseClock = new util.Clock();
  slider_shape_demo = new visual.Rect ({
    win: psychoJS.window, name: 'slider_shape_demo', 
    width: [1.5, 0.15][0], height: [1.5, 0.15][1],
    ori: 0.0, 
    pos: [0, (- 0.67)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 0.0, 
    depth: -2, 
    interpolate: true, 
  });
  
  continuousSlider_demo = new visual.Slider({
    win: psychoJS.window, name: 'continuousSlider_demo',
    startValue: undefined,
    size: [1.0, 0.1], pos: [0, (- 0.67)], ori: 0.0, units: 'norm',
    labels: ["Barely at all", "", "Strongest\nimaginable"], fontSize: 0.06, ticks: [0, 50, 100],
    granularity: 0.0, style: ["RATING"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color([0.6078, (- 0.2784), (- 0.2784)]), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Arial', bold: true, italic: false, depth: -3, 
    flip: false,
  });
  
  questionText_demo = new visual.TextStim({
    win: psychoJS.window,
    name: 'questionText_demo',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.7], draggable: false, height: 0.08,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  movie_demo = new visual.MovieStim({
    win: psychoJS.window,
    name: 'movie_demo',
    units: psychoJS.window.units,
    movie: 'stimuli/testvideo_4s.mp4',
    pos: [0, 0],
    anchor: 'center',
    size: [1, 1],
    ori: 0.0,
    opacity: undefined,
    loop: false,
    noAudio: false,
    depth: -5
    });

  // Initialize components for Routine "confirm"
  confirmClock = new util.Clock();
  demo_confirm = new visual.TextStim({
    win: psychoJS.window,
    name: 'demo_confirm',
    text: 'If you’d like to practice rating again, press “b.”\n\nIf the instructions are clear and you’re ready to begin the task,\npress the spacebar to proceed.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.07,  wrapWidth: 1.2, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_demo = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "begintrial"
  begintrialClock = new util.Clock();
  text_begintrial = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_begintrial',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.07,  wrapWidth: 1.3, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "clip"
  clipClock = new util.Clock();
    // Run 'Begin Experiment' code from code_clip
  slider_decimals = 1;
  slideSpeed = 12;
  oldRating = 50;
  slider_width = 1;
  slider_height = 0.05;
  slider_orientation = 0;
  slider_granularity = 0.1;
  
  mouse_clip = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_clip.mouseClock = new util.Clock();
  slider_shape_clip = new visual.Rect ({
    win: psychoJS.window, name: 'slider_shape_clip', units : 'norm', 
    width: [1.5, 0.15][0], height: [1.5, 0.15][1],
    ori: 0.0, 
    pos: [0, (- 0.67)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 0.0, 
    depth: -2, 
    interpolate: true, 
  });
  
  continuousSlider_clip = new visual.Slider({
    win: psychoJS.window, name: 'continuousSlider_clip',
    startValue: undefined,
    size: [1.0, 0.1], pos: [0, (- 0.67)], ori: 0.0, units: 'norm',
    labels: ["Barely at all", "", "Strongest\nimaginable"], fontSize: 0.06, ticks: [0, 50, 100],
    granularity: 0.0, style: ["RATING"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color([0.6078, (- 0.2784), (- 0.2784)]), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Arial', bold: true, italic: false, depth: -3, 
    flip: false,
  });
  
  questionText_clip = new visual.TextStim({
    win: psychoJS.window,
    name: 'questionText_clip',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.7], draggable: false, height: 0.1,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  movie_clip = new visual.MovieStim({
    win: psychoJS.window,
    name: 'movie_clip',
    units: psychoJS.window.units,
    movie: undefined,
    pos: [0, 0],
    anchor: 'center',
    size: [1, 1],
    ori: 0.0,
    opacity: undefined,
    loop: false,
    noAudio: false,
    depth: -5
    });
  // Initialize components for Routine "attention"
  attentionClock = new util.Clock();
  mouse_atten = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_atten.mouseClock = new util.Clock();
  text_atten = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_atten',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], draggable: false, height: 0.06,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  button_A_atten = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_A_atten',
    text: 'A',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [(- 0.4), (- 0.6)],
    letterHeight: 0.05,
    size: [0.2, 0.2],
    ori: 0.0
    ,
    depth: -3
  });
  button_A_atten.clock = new util.Clock();
  
  button_B_atten = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_B_atten',
    text: 'B',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [(- 0.2), (- 0.6)],
    letterHeight: 0.05,
    size: [0.2, 0.2],
    ori: 0.0
    ,
    depth: -4
  });
  button_B_atten.clock = new util.Clock();
  
  button_C_atten = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_C_atten',
    text: 'C',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0, (- 0.6)],
    letterHeight: 0.05,
    size: [0.2, 0.2],
    ori: 0.0
    ,
    depth: -5
  });
  button_C_atten.clock = new util.Clock();
  
  button_D_atten = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_D_atten',
    text: 'D',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0.2, (- 0.6)],
    letterHeight: 0.05,
    size: [0.2, 0.2],
    ori: 0.0
    ,
    depth: -6
  });
  button_D_atten.clock = new util.Clock();
  
  button_E_atten = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_E_atten',
    text: 'E',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0.4, (- 0.6)],
    letterHeight: 0.05,
    size: [0.2, 0.2],
    ori: 0.0
    ,
    depth: -7
  });
  button_E_atten.clock = new util.Clock();
  
  // Initialize components for Routine "ratings"
  ratingsClock = new util.Clock();
  
  text_rating_intro = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_rating_intro',
    text: 'Please respond to the following questions about the previous video clip by selecting a point on the bar.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.6], draggable: false, height: 0.09,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  mouse_ratings = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_ratings.mouseClock = new util.Clock();
  text_emo_ratings = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_emo_ratings',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], draggable: false, height: 0.08,  wrapWidth: 1.2, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  continuousSlider_ratings = new visual.Slider({
    win: psychoJS.window, name: 'continuousSlider_ratings',
    startValue: undefined,
    size: [1.0, 0.1], pos: [0, (- 0.3)], ori: 0.0, units: 'norm',
    labels: ["Barely at all", "", "Strongest\nimaginable"], fontSize: 0.06, ticks: [0, 50, 100],
    granularity: 0.0, style: ["RATING"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color([0.6078, (- 0.2784), (- 0.2784)]), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Arial', bold: true, italic: false, depth: -4, 
    flip: false,
  });
  
  // Initialize components for Routine "quiz"
  quizClock = new util.Clock();
  mouse_quiz = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_quiz.mouseClock = new util.Clock();
  text_quiz = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_quiz',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], draggable: false, height: 0.06,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  button_A_quiz = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_A_quiz',
    text: 'A',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [(- 0.4), (- 0.6)],
    letterHeight: 0.05,
    size: [0.2, 0.2],
    ori: 0.0
    ,
    depth: -3
  });
  button_A_quiz.clock = new util.Clock();
  
  button_B_quiz = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_B_quiz',
    text: 'B',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [(- 0.2), (- 0.6)],
    letterHeight: 0.05,
    size: [0.2, 0.2],
    ori: 0.0
    ,
    depth: -4
  });
  button_B_quiz.clock = new util.Clock();
  
  button_C_quiz = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_C_quiz',
    text: 'C',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0, (- 0.6)],
    letterHeight: 0.05,
    size: [0.2, 0.2],
    ori: 0.0
    ,
    depth: -5
  });
  button_C_quiz.clock = new util.Clock();
  
  button_D_quiz = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_D_quiz',
    text: 'D',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0.2, (- 0.6)],
    letterHeight: 0.05,
    size: [0.2, 0.2],
    ori: 0.0
    ,
    depth: -6
  });
  button_D_quiz.clock = new util.Clock();
  
  button_E_quiz = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_E_quiz',
    text: 'E',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0.4, (- 0.6)],
    letterHeight: 0.05,
    size: [0.2, 0.2],
    ori: 0.0
    ,
    depth: -7
  });
  button_E_quiz.clock = new util.Clock();
  
  // Initialize components for Routine "real"
  realClock = new util.Clock();
  mouse_real = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_real.mouseClock = new util.Clock();
  text_real = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_real',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], draggable: false, height: 0.07,  wrapWidth: 1.4, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  real_answer = new visual.Slider({
    win: psychoJS.window, name: 'real_answer',
    startValue: undefined,
    size: [1.0, 0.1], pos: [0, (- 0.3)], ori: 0.0, units: psychoJS.window.units,
    labels: ["Strongly\ndisagree", "Disagree", "Neutral", "Agree", "Strongly\nagree"], fontSize: 0.05, ticks: [0, 25, 50, 75, 100],
    granularity: 0.0, style: ["RATING"],
    color: new util.Color('White'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Arial', bold: true, italic: false, depth: -2, 
    flip: false,
  });
  
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  text_ending = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_ending',
    text: 'The experiment is now complete.\nThank you for your participation.\nThis window will close shortly.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var consentLoop;
function consentLoopLoopBegin(consentLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    consentLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 5, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'consentLoop'
    });
    psychoJS.experiment.addLoop(consentLoop); // add the loop to the experiment
    currentLoop = consentLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisConsentLoop of consentLoop) {
      snapshot = consentLoop.getSnapshot();
      consentLoopLoopScheduler.add(importConditions(snapshot));
      consentLoopLoopScheduler.add(Consent1RoutineBegin(snapshot));
      consentLoopLoopScheduler.add(Consent1RoutineEachFrame());
      consentLoopLoopScheduler.add(Consent1RoutineEnd(snapshot));
      consentLoopLoopScheduler.add(Consent2RoutineBegin(snapshot));
      consentLoopLoopScheduler.add(Consent2RoutineEachFrame());
      consentLoopLoopScheduler.add(Consent2RoutineEnd(snapshot));
      consentLoopLoopScheduler.add(consentLoopLoopEndIteration(consentLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function consentLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(consentLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function consentLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var demoLoop;
function demoLoopLoopBegin(demoLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    demoLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 10, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'demoLoop'
    });
    psychoJS.experiment.addLoop(demoLoop); // add the loop to the experiment
    currentLoop = demoLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisDemoLoop of demoLoop) {
      snapshot = demoLoop.getSnapshot();
      demoLoopLoopScheduler.add(importConditions(snapshot));
      demoLoopLoopScheduler.add(demoRoutineBegin(snapshot));
      demoLoopLoopScheduler.add(demoRoutineEachFrame());
      demoLoopLoopScheduler.add(demoRoutineEnd(snapshot));
      demoLoopLoopScheduler.add(confirmRoutineBegin(snapshot));
      demoLoopLoopScheduler.add(confirmRoutineEachFrame());
      demoLoopLoopScheduler.add(confirmRoutineEnd(snapshot));
      demoLoopLoopScheduler.add(demoLoopLoopEndIteration(demoLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function demoLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(demoLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function demoLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trialLoop;
function trialLoopLoopBegin(trialLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trialLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'stim_positive.xlsx',
      seed: undefined, name: 'trialLoop'
    });
    psychoJS.experiment.addLoop(trialLoop); // add the loop to the experiment
    currentLoop = trialLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrialLoop of trialLoop) {
      snapshot = trialLoop.getSnapshot();
      trialLoopLoopScheduler.add(importConditions(snapshot));
      trialLoopLoopScheduler.add(begintrialRoutineBegin(snapshot));
      trialLoopLoopScheduler.add(begintrialRoutineEachFrame());
      trialLoopLoopScheduler.add(begintrialRoutineEnd(snapshot));
      trialLoopLoopScheduler.add(clipRoutineBegin(snapshot));
      trialLoopLoopScheduler.add(clipRoutineEachFrame());
      trialLoopLoopScheduler.add(clipRoutineEnd(snapshot));
      trialLoopLoopScheduler.add(attentionRoutineBegin(snapshot));
      trialLoopLoopScheduler.add(attentionRoutineEachFrame());
      trialLoopLoopScheduler.add(attentionRoutineEnd(snapshot));
      const ratingLoopLoopScheduler = new Scheduler(psychoJS);
      trialLoopLoopScheduler.add(ratingLoopLoopBegin(ratingLoopLoopScheduler, snapshot));
      trialLoopLoopScheduler.add(ratingLoopLoopScheduler);
      trialLoopLoopScheduler.add(ratingLoopLoopEnd);
      trialLoopLoopScheduler.add(quizRoutineBegin(snapshot));
      trialLoopLoopScheduler.add(quizRoutineEachFrame());
      trialLoopLoopScheduler.add(quizRoutineEnd(snapshot));
      trialLoopLoopScheduler.add(trialLoopLoopEndIteration(trialLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var ratingLoop;
function ratingLoopLoopBegin(ratingLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    ratingLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'rating_questions.xlsx',
      seed: undefined, name: 'ratingLoop'
    });
    psychoJS.experiment.addLoop(ratingLoop); // add the loop to the experiment
    currentLoop = ratingLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisRatingLoop of ratingLoop) {
      snapshot = ratingLoop.getSnapshot();
      ratingLoopLoopScheduler.add(importConditions(snapshot));
      ratingLoopLoopScheduler.add(ratingsRoutineBegin(snapshot));
      ratingLoopLoopScheduler.add(ratingsRoutineEachFrame());
      ratingLoopLoopScheduler.add(ratingsRoutineEnd(snapshot));
      ratingLoopLoopScheduler.add(ratingLoopLoopEndIteration(ratingLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function ratingLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(ratingLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function ratingLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trialLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trialLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var t;
var frameN;
var continueRoutine;
var Consent1MaxDurationReached;
var _key_consent1_allKeys;
var Consent1MaxDuration;
var Consent1Components;
function Consent1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Consent1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Consent1Clock.reset();
    routineTimer.reset();
    Consent1MaxDurationReached = false;
    // update component parameters for each repeat
    key_consent1.keys = undefined;
    key_consent1.rt = undefined;
    _key_consent1_allKeys = [];
    // Tracking the screen size
    const [screenWidth, screenHeight] = psychoJS.window.size;
    // console.log(`Screen width: ${screenWidth}, Screen height: ${screenHeight}`);
    psychoJS.experiment.addData('screenWidth', screenWidth);
    psychoJS.experiment.addData('screenHeight', screenHeight);
    psychoJS.experiment.addData('Consent1.started', globalClock.getTime());
    Consent1MaxDuration = null
    // keep track of which components have finished
    Consent1Components = [];
    Consent1Components.push(consent_1);
    Consent1Components.push(key_consent1);
    
    for (const thisComponent of Consent1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Consent1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Consent1' ---
    // get current time
    t = Consent1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *consent_1* updates
    if (t >= 0.0 && consent_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consent_1.tStart = t;  // (not accounting for frame time here)
      consent_1.frameNStart = frameN;  // exact frame index
      
      consent_1.setAutoDraw(true);
    }
    
    
    // *key_consent1* updates
    if (t >= 0 && key_consent1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_consent1.tStart = t;  // (not accounting for frame time here)
      key_consent1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_consent1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_consent1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_consent1.clearEvents(); });
    }
    
    if (key_consent1.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_consent1.getKeys({keyList: ['space'], waitRelease: false});
      _key_consent1_allKeys = _key_consent1_allKeys.concat(theseKeys);
      if (_key_consent1_allKeys.length > 0) {
        key_consent1.keys = _key_consent1_allKeys[_key_consent1_allKeys.length - 1].name;  // just the last key pressed
        key_consent1.rt = _key_consent1_allKeys[_key_consent1_allKeys.length - 1].rt;
        key_consent1.duration = _key_consent1_allKeys[_key_consent1_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Consent1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Consent1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Consent1' ---
    for (const thisComponent of Consent1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Consent1.stopped', globalClock.getTime());
    key_consent1.stop();
    // the Routine "Consent1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Consent2MaxDurationReached;
var _key_consent2_allKeys;
var Consent2MaxDuration;
var Consent2Components;
function Consent2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Consent2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Consent2Clock.reset();
    routineTimer.reset();
    Consent2MaxDurationReached = false;
    // update component parameters for each repeat
    key_consent2.keys = undefined;
    key_consent2.rt = undefined;
    _key_consent2_allKeys = [];
    psychoJS.experiment.addData('Consent2.started', globalClock.getTime());
    Consent2MaxDuration = null
    // keep track of which components have finished
    Consent2Components = [];
    Consent2Components.push(consent_2);
    Consent2Components.push(key_consent2);
    
    for (const thisComponent of Consent2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Consent2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Consent2' ---
    // get current time
    t = Consent2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *consent_2* updates
    if (t >= 0.0 && consent_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consent_2.tStart = t;  // (not accounting for frame time here)
      consent_2.frameNStart = frameN;  // exact frame index
      
      consent_2.setAutoDraw(true);
    }
    
    
    // *key_consent2* updates
    if (t >= 0 && key_consent2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_consent2.tStart = t;  // (not accounting for frame time here)
      key_consent2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_consent2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_consent2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_consent2.clearEvents(); });
    }
    
    if (key_consent2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_consent2.getKeys({keyList: ['space', 'b'], waitRelease: false});
      _key_consent2_allKeys = _key_consent2_allKeys.concat(theseKeys);
      if (_key_consent2_allKeys.length > 0) {
        key_consent2.keys = _key_consent2_allKeys[_key_consent2_allKeys.length - 1].name;  // just the last key pressed
        key_consent2.rt = _key_consent2_allKeys[_key_consent2_allKeys.length - 1].rt;
        key_consent2.duration = _key_consent2_allKeys[_key_consent2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Consent2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Consent2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Consent2' ---
    for (const thisComponent of Consent2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Consent2.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_consent
    if ((key_consent2.keys === "space")) {
        consentLoop.finished = true;
    }
    
    key_consent2.stop();
    // the Routine "Consent2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var IntroMaxDurationReached;
var _key_intro_allKeys;
var IntroMaxDuration;
var IntroComponents;
function IntroRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Intro' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    IntroClock.reset();
    routineTimer.reset();
    IntroMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_intro
    
    key_intro.keys = undefined;
    key_intro.rt = undefined;
    _key_intro_allKeys = [];
    // Tracking the screen size
    const [screenWidth, screenHeight] = psychoJS.window.size;
    psychoJS.experiment.addData('screenWidth', screenWidth);
    psychoJS.experiment.addData('screenHeight', screenHeight);
    psychoJS.experiment.addData('Intro.started', globalClock.getTime());
    IntroMaxDuration = null
    // keep track of which components have finished
    IntroComponents = [];
    IntroComponents.push(text_intro);
    IntroComponents.push(key_intro);
    
    for (const thisComponent of IntroComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function IntroRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Intro' ---
    // get current time
    t = IntroClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_intro* updates
    if (t >= 0.0 && text_intro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_intro.tStart = t;  // (not accounting for frame time here)
      text_intro.frameNStart = frameN;  // exact frame index
      
      text_intro.setAutoDraw(true);
    }
    
    
    // *key_intro* updates
    if (t >= 0 && key_intro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_intro.tStart = t;  // (not accounting for frame time here)
      key_intro.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_intro.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_intro.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_intro.clearEvents(); });
    }
    
    if (key_intro.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_intro.getKeys({keyList: ['space'], waitRelease: false});
      _key_intro_allKeys = _key_intro_allKeys.concat(theseKeys);
      if (_key_intro_allKeys.length > 0) {
        key_intro.keys = _key_intro_allKeys[_key_intro_allKeys.length - 1].name;  // just the last key pressed
        key_intro.rt = _key_intro_allKeys[_key_intro_allKeys.length - 1].rt;
        key_intro.duration = _key_intro_allKeys[_key_intro_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of IntroComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function IntroRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Intro' ---
    for (const thisComponent of IntroComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Intro.stopped', globalClock.getTime());
    key_intro.stop();
    // the Routine "Intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var demoMaxDurationReached;
var thisFrame;
var slider_data;
var mouseRec;
var audioStopped;
var mouseInSlider;
var gotValidClick;
var demoMaxDuration;
var demoComponents;
var demo_text;

function demoRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'demo' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    demoClock.reset();
    routineTimer.reset();
    demoMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_demo
    thisFrame = 0;
    slider_data = [];
    mouseRec = mouse_demo.getPos();
    audioStopped = false;
    mouseInSlider = false;
    
    // setup some python lists for storing info about the mouse_demo
    gotValidClick = false; // until a click is received
    continuousSlider_demo.reset()
    questionText_demo.setText(demo_text);
    // Tracking the screen size
    const [screenWidth, screenHeight] = psychoJS.window.size;
    psychoJS.experiment.addData('screenWidth', screenWidth);
    psychoJS.experiment.addData('screenHeight', screenHeight);
    psychoJS.experiment.addData('demo.started', globalClock.getTime());
    demoMaxDuration = null
    // keep track of which components have finished
    demoComponents = [];
    demoComponents.push(mouse_demo);
    demoComponents.push(slider_shape_demo);
    demoComponents.push(continuousSlider_demo);
    demoComponents.push(questionText_demo);
    demoComponents.push(movie_demo);
    
    for (const thisComponent of demoComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function demoRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'demo' ---
    // get current time
    t = demoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_demo
    if ((slider_shape_demo.contains(mouse_demo) && (! mouseInSlider))) {
        mouseInSlider = true;
    }
    if ((slider_shape_demo.contains(mouse_demo) && mouseInSlider)) {
        if ((mouse_demo.getPos()[slider_orientation] !== mouseRec[slider_orientation])) {
            mouseRec = mouse_demo.getPos();
            continuousSlider_demo.markerPos = (((mouseRec[slider_orientation] / slider_width) * 100) + (100 / 2));
        }
        if (continuousSlider_demo.markerPos) {
            if ((oldRating !== continuousSlider_demo.markerPos)) {
                oldRating = continuousSlider_demo.markerPos;
            }
        }
        if ((continuousSlider_demo.markerPos && ((thisFrame % slideSpeed) === 0))) {
            slider_data.push([util.round(oldRating, slider_decimals), Number.parseInt((t * 1000))]);
        }
    }
    thisFrame = (thisFrame + 1);
    
    
    // *slider_shape_demo* updates
    if (t >= 0.0 && slider_shape_demo.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_shape_demo.tStart = t;  // (not accounting for frame time here)
      slider_shape_demo.frameNStart = frameN;  // exact frame index
      
      slider_shape_demo.setAutoDraw(true);
    }
    
    
    // *continuousSlider_demo* updates
    if (t >= 0.0 && continuousSlider_demo.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continuousSlider_demo.tStart = t;  // (not accounting for frame time here)
      continuousSlider_demo.frameNStart = frameN;  // exact frame index
      
      continuousSlider_demo.setAutoDraw(true);
    }
    
    
    // *questionText_demo* updates
    if (t >= 0.0 && questionText_demo.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      questionText_demo.tStart = t;  // (not accounting for frame time here)
      questionText_demo.frameNStart = frameN;  // exact frame index
      
      questionText_demo.setAutoDraw(true);
    }
    
    
    // *movie_demo* updates
    if (t >= 0.0 && movie_demo.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      movie_demo.tStart = t;  // (not accounting for frame time here)
      movie_demo.frameNStart = frameN;  // exact frame index
      
      movie_demo.setAutoDraw(true);
      movie_demo.play();
    }
    
    if (movie_demo.status === PsychoJS.Status.FINISHED) {  // force-end the Routine
        continueRoutine = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of demoComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function demoRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'demo' ---
    for (const thisComponent of demoComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('demo.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_demo
    psychoJS.experiment.addData("continuousrating_demo", slider_data);
    
    // store data for psychoJS.experiment (ExperimentHandler)
    movie_demo.stop();  // ensure movie has stopped at end of Routine
    // the Routine "demo" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var confirmMaxDurationReached;
var _key_demo_allKeys;
var confirmMaxDuration;
var confirmComponents;
function confirmRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'confirm' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    confirmClock.reset();
    routineTimer.reset();
    confirmMaxDurationReached = false;
    // update component parameters for each repeat
    key_demo.keys = undefined;
    key_demo.rt = undefined;
    _key_demo_allKeys = [];
    psychoJS.experiment.addData('confirm.started', globalClock.getTime());
    confirmMaxDuration = null
    // keep track of which components have finished
    confirmComponents = [];
    confirmComponents.push(demo_confirm);
    confirmComponents.push(key_demo);
    
    for (const thisComponent of confirmComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function confirmRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'confirm' ---
    // get current time
    t = confirmClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *demo_confirm* updates
    if (t >= 0.0 && demo_confirm.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demo_confirm.tStart = t;  // (not accounting for frame time here)
      demo_confirm.frameNStart = frameN;  // exact frame index
      
      demo_confirm.setAutoDraw(true);
    }
    
    
    // *key_demo* updates
    if (t >= 0.0 && key_demo.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_demo.tStart = t;  // (not accounting for frame time here)
      key_demo.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_demo.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_demo.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_demo.clearEvents(); });
    }
    
    if (key_demo.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_demo.getKeys({keyList: ['space', 'b'], waitRelease: false});
      _key_demo_allKeys = _key_demo_allKeys.concat(theseKeys);
      if (_key_demo_allKeys.length > 0) {
        key_demo.keys = _key_demo_allKeys[_key_demo_allKeys.length - 1].name;  // just the last key pressed
        key_demo.rt = _key_demo_allKeys[_key_demo_allKeys.length - 1].rt;
        key_demo.duration = _key_demo_allKeys[_key_demo_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of confirmComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function confirmRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'confirm' ---
    for (const thisComponent of confirmComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('confirm.stopped', globalClock.getTime());

    // Run 'End Routine' code from code_consent
    if ((key_demo.keys === "space")) {
      demoLoop.finished = true;
    }

    key_demo.stop();
    // the Routine "confirm" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var begintrialMaxDurationReached;
var _key_resp_allKeys;
var begintrialMaxDuration;
var begintrialComponents;
var cont_emotion_que;

function begintrialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'begintrial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    begintrialClock.reset();
    routineTimer.reset();
    begintrialMaxDurationReached = false;
    // update component parameters for each repeat
    trial_start_text = 
    "Movie clip " + TrialN + " of 9 is about to start.\n\n" +
    "If you need a break before the next video,\nplease take a moment now.\n\n" +
    "It is crucial to focus on both the video\nand the continuous rating as the movie plays!\n\n" +
    "When you're ready, press the spacebar to begin.";
    text_begintrial.setText(trial_start_text);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // Tracking the screen size
    const [screenWidth, screenHeight] = psychoJS.window.size;
    psychoJS.experiment.addData('screenWidth', screenWidth);
    psychoJS.experiment.addData('screenHeight', screenHeight);
    psychoJS.experiment.addData('begintrial.started', globalClock.getTime());
    begintrialMaxDuration = null
    // keep track of which components have finished
    begintrialComponents = [];
    begintrialComponents.push(text_begintrial);
    begintrialComponents.push(key_resp);
    
    for (const thisComponent of begintrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function begintrialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'begintrial' ---
    // get current time
    t = begintrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_begintrial* updates
    if (t >= 0.0 && text_begintrial.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_begintrial.tStart = t;  // (not accounting for frame time here)
      text_begintrial.frameNStart = frameN;  // exact frame index
      
      text_begintrial.setAutoDraw(true);
    }
    
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of begintrialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function begintrialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'begintrial' ---
    for (const thisComponent of begintrialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('begintrial.stopped', globalClock.getTime());
    key_resp.stop();
    // the Routine "begintrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var clipMaxDurationReached;
var clipMaxDuration;
var clipComponents;
var cont_emotion_que;
function clipRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'clip' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    clipClock.reset();
    routineTimer.reset();
    clipMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_clip
    thisFrame = 0;
    slider_data = [];
    mouseRec = mouse_clip.getPos();
    audioStopped = false;
    mouseInSlider = false;
    // setup some python lists for storing info about the mouse_clip
    gotValidClick = false; // until a click is received
    continuousSlider_clip.reset()
    questionText_clip.setText(cont_emotion_que);
    movie_clip.setMovie(clip_stim);
    psychoJS.experiment.addData('clip.started', globalClock.getTime());
    // Tracking the screen size
    const [screenWidth, screenHeight] = psychoJS.window.size;
    psychoJS.experiment.addData('screenWidth', screenWidth);
    psychoJS.experiment.addData('screenHeight', screenHeight);
    clipMaxDuration = null
    // keep track of which components have finished
    clipComponents = [];
    clipComponents.push(mouse_clip);
    clipComponents.push(slider_shape_clip);
    clipComponents.push(continuousSlider_clip);
    clipComponents.push(questionText_clip);
    clipComponents.push(movie_clip);
    
    for (const thisComponent of clipComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function clipRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'clip' ---
    // get current time
    t = clipClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_clip
    if ((slider_shape_clip.contains(mouse_clip) && (! mouseInSlider))) {
      mouseInSlider = true;
  }
  if ((slider_shape_clip.contains(mouse_clip) && mouseInSlider)) {
      if ((mouse_clip.getPos()[slider_orientation] !== mouseRec[slider_orientation])) {
          mouseRec = mouse_clip.getPos();
          continuousSlider_clip.markerPos = (((mouseRec[slider_orientation] / slider_width) * 100) + (100 / 2));
      }
      if (continuousSlider_clip.markerPos) {
          if ((oldRating !== continuousSlider_clip.markerPos)) {
              oldRating = continuousSlider_clip.markerPos;
          }
      }
      if ((continuousSlider_clip.markerPos && ((thisFrame % slideSpeed) === 0))) {
          slider_data.push([util.round(oldRating, slider_decimals), Number.parseInt((t * 1000))]);
        }
    }
    thisFrame = (thisFrame + 1);

    
    // *slider_shape_clip* updates
    if (t >= 0.0 && slider_shape_clip.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_shape_clip.tStart = t;  // (not accounting for frame time here)
      slider_shape_clip.frameNStart = frameN;  // exact frame index
      
      slider_shape_clip.setAutoDraw(true);
    }
    
    
    // *continuousSlider_clip* updates
    if (t >= 0.0 && continuousSlider_clip.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continuousSlider_clip.tStart = t;  // (not accounting for frame time here)
      continuousSlider_clip.frameNStart = frameN;  // exact frame index
      
      continuousSlider_clip.setAutoDraw(true);
    }
    
    
    // *questionText_clip* updates
    if (t >= 0.0 && questionText_clip.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      questionText_clip.tStart = t;  // (not accounting for frame time here)
      questionText_clip.frameNStart = frameN;  // exact frame index
      
      questionText_clip.setAutoDraw(true);
    }
    
    
    // *movie_clip* updates
    if (t >= 0.0 && movie_clip.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      movie_clip.tStart = t;  // (not accounting for frame time here)
      movie_clip.frameNStart = frameN;  // exact frame index
      
      movie_clip.setAutoDraw(true);
      movie_clip.play();
    }
    
    // Don't know the reason but the following lines didn't work.
    // if (movie_clip.status === PsychoJS.Status.FINISHED) {  // force-end the Routine
    //     continueRoutine = false;
    // }

    // console.log("Video duration:", movie_clip._movie.duration);
    // console.log("t:", t);
    // console.log("movie_clip.tStart:", movie_clip.tStart);

    // Byeol added this if loop to stop the video once it has played to the end.
    if (t >= (movie_clip._movie.duration + movie_clip.tStart) && movie_clip.status === PsychoJS.Status.STARTED) {
        continueRoutine = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of clipComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function clipRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'clip' ---
    for (const thisComponent of clipComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('clip.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_clip
    psychoJS.experiment.addData("continuousrating", slider_data);
    
    // store data for psychoJS.experiment (ExperimentHandler)
    movie_clip.stop();  // ensure movie has stopped at end of Routine
    // the Routine "clip" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var attentionMaxDurationReached;
var button;
var attentionMaxDuration;
var attentionComponents;
function attentionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'attention' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    attentionClock.reset();
    routineTimer.reset();
    attentionMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_atten
    button = 0;
    text_atten.setAlignHoriz('left');
    
    // setup some python lists for storing info about the mouse_atten
    gotValidClick = false; // until a click is received
    text_atten.setText(attention_ques);
    // reset button_A_atten to account for continued clicks & clear times on/off
    button_A_atten.reset()
    // reset button_B_atten to account for continued clicks & clear times on/off
    button_B_atten.reset()
    // reset button_C_atten to account for continued clicks & clear times on/off
    button_C_atten.reset()
    // reset button_D_atten to account for continued clicks & clear times on/off
    button_D_atten.reset()
    // reset button_E_atten to account for continued clicks & clear times on/off
    button_E_atten.reset()
    psychoJS.experiment.addData('attention.started', globalClock.getTime());
    // Tracking the screen size
    const [screenWidth, screenHeight] = psychoJS.window.size;
    psychoJS.experiment.addData('screenWidth', screenWidth);
    psychoJS.experiment.addData('screenHeight', screenHeight);
    attentionMaxDuration = null
    // keep track of which components have finished
    attentionComponents = [];
    attentionComponents.push(mouse_atten);
    attentionComponents.push(text_atten);
    attentionComponents.push(button_A_atten);
    attentionComponents.push(button_B_atten);
    attentionComponents.push(button_C_atten);
    attentionComponents.push(button_D_atten);
    attentionComponents.push(button_E_atten);
    
    for (const thisComponent of attentionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var button_atten;
function attentionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'attention' ---
    // get current time
    t = attentionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_atten* updates
    if (t >= 0.0 && text_atten.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_atten.tStart = t;  // (not accounting for frame time here)
      text_atten.frameNStart = frameN;  // exact frame index
      
      text_atten.setAutoDraw(true);
    }
    
    
    // *button_A_atten* updates
    if (t >= 0 && button_A_atten.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_A_atten.tStart = t;  // (not accounting for frame time here)
      button_A_atten.frameNStart = frameN;  // exact frame index
      
      button_A_atten.setAutoDraw(true);
    }
    
    if (button_A_atten.status === PsychoJS.Status.STARTED) {
      // check whether button_A_atten has been pressed
      if (button_A_atten.isClicked) {
        if (!button_A_atten.wasClicked) {
          // store time of first click
          button_A_atten.timesOn.push(button_A_atten.clock.getTime());
          // store time clicked until
          button_A_atten.timesOff.push(button_A_atten.clock.getTime());
          // Byeol: you need this part here not later
          // end routine when button_A_atten is clicked
          continueRoutine = false;
          button_atten = 1;
        } else {
          // update time clicked until;
          button_A_atten.timesOff[button_A_atten.timesOff.length - 1] = button_A_atten.clock.getTime();
        }
        // Byeol: the following part came from the autotranslation, but doesn't work
        // if (!button_A_atten.wasClicked) {
        //   // end routine when button_A_atten is clicked
        //   continueRoutine = false;
        //   var button_atten;
        //   button_atten = 1;
        // }
        // if button_A_atten is still clicked next frame, it is not a new click
        button_A_atten.wasClicked = true;
      } else {
        // if button_A_atten is clicked next frame, it is a new click
        button_A_atten.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_A_atten hasn't started / has finished
      button_A_atten.clock.reset();
      // if button_A_atten is clicked next frame, it is a new click
      button_A_atten.wasClicked = false;
    }
    
    // *button_B_atten* updates
    if (t >= 0 && button_B_atten.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_B_atten.tStart = t;  // (not accounting for frame time here)
      button_B_atten.frameNStart = frameN;  // exact frame index
      
      button_B_atten.setAutoDraw(true);
    }
    
    if (button_B_atten.status === PsychoJS.Status.STARTED) {
      // check whether button_B_atten has been pressed
      if (button_B_atten.isClicked) {
        if (!button_B_atten.wasClicked) {
          // store time of first click
          button_B_atten.timesOn.push(button_B_atten.clock.getTime());
          // store time clicked until
          button_B_atten.timesOff.push(button_B_atten.clock.getTime());
          // end routine when button_A_atten is clicked
          continueRoutine = false;
          button_atten = 2;
        } else {
          // update time clicked until;
          button_B_atten.timesOff[button_B_atten.timesOff.length - 1] = button_B_atten.clock.getTime();
        }
        // if button_B_atten is still clicked next frame, it is not a new click
        button_B_atten.wasClicked = true;
      } else {
        // if button_B_atten is clicked next frame, it is a new click
        button_B_atten.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_B_atten hasn't started / has finished
      button_B_atten.clock.reset();
      // if button_B_atten is clicked next frame, it is a new click
      button_B_atten.wasClicked = false;
    }
    
    // *button_C_atten* updates
    if (t >= 0 && button_C_atten.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_C_atten.tStart = t;  // (not accounting for frame time here)
      button_C_atten.frameNStart = frameN;  // exact frame index
      
      button_C_atten.setAutoDraw(true);
    }
    
    if (button_C_atten.status === PsychoJS.Status.STARTED) {
      // check whether button_C_atten has been pressed
      if (button_C_atten.isClicked) {
        if (!button_C_atten.wasClicked) {
          // store time of first click
          button_C_atten.timesOn.push(button_C_atten.clock.getTime());
          // store time clicked until
          button_C_atten.timesOff.push(button_C_atten.clock.getTime());
          // end routine when button_A_atten is clicked
          continueRoutine = false;
          button_atten = 3;
        } else {
          // update time clicked until;
          button_C_atten.timesOff[button_C_atten.timesOff.length - 1] = button_C_atten.clock.getTime();
        }
        // if button_C_atten is still clicked next frame, it is not a new click
        button_C_atten.wasClicked = true;
      } else {
        // if button_C_atten is clicked next frame, it is a new click
        button_C_atten.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_C_atten hasn't started / has finished
      button_C_atten.clock.reset();
      // if button_C_atten is clicked next frame, it is a new click
      button_C_atten.wasClicked = false;
    }
    
    // *button_D_atten* updates
    if (t >= 0 && button_D_atten.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_D_atten.tStart = t;  // (not accounting for frame time here)
      button_D_atten.frameNStart = frameN;  // exact frame index
      
      button_D_atten.setAutoDraw(true);
    }
    
    if (button_D_atten.status === PsychoJS.Status.STARTED) {
      // check whether button_D_atten has been pressed
      if (button_D_atten.isClicked) {
        if (!button_D_atten.wasClicked) {
          // store time of first click
          button_D_atten.timesOn.push(button_D_atten.clock.getTime());
          // store time clicked until
          button_D_atten.timesOff.push(button_D_atten.clock.getTime());
          // end routine when button_A_atten is clicked
          continueRoutine = false;
          button_atten = 4;
        } else {
          // update time clicked until;
          button_D_atten.timesOff[button_D_atten.timesOff.length - 1] = button_D_atten.clock.getTime();
        }
        // if button_D_atten is still clicked next frame, it is not a new click
        button_D_atten.wasClicked = true;
      } else {
        // if button_D_atten is clicked next frame, it is a new click
        button_D_atten.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_D_atten hasn't started / has finished
      button_D_atten.clock.reset();
      // if button_D_atten is clicked next frame, it is a new click
      button_D_atten.wasClicked = false;
    }
    
    // *button_E_atten* updates
    if (t >= 0 && button_E_atten.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_E_atten.tStart = t;  // (not accounting for frame time here)
      button_E_atten.frameNStart = frameN;  // exact frame index
      
      button_E_atten.setAutoDraw(true);
    }
    
    if (button_E_atten.status === PsychoJS.Status.STARTED) {
      // check whether button_E_atten has been pressed
      if (button_E_atten.isClicked) {
        if (!button_E_atten.wasClicked) {
          // store time of first click
          button_E_atten.timesOn.push(button_E_atten.clock.getTime());
          // store time clicked until
          button_E_atten.timesOff.push(button_E_atten.clock.getTime());
          // end routine when button_A_atten is clicked
          continueRoutine = false;
          button_atten = 5;
        } else {
          // update time clicked until;
          button_E_atten.timesOff[button_E_atten.timesOff.length - 1] = button_E_atten.clock.getTime();
        }
        // if button_E_atten is still clicked next frame, it is not a new click
        button_E_atten.wasClicked = true;
      } else {
        // if button_E_atten is clicked next frame, it is a new click
        button_E_atten.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_E_atten hasn't started / has finished
      button_E_atten.clock.reset();
      // if button_E_atten is clicked next frame, it is a new click
      button_E_atten.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of attentionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function attentionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'attention' ---
    for (const thisComponent of attentionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('attention.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    // psychoJS.experiment.addData('button_A_atten.numClicks', button_A_atten.numClicks);
    // psychoJS.experiment.addData('button_A_atten.timesOn', button_A_atten.timesOn);
    // psychoJS.experiment.addData('button_A_atten.timesOff', button_A_atten.timesOff);
    // psychoJS.experiment.addData('button_B_atten.numClicks', button_B_atten.numClicks);
    // psychoJS.experiment.addData('button_B_atten.timesOn', button_B_atten.timesOn);
    // psychoJS.experiment.addData('button_B_atten.timesOff', button_B_atten.timesOff);
    // psychoJS.experiment.addData('button_C_atten.numClicks', button_C_atten.numClicks);
    // psychoJS.experiment.addData('button_C_atten.timesOn', button_C_atten.timesOn);
    // psychoJS.experiment.addData('button_C_atten.timesOff', button_C_atten.timesOff);
    // psychoJS.experiment.addData('button_D_atten.numClicks', button_D_atten.numClicks);
    // psychoJS.experiment.addData('button_D_atten.timesOn', button_D_atten.timesOn);
    // psychoJS.experiment.addData('button_D_atten.timesOff', button_D_atten.timesOff);
    // psychoJS.experiment.addData('button_E_atten.numClicks', button_E_atten.numClicks);
    // psychoJS.experiment.addData('button_E_atten.timesOn', button_E_atten.timesOn);
    // psychoJS.experiment.addData('button_E_atten.timesOff', button_E_atten.timesOff);
    psychoJS.experiment.addData('atten_response', button_atten);
    if (button_atten === atten_answer) {
      isAnswerCorrect = 1;
    } else {
      isAnswerCorrect = 0;
    }    
    psychoJS.experiment.addData('atten_pass', isAnswerCorrect);
    // the Routine "attention" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ratingsMaxDurationReached;
var ratingsMaxDuration;
var ratingsComponents;
function ratingsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ratings' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    ratingsClock.reset();
    routineTimer.reset();
    ratingsMaxDurationReached = false;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_ratings
    gotValidClick = false; // until a click is received
    mouse_ratings.mouseClock.reset();
    text_emo_ratings.setText(rating_ques);
    continuousSlider_ratings.reset()
    psychoJS.experiment.addData('ratings.started', globalClock.getTime());
    ratingsMaxDuration = null
    // keep track of which components have finished
    ratingsComponents = [];
    ratingsComponents.push(text_rating_intro);
    ratingsComponents.push(mouse_ratings);
    ratingsComponents.push(text_emo_ratings);
    ratingsComponents.push(continuousSlider_ratings);
    
    for (const thisComponent of ratingsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ratingsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ratings' ---
    // get current time
    t = ratingsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_rating_intro* updates
    if (t >= 0.0 && text_rating_intro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_rating_intro.tStart = t;  // (not accounting for frame time here)
      text_rating_intro.frameNStart = frameN;  // exact frame index
      
      text_rating_intro.setAutoDraw(true);
    }
    
    
    // *text_emo_ratings* updates
    if (t >= 0.5 && text_emo_ratings.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_emo_ratings.tStart = t;  // (not accounting for frame time here)
      text_emo_ratings.frameNStart = frameN;  // exact frame index
      
      text_emo_ratings.setAutoDraw(true);
    }
    
    
    // *continuousSlider_ratings* updates
    if (t >= 0.5 && continuousSlider_ratings.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continuousSlider_ratings.tStart = t;  // (not accounting for frame time here)
      continuousSlider_ratings.frameNStart = frameN;  // exact frame index
      
      continuousSlider_ratings.setAutoDraw(true);
    }
    
    
    // Check continuousSlider_ratings for response to end Routine
    if (continuousSlider_ratings.getRating() !== undefined && continuousSlider_ratings.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ratingsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ratingsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ratings' ---
    for (const thisComponent of ratingsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ratings.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('continuousSlider_ratings.response', continuousSlider_ratings.getRating());
    psychoJS.experiment.addData('continuousSlider_ratings.rt', continuousSlider_ratings.getRT());
    // the Routine "ratings" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var quizMaxDurationReached;
var button;
var quizMaxDuration;
var quizComponents;
function quizRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'quiz' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    quizClock.reset();
    routineTimer.reset();
    quizMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_quiz
    button = 0;
    text_quiz.setAlignHoriz('left');
    
    // setup some python lists for storing info about the mouse_quiz
    gotValidClick = false; // until a click is received
    mouse_quiz.mouseClock.reset();
    text_quiz.setText(compre_ques);
    // reset button_A_quiz to account for continued clicks & clear times on/off
    button_A_quiz.reset()
    // reset button_B_quiz to account for continued clicks & clear times on/off
    button_B_quiz.reset()
    // reset button_C_quiz to account for continued clicks & clear times on/off
    button_C_quiz.reset()
    // reset button_D_quiz to account for continued clicks & clear times on/off
    button_D_quiz.reset()
    // reset button_E_quiz to account for continued clicks & clear times on/off
    button_E_quiz.reset()
    psychoJS.experiment.addData('quiz.started', globalClock.getTime());
    // Tracking the screen size
    const [screenWidth, screenHeight] = psychoJS.window.size;
    psychoJS.experiment.addData('screenWidth', screenWidth);
    psychoJS.experiment.addData('screenHeight', screenHeight);
    quizMaxDuration = null
    // keep track of which components have finished
    quizComponents = [];
    quizComponents.push(mouse_quiz);
    quizComponents.push(text_quiz);
    quizComponents.push(button_A_quiz);
    quizComponents.push(button_B_quiz);
    quizComponents.push(button_C_quiz);
    quizComponents.push(button_D_quiz);
    quizComponents.push(button_E_quiz);
    
    for (const thisComponent of quizComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function quizRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'quiz' ---
    // get current time
    t = quizClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_quiz* updates
    if (t >= 0.0 && text_quiz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_quiz.tStart = t;  // (not accounting for frame time here)
      text_quiz.frameNStart = frameN;  // exact frame index
      
      text_quiz.setAutoDraw(true);
    }
    
    
    // *button_A_quiz* updates
    if (t >= 0 && button_A_quiz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_A_quiz.tStart = t;  // (not accounting for frame time here)
      button_A_quiz.frameNStart = frameN;  // exact frame index
      
      button_A_quiz.setAutoDraw(true);
    }
    
    if (button_A_quiz.status === PsychoJS.Status.STARTED) {
      // check whether button_A_quiz has been pressed
      if (button_A_quiz.isClicked) {
        if (!button_A_quiz.wasClicked) {
          // store time of first click
          button_A_quiz.timesOn.push(button_A_quiz.clock.getTime());
          // store time clicked until
          button_A_quiz.timesOff.push(button_A_quiz.clock.getTime());
          // end routine when button_A_quiz is clicked
          continueRoutine = false;
          button = 1;  
        } else {
          // update time clicked until;
          button_A_quiz.timesOff[button_A_quiz.timesOff.length - 1] = button_A_quiz.clock.getTime();
        }
        // if button_A_quiz is still clicked next frame, it is not a new click
        button_A_quiz.wasClicked = true;
      } else {
        // if button_A_quiz is clicked next frame, it is a new click
        button_A_quiz.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_A_quiz hasn't started / has finished
      button_A_quiz.clock.reset();
      // if button_A_quiz is clicked next frame, it is a new click
      button_A_quiz.wasClicked = false;
    }
    
    // *button_B_quiz* updates
    if (t >= 0 && button_B_quiz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_B_quiz.tStart = t;  // (not accounting for frame time here)
      button_B_quiz.frameNStart = frameN;  // exact frame index
      
      button_B_quiz.setAutoDraw(true);
    }
    
    if (button_B_quiz.status === PsychoJS.Status.STARTED) {
      // check whether button_B_quiz has been pressed
      if (button_B_quiz.isClicked) {
        if (!button_B_quiz.wasClicked) {
          // store time of first click
          button_B_quiz.timesOn.push(button_B_quiz.clock.getTime());
          // store time clicked until
          button_B_quiz.timesOff.push(button_B_quiz.clock.getTime());
          // end routine when button_B_quiz is clicked
          continueRoutine = false;
          button = 2; 
        } else {
          // update time clicked until;
          button_B_quiz.timesOff[button_B_quiz.timesOff.length - 1] = button_B_quiz.clock.getTime();
        }
        // if button_B_quiz is still clicked next frame, it is not a new click
        button_B_quiz.wasClicked = true;
      } else {
        // if button_B_quiz is clicked next frame, it is a new click
        button_B_quiz.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_B_quiz hasn't started / has finished
      button_B_quiz.clock.reset();
      // if button_B_quiz is clicked next frame, it is a new click
      button_B_quiz.wasClicked = false;
    }
    
    // *button_C_quiz* updates
    if (t >= 0 && button_C_quiz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_C_quiz.tStart = t;  // (not accounting for frame time here)
      button_C_quiz.frameNStart = frameN;  // exact frame index
      
      button_C_quiz.setAutoDraw(true);
    }
    
    if (button_C_quiz.status === PsychoJS.Status.STARTED) {
      // check whether button_C_quiz has been pressed
      if (button_C_quiz.isClicked) {
        if (!button_C_quiz.wasClicked) {
          // store time of first click
          button_C_quiz.timesOn.push(button_C_quiz.clock.getTime());
          // store time clicked until
          button_C_quiz.timesOff.push(button_C_quiz.clock.getTime());
          // end routine when button_C_quiz is clicked
          continueRoutine = false;
          button = 3;     
        } else {
          // update time clicked until;
          button_C_quiz.timesOff[button_C_quiz.timesOff.length - 1] = button_C_quiz.clock.getTime();
        }
        // if button_C_quiz is still clicked next frame, it is not a new click
        button_C_quiz.wasClicked = true;
      } else {
        // if button_C_quiz is clicked next frame, it is a new click
        button_C_quiz.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_C_quiz hasn't started / has finished
      button_C_quiz.clock.reset();
      // if button_C_quiz is clicked next frame, it is a new click
      button_C_quiz.wasClicked = false;
    }
    
    // *button_D_quiz* updates
    if (t >= 0 && button_D_quiz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_D_quiz.tStart = t;  // (not accounting for frame time here)
      button_D_quiz.frameNStart = frameN;  // exact frame index
      
      button_D_quiz.setAutoDraw(true);
    }
    
    if (button_D_quiz.status === PsychoJS.Status.STARTED) {
      // check whether button_D_quiz has been pressed
      if (button_D_quiz.isClicked) {
        if (!button_D_quiz.wasClicked) {
          // store time of first click
          button_D_quiz.timesOn.push(button_D_quiz.clock.getTime());
          // store time clicked until
          button_D_quiz.timesOff.push(button_D_quiz.clock.getTime());
          // end routine when button_D_quiz is clicked
          continueRoutine = false;
          button = 4;
        } else {
          // update time clicked until;
          button_D_quiz.timesOff[button_D_quiz.timesOff.length - 1] = button_D_quiz.clock.getTime();
        }
        // if button_D_quiz is still clicked next frame, it is not a new click
        button_D_quiz.wasClicked = true;
      } else {
        // if button_D_quiz is clicked next frame, it is a new click
        button_D_quiz.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_D_quiz hasn't started / has finished
      button_D_quiz.clock.reset();
      // if button_D_quiz is clicked next frame, it is a new click
      button_D_quiz.wasClicked = false;
    }
    
    // *button_E_quiz* updates
    if (t >= 0 && button_E_quiz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_E_quiz.tStart = t;  // (not accounting for frame time here)
      button_E_quiz.frameNStart = frameN;  // exact frame index
      
      button_E_quiz.setAutoDraw(true);
    }
    
    if (button_E_quiz.status === PsychoJS.Status.STARTED) {
      // check whether button_E_quiz has been pressed
      if (button_E_quiz.isClicked) {
        if (!button_E_quiz.wasClicked) {
          // store time of first click
          button_E_quiz.timesOn.push(button_E_quiz.clock.getTime());
          // store time clicked until
          button_E_quiz.timesOff.push(button_E_quiz.clock.getTime());
          // end routine when button_E_quiz is clicked
          continueRoutine = false;
          button = 5;  
        } else {
          // update time clicked until;
          button_E_quiz.timesOff[button_E_quiz.timesOff.length - 1] = button_E_quiz.clock.getTime();
        }
        // if button_E_quiz is still clicked next frame, it is not a new click
        button_E_quiz.wasClicked = true;
      } else {
        // if button_E_quiz is clicked next frame, it is a new click
        button_E_quiz.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_E_quiz hasn't started / has finished
      button_E_quiz.clock.reset();
      // if button_E_quiz is clicked next frame, it is a new click
      button_E_quiz.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of quizComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quizRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'quiz' ---
    for (const thisComponent of quizComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('quiz.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    // psychoJS.experiment.addData('button_A_quiz.numClicks', button_A_quiz.numClicks);
    // psychoJS.experiment.addData('button_A_quiz.timesOn', button_A_quiz.timesOn);
    // psychoJS.experiment.addData('button_A_quiz.timesOff', button_A_quiz.timesOff);
    // psychoJS.experiment.addData('button_B_quiz.numClicks', button_B_quiz.numClicks);
    // psychoJS.experiment.addData('button_B_quiz.timesOn', button_B_quiz.timesOn);
    // psychoJS.experiment.addData('button_B_quiz.timesOff', button_B_quiz.timesOff);
    // psychoJS.experiment.addData('button_C_quiz.numClicks', button_C_quiz.numClicks);
    // psychoJS.experiment.addData('button_C_quiz.timesOn', button_C_quiz.timesOn);
    // psychoJS.experiment.addData('button_C_quiz.timesOff', button_C_quiz.timesOff);
    // psychoJS.experiment.addData('button_D_quiz.numClicks', button_D_quiz.numClicks);
    // psychoJS.experiment.addData('button_D_quiz.timesOn', button_D_quiz.timesOn);
    // psychoJS.experiment.addData('button_D_quiz.timesOff', button_D_quiz.timesOff);
    // psychoJS.experiment.addData('button_E_quiz.numClicks', button_E_quiz.numClicks);
    // psychoJS.experiment.addData('button_E_quiz.timesOn', button_E_quiz.timesOn);
    // psychoJS.experiment.addData('button_E_quiz.timesOff', button_E_quiz.timesOff);
    psychoJS.experiment.addData('quiz_response', button);
    if (button === que_answer) {
      isAnswerCorrect = 1;
    } else {
      isAnswerCorrect = 0;
    }    
    psychoJS.experiment.addData('quiz_pass', isAnswerCorrect);
    // the Routine "quiz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var realMaxDurationReached;
var realMaxDuration;
var realComponents;
function realRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'real' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    realClock.reset();
    routineTimer.reset();
    realMaxDurationReached = false;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_real
    gotValidClick = false; // until a click is received
    mouse_real.mouseClock.reset();
    text_real.setText('This question will not affect your payment.\nWe simply ask for your honest response. \n\nDid you pay sufficient attention during the study, and do you believe that your data should be included in the final dataset?\n\nClick anywhere on the bar to submit your response.\n\n');
    real_answer.reset()
    psychoJS.experiment.addData('real.started', globalClock.getTime());
    // Tracking the screen size
    const [screenWidth, screenHeight] = psychoJS.window.size;
    psychoJS.experiment.addData('screenWidth', screenWidth);
    psychoJS.experiment.addData('screenHeight', screenHeight);
    realMaxDuration = null
    // keep track of which components have finished
    realComponents = [];
    realComponents.push(mouse_real);
    realComponents.push(text_real);
    realComponents.push(real_answer);
    
    for (const thisComponent of realComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function realRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'real' ---
    // get current time
    t = realClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_real* updates
    if (t >= 0.0 && text_real.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_real.tStart = t;  // (not accounting for frame time here)
      text_real.frameNStart = frameN;  // exact frame index
      
      text_real.setAutoDraw(true);
    }
    
    
    // *real_answer* updates
    if (t >= 0.0 && real_answer.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      real_answer.tStart = t;  // (not accounting for frame time here)
      real_answer.frameNStart = frameN;  // exact frame index
      
      real_answer.setAutoDraw(true);
    }
    
    
    // Check real_answer for response to end Routine
    if (real_answer.getRating() !== undefined && real_answer.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of realComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function realRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'real' ---
    for (const thisComponent of realComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('real.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('real_answer.response', real_answer.getRating());
    psychoJS.experiment.addData('real_answer.rt', real_answer.getRT());
    // the Routine "real" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var EndMaxDurationReached;
var EndMaxDuration;
var EndComponents;
function EndRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'End' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    EndClock.reset(routineTimer.getTime());
    routineTimer.add(5.000000);
    EndMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('End.started', globalClock.getTime());
    EndMaxDuration = null
    // keep track of which components have finished
    EndComponents = [];
    EndComponents.push(text_ending);
    
    for (const thisComponent of EndComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function EndRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'End' ---
    // get current time
    t = EndClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_ending* updates
    if (t >= 0.0 && text_ending.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_ending.tStart = t;  // (not accounting for frame time here)
      text_ending.frameNStart = frameN;  // exact frame index
      
      text_ending.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_ending.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_ending.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'End' ---
    for (const thisComponent of EndComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('End.stopped', globalClock.getTime());
    if (EndMaxDurationReached) {
        EndClock.add(EndMaxDuration);
    } else {
        EndClock.add(5.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
