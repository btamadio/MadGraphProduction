## Photos++ QED config for Pythia8B

## Disable native QED FSR
assert hasattr(genSeq, "Pythia8B")
genSeq.Pythia8B.Commands += ["TimeShower:QEDshowerByL = off"]

## Enable Photos++
include("MC15JobOptions/nonStandard/Photospp_Fragment.py")
