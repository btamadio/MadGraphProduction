## Min bias truth jet filter for min bias sample preparation (high slice)

include("MC15JobOptions/AntiKt4TruthJets_pileup.py")
include("MC15JobOptions/AntiKt6TruthJets_pileup.py")

include("MC15JobOptions/JetFilter_Fragment.py")
filtSeq.QCDTruthJetFilter.MaxPt = 35.*GeV
filtSeq.QCDTruthJetFilter.TruthJetContainer = "AntiKt6TruthJets"
filtSeq.QCDTruthJetFilter.DoShape = False
