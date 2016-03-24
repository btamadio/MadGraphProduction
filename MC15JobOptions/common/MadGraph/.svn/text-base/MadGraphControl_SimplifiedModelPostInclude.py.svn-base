# This comes after all Simplified Model setup files
from MadGraphControl.MadGraphUtils import SUSY_SM_Generation

# Set maximum number of events if the event multiplier has been modified
if evt_multiplier>0:
    if runArgs.maxEvents>0:
        nevts=runArgs.maxEvents*evt_multiplier
    else:
        nevts=5000*evt_multiplier

if njets<0:
    evgenLog.fatal('njets is not set')
    raise RuntimeError('njet is not set')

# Set up for grid pack running
gridpackDirName=None
if hasattr(runArgs, "inputGenConfFile"):
    gridpackDirName='madevent/'

if 'writeGridpack' not in dir():
    writeGridpack=False

# Pass arguments as a dictionary: the "decays" argument is not accepted in older versions of MadGraphControl
argdict = {'runArgs'  : runArgs,
           'process'  : process,
           'gentype'  : gentype,
           'decaytype': decaytype,
           'masses'   : masses,
           'decays'   : decays,
           }

if not SLHAonly:

    argdict.update({'nevts'          : nevts,
                    'syst_mod'       : syst_mod,
                    'writeGridpack'  : writeGridpack,
                    'gridpackDirName': gridpackDirName,
                    'keepOutput'     : keepOutput,
                    'pdlabel'        : "'nn23lo1'",
                    'lhaid'          : 247000,
                    })
    try:
        [qcut,outputDS] = SUSY_SM_Generation(**argdict)
    except TypeError:
        # Older version of MadGraphControl
        del argdict['decays']
        [qcut,outputDS] = SUSY_SM_Generation(**argdict)
else:
    argdict.update({'nevts'     : 10000,
                    'syst_mod'  : None,
                    'SLHAonly'  : True,
                    'keepOutput': keepOutput,
                    })
    try:
        [qcut,outputDS] = SUSY_SM_Generation(**argdict)
    except TypeError:
        # Older version of MadGraphControl
        del argdict['decays']
        [qcut,outputDS] = SUSY_SM_Generation(**argdict)
    
from __main__ import opts
if (qcut<0 or outputDS is None or ''==outputDS) and not opts.config_only:
    evgenLog.warning('Looks like something went wrong with the MadGraph generation - bailing out!')
    raise RuntimeError('Error in MadGraph generation')

import os
if 'ATHENA_PROC_NUMBER' in os.environ:
    evgenLog.info('Noticed that you have run with an athena MP-like whole-node setup.  Will re-configure now to make sure that the remainder of the job runs serially.')
    njobs = os.environ.pop('ATHENA_PROC_NUMBER')
    # Try to modify the opts underfoot
    if not hasattr(opts,'nprocs'): mglog.warning('Did not see option!')
    else: opts.nprocs = 0
    print opts

runArgs.qcut = qcut
runArgs.inputGeneratorFile = outputDS
if 'syst_mod' in dir():
    runArgs.syst_mod = syst_mod
runArgs.decaytype = decaytype
runArgs.gentype = gentype

# Pythia8 setup
genSeq.Pythia8.Commands += ["Init:showAllParticleData = on",
                            "Next:numberShowLHA = 10",
                            "Next:numberShowEvent = 10",
                            ]
if njets>0:
    genSeq.Pythia8.Commands += ["Merging:mayRemoveDecayProducts = on",
                                "Merging:nJetMax = "+str(njets),
                                "Merging:doKTMerging = on",
                                "Merging:TMS = "+str(qcut),
                                "Merging:ktType = 1",
                                "Merging:Dparameter = 0.4",
                                "Merging:nQuarksMerge = 4"]

if hasattr(runArgs,'syst_mod') and runArgs.syst_mod is not None:
    evgenLog.error('No known equivalent for systematics in Pythia8!')


# Configuration for EvgenJobTransforms
#--------------------------------------------------------------
evgenConfig.generators += ["EvtGen"]

if not hasattr(runArgs,'inputGeneratorFile'):
    print 'ERROR: something wasnt write in file name transfer from the fragment.'
    runArgs.inputGeneratorFile='madgraph.*._events.tar.gz'
evgenConfig.keywords += ["SUSY"]
if not opts.config_only:
    evgenConfig.inputfilecheck = runArgs.inputGeneratorFile.split('._0')[0]
