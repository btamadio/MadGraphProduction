## Herwig++ job option file for SUSY GMSB processes

## Setup Herwig++
include ( 'MC15JobOptions/Herwigpp_UEEE5_CTEQ6L1_Common.py' )

# define spectrum file name
dsid = int(runArgs.runNumber)
splitconfig = runArgs.jobConfig[0].split('/')[-1].split('.')[2].split('_')
slhaconfig = '_'.join(splitconfig[2:6])
slha_file = 'susy.%i.%s.slha'%(dsid,slhaconfig)

# Add Herwig++ parameters for this process
include ( 'MC15JobOptions/Herwigpp_SUSYConfig.py' )
include ( 'MC15JobOptions/Herwigpp_EvtGen.py' )
cmds = buildHerwigppCommands(['all'], slha_file) 

## Define metadata
evgenConfig.description = 'GMSB signal grid with stau/slepton NLSP, Lambda = %s TeV, tanbeta = %s'%(splitconfig[4].replace('Lambda',''), splitconfig[5].replace('tanbeta',''))
evgenConfig.keywords    = ['SUSY','GMSB']
evgenConfig.contact     = ['oliver.ricken@cern.ch', 'bertrand.martindl@cern.ch']

# print checks
log.info('*** Begin Herwig++ commands ***')
log.info(cmds)
log.info('*** End Herwig++ commands ***')


# Set the command vector
genSeq.Herwigpp.Commands += cmds.splitlines()

# clean up
del cmds


