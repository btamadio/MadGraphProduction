## Configure Pythia8 to read input events from an LHEF file
assert hasattr(genSeq, "Pythia8")
genSeq.Pythia8.LHEFile = "events.lhe"
genSeq.Pythia8.CollisionEnergy = int(runArgs.ecmEnergy)
