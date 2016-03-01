include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPreInclude.py' )
include ( 'MC15JobOptions/calculateWidth.py' )
masses['1000021'] = float(runArgs.jobConfig[0].split('_')[4])
masses['1000022'] = float(runArgs.jobConfig[0].split('_')[5])
if masses['1000022']<0.5: masses['1000022']=0.5
for squark in squarksl:
    masses[str(squark)] = float(runArgs.jobConfig[0].split('_')[6].split('.')[0])
    decays[str(squark)] = 'DECAY   '+str(squark)+'     '+str(calculateWidth(float(masses['1000021']),float(masses[str(squark)])))
gentype = str(runArgs.jobConfig[0].split('_')[2])
decaytype = str(runArgs.jobConfig[0].split('_')[3])
process = '''
generate p p > go go @1
add process p p > go go j $ sq @2
add process p p > go go j j $ sq @3
add process p p > go sq, sq > go j @4
add process p p > go sq j $ sq, sq > go j @5
add process p p > sq sq, sq > go j @6
'''
njets = 2
evgenLog.info('Registered generation of gluino grid '+str(runArgs.runNumber))

evgenConfig.contact  = [ "brian.thomas.amadio@cern.ch" ]
evgenConfig.keywords += ['simplifiedModel','gluino']
evgenConfig.description = 'gluino production in simplified model'

include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPostInclude.py' )

if njets>0:
    genSeq.Pythia8.Commands += ["Merging:Process = pp>{go,1000021}{go,1000021}"]
