## Config for Py8 tune AZNLO with CTEQ6L1 with AZNLO tune and renormalization scale down
include("MC15JobOptions/nonStandard/Pythia8_AZNLO_CTEQ6L1_RenDown_Common.py")

# Add EvtGen for b fragmentation as default.  No EvtGen is available in "nonStandard"
include("MC15JobOptions/Pythia8_EvtGen.py")
