## Configure Herwig / Jimmy for Tauola

assert hasattr(genSeq, "Herwig")
genSeq.Herwig.HerwigCommand += ["taudec TAUOLA"]
## Enable TAUOLA
include("MC15JobOptions/Tauola_Fragment.py")