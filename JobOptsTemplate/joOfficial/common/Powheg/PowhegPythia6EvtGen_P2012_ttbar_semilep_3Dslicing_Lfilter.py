# slice_config ={ last_digit_of_DSID:[minpt, maxpt, minpairpt, maxpairpt, efficiency_multiplier]}
slice_config  = { 0:[0,200,0,150, -1, 20],
                  1:[0,200,150,350, -1, 10000],
                  2:[0,200,350,13000, -1, 100000],
                  3:[200,500,0,150, -1, 100],
                  4:[200,500,150,350, -1, 300],
                  5:[200,500,350,13000, -1, 1000],
                  6:[500,6500,0,150, -1, 2000],
                  7:[500,6500,150,350, -1, 17000],
                  8:[500,6500,350,13000, -1, 9500]}

runID = int(runArgs.runNumber)%10
top_pt_min = slice_config[runID][0]
top_pt_max = slice_config[runID][1]
tt_pt_min = slice_config[runID][2]
tt_pt_max = slice_config[runID][3]
supp = slice_config[runID][4]
nev = slice_config[runID][5]
evgenConfig.description    = "POWHEG+Pythia6 ttbar + light jets production with Powheg hdamp equal top mass, Perugia 2012 tune, at least one lepton filter, additional light-jet filter, had top pT min = %i GeV, max = %i GeV; ttbar pT min = %i GeV, max = %i GeV; supp factor = %i, at least one AntiKt10Truth jet pT>200 GeV and |eta|<2"%(top_pt_min, top_pt_max, tt_pt_min, tt_pt_max, supp)
evgenConfig.keywords    = [ 'SM', 'top', 'ttbar', 'lepton']
evgenConfig.contact     = ['lily.asquith@cern.ch', 'eloi.paul.le.quilleuc@cern.ch', 'georges.aad@cern.ch' ]
evgenConfig.minevents = 500

# MC15: everything goes inside this if statement
if runArgs.trfSubstepName == 'generate' :
   include('PowhegControl/PowhegControl_tt_Common.py')
   PowhegConfig.topdecaymode = 22222
   PowhegConfig.hdamp        = 172.5
   PowhegConfig.nEvents    *= nev
   PowhegConfig.bornsuppfact = supp
   print PowhegConfig
   PowhegConfig.generateRunCard()
   PowhegConfig.generateEvents()
   include('MC15JobOptions/PowhegPythia_Perugia2012_Common.py')
   include('MC15JobOptions/Pythia_Tauola.py')
   include('MC15JobOptions/Pythia_Photos.py')
   include('MC15JobOptions/TTbarWToLeptonFilter.py')
   filtSeq.TTbarWToLeptonFilter.NumLeptons = -1
   filtSeq.TTbarWToLeptonFilter.Ptcut = 0.
   include('MC15JobOptions/BoostedHadTopAndTopPair.py')
   filtSeq.BoostedHadTopAndTopPair.tHadPtMin  = top_pt_min*1000
   filtSeq.BoostedHadTopAndTopPair.tHadPtMax  = top_pt_max*1000
   filtSeq.BoostedHadTopAndTopPair.tPairPtMin = tt_pt_min*1000
   filtSeq.BoostedHadTopAndTopPair.tPairPtMax = tt_pt_max*1000
   include('MC15JobOptions/TTbarPlusHFFilter.py')
   filtSeq.TTbarPlusBFilter.SelectL = True
   filtSeq.TTbarPlusBFilter.SelectB = False
   filtSeq.TTbarPlusBFilter.SelectC = False
   include('MC15JobOptions/AntiKt10TruthJets.py')
   include('MC15JobOptions/JetFilter_Fragment.py')
   filtSeq.QCDTruthJetFilter.TruthJetContainer="AntiKt10TruthJets"
   filtSeq.QCDTruthJetFilter.MinPt = 100000. 
   filtSeq.QCDTruthJetFilter.MaxEta = 2.
#  Run EvtGen as afterburner
include('MC15JobOptions/Pythia_Powheg_EvtGen.py')
