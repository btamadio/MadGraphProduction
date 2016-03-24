from MadGraphControl.MadGraphUtils import *

nevents=40000
mode=0

### DSID list
DSIDDic = {305037:'400',305038:'500',305039:'600',305040:'700',305041:'800',305042:'900',305043:'1000'}
mass = DSIDDic[runArgs.runNumber]

### Cards
fcard = open('proc_card_mg5.dat','w')
fcard.write("""
    define l+ = e+ mu+
    define l- = e- mu-
    define vl = ve vm
    define vl~ = ve~ vm~
    import model Vector_Triplet_UFO
    generate    p p > vc+ > w+ z j j / a QCD=0, w+ > l+ vl,  z > l+ l- @1
    add process p p > vc- > w- z j j / a QCD=0, w- > l- vl~, z > l+ l- @2
    output -f
    """)
fcard.close()

extras = {
    'pdlabel':"'lhapdf'",
    'lhaid':"247000",
    'ptj':"15",
    'pta':"0",
    'ptb':"0",
    'etal':"2.7",
    'drjj':"0",
    'drll':"0",
    'draa':"0",
    'draj':"0",
    'drjl':"0",
    'dral':"0",
    'sys_pdf':"NNPDF23_lo_as_0130_qed.LHgrid" }
    
build_run_card(run_card_old='MadGraph_run_card_HVT.dat',run_card_new='run_card.dat',nevts=nevents,rand_seed=runArgs.randomSeed,beamEnergy=runArgs.ecmEnergy/2.,extras=extras)

print_cards()
    
runName='HVT_VBS_vc_lvll_'+mass+'_gv3_cf0_ch1_qcd0'

process_dir = new_process(card_loc='proc_card_mg5.dat')

evgenConfig.generators = ["MadGraph"]

generate(run_card_loc='run_card.dat',param_card_loc='MadGraph_param_card_HVTm'+mass+'.dat',mode=mode,proc_dir=process_dir,run_name=runName)

############################
# Shower JOs will go here

import os
if 'ATHENA_PROC_NUMBER' in os.environ:
   njobs = os.environ.pop('ATHENA_PROC_NUMBER')
   # Try to modify the opts underfoot
   if not hasattr(opts,'nprocs'): print 'Warning: Did not see option!'
   else: opts.nprocs = 0
   print opts

arrange_output(run_name=runName,proc_dir=process_dir,outputDS=runName+'._00001.events.tar.gz')

include("MC15JobOptions/nonStandard/Pythia8_A14_NNPDF23LO_Common.py")
include("MC15JobOptions/Pythia8_LHEF.py")
evgenConfig.generators += ["MadGraph", "Pythia8"]
evgenConfig.contact = ["Benjamin Freund <Benjamin.Freund@cern.ch>"]
genSeq.Pythia8.Commands += [
    "Init:showAllParticleData = on",
    "Next:numberShowLHA = 10",
    "Next:numberShowEvent = 10"]
evgenConfig.description = 'MadGraph_GM_VBS_H5p'
evgenConfig.keywords+=['BSM','VBS','Higgs','WZ','leptonic']
#stringy = 'madgraph.'+str(runArgs.runNumber)+'.MadGraph_EffDM'
#runArgs.inputGeneratorFile=stringy+'._00001.events.tar.gz'
evgenConfig.inputfilecheck = runName
runArgs.inputGeneratorFile=runName+'._00001.events.tar.gz'                     
