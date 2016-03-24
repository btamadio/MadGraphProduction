include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPreInclude.py' )

JOName = os.path.basename(runArgs.jobConfig[0])

gentype = JOName.split('_')[2]
decaytype = JOName.split('_')[3]

masses['1000006'] = float(JOName.split('_')[4])
masses['1000022'] = float(JOName.split('_')[5])
if masses['1000022']<0.5: masses['1000022']=0.5

process = '''
generate p p > t1 t1~ $ go susylq susylq~ b1 b2 t2 b1~ b2~ t2~ @1
add process p p > t1 t1~ j $ go susylq susylq~ b1 b2 t2 b1~ b2~ t2~ @2
add process p p > t1 t1~ j j $ go susylq susylq~ b1 b2 t2 b1~ b2~ t2~ @2
'''

njets = 2

if 'MET' in JOName.split('_')[-1]:
    metFilter = JOName.split('_')[-1]
    metFilter = int(metFilter.split("MET")[1].split(".")[0])
    
    print "Using MET Filter: " + str(metFilter)
    
    if metFilter != 100 and metFilter != 250:
        print "Unknown MET filter!"
    else:
        include ( 'MC15JobOptions/MissingEtFilter.py' )
        if metFilter == 100:
            print "Filter on MET: 100-250 GeV"
            filtSeq.MissingEtFilter.METCut = 100*GeV
            filtSeq.MissingEtFilterUpperCut.METCut = 250*GeV
            evt_multiplier = 10
            
        elif metFilter == 250:
            print "Filter on MET: >250 GeV"
            filtSeq.MissingEtFilter.METCut = 250*GeV
            evt_multiplier = 40
    
    print
                
        
evgenLog.info('Registered generation of stop pair production, stop to c+LSP; grid point '+str(runArgs.runNumber)+' decoded into mass point mstop=' + str(masses['1000006']) + ', mlsp='+str(masses['1000022']))

evgenConfig.contact  = [ "jan.schaeffer@cern.ch" ]
evgenConfig.keywords += ['simplifiedModel','charm']
evgenConfig.description = 'stop direct pair production, st->c+LSP in simplified model'

include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPostInclude.py' )

if njets>0:
    genSeq.Pythia8.Commands += ["Merging:Process = pp>{t1,1000006}{t1~,-1000006}"]
