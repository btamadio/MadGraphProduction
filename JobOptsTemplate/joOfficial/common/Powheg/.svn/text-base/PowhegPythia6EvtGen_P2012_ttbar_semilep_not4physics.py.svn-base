# Slice_config ={ DSID:[minpt, maxpt, efficiency_multiplier]}
# efficiency multipliers are (1.2/empirical filter efficiency)+2
# changed supps to top_pt_max in order to help with distributions - so efficiencies may be wrong now.
slice_config  = { 0:[0,200,5], 
                  1:[200,350,14],
                  2:[350,500,173],
                  3:[500,750,40],
                  4:[750,1000,78],
                  5:[1000,1250,135],
                  6:[1250,1500,242],
                  7:[1500,6500,302] }

theRun = int(runArgs.runNumber)%10
top_pt_min = slice_config[theRun][0]
top_pt_max = slice_config[theRun][1]
supp = top_pt_min
nev = slice_config[theRun][2]
evgenConfig.description    = "POWHEG+Pythia6 ttbar production with Powheg hdamp equal top mass, Perugia 2012 tune, at least one lepton filter, had top pT min = %i GeV, max = %i GeV; bornsuppfact = %i GeV"%(top_pt_min, top_pt_max, supp)
evgenConfig.keywords    = [ 'SM', 'top', 'ttbar', 'lepton']
evgenConfig.contact     = ['lily.asquith@cern.ch', 'eloi.paul.le.quilleuc@cern.ch' ]

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
   #include('BoostedHadTopAndTopPair.py')
   filtSeq.BoostedHadTopAndTopPair.tHadPtMin  = top_pt_min*1000
   filtSeq.BoostedHadTopAndTopPair.tHadPtMax  = top_pt_max*1000
#  Run EvtGen as afterburner
include('MC15JobOptions/Pythia_Powheg_EvtGen.py')
