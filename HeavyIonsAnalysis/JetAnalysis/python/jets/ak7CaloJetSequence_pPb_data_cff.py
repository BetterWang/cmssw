

import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *

ak7Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("ak7CaloJets"),
    matched = cms.InputTag("ak7HiGenJetsCleaned")
    )

ak7Caloparton = patJetPartonMatch.clone(src = cms.InputTag("ak7CaloJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

ak7Calocorr = patJetCorrFactors.clone(
    useNPV = False,
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("ak7CaloJets"),
    payload = "AK7Calo_HI"
    )

ak7CalopatJets = patJets.clone(jetSource = cms.InputTag("ak7CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak7Calocorr")),
                                               genJetMatch = cms.InputTag("ak7Calomatch"),
                                               genPartonMatch = cms.InputTag("ak7Caloparton"),
                                               jetIDMap = cms.InputTag("ak7CaloJetID"),
                                               addBTagInfo         = False,
                                               addTagInfos         = False,
                                               addDiscriminators   = False,
                                               addAssociatedTracks = False,
                                               addJetCharge        = False,
                                               addJetID            = False,
                                               getJetMCFlavour     = False,
                                               addGenPartonMatch   = False,
                                               addGenJetMatch      = False,
                                               embedGenJetMatch    = False,
                                               embedGenPartonMatch = False,
                                               embedCaloTowers     = False,
                                               embedPFCandidates = False
				            )

ak7CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("ak7CalopatJets"),
                                                             genjetTag = 'ak7HiGenJetsCleaned',
                                                             rParam = 0.7,
                                                             matchJets = cms.untracked.bool(False),
                                                             matchTag = 'ak7CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("generalTracks"),
                                                             fillGenJets = False,
                                                             isMC = False,
                                                             genParticles = cms.untracked.InputTag("genParticles")
                                                             )

ak7CaloJetSequence_mc = cms.Sequence(
						  ak7Calomatch
                                                  *
                                                  ak7Caloparton
                                                  *
                                                  ak7Calocorr
                                                  *
                                                  ak7CalopatJets
                                                  *
                                                  ak7CaloJetAnalyzer
                                                  )

ak7CaloJetSequence_data = cms.Sequence(ak7Calocorr
                                                    *
                                                    ak7CalopatJets
                                                    *
                                                    ak7CaloJetAnalyzer
                                                    )

ak7CaloJetSequence = cms.Sequence(ak7CaloJetSequence_data)
