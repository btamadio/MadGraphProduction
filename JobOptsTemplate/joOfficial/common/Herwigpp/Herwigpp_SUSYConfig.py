## Functions to construct Herwig++ configuration for SUSY signal generation

sparticles = {}

## Gluino
sparticles['gluino']	  = ['~g']

## Squarks
sparticles['supL']      = ['~u_L','~u_Lbar']
sparticles['sdownL']    = ['~d_L','~d_Lbar']
sparticles['scharmL']   = ['~c_L','~c_Lbar']
sparticles['sstrangeL'] = ['~s_L','~s_Lbar']
sparticles['sbottom1']  = ['~b_1','~b_1bar']
sparticles['stop1']     = ['~t_1','~t_1bar']
#
sparticles['supR']      = ['~u_R','~u_Rbar']
sparticles['sdownR']    = ['~d_R','~d_Rbar']
sparticles['scharmR']   = ['~c_R','~c_Rbar']
sparticles['sstrangeR'] = ['~s_R','~s_Rbar']
sparticles['sbottom2']  = ['~b_2','~b_2bar']
sparticles['stop2']     = ['~t_2','~t_2bar']
## Collections of squarks
sparticles['squarksG1_L'] = sparticles['supL']+sparticles['sdownL']
sparticles['squarksG1_R'] = sparticles['supR']+sparticles['sdownR']
sparticles['squarksG2_L'] = sparticles['scharmL']+sparticles['sstrangeL']
sparticles['squarksG2_R'] = sparticles['scharmR']+sparticles['sstrangeR']
#
sparticles['sbottoms']    = sparticles['sbottom1']+sparticles['sbottom2']
sparticles['stops']       = sparticles['stop1']+sparticles['stop2']
#
sparticles['squarks_L']   = sparticles['squarksG1_L']+sparticles['squarksG2_L']
sparticles['squarks_R']   = sparticles['squarksG1_R']+sparticles['squarksG2_R']
sparticles['squarks']     = sparticles['squarks_L']+sparticles['squarks_R']

## Gauginos
sparticles['neutralinos'] = ['~chi_10','~chi_20','~chi_30','~chi_40']
sparticles['charginos']   = ['~chi_1+','~chi_2+','~chi_1-','~chi_2-']
sparticles['gauginos']    = sparticles['neutralinos']+sparticles['charginos']

## Sleptons
sparticles['selectronL'] = ['~e_L-','~e_L+']
sparticles['smuonL']     = ['~mu_L-','~mu_L+']
sparticles['stau1']      = ['~tau_1-','~tau_1+']
#
sparticles['selectronR'] = ['~e_R-','~e_R+']
sparticles['smuonR']     = ['~mu_R-','~mu_R+']
sparticles['stau2']      = ['~tau_2-','~tau_2+']
## Collections of sleptons
sparticles['sleptons_L'] = sparticles['selectronL']+sparticles['smuonL']
sparticles['sleptons_R'] = sparticles['selectronR']+sparticles['smuonR']
sparticles['staus']      = sparticles['stau1']+sparticles['stau2']
sparticles['sleptons']   = sparticles['sleptons_L']+sparticles['sleptons_R']

## Sneutrinos
sparticles['sneutrino_eL']   = ['~nu_eL', '~nu_eLbar']
sparticles['sneutrino_muL']  = ['~nu_muL', '~nu_muLbar']
sparticles['sneutrino_tauL'] = ['~nu_tauL', '~nu_tauLbar']
## Collections of sneutrinos
sparticles['sneutrinos_L'] = sparticles['sneutrino_eL']+sparticles['sneutrino_muL']+sparticles['sneutrino_tauL']
sparticles['sneutrinos'] = sparticles['sneutrinos_L']

## Collection of all particles
sparticles['all'] = sparticles['gluino'] + sparticles['squarks'] + sparticles['sbottoms'] + sparticles['stops'] + sparticles['gauginos'] + sparticles['sleptons'] + sparticles['staus'] + sparticles['sneutrinos']

def addOutgoingSparticle(index, sparticle):
    cmdline = """insert HPConstructor:Outgoing %(index)d /Herwig/Particles/%(sparticle)s""" % \
        {'index':index,'sparticle':sparticle}
    return cmdline


def buildHerwigppCommands(sparticle_list, slha_file, mode='SingleParticleInclusive', earlyCopy=False):
    header = """
## Generate the process in MSSM equivalent to 2-parton -> 2-sparticle processes in Fortran Herwig
## Read the MSSM model details
read MSSM.model
cd /Herwig/NewPhysics
"""

    process_mode = """
## Establish how processes are selected
## SingleParticleInclusive means that at least one of the
## outgoing particles must be in the HPConstructor:Outgoing.
## TwoParticleInclusive means that both of the outgoing particles
## must be in the HPConstructor:Outgoing.
## Exclusive means that only two outgoing particles can be supplied
## in HPConstructor:Outgoing, and only that pair will be produced.
##
## E.g. if the outgoing particles were the ~g and ~u_L, then:
## SingleParticleInclusive produces any process involving ~g or ~u_L,
## including ~g/~g, ~g/~u_L, ~u_L/~d_L, ~g/~chi_10 etc.
## TwoParticleInclusive produces processes involving ~g and ~u_L only,
## i.e. ~g/~g, ~g/~u_L, ~u_L/~u_L.
## Exclusive produces only one process,
## i.e. ~g/~u_L.
##
set HPConstructor:Processes %(mode)s
""" % {'mode':mode}

    incoming_partons = """
#incoming parton
insert HPConstructor:Incoming 0 /Herwig/Particles/g
insert HPConstructor:Incoming 1 /Herwig/Particles/u
insert HPConstructor:Incoming 2 /Herwig/Particles/ubar
insert HPConstructor:Incoming 3 /Herwig/Particles/d
insert HPConstructor:Incoming 4 /Herwig/Particles/dbar
insert HPConstructor:Incoming 5 /Herwig/Particles/s
insert HPConstructor:Incoming 6 /Herwig/Particles/sbar
insert HPConstructor:Incoming 7 /Herwig/Particles/c
insert HPConstructor:Incoming 8 /Herwig/Particles/cbar
insert HPConstructor:Incoming 9 /Herwig/Particles/b
insert HPConstructor:Incoming 10 /Herwig/Particles/bbar
"""
    sparticle_flatlist = []
    for sparty in sparticle_list:
        try:
        	sparticle_flatlist += sparticles[sparty]
        except KeyError:
        	sparticle_flatlist += [sparty]
    ## A slightly clunky way of removing duplicates
    helperdict = {}
    for sparticle in sparticle_flatlist:
        helperdict[sparticle] = 1
    sparticle_flatlist = helperdict.keys()

    outgoing_sparticles = """
#outgoing sparticles
"""
    for index,sparticle in enumerate(sparticle_flatlist):
        outgoing_sparticles += addOutgoingSparticle(index,sparticle)
        outgoing_sparticles += '\n'

    footer = """
## Read the SUSY spectrum file (SLHA format)
setup MSSM/Model %(slha_file)s
""" % {'slha_file':slha_file}

    ## SLHA files are copied later on to the working directory via the auxfiles mechanism
    evgenConfig.auxfiles += [ slha_file, 'MSSM.model' ]

    ## use earlyCopy in case this should be done now to tweak/read the SLHA file
    if earlyCopy:
        from PyJobTransformsCore.trfutil import get_files
        get_files( slha_file, keepDir=False, errorIfNotFound=True )

    cmd = header + process_mode + incoming_partons + outgoing_sparticles + footer
    return cmd
