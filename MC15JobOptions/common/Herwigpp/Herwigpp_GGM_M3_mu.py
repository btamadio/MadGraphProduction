# SUSY GGM Herwig++ MC15 jobOptions for photon+jets analysis
# gluino-gluino production

from AthenaCommon import Logging
log = Logging.logging.getLogger('Generate.GGM_M3_mu')

# setup Herwig++
include('MC15JobOptions/Herwigpp_UEEE5_CTEQ6L1_Common.py')
include('MC15JobOptions/Herwigpp_SUSYConfig.py')
include('MC15JobOptions/Herwigpp_EvtGen.py')

# define spectrum file name
dsid = runArgs.runNumber
split_config = runArgs.jobConfig[0].split('/')[-1].split('.')[2].split('_')
m3, mu = split_config[-2:]

slha_file = 'susy.%i.GGM_M3_mu_%s_%s.slha'%(dsid, m3, mu)

# Add Herwig++ parameters for this process
cmds = buildHerwigppCommands(['gluino'], slha_file, 'TwoParticleInclusive')

# define metadata
evgenConfig.description = 'GGM (strong) M3/mu grid, higgsino like neutralino, decay to photon/Z, mu>0, M3 = %s GeV, mu = %s GeV'%(m3,mu)
evgenConfig.keywords = ['SUSY', 'GMSB', 'gluino', 'Higgsino']
evgenConfig.contact  = ['falonso@cern.ch']

# print checks
log.info('*** Begin Herwig++ commands ***')
log.info(cmds)
log.info('*** End Herwig++ commands ***')

# Set the command vector
genSeq.Herwigpp.Commands += cmds.splitlines()

# clean up
del cmds
