include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPreInclude.py' )

masses['1000006'] = float(runArgs.jobConfig[0].split('_')[4])
masses['1000024'] = float(runArgs.jobConfig[0].split('_')[5])
masses['1000022'] = float(runArgs.jobConfig[0].split('_')[6].split('.')[0])
if masses['1000022']<0.5: masses['1000022']=0.5
gentype = str(runArgs.jobConfig[0].split('_')[2])
decaytype = str(runArgs.jobConfig[0].split('_')[3])
process = '''
generate p p > t1 t1~ $ go susylq susylq~ b1 b2 t2 b1~ b2~ t2~ @1
add process p p > t1 t1~ j $ go susylq susylq~ b1 b2 t2 b1~ b2~ t2~ @2
add process p p > t1 t1~ j j $ go susylq susylq~ b1 b2 t2 b1~ b2~ t2~ @3
'''

njets = 2
evgenLog.info('Registered generation of stop pair production, stop to b+chargino; grid point '+str(runArgs.runNumber)+' decoded into mass point ' + str(masses['1000006']))

if '1Lep20orMET60' in runArgs.jobConfig[0].split('_')[-1]:

    evgenLog.info('1lepton or MET60 filter is applied')
    include ( 'MC15JobOptions/LeptonFilter.py' )
    filtSeq.LeptonFilter.Ptcut  = 20000.
    filtSeq.LeptonFilter.Etacut = 2.8 
    include('MC15JobOptions/MissingEtFilter.py')
    filtSeq.MissingEtFilter.METCut = 60000.
    filtSeq.Expression = "LeptonFilter or MissingEtFilter"

    evt_multiplier = 3.0

elif 'MET60' in runArgs.jobConfig[0].split('_')[-1]:
    evgenLog.info('MET60 filter is applied')
    include ( 'MC15JobOptions/MissingEtFilter.py' )

    filtSeq.MissingEtFilter.METCut = 60*GeV

    evt_multiplier = 10.

elif '2Lep18' in runArgs.jobConfig[0].split('_')[-1]:
    
    evgenLog.info('2lepton filter is applied')
    include ( 'MC15JobOptions/MultiElecMuTauFilter.py' )
    filtSeq.MultiElecMuTauFilter.MinPt  = 18000.
    filtSeq.MultiElecMuTauFilter.MaxEta = 2.8
    filtSeq.MultiElecMuTauFilter.NLeptons = 2
    filtSeq.MultiElecMuTauFilter.IncludeHadTaus = 0
    
    filtSeq.Expression = "MultiElecMuTauFilter"

    evt_multiplier = 50.0
    
evgenConfig.contact  = [ "takashi.yamanaka@cern.ch" ]
evgenConfig.keywords += ['simplifiedModel']
evgenConfig.description = 'stop direct pair production, st->b+chargino in simplified model, m_stop = %s GeV, m_C1 = %s GeV, m_N1 = %s GeV'%(masses['1000006'],masses['1000024'],masses['1000022'])

genSeq.Pythia8.Commands += ["24:mMin = 0.2"]

include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPostInclude.py' )

if njets>0:
    genSeq.Pythia8.Commands += ["Merging:Process = pp>{t1,1000006}{t1~,-1000006}"]
