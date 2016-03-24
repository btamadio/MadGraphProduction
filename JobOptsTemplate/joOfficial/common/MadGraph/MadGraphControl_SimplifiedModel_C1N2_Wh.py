include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPreInclude.py' )

def MassToFloat(s):
  if "p" in s:
    return float(s.replace("p", "."))
  return float(s)

splitConfig = runArgs.jobConfig[0].rstrip('.py').split('_')

#C1/N2 degenerate
masses['1000024'] = MassToFloat(splitConfig[5])
masses['1000023'] = MassToFloat(splitConfig[5])
masses['1000022'] = MassToFloat(splitConfig[6])
if masses['1000022']<0.5: masses['1000022']=0.5

#will be C1N2
gentype = splitConfig[2]
#will be Wha ->all higgs decays, or Whb only h->gamma gamma 
if splitConfig[4] == 'hall':
  decaytype = 'Whall'
  descriptionid= 'h -> all'
if splitConfig[4] == 'hgg':
  decaytype = 'Whgg'
  descriptionid= 'h -> gamma gamma'
process = '''
generate p p > x1+ n2 $ susystrong \@1
add process p p > x1- n2 $ susystrong \@2
add process p p > x1+ n2 j $ susystrong \@3
add process p p > x1- n2 j $ susystrong \@4
add process p p > x1+ n2 j j $ susystrong \@5
add process p p > x1- n2 j j $ susystrong \@6
'''
njets = 2
evgenLog.info('Registered generation of ~chi1+/- ~chi20 production, decay via Wh '+descriptionid+'; grid point '+str(runArgs.runNumber)+' decoded into mass point ' + str(masses['1000024']) + ' ' + str(masses['1000022']))

evgenConfig.contact  = [ "acervell@cern.ch" ]
evgenConfig.keywords += ['gaugino', 'chargino', 'neutralino']
evgenConfig.description = '~chi1+/- ~chi20 production, decay via Wh, %s, in simplified model, m_C1N2 = %s GeV, m_N1 = %s GeV'%(descriptionid,masses['1000024'],masses['1000022'])

genSeq.Pythia8.Commands += [ "24:mMin = 0.2", "23:mMin = 0.2" ]

if  'Whall' in decaytype:
    evgenLog.info('h->all will be generated')  
if  'Whgg' in decaytype:
    evgenLog.info('only h->gamma gamma will be generated')  
if 'le' in splitConfig[7]: # Use '3L' for new samples
    evgenLog.info('only W->lep will be generated')
    genSeq.Pythia8.Commands += [
        "24:onMode = off", #switch off all W decays
        "24:onIfAny = 11 13 15", # switch on W->lnu
        ]

if 'had' in splitConfig[7]: # Use '3L' for new samples
    evgenLog.info('only W->hadron will be generated')
    genSeq.Pythia8.Commands += [
        "24:onMode = off", #switch off all W decays
        "24:onIfAny = 1 2 3 4 5" # switch on W->qqbar
        ]
#--------------------------------------------------------------
# add some filter here
#--------------------------------------------------------------

# need more events from MG due to filter - this needs to be set before MadGraphControl_SimplifiedModelPostInclude.py is run (it's set at 2 there)
# 3 is only sufficient for large mass splittings
#evt_multiplier = 3

#filter for 3lep with low dM

include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPostInclude.py' )

if njets>0:
    genSeq.Pythia8.Commands += [ "Merging:Process = pp>{x1+,1000024}{x1-,-1000024}{n2,1000023}",
                                 "1000024:spinType = 1",
                                 "1000023:spinType = 1" ]
