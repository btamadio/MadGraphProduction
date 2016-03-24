# R-Hadron common evgen jobOption fragment
# compiled by Sascha Mehlhase (sascha.mehlhase@cern.ch)
# 24 June 2015
# common template file for all R-Hadron samples

# getting config from top-level jobOption name
rhconf = runArgs.jobConfig[0].split('/')[-1].split(".")[2].split("_")

# setting particle type
if rhconf[3] in ["gluino", "sbottom", "stop"]: CASE = rhconf[3]
else: raise RunTimError('No sensible CASE was set!')

# setting interaction model
if rhconf[2] == "gen": MODEL = "generic"
elif rhconf[2] == "reg": MODEL = "regge"
elif rhconf[2] == "int": MODEL = "intermediate"
else: raise RunTimError('No sensible MODEL was set!')

# setting gluino-ball probability
if CASE == "gluino": GBALLPROB = float(rhconf[4].replace("p","0."))

# setting gluino/squark mass
if CASE == "gluino": MASS = int(rhconf[5])
else: MASS = int(rhconf[4])

# checking stable vs. meta-stable case
if "ns" in rhconf[-1]: # meta-stable case
  # setting mass of neutralino
  if CASE == "gluino": MASSX = int(rhconf[7])
  else: MASSX = int(rhconf[6])
  
  # setting immediate-decay flag
  DECAY = 'false'
  
  # setting lifetime of gluino/squark
  LIFETIME = rhconf[-1].replace("ns","").replace("p","0.")

  # setting decay type
  if CASE == "gluino": TYPE = rhconf[6]
  else: TYPE = rhconf[5]
  DECAYTYPE=""
  if TYPE == "tt": DECAYTYPE="NOGLUINOGLUONDECAY=True;NOGLUINOLIGHTSQUARKDECAY=True;"
  elif TYPE == "qq": DECAYTYPE="NOGLUINOGLUONDECAY=True;NOGLUINOTTBARDECAY=True;"
  elif TYPE == "g": DECAYTYPE="NOGLUINOLIGHTSQUARKDECAY=True;NOGLUINOTTBARDECAY=True;"

  include("MC15JobOptions/PythiaRhad_AUET2BCTEQ6L1_Common.py")
  
  # filling evgenConfig variables
  evgenConfig.description += " meta-stable {model} {case} {mass}GeV {lifetime}ns {type} X0 {massx}GeV".format(model = MODEL, case = CASE, mass = MASS, lifetime = LIFETIME, type = TYPE, massx = MASSX)
  if CASE == "gluino": evgenConfig.description += " {gluinoballprob} gballprob".format(gluinoballprob = GBALLPROB)
  evgenConfig.specialConfig = "MODEL={model};CASE={case};MASS={mass};DECAY={decay};LIFETIME={lifetime};MASSX={massx};CHARGE=999;{decaytype}preInclude=SimulationJobOptions/preInclude.Rhadrons.py;".format(model = MODEL, case = CASE, mass = MASS, decay = DECAY, lifetime = LIFETIME, massx = MASSX, decaytype = DECAYTYPE)
else: # stable case

  include("MC15JobOptions/PythiaRhad_AUET2BCTEQ6L1_Common.py")

  # filling evgenConfig variables
  evgenConfig.description += " stable {model} {case} {mass}GeV".format(model = MODEL, case = CASE, mass = MASS)
  if CASE == "gluino": evgenConfig.description += " {gluinoballprob} gballprob".format(gluinoballprob = GBALLPROB)
  evgenConfig.specialConfig = "MODEL={model};CASE={case};MASS={mass};preInclude=SimulationJobOptions/preInclude.Rhadrons.py;".format(model = MODEL, case = CASE, mass = MASS)

from AthenaCommon import Logging
PSPRlog = Logging.logging.getLogger('PythiaRhad_SUSY_AUET2BCTEQ6L1_Rhadrons') # Or whatever name you like
PSPRlog.info(runArgs)
PSPRlog.info(rhconf)
PSPRlog.info(evgenConfig)

