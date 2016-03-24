## Sherpa config with NNPDF3.0 NNLO PDF
include("MC15JobOptions/Sherpa_2.2.0_Base_Fragment.py")

## NNPDF3.0 NNLO is Sherpa's default PDF/tune, thus no need to set anything up
evgenConfig.tune = "NNPDF3.0 NNLO"
