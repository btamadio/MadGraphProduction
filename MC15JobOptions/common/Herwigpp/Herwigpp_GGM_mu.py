# SUSY GGM Herwig++ Mc15 jobOptions for photon+jets analysis
# electroweak production

from AthenaCommon import Logging
log = Logging.logging.getLogger('Generate.GGM_mu')

# setup Herwig++
include('MC15JobOptions/Herwigpp_UEEE5_CTEQ6L1_Common.py')
include('MC15JobOptions/Herwigpp_SUSYConfig.py')
include('MC15JobOptions/Herwigpp_EvtGen.py')

# define spectrum file name
dsid = runArgs.runNumber
split_config = runArgs.jobConfig[0].split('/')[-1].split('.')[2].split('_')
mu = split_config[-1]

slha_file = 'susy.%i.GGM_mu_%s.slha' % (dsid, mu)

# Add Herwig++ parameters for this process
cmds = buildHerwigppCommands(['gauginos'], slha_file, 'TwoParticleInclusive')

# define metadata
evgenConfig.description = 'GGM (EWK) mu grid, higgsino like neutralino, decay to photon/Z, mu>0, mu = %s GeV'%(mu)
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
