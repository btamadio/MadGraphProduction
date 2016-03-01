#!/bin/bash
run=$1
seed=$2
jobname=$3
mGluino=$4
mNeutralino=$5
mSquark=$6
nQuark=$7
mkdir -p /project/projectdirs/atlas/btamadio/RPV_SUSY/MadGraphProduction/production
rm -rf /project/projectdirs/atlas/btamadio/RPV_SUSY/MadGraphProduction/production/RPV_${jobname}_${run}_${seed}
mkdir /project/projectdirs/atlas/btamadio/RPV_SUSY/MadGraphProduction/production/RPV_${jobname}_${run}_${seed}
cd /project/projectdirs/atlas/btamadio/RPV_SUSY/MadGraphProduction/production/RPV_${jobname}_${run}_${seed}
shopt -s expand_aliases
source /common/atlas/scripts/setupATLAS.sh
setupATLAS
cp /project/projectdirs/atlas/btamadio/RPV_SUSY/MadGraphProduction/JobOptsTemplate/MC15JobOptsSepFull.tar.gz .
tar -zvxf MC15JobOptsSepFull.tar.gz
mv MC15JobOptions/MC15.800001.MadGraphPythia8EvtGen_A14NNPDF23LO_GG_RPV_1100_900.py MC15JobOptions/MC15.${run}.MadGraphPythia8EvtGen_A14NNPDF23LO_GG_RPV${nQuark}_${mGluino}_${mNeutralino}_${mSquark}.py
rm MC15JobOptsSepFull.tar.gz
tar -zcvf MC15JobOpts.tar.gz *
lsetup asetup
asetup AtlasProduction,20.7.0.1,here
Generate_tf.py --AMITag=e3962 --maxEvents=20000 --ecmEnergy=13000 --runNumber=${run} --firstEvent=1 --randomSeed=${seed} --outputEVNTFile=OUT.${run}.EVNT.pool.root --jobConfig=MC15JobOptions/MC15.${run}.MadGraphPythia8EvtGen_A14NNPDF23LO_GG_RPV${nQuark}_${mGluino}_${mNeutralino}_${mSquark}.py --evgenJobOpts=MC15JobOpts.tar.gz
echo "Generate_tf DONE"