## Config for Py8 Monash tune 
## This is not the default recommended tune, but forms the base for A14
## In principle it could be set with Tune:pp=14, but there are some problems with PDFs

include("MC15JobOptions/Pythia8_Base_Fragment.py")

genSeq.Pythia8.Commands += [
"Tune:ee = 7",
"Tune:pp = 14",
"PDF:useLHAPDF=on",
"PDF:LHAPDFset = NNPDF23_lo_as_0130_qed"
]

evgenConfig.tune = "Monash"
