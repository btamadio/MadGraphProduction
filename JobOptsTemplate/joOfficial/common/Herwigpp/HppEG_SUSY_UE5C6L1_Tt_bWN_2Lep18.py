# SUSY Herwig++ jobOptions for direct stop pair production grid
# Use SUSYHIT and bottom-up schema for SLHA files

from AthenaCommon import Logging
log = Logging.logging.getLogger('Generate.Stop')

if not 'evgenConfig' in dir():
    raise RuntimeError('These jobOptions should be run through Generate_tf.py')

# setup Herwig++
include ( 'MC15JobOptions/Herwigpp_UEEE5_CTEQ6L1_Common.py' )
include ( 'MC15JobOptions/Herwigpp_EvtGen.py')

# Points
try:
    mstop = float(runArgs.jobConfig[0].split('_')[4].split('t')[1])
    mn1   = float(runArgs.jobConfig[0].split('_')[5].split('.')[0].split('n')[1])
    dsid  = float(runArgs.runNumber)
except:
    raise RuntimeError('DSID %s is not found in the grid point dictionary. Aborting!' % runArgs.runNumber)

# define spectrum file name
slha_file = 'susy.%06d.Tt_bWN_t%03d_n%03d.slha' % (dsid,mstop,mn1)

# Add Herwig++ parameters for this process
include ( 'MC15JobOptions/Herwigpp_SUSYConfig.py' )
cmds = buildHerwigppCommands(['stop1'], slha_file, 'TwoParticleInclusive')

# define metadata
evgenConfig.description = 'stop grid generation with three-body decays, m_stop = %s GeV, m_N1 = %s GeV'%(mstop,mn1)
evgenConfig.keywords = ['SUSY','simplifiedModel','stop']
evgenConfig.contact  = ['Alaettin.Serhan.Mete@cern.ch']

# print checks
log.info('*** Begin Herwig++ commands ***')
log.info(cmds)
log.info('*** End Herwig++ commands ***')

# Set the command vector
genSeq.Herwigpp.Commands += cmds.splitlines()

# clean up
del cmds

#============================================================
#
# Filter events
#
#############################################################

# Include MultiElecMuTauFilter
include ( 'MC15JobOptions/MultiElecMuTauFilter.py' )
filtSeq.MultiElecMuTauFilter.MinPt  = 18000.
filtSeq.MultiElecMuTauFilter.MaxEta = 2.8
filtSeq.MultiElecMuTauFilter.NLeptons = 2
filtSeq.MultiElecMuTauFilter.IncludeHadTaus = 0

filtSeq.Expression = "MultiElecMuTauFilter"

#==============================================================
#
# End of job options file
#
###############################################################
