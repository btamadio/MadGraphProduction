evgenConfig.tune = "Innsbruck2014 CTEQ6LL"

## Innsbruck tune
genSeq.Pythia.PythiaCommand += [
        "pypars mstp 51 10042",
        "pypars mstp 52 2",
        "pypars parp 82 2.760",
        "pypars parp 90 0.219",
        "pypars parp 83 1.82",
        "pypars parp 78 0.516",
        "pypars parp 1 0.165",
        "pydat1 paru 112 0.165",
        "pypars parp 72 0.389"]

