def get_mg_variations(mass, syst_mod, xqcut=None):
    if xqcut is None:
        xqcut = 500  # default
        if mass < xqcut*4.:
            xqcut = mass*0.25
            pass
        if syst_mod:
            if 'qcup' in syst_mod:
                xqcut = xqcut*2.
            elif 'qcdw' in syst_mod:
                xqcut = xqcut*0.5

    mglog.info('For matching, will use xqcut of '+str(xqcut))

    alpsfact = 1.0
    scalefact = 1.0
    if syst_mod:
        if 'alup' in syst_mod:
            alpsfact = 2.0
        elif 'aldw' in syst_mod:
            alpsfact = 0.5

        if 'scup' in syst_mod:
            scalefact = 2.0
        elif 'scdw' in syst_mod:
            scalefact = 0.5

    return xqcut, alpsfact, scalefact


###
from MadGraphControl.MadGraphUtils import *

# in case someone needs to be able to keep the output directory for testing
keepOutput = False

import re
plist = re.sub(r'.+mAMSB_', '', runArgs.jobConfig[0].rstrip('.py')).split('_')
m0 = int(plist[0])
m32 = int(plist[1])
tanb = 5
slha_file = 'susy.%s.mAMSB_%s_%s_%s_P.slha' % (runArgs.runNumber, m0, m32, tanb)

lifetime = float(0)
match = re.search(r'_LL(\d+p\d+)[_.]|_(Stable)[_.]', runArgs.jobConfig[0])
if match:
    if match.group(1):
        lifetime = float(match.group(1).replace('p', '.'))
    elif match.group(2):
        lifetime = float(-1.0)

jetptmin = float(0)
metmin = float(0)
match = re.search(r'_Filt1Jet(\d+)[_.]|_FiltMet(\d+)[_.]|_Filt1Jet(\d+)Met(\d+)[_.]', runArgs.jobConfig[0])
if match:
    if match.group(1):
        jetptmin = float(match.group(1))
    elif match.group(2):
        metmin = float(match.group(2))
    elif match.group(3) and match.group(4):
        jetptmin = float(match.group(3))
        metmin = float(match.group(4))

# Event multipliers for getting more events out of madgraph to feed through athena (esp. for filters)
if jetptmin == 0 and metmin == 0:
    evt_multiplier = 2.0
else:
    evt_multiplier = 20.0  # assuming GenFiltEff. ~10%

nevts = 5000*evt_multiplier


# MadGraph5 systematics variations
list_mg_syst = ['scup',
                'scdw',
                'alup',
                'aldw',
                'qcup',
                'qcdw']

# Pythia8 systematics variations
dict_py8_syst = {'py1up': 'Pythia8_A14_NNPDF23LO_Var1Up_EvtGen_Common.py',
                 'py1dw': 'Pythia8_A14_NNPDF23LO_Var1Down_EvtGen_Common.py',
                 'py2up': 'Pythia8_A14_NNPDF23LO_Var2Up_EvtGen_Common.py',
                 'py2dw': 'Pythia8_A14_NNPDF23LO_Var2Down_EvtGen_Common.py',
                 'py3aup': 'Pythia8_A14_NNPDF23LO_Var3aUp_EvtGen_Common.py',
                 'py3adw': 'Pythia8_A14_NNPDF23LO_Var3aDown_EvtGen_Common.py',
                 'py3bup': 'Pythia8_A14_NNPDF23LO_Var3bUp_EvtGen_Common.py',
                 'py3bdw': 'Pythia8_A14_NNPDF23LO_Var3bDown_EvtGen_Common.py',
                 'py3cup': 'Pythia8_A14_NNPDF23LO_Var3cUp_EvtGen_Common.py',
                 'py3cdw': 'Pythia8_A14_NNPDF23LO_Var3cDown_EvtGen_Common.py'}

mg_syst_mod = None
par = [x for x in plist if x in list_mg_syst]
if par:
    mg_syst_mod = par[0]

py8_syst_mod = None
par = [x for x in plist if x in dict_py8_syst.keys()]
if par:
    py8_syst_mod = par[0]

process = '''
generate p p > x1+ x1- $ susystrong @1
add process p p > x1+ n1 $ susystrong @1
add process p p > x1- n1 $ susystrong @1
add process p p > x1+ x1- j $ susystrong @2
add process p p > x1+ n1 j $ susystrong @2
add process p p > x1- n1 j $ susystrong @2
add process p p > x1+ x1- j j $ susystrong @3
add process p p > x1+ n1 j j $ susystrong @3
add process p p > x1- n1 j j $ susystrong @3
'''
njets = 2

pdlabel = 'nn23lo1'
lhaid = 247000

# Set beam energy
beamEnergy = 6500.
if hasattr(runArgs, 'ecmEnergy'):
    beamEnergy = runArgs.ecmEnergy * 0.5

# Set random seed
rand_seed = 1234
if hasattr(runArgs, "randomSeed"):
    # Giving a unique seed number (not exceeding the limit of ~30081^2)
    rand_seed = 1000 * int(str(runArgs.runNumber)[1:6]) + runArgs.randomSeed

if not 'MADGRAPH_DATA' in os.environ:
    os.environ['MADGRAPH_DATA'] = os.getcwd()
    mglog.warning('Setting your MADGRAPH_DATA environmental variable to the working directory')

if py8_syst_mod:
    include("MC15JobOptions/"+dict_py8_syst[py8_syst_mod])
else:
    include("MC15JobOptions/Pythia8_A14_NNPDF23LO_EvtGen_Common.py")

include("MC15JobOptions/Pythia8_MadGraph.py")

# Generate the new process!
full_proc = """
import model mssm-full
"""+helpful_definitions()+"""
# Specify process(es) to run

"""+process+"""
# Output processes to MadEvent directory
output -f
"""
thedir = new_process(card_loc=full_proc)
if 1 == thedir:
    mglog.error('Error in process generation!')
mglog.info('Using process directory '+thedir)

# Grab the param card and move the new masses into place
from PyJobTransformsCore.trfutil import get_files
get_files(slha_file, keepDir=False, errorIfNotFound=True)
include('MC15JobOptions/SUSYMetadata.py')
(mN1, mC1) = mass_extract(slha_file, ['1000022', '1000024'])
mglog.info('chargino1 mass = '+mC1+' neutralino1 mass = '+mN1)

if lifetime != 0:
    # remove chargino1 decay from slha file
    remove_decay(slha_file, '1000024')

build_param_card(param_card_old=slha_file, param_card_new='param_card.dat')

xqcut, alpsfact, scalefact = get_mg_variations(float(mC1), mg_syst_mod)
mglog.info("MG5 params: %s %s %s"%(xqcut, alpsfact, scalefact))

# Grab the run card and move it into place
extras = {'ktdurham': xqcut,
          'lhe_version': '2.0',
          'cut_decays': 'F',
          'pdlabel': pdlabel,
          'lhaid': lhaid,
          'drjj': 0.0}
build_run_card(run_card_old=get_default_runcard(),
               run_card_new='run_card.dat',
               xqcut=xqcut,
               nevts=nevts,
               rand_seed=rand_seed,
               beamEnergy=beamEnergy,
               scalefact=scalefact,
               alpsfact=alpsfact,
               extras=extras)

if generate(run_card_loc='run_card.dat', param_card_loc='param_card.dat', mode=0, njobs=1, run_name='Test', proc_dir=thedir):
    mglog.error('Error generating events!')

# Move output files into the appropriate place, with the appropriate name
the_spot = arrange_output(run_name='Test', proc_dir=thedir, outputDS='madgraph_OTF._00001.events.tar.gz')
if the_spot == '':
    mglog.error('Error arranging output dataset!')

mglog.info('Removing process directory...')
shutil.rmtree(thedir, ignore_errors=True)

mglog.info('All done generating events!!')

outputDS = the_spot

if xqcut < 0 or outputDS is None or '' == outputDS:
    evgenLog.warning('Looks like something went wrong with the MadGraph generation - bailing out!')
    raise RuntimeError('Error in MadGraph generation')

import os
if 'ATHENA_PROC_NUMBER' in os.environ:
    evgenLog.info('Noticed that you have run with an athena MP-like whole-node setup.  Will re-configure now to make sure that the remainder of the job runs serially.')
    njobs = os.environ.pop('ATHENA_PROC_NUMBER')
    # Try to modify the opts underfoot
    if not hasattr(opts, 'nprocs'):
        mglog.warning('Did not see option!')
    else:
        opts.nprocs = 0
    mglog.info(opts)

runArgs.qcut = xqcut
runArgs.inputGeneratorFile = outputDS
runArgs.gentype = 'C1N1,C1C1'
if mg_syst_mod:
    runArgs.syst_mod = mg_syst_mod
elif py8_syst_mod:
    runArgs.syst_mod = py8_syst_mod

# Pythia8 setup
genSeq.Pythia8.Commands += ["Init:showAllParticleData = on",
                            "Next:numberShowLHA = 10",
                            "Next:numberShowEvent = 10",
                            ]
if njets > 0:
    genSeq.Pythia8.Commands += ["Merging:mayRemoveDecayProducts = on",
                                "Merging:nJetMax = "+str(njets),
                                "Merging:doKTMerging = on",
                                "Merging:TMS = "+str(xqcut),
                                "Merging:ktType = 1",
                                "Merging:Dparameter = 0.4",
                                "Merging:Process = pp>{x1+,1000024}{x1-,-1000024}{n1,1000022}",
                                "1000024:spinType = 1",
                                "1000022:spinType = 1"]


# Configuration for EvgenJobTransforms
# --------------------------------------------------------------
evgenLog.info('Registered generation of mAMSB')

evgenConfig.contact = ['shimpei.yamamoto@cern.ch']
evgenConfig.keywords += ['SUSY', 'chargino', 'longLived']
evgenConfig.description = 'C1N1/C1C1 production, C1 being long lived (mass:%s, lifetime:%s, slha:%s)' % (mC1, lifetime, slha_file)
if lifetime != 0:
    evgenConfig.specialConfig = 'AMSBC1Mass=%s*GeV;AMSBN1Mass=%s*GeV;AMSBC1Lifetime=%s*ns;preInclude=SimulationJobOptions/preInclude.AMSB.py' % (mC1, mN1, lifetime)

evgenConfig.generators += ["EvtGen"]

if not hasattr(runArgs, 'inputGeneratorFile'):
    mglog.error('something went wrong with the file name.')
    runArgs.inputGeneratorFile = 'madgraph.*._events.tar.gz'
evgenConfig.inputfilecheck = runArgs.inputGeneratorFile.split('._0')[0]

# Generator Filter
if jetptmin > 0:
    include("MC15JobOptions/JetFilterAkt4.py")
    filtSeq.QCDTruthJetFilter.MinPt = jetptmin*GeV
if metmin > 0:
    include("MC15JobOptions/MissingEtFilter.py")
    filtSeq.MissingEtFilter.METCut = metmin*GeV
if jetptmin > 0 and metmin > 0:
    filtSeq.Expression = "(QCDTruthJetFilter) or (MissingEtFilter)"

# Clean up
del m0, m32, tanb, slha_file, mC1, mN1, lifetime, par, jetptmin, xqcut, alpsfact, scalefact
