from Herwigpp_i.Herwigpp_iConf import Herwigpp
genSeq += Herwigpp()
evgenConfig.generators += ["Herwigpp"]

genSeq.Herwigpp.Commands += ["set /Herwig/Model:EW/Sin2ThetaW 0.23113"]

