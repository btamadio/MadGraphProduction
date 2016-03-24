## Photos++ QED config for Pythia8

## Disable native QED FSR
assert hasattr(genSeq, "Pythia8")
genSeq.Pythia8.Commands += ["TimeShower:QEDshowerByL = off"]

## Enable Photos++
include("MC15JobOptions/nonStandard/Photospp_Fragment.py")
