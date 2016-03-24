# Generator transform pre-include
#  Gets us ready for on-the-fly SUSY SM generation
include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPreInclude.py' )
# Simple variable setups

gentype=runArgs.jobConfig[0].split('SM')[1].split('_')[1]
if 'SLN1' in runArgs.jobConfig[0]: decaytype='onestepN2_SLN1'
elif 'ZN1' in runArgs.jobConfig[0]: decaytype='onestepN2_ZN1'

mass_string = runArgs.jobConfig[0].replace('.py','').split('N1_')[1]

if gentype=='GG':
# Direct gluino decay to LSP (0-lepton, grid 1 last year)
    masses['1000021'] = float( mass_string.split('_')[0] )  #gluino
    masses['1000022'] = float( mass_string.split('_')[1] )  #chi10
    masses['1000023'] = 0.5*(masses['1000021']+masses['1000022'])  #chi20

    if 'SL' in decaytype:
        masses['1000011'] = 0.5*(masses['1000022']+masses['1000023'])  #slepton
        masses['1000012'] = 0.5*(masses['1000022']+masses['1000023'])  #slepton
        masses['1000013'] = 0.5*(masses['1000022']+masses['1000023'])  #slepton
        masses['1000014'] = 0.5*(masses['1000022']+masses['1000023'])  #slepton
        masses['1000015'] = 0.5*(masses['1000022']+masses['1000023'])  #slepton
        masses['1000016'] = 0.5*(masses['1000022']+masses['1000023'])  #slepton
    else:
        masses['1000011'] = 4.5e5 #slepton
        masses['1000012'] = 4.5e5 #slepton
        masses['1000013'] = 4.5e5 #slepton
        masses['1000014'] = 4.5e5 #slepton
        masses['1000015'] = 4.5e5 #slepton
        masses['1000016'] = 4.5e5 #slepton
        
    process = '''
    generate p p > go go
    add process p p > go go j
    '''

# This comes after all Simplified Model setup files
evgenLog.info('Will use Pythia8...')

#--------------------------------------------------------------
# Algorithms Private Options
#--------------------------------------------------------------
pythia = genSeq.Pythia8



evgenConfig.contact  = [ "emma.sian.kuwertz@cern.ch" ]
if 'GG' in gentype: evgenConfig.keywords += ['simplifiedModel','gluino']
elif 'SS' in gentype: evgenConfig.keywords += ['simplifiedModel','squark']
elif 'BB' in gentype: evgenConfig.keywords += ['simplifiedModel','sbottom']
if 'SL' in decaytype:
    evgenConfig.description = 'SUSY Simplified Model with gluino production and decays via sleptons with MadGraph/Pythia8, m_glu = %s GeV, m_N2 = %s GeV, m_slep = %s GeV, m_N1 = %s GeV'%(masses['1000021'],masses['1000023'],masses['1000011'],masses['1000022'])
    evgenConfig.keywords += ['slepton']
else:
    evgenConfig.description = 'SUSY Simplified Model with gluino production and decays via Z with MadGraph/Pythia8, m_glu = %s GeV, m_N2 = %s GeV, m_N1 = %s GeV'%(masses['1000021'],masses['1000023'],masses['1000022'])
    evgenConfig.keywords += ['Z']

# Two-lepton filter
if '2L' in runArgs.jobConfig[0]:
    evt_multiplier = 50
    include('MC15JobOptions/MultiLeptonFilter.py')
    MultiLeptonFilter = filtSeq.MultiLeptonFilter
    MultiLeptonFilter.Ptcut = 5000.
    MultiLeptonFilter.Etacut = 2.8
    MultiLeptonFilter.NLeptons = 2

njets = 1
include('MC15JobOptions/MadGraphControl_SimplifiedModelPostInclude.py')

if gentype=='SS':
    pythia.Commands += ["Merging:Process = pp>{ul,1000002}{ul~,-1000002}{ur,2000002}{ur~,-2000002}{dl,1000001}{dl~,-1000001}{dr,2000001}{dr~,-2000001}{sl,1000003}{sl~,-1000003}{sr,2000003}{sr~,-2000003}{cl,1000004}{cl~,-1000004}{cr,2000004}{cr~,-2000004}"]
elif gentype=='GG':
    pythia.Commands += ["Merging:Process = pp>{go,1000021}{go,1000021}"]
elif gentype=='BB':
    pythia.Commands += ["Merging:Process = pp>{b1,1000005}{b1~,-1000005}"]

if 'Z' in decaytype:
    pythia.Commands += ["23:mMin = 0.2"]
