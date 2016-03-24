include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPreInclude.py' ) 

if "LLE" not in runArgs.jobConfig[0]:
	raise RuntimeError("This File is made for RPVLLE models.")


evgenConfig.keywords += ["simplifiedModel","RPV"]

JobOptionsFile = runArgs.jobConfig[0][runArgs.jobConfig[0].find("MC15.") : ]
JobArguments =  JobOptionsFile.strip(".py").split("_")

#ReadIn the Parameters
Model=JobArguments[2]
NLSPMass=int(JobArguments[3])
LSPMass=int(JobArguments[4])
decaytype = JobArguments[5]

if decaytype == "LLE12k":
	evgenConfig.keywords += ["Lambda121","Lambda122"]
elif decaytype == "LLEi33":
	evgenConfig.keywords += ["Lambda133","Lambda233"]
	
genSeq.Pythia8.Commands += ["25:mMin = 0.2"] #Allow in Pythia8 off shell Higgs
genSeq.Pythia8.Commands += ["24:mMin = 0.2"] #Allow in Pythia8 off shell Z
genSeq.Pythia8.Commands += ["23:mMin = 0.2"] #Allow in Pythia8 off shell W

if LSPMass > NLSPMass:
	raise RuntimeError("The given LSP Mass %i is greater than the NLSP mass %i"%(LSPMass,NLSPMass))


njets = 2

if Model.startswith("C1C1"):
	masses ['1000022' ] = LSPMass
	masses ['1000024' ] = NLSPMass
	genSeq.Pythia8.Commands += ["1000022:mMin = "+str(LSPMass-1)]
	gentype="C1C1"
	evgenConfig.keywords += ['gaugino','neutralino']
	process='''
define killpartx1 = susystrong h1 h2 h3 h- h+
generate p p > x1+ x1- / killpartx1 @1
add process p p > x1+ x1- j / killpartx1 @2
add process p p > x1+ x1- j j / killpartx1 @3
'''	
	if decaytype == "LLE12k":
		evgenConfig.description = 'RPV-LLE simplified model. ~chi1+~chi1- production, decay into W + LSP. LSP decays via non zero Lambda_12k. m_C1 = %s GeV, m_N1 = %s GeV'%(masses['1000024'],masses['1000022'])
	elif decaytype == "LLEi33":
		evgenConfig.description = 'RPV-LLE simplified model. ~chi1+~chi1- production, decay into W + LSP. LSP decays via non zero Lambda_i33. m_C1 = %s GeV, m_N1 = %s GeV'%(masses['1000024'],masses['1000022'])

	if njets>0:
		genSeq.Pythia8.Commands += [ "Merging:Process = pp>{x1+,1000024}{x1-,-1000024}",
					     "1000024:spinType = 1" ]
else:
	raise RuntimeError("Unrecognised production mode %s"%(Model))

	


evgenConfig.contact  = [ "johannes.josef.junggeburth@cern.ch" ]

include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPostInclude.py' )
