include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPreInclude.py' )

for q in squarksl: masses[q] = float(runArgs.jobConfig[0].split('_')[4])
masses['1000024'] = float(runArgs.jobConfig[0].split('_')[5])
masses['1000022'] = float(runArgs.jobConfig[0].split('_')[6].split('.')[0])
if masses['1000022']<0.5: masses['1000022']=0.5
genSeq.Pythia8.Commands += ["24:mMin = 0.2"]
genSeq.Pythia8.Commands += ["23:mMin = 0.2"]


gentype = str(runArgs.jobConfig[0].split('_')[2])
decaytype = str(runArgs.jobConfig[0].split('_')[3])
process = '''
define susylqL = ul dl cl sl
define susylqL~ = ul~ dl~ cl~ sl~
define susylqR = ur dr cr sr
define susylqR~ = ur~ dr~ cr~ sr~
generate p p > susylqL susylqL~ $ go susyweak susylqR susylqR~ @1
add process p p > susylqL susylqL~ j $ go susyweak susylqR susylqR~ @2
add process p p > susylqL susylqL~ j j $ go susyweak susylqR susylqR~ @3
'''

njets = 2
evt_multiplier = 4
evgenLog.info('Registered generation of squark grid '+str(runArgs.runNumber))



evgenConfig.contact  = [ "ljiljana.morvaj@cern.ch" ]
evgenConfig.keywords += ['simplifiedModel', 'squark']
evgenConfig.description = 'squark production in simplified model, one-step decays through chargino, m_sq = %s GeV, m_C1 = %s GeV, m_N1 = %s GeV'%(masses[squarks[0]],masses['1000024'],masses['1000022'])

include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPostInclude.py' )

if njets>0:
    genSeq.Pythia8.Commands += ["Merging:Process = pp>{ul,1000002}{ul~,-1000002}{dl,1000001}{dl~,-1000001}{sl,1000003}{sl~,-1000003}{cl,1000004}{cl~,-1000004}"]


