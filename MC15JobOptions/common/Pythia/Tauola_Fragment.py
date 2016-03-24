## Tauola config
from Tauola_i.Tauola_iConf import Tauola
genSeq += Tauola()

genSeq.Tauola.TauolaCommand = \
    ["tauola polar 1",
     "tauola radcor 1",
     "tauola phox 0.01",
     "tauola dmode 0",
     "tauola jak1 0",
     "tauola jak2 0"]

evgenConfig.generators += [ "Tauola" ]
