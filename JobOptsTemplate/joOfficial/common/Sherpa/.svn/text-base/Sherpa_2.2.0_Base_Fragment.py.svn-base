## Base config for Sherpa
from Sherpa_i.Sherpa_iConf import Sherpa_i
genSeq += Sherpa_i()
evgenConfig.generators = ["Sherpa"]

## Loop removal should not be necessary anymore with HEPMC_TREE_LIKE=1 below
fixSeq.FixHepMC.LoopsByBarcode = False

## Disable TestHepMC for the time being, cf.
## https://its.cern.ch/jira/browse/ATLMCPROD-1862
if hasattr(testSeq, "TestHepMC"):
    testSeq.remove(TestHepMC())

## Tell Sherpa to read its run card sections from the jO
genSeq.Sherpa_i.Parameters += [ 'RUNDATA=%s' % runArgs.jobConfig[0] ]
## Tell Sherpa to write logs into a separate file
## (need for production, looping job detection, Wolfgang Ehrenfeld)
genSeq.Sherpa_i.Parameters += [ 'LOG_FILE=sherpa.log' ]


## General ATLAS parameters
genSeq.Sherpa_i.Parameters += [
    "MAX_PROPER_LIFETIME=10.0",
    "HEPMC_TREE_LIKE=1",
    "PRETTY_PRINT=Off",
    ]

## Particle masses/widths
genSeq.Sherpa_i.Parameters += [
    "MASS[6]=172.5",
    "WIDTH[6]=1.32",        #updated to comply latest updated top results    
    "MASS[15]=1.777",
    "WIDTH[15]=2.26735e-12",
    "MASS[23]=91.1876",
    "WIDTH[23]=2.4952",
    "MASS[24]=80.399",
    "WIDTH[24]=2.085",
    ]

## Switch to EW_SCHEME=0 to be able to set PDG value of thetaW
## Requires workaround to still keep WIDTH_SCHEME=CMS in 2.2.0
## The first three lines should be removed for Sherpa >= 2.2.1
genSeq.Sherpa_i.Parameters += [
    "SHERPA_LDADD=SherpaModelSM_EW0",
    "OL_IGNORE_MODEL=1",
    "MODEL=SM_EW0",
    "EW_SCHEME=0",
    "SIN2THETAW=0.23113",
    ]

## set/add partial widths for H, W, Z to PDG values
## cf. https://sherpa.hepforge.org/doc/SHERPA-MC-2.2.0.html#HDH_005fWIDTH
genSeq.Sherpa_i.Parameters += [
    "HDH_WIDTH[6,24,5]=1.32",    #updated to comply latest updated top results
    "HDH_WIDTH[-6,-24,-5]=1.32",  #updated to comply latest updated top results
    "HDH_WIDTH[25,5,-5]=2.35e-3",
    "HDH_WIDTH[25,15,-15]=2.57e-4",
    "HDH_WIDTH[25,13,-13]=8.91e-7",
    "HDH_WIDTH[25,4,-4]=1.18e-4",
    "HDH_WIDTH[25,3,-3]=1.00e-6",
    "HDH_WIDTH[25,21,21]=3.49e-4",
    "HDH_WIDTH[25,22,22]=9.28e-6",
    "HDH_WIDTH[24,2,-1]=0.7041",
    "HDH_WIDTH[24,4,-3]=0.7041",
    "HDH_WIDTH[24,12,-11]=0.2256",
    "HDH_WIDTH[24,14,-13]=0.2256",
    "HDH_WIDTH[24,16,-15]=0.2256",
    "HDH_WIDTH[-24,-2,1]=0.7041",
    "HDH_WIDTH[-24,-4,3]=0.7041",
    "HDH_WIDTH[-24,-12,11]=0.2256",
    "HDH_WIDTH[-24,-14,13]=0.2256",
    "HDH_WIDTH[-24,-16,15]=0.2256",
    "HDH_WIDTH[23,1,-1]=0.3828",
    "HDH_WIDTH[23,2,-2]=0.2980",
    "HDH_WIDTH[23,3,-3]=0.3828",
    "HDH_WIDTH[23,4,-4]=0.2980",
    "HDH_WIDTH[23,5,-5]=0.3828",
    "HDH_WIDTH[23,11,-11]=0.0840",
    "HDH_WIDTH[23,12,-12]=0.1663",
    "HDH_WIDTH[23,13,-13]=0.0840",
    "HDH_WIDTH[23,14,-14]=0.1663",
    "HDH_WIDTH[23,15,-15]=0.0840",
    "HDH_WIDTH[23,16,-16]=0.1663",
    ]

## OpenLoops parameters
genSeq.Sherpa_i.Parameters += [
    "OL_PARAMETERS=preset=2 write_parameters=1",
    ]
