# Keep most of the job only for the generate step...
theRun = int(runArgs.runNumber)%10

ktmin = { 1:2 , 2:5 , 3:15 , 4:30 , 5:75 , 6:150 , 7:250 ,
          8:750 , 9:1250 }
supp  = { 1:60 , 2:160 , 3:400 , 4:800 , 5:1800 , 6:3200 ,
          7:5300 , 8:9000 , 9:11000 }

if runArgs.trfSubstepName == 'generate' :

    # This includes the setting of random seeds and c.o.m. energy
    include('PowhegControl/PowhegControl_Dijet_Common.py')
    PowhegConfig.bornktmin = int(runArgs.runNumber)
    PowhegConfig.pdf = 11000
    
    PowhegConfig.bornktmin = ktmin[ theRun ]
    PowhegConfig.bornsuppfact = supp[ theRun ]
    
    # Just 22k to make 20k output
    # 22k = 5-7 hrs on a batch node; can do up to 3x as many
    if theRun in [1,2,3]: PowhegConfig.nEvents = 12000
    if theRun in [4]:     PowhegConfig.nEvents = 22000
    if theRun in [5]:     PowhegConfig.nEvents = 33000
    if theRun in [6]:   PowhegConfig.nEvents = 66000
    if theRun in [7,8]:     PowhegConfig.nEvents = 55000
    if theRun in [9]:     PowhegConfig.nEvents = 36000
    
    print PowhegConfig

    PowhegConfig.generateRunCard()
    PowhegConfig.generateEvents()

##--------------------------------------------------------------
## EVGEN transform
##--------------------------------------------------------------
evgenConfig.description    = "POWHEG+fHerwig dijet production with bornktmin = %i GeV, bornsuppfact = %i GeV, muR=muF=1"%(ktmin[theRun],supp[theRun])
evgenConfig.keywords       = [ "QCD", "dijet", "jets", "SM" ]
evgenConfig.contact        = [ "ZLMarshall@lbl.gov" ]
evgenConfig.generators    += [ "Powheg" ]

# For JZ 1-6 this is no problem
evgenConfig.minevents = 5000
# For JZ 7 things are a bit tighter
if theRun in [4,7]: evgenConfig.minevents = 2000
# For the remainder, it's way tight
if theRun in [8]: evgenConfig.minevents = 1000
if theRun in [9]: evgenConfig.minevents = 200

import os
if 'ATHENA_PROC_NUMBER' in os.environ:
    # Try to modify the opts underfoot
    if not hasattr(opts,'nprocs'): mglog.warning('Did not see option!')
    else: opts.nprocs = 0

##--------------------------------------------------------------
## fHerwig showering
##--------------------------------------------------------------
if runArgs.trfSubstepName == 'generate' :

    ## Base config for HERWIG 6.5 + Jimmy 4.31 using the AUET2 CT10 tune
    include("MC15JobOptions/nonStandard/Herwig_AUET2_CT10_Common.py")
    include("MC15JobOptions/nonStandard/Herwig_Powheg.py")
    include("MC15JobOptions/nonStandard/Herwig_Photos.py")
    include("MC15JobOptions/nonStandard/Herwig_Tauola.py")

    # Add the jet filter
    include("MC15JobOptions/JetFilter_JZ%i.py"%(theRun))
    # Make J9 inclusive
    if 9==theRun: filtSeq.QCDTruthJetFilter.MaxPt = -1

    evgenConfig.inputconfcheck = "jetjet_J%i"%(theRun)

## Run EvtGen in afterburner mode
include("MC15JobOptions/nonStandard/Herwig_EvtGen.py")

