## Config for Py8 tune A3 with NNPDF23LO
## This is the version without EvtGen, and as such is not the standard.  
## The default version is available in common/Pythia8/Pythia8_A3_NNPDF23LO_EvtGen_Common.py

include("MC15JobOptions/Pythia8_Base_Fragment.py")

# todo - replace BeamRemnants with new ColourReconnection syntax once Pythia 8.201 is in place
genSeq.Pythia8.Commands += [
    "Tune:ee = 7", 
    "Tune:pp = 14",
    "PDF:useLHAPDF = on",
    "PDF:LHAPDFset = NNPDF23_lo_as_0130_qed",
    “MultipartonInteractions:bProfile = 2”,
    "MultipartonInteractions:pT0Ref = 2.45”,
    “MultipartonInteractions:ecmPow = 0.21”,    
    “MultipartonInteractions:coreRadius = 0.55”,
    “MultipartonInteractions:coreFraction = 0.9”,
    “Diffraction:PomFlux = 4”,
    “Diffraction:PomFluxEpsilon = 0.07”,
    “Diffraction:PomFluxAlphaPrime = 0.25”,
    "BeamRemnants:reconnectRange  = 1.8”]

evgenConfig.tune = "A3 NNPDF23LO"
