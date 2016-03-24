## Config for Py8 tune A14 with NNPDF23LO Var3c Up
## The default version of this tune fragment include EvtGen for standardised b fragmentation

# Reference the non-standard version without EvtGen
include("MC15JobOptions/nonStandard/Pythia8_A14_NNPDF23LO_Var3cUp_Common.py")

# Add EvtGen for b fragmentation as default.  No EvtGen is available in "nonStandard"
include("MC15JobOptions/Pythia8_EvtGen.py")

