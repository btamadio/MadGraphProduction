## Config for Py8 tune A14 with NNPDF23LO
include("MC15JobOptions/Pythia8_Base_Fragment.py")

genSeq.Pythia8.UseLHAPDF=False

genSeq.Pythia8.Commands += [
        "Tune:ee = 7",
        "Tune:pp = 14",
        "PDF:useLHAPDF = on",
        "PDF:LHAPDFset = NNPDF23_lo_as_0130_qed",
        "SpaceShower:rapidityOrder = on",
        "SigmaProcess:alphaSvalue = 0.140",
        "SpaceShower:pT0Ref = 1.60",
        "SpaceShower:pTmaxFudge = 1.05",
        "SpaceShower:pTdampFudge = 1.04",
        "SpaceShower:alphaSvalue = 0.127",
        "TimeShower:alphaSvalue = 0.139",
        "BeamRemnants:primordialKThard = 1.88",
        "MultipartonInteractions:pT0Ref = 2.09",
        "MultipartonInteractions:alphaSvalue = 0.126",
        "BeamRemnants:reconnectRange = 1.71"]

evgenConfig.tune = "A14 NNPDF23LO"
