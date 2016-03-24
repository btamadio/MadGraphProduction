from AthenaCommon import Logging
log = Logging.logging.getLogger('Generate.Gluino')

if not 'evgenConfig' in dir():
    raise RuntimeError('These jobOptions should be run through Generate_tf.py')

# setup Herwig++
include ( 'MC15JobOptions/Herwigpp_UEEE5_CTEQ6L1_Common.py' )
include ( 'MC15JobOptions/Herwigpp_EvtGen.py')

# Points
masses = {}
try:
    masses['1000021'] = float(runArgs.jobConfig[0].split('_')[5])
    masses['1000022'] = float(runArgs.jobConfig[0].split('_')[6].split('.')[0])
    dsid  = float(runArgs.runNumber)
except:
    raise RuntimeError('DSID %s is not found in the grid point dictionary. Aborting!' % runArgs.runNumber)

include ( 'MC15JobOptions/SUSYMetadata.py' )
slha_file = 'susy.%i.GG_ttN1UDD.slha'%(dsid)
build_slha_file(param_card_old='param_card.SM.GG.ttN1UDD.dat',param_card_new=slha_file,masses=masses)

# Add Herwig++ parameters for this process
include ( 'MC15JobOptions/Herwigpp_SUSYConfig.py' )
cmds = buildHerwigppCommands(['gluino'], slha_file, 'TwoParticleInclusive')

# define metadata
evgenConfig.description = 'gluino grid (Gtt) generation with RPV UDD decays, m_gluino = %s GeV, m_N1 = %s GeV'%(masses['1000021'],masses['1000022'])
evgenConfig.keywords = ['SUSY','simplifiedModel','gluino','RPV']
evgenConfig.contact  = ['Jamie.Boyd@cern.ch']

# print checks
log.info('*** Begin Herwig++ commands ***')
log.info(cmds)
log.info('*** End Herwig++ commands ***')

# Set the command vector
genSeq.Herwigpp.Commands += cmds.splitlines()

# clean up
del cmds

