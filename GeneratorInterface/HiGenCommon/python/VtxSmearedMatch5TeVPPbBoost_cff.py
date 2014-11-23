import FWCore.ParameterSet.Config as cms
 
from IOMC.EventVertexGenerators.VtxSmearedParameters_cfi import *
VtxSmeared = cms.EDProducer("MixBoostEvtVtxGenerator",
                            useCF = cms.untracked.bool(True),
                            mixLabel = cms.InputTag("mixGen","generator")
                            Beta=cms.double(-0.434)
                            )
