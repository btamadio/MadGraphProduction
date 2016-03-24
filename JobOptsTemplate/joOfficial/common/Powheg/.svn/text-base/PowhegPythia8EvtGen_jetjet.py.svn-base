# This includes the setting of random seeds and c.o.m. energy
include('PowhegControl/PowhegControl_Dijet_Common.py')
PowhegConfig.bornktmin = int(runArgs.runNumber)
PowhegConfig.pdf = 11000

ktmin = { 1:2 , 2:5 , 3:15 , 4:30 , 5:75 , 6:150 , 7:250 ,
          8:750 , 9:1250 }
supp  = { 1:60 , 2:160 , 3:400 , 4:800 , 5:1800 , 6:3200 ,
          7:5300 , 8:9000 , 9:11000 }

theRun = int(runArgs.runNumber)%10
PowhegConfig.bornktmin = ktmin[ theRun ]
PowhegConfig.bornsuppfact = supp[ theRun ]

# Just 22k to make 20k output
# 22k = 5-7 hrs on a batch node; can do up to 3x as many
if theRun in [1,2,3]: PowhegConfig.nEvents = 12000
if theRun in [4]:     PowhegConfig.nEvents = 22000
if theRun in [5]:     PowhegConfig.nEvents = 33000
if theRun in [6,7]:   PowhegConfig.nEvents = 66000
if theRun in [8]:     PowhegConfig.nEvents = 55000
if theRun in [9]:     PowhegConfig.nEvents = 36000

print PowhegConfig

PowhegConfig.generateRunCard()
PowhegConfig.generateEvents()

##--------------------------------------------------------------
## EVGEN transform
##--------------------------------------------------------------
evgenConfig.description    = "POWHEG+Pythia8 dijet production with bornktmin = %i GeV, bornsuppfact = %i GeV, muR=muF=1"%(PowhegConfig.bornktmin,PowhegConfig.bornsuppfact)
evgenConfig.keywords       = [ "QCD", "dijet", "jets", "SM" ]
evgenConfig.contact        = [ "ZLMarshall@lbl.gov" ]
evgenConfig.generators    += [ "Pythia8" ]

# For JZ 1-6 this is no problem
evgenConfig.minevents = 5000
# For JZ 7 things are a bit tighter
if theRun in [7]: evgenConfig.minevents = 3000
# For the remainder, it's way tight
if theRun in [8]: evgenConfig.minevents = 1000
if theRun in [9]: evgenConfig.minevents = 200

##--------------------------------------------------------------
## Pythia8 showering with new, main31-style shower
##--------------------------------------------------------------
include('MC15JobOptions/Pythia8_A14_NNPDF23LO_EvtGen_Common.py')
include("MC15JobOptions/Pythia8_Powheg_Main31.py")

# Add the jet filter
include("MC15JobOptions/JetFilter_JZ%i.py"%(theRun))
# Make J9 inclusive
if 9==theRun: filtSeq.QCDTruthJetFilter.MaxPt = -1

evgenConfig.inputconfcheck = "jetjet_J%i"%(theRun)

