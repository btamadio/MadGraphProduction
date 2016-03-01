#!/bin/bash
run=$1
seed=$2
mass=$2
mkdir -p production
rm -rf production/VLT_${run}_${seed}_${mass}
mkdir production/VLT_${run}_${seed}_${mass}
cd production/VLT_${run}_${seed}_${mass}
shopt -s expand_aliases
cp ../../JobOptsVLT/MC15.304744.MGPy8EG_NNPDF30LO_A14NNPDF23LO_WTht900LH01.py MC15.${run}.MGPy8EG_NNPDF30LO_A14NNPDF23LO_WTht${mass}LH01.py
shopt -s expand_aliases
source /common/atlas/scripts/setupATLAS.sh
setupATLAS
lsetup asetup
asetup AtlasProduction,20.7.0.1,here
Generate_tf.py --AMITag=e3962 --maxEvents=5000 --ecmEnergy=13000 --runNumber=${run} --firstEvent=1 --randomSeed=${seed} --outputEVNTFile=OUT.${run}.EVNT.pool.root --jobConfig=MC15.${run}.MGPy8EG_NNPDF30LO_A14NNPDF23LO_WTht${mass}LH01.py
echo "Generate_tf DONE"
ls -ltr
cd ../..
mkdir -p VLT_EVNT
mv production/VLT_${run}_${seed}_${mass}/OUT.${run}.EVNT.pool.root VLT_EVNT
mkdir -p derivation
rm -rf derivation/VLT_${run}_${seed}_${mass}
mkdir derivation/VLT_${run}_${seed}_${mass}
cd derivation/VLT_${run}_${seed}_${mass}
cp ../../VLT_EVNT/OUT.${run}.EVNT.pool.root .
shopt -s expand_aliases
asetup AtlasDerivation,20.1.8.3,here
Reco_tf.py --inputEVNTFile OUT.${run}.EVNT.pool.root --outputDAODFile OUT.${run}.DAOD.pool.root --reductionConf TRUTH3
echo "Reco_tf DONE"
ls -ltr
mkdir -p ../../VLT_TRUTH3
mv DAOD_TRUTH3.OUT.${run}.DAOD.pool.root ../../VLT_TRUTH3/