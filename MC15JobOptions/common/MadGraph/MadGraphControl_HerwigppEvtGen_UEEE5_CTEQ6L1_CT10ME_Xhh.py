from MadGraphControl.MadGraphUtils import *

mode=0


run_number=runArgs.runNumber
if(run_number>run_number_max) :
  log.fatal('Run number out of validity range for this generation. run_number_max '+str(run_number_max))
  raise RunTimeError('Run number too high.')
    
imass=run_number-run_number_min

def numbers_to_mass(argument):
    switcher = {
        0: 260.,
        1: 300.,
        2: 400.,
        3: 500.,
        4: 600.,
        5: 700.,
        6: 800.,
        7: 900.,
        8: 1000.,
        9: 1100.,
       10: 1200.,
       11: 1300.,
       12: 1400.,
       13: 1500.,
       14: 1600.,
       15: 1800.,
       16: 2000.,
       17: 2250.,
       18: 2500.,
       19: 2750.,
       20: 3000.
    }
    return switcher.get(argument, "nothing")

mX = numbers_to_mass(imass)
scale = mX/2.
 

#---------------------------------------------------------------------------------------------------
# Setting mHH and WHH for param_card.dat
#---------------------------------------------------------------------------------------------------
parameters={'1560':str(mX), #MHH
            '1561':'1.000000e-02'} #WHH

#---------------------------------------------------------------------------------------------------
# Setting higgs mass to 125 GeV for param_card.dat
#---------------------------------------------------------------------------------------------------
higgsMass={'25':'1.250900e+02'} #MH

#---------------------------------------------------------------------------------------------------
# Setting some parameters for run_card.dat
#---------------------------------------------------------------------------------------------------
extras = { 'lhe_version':'3.0', 
           'cut_decays':'F', 
           'pdlabel':'lhapdf',
           'lhaid':'10800', 
           'scale':str(scale),
           'dsqrt_q2fact1':str(scale),
           'dsqrt_q2fact2':str(scale),      
           'parton_shower':'HERWIGPP',
           'ptj':'0',
           'ptb':'0',
           'pta':'0',
           'ptjmax':'-1',
           'ptbmax':'-1',
           'ptamax':'-1',
           'etaj':'-1',
           'etab':'-1',
           'etaa':'-1',
           'etajmin':'0',
           'etabmin':'0',
           'etaamin':'0',
           'mmaa':'0',
           'mmaamax':'-1',
           'mmbb':'0',
           'mmbbmax':'-1',
           'drjj':'0',
           'drbb':'0',
           'draa':'0',
           'drbj':'0',
           'draj':'0',
           'drab':'0',
           'drjjmax':'-1',
           'drbbmax':'-1',
           'draamax':'-1',
           'drbjmax':'-1',
           'drajmax':'-1',
           'drabmax':'-1' }

#---------------------------------------------------------------------------------------------------
# Generating di-higgs through Heavy Higgs resonance with MadGraph
#---------------------------------------------------------------------------------------------------
fcard = open('proc_card_mg5.dat','w')
fcard.write("""
import model sm
define p = g u c d s u~ c~ d~ s~
define j = g u c d s u~ c~ d~ s~
import model HeavyHiggsTHDM
generate p p > hh > h h 
output -f""")
fcard.close()

beamEnergy=-999
if hasattr(runArgs,'ecmEnergy'):
    beamEnergy = runArgs.ecmEnergy / 2.
else: 
    raise RuntimeError("No center of mass energy found.")

#---------------------------------------------------------------------------------------------------
# Filter efficiency is ~50%
# Thus, setting the number of generated events to
# to avoid crashing due to not having enough events
# Also putting protection to avoid from crashing when maxEvents=-1

nevents=5000*safefactor
if runArgs.maxEvents > 0:
    nevents=runArgs.maxEvents*safefactor

#---------------------------------------------------------------------------------------------------
# Using the helper function from MadGraphControl for setting up the run_card
# Build a new run_card.dat from an existing one
# Using the values given in "extras" above for the selected parameters when setting up the run_card
# If not set in "extras", default values are used 
#---------------------------------------------------------------------------------------------------
build_run_card(run_card_old=get_default_runcard(),run_card_new='run_card.dat',
               nevts=nevents,rand_seed=runArgs.randomSeed,beamEnergy=beamEnergy,extras=extras,xqcut=0.0)

#---------------------------------------------------------------------------------------------------
# Using the helper function from MadGraphControl for setting up the param_card
# Build a new param_card.dat from an existing one
# Used values given in "parameters" for MHH and WHH, if not set there, default values are used
# Higgs mass is set to 125 GeV by "higgsMass"
#---------------------------------------------------------------------------------------------------
build_param_card(param_card_old='param_card.HeavyScalar.dat',param_card_new='param_card_new.dat',masses=higgsMass,extras=parameters)  

 
print_cards()
    
runName='run_01'     

process_dir = new_process()
generate(run_card_loc='run_card.dat',param_card_loc='param_card_new.dat',mode=mode,proc_dir=process_dir,run_name=runName)

arrange_output(run_name=runName,proc_dir=process_dir,outputDS=runName+'._00001.events.tar.gz')

#--------------------------------------------------------------
# Showering with HerwigPP, UE-EE-5 tune
#--------------------------------------------------------------


include("MC15JobOptions/Herwigpp_UEEE5_CTEQ6L1_CT10ME_LHEF_EvtGen_Common.py")
## To modify Higgs BR
cmds = """
create ThePEG::ParticleData XH 
setup XH 1560  XH """
cmds+=str(mX)
cmds+=""" 1.0 10.0 1.973269631e-13 2 3 2 0
set /Herwig/EventHandlers/LHEReader:AllowedToReOpen 0
set /Herwig/Shower/KinematicsReconstructor:ReconstructionOption General
set /Herwig/Shower/KinematicsReconstructor:InitialInitialBoostOption LongTransBoost
"""


from Herwigpp_i import config as hw
genSeq.Herwigpp.Commands += cmds.splitlines()
genSeq.Herwigpp.Commands += cmdspsh.splitlines()
del cmds
del cmdspsh

#---------------------------------------------------------------------------------------------------
# EVGEN Configuration
#---------------------------------------------------------------------------------------------------
evgenConfig.generators += ["MadGraph", "Herwigpp"]
evgenConfig.description+= "X is a "+str(mX)+" scalar."

evgenConfig.contact = ['Biagio Di Miccol <Biagio.di.micco@cern.ch>']

evgenConfig.inputfilecheck = runName
runArgs.inputGeneratorFile=runName+'._00001.events.tar.gz'


#---------------------------------------------------------------------------------------------------
# Generator Filters
#---------------------------------------------------------------------------------------------------
#from GeneratorFilters.GeneratorFiltersConf import ParentChildFilter
#filtSeq += ParentChildFilter("hbbFilter", PDGParent = [25], PDGChild = [5])
#filtSeq += ParentChildFilter("hWWFilter", PDGParent = [25], PDGChild = [24])
#filtSeq.Expression = "hbbFilter and hWWFilter"
