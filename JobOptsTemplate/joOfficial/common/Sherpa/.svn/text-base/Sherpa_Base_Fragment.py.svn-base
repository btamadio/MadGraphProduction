## Base config for Sherpa
from Sherpa_i.Sherpa_iConf import Sherpa_i
genSeq += Sherpa_i()
evgenConfig.generators = ["Sherpa"]

## Turn-on Loop-induced removal function from FixHepMC 
## this is important to avoid xAOD level crashes 
fixSeq.FixHepMC.LoopsByBarcode = True

## Tell Sherpa to read its run card sections from the jO
genSeq.Sherpa_i.Parameters += [ 'RUNDATA=%s' % runArgs.jobConfig[0] ]
## Tell Sherpa to write logs into a separate file
## (need for production, looping job detection, Wolfgang Ehrenfeld)
genSeq.Sherpa_i.Parameters += [ 'LOG_FILE=sherpa.log' ]

## Correct BR of W and Z as from PDG. Important for processes 
## with V produced in the hard scattering.   
## To be used only for samples with fixed N leptonic decays 
   
WlvBRfac = 0.1082/0.1111
WqqBRfac = 0.3377/0.3333
ZllBRfac = 0.03366/0.0344  
ZvvBRfac = 0.20/0.2041 

## General ATLAS parameters
## MI_HANDLER set not needed as already default in Sherpa 2.1 
genSeq.Sherpa_i.Parameters += [
    "MASS[6]=172.5",
    "MASS[23]=91.1876",
    "MASS[24]=80.399",
    "WIDTH[23]=2.4952",
    "WIDTH[24]=2.085",
    "SIN2THETAW=0.23113",
    "MAX_PROPER_LIFETIME=10.0",
    "WIDTH[15]=2.26735e-12"
    ]
## the following setting was in MC12 and is now obsolete
##    "MI_HANDLER=Amisic"  
