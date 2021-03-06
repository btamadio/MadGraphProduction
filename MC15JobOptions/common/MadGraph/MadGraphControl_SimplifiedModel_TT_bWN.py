include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPreInclude.py' )

masses['1000006'] = float(runArgs.jobConfig[0].split('_')[4])
masses['1000022'] = float(runArgs.jobConfig[0].split('_')[5].split('.')[0])

if masses['1000022']<0.5: masses['1000022']=0.5

gentype = str(runArgs.jobConfig[0].split('_')[2])
decaytype = str(runArgs.jobConfig[0].split('_')[3])

process = '''
generate p p > t1 t1~ $ go susylq susylq~ b1 b2 t2 b1~ b2~ t2~ @1
add process p p > t1 t1~ j $ go susylq susylq~ b1 b2 t2 b1~ b2~ t2~ @2
add process p p > t1 t1~ j j $ go susylq susylq~ b1 b2 t2 b1~ b2~ t2~ @3
'''
njets = 2
evgenLog.info('Registered generation of stop pair production, stop to t+LSP;grid point ' + str(runArgs.runNumber) + ' decoded into mass point ' + str(masses['1000006']))

evgenConfig.contact  = [ "Alaettin.Serhan.Mete@cern.ch" ]
evgenConfig.keywords += ['simplifiedModel', 'stop']
evgenConfig.description = 'stop direct pair production, st->b+W+LSP in simplified model, m_stop = %s GeV, m_N1 = %s GeV'%(masses['1000006'],masses['1000022'])

if '2L15' in runArgs.jobConfig[0].split('_')[-1]:
    evgenLog.info('2Lepton15 filter is applied')
    include ( 'MC15JobOptions/MultiElecMuTauFilter.py' )
    filtSeq.MultiElecMuTauFilter.MinPt  = 15000.
    filtSeq.MultiElecMuTauFilter.MaxEta = 2.8
    filtSeq.MultiElecMuTauFilter.NLeptons = 2
    filtSeq.MultiElecMuTauFilter.IncludeHadTaus = 0
    filtSeq.Expression = "MultiElecMuTauFilter"
    evt_multiplier = 50

elif '1L20orMET60' in runArgs.jobConfig[0].split('_')[-1]:
    evgenLog.info('1Lepton or MET60 filter is applied')
    include ( 'MC15JobOptions/MultiElecMuTauFilter.py' )
    filtSeq.MultiElecMuTauFilter.MinPt  = 20000.
    filtSeq.MultiElecMuTauFilter.MaxEta = 2.8
    filtSeq.MultiElecMuTauFilter.NLeptons = 1
    filtSeq.MultiElecMuTauFilter.IncludeHadTaus = 0
    include ( 'MC15JobOptions/MissingEtFilter.py' )
    filtSeq.MissingEtFilter.METCut = 60000.
    filtSeq.Expression = "MultiElecMuTauFilter or MissingEtFilter"
    evt_multiplier = 3

include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPostInclude.py' )

if njets>0:
    genSeq.Pythia8.Commands += ["Merging:Process = pp>{t1,1000006}{t1~,-1000006}"]
