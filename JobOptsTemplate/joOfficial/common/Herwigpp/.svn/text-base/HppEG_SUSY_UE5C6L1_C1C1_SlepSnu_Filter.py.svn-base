## Herwig++ job option file for Susy 2-parton -> 2-sparticle processes

## Get a handle on the top level algorithms' sequence
from AthenaCommon import Logging
log = Logging.logging.getLogger('Generate.SMModeCDG')

if not 'evgenConfig' in dir():
    raise RuntimeError('These jobOptions should be run through Generate_trf.py')

## Setup Herwig++
include ( 'MC15JobOptions/Herwigpp_UEEE5_CTEQ6L1_Common.py' )
include ( 'MC15JobOptions/Herwigpp_EvtGen.py')

# Points
try:
    gentype   = str(runArgs.jobConfig[0].split('_')[2])
    decaytype = str(runArgs.jobConfig[0].split('_')[3])
    dsid      = float(runArgs.runNumber)
    xln       = str(runArgs.jobConfig[0].split('_')[4])
    mc1       = str(runArgs.jobConfig[0].split('_')[5])
    mn1       = str(runArgs.jobConfig[0].split('_')[6])
except:
    raise RuntimeError('DSID %s is not found in the grid point dictionary. Aborting!' % runArgs.runNumber)

# define spectrum file name
slha_file = 'susy.%06d.%s_%s_%s_%s_%s.slha' % (dsid,gentype,decaytype,xln,mc1,mn1)

# Add Herwig++ parameters for this process
include ( 'MC15JobOptions/Herwigpp_SUSYConfig.py' )

# Add Herwig++ parameters for this process
cmds = buildHerwigppCommands(['~chi_1+','~chi_1-'],slha_file,'Exclusive')

## Define metadata
evgenConfig.contact = ['Alaettin.Serhan.Mete@cern.ch']
evgenConfig.keywords += ['SUSY', 'gaugino', 'chargino', 'slepton', 'sneutrino']
evgenConfig.description = '~chi1+/~chi1- production, decay via slepton/sneutrino in simplified model, m_C1 = %s GeV, m_N1 = %s GeV, x = %s'%(mc1.replace('p','.'),mn1.replace('p','.'),xln.strip('x').replace('p','.'))

## Print checks
log.info('*** Begin Herwig++ commands ***')
log.info(cmds)
log.info('*** End Herwig++ commands ***')

## Set the command vector
genSeq.Herwigpp.Commands += cmds.splitlines()

# clean up
del cmds

## Lepton filter
if '2L8' in runArgs.jobConfig[0].split('_')[-1]:
    evgenLog.info('2lepton8 filter is applied')

    include ( 'MC15JobOptions/MultiElecMuTauFilter.py' )
    filtSeq.MultiElecMuTauFilter.NLeptons  = 2
    filtSeq.MultiElecMuTauFilter.MinPt = 8000.         # pt-cut on the lepton
    filtSeq.MultiElecMuTauFilter.MaxEta = 2.8          # stay away from MS 2.7 just in case
    filtSeq.MultiElecMuTauFilter.IncludeHadTaus = 0    # don't include hadronic taus

    filtSeq.Expression = "MultiElecMuTauFilter"
