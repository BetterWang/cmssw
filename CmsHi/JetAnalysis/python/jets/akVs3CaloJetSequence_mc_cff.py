
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akVs3Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs3CaloJets"),
    matched = cms.InputTag("ak3HiGenJets")
    )

akVs3Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVs3CaloJets"),
                                                        matched = cms.InputTag("hiGenParticles")
                                                        )

akVs3Calocorr = patJetCorrFactors.clone(
    useNPV = False,
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akVs3CaloJets"),
    payload = "AK3Calo_hiIterativeTracks"
    )

akVs3CalopatJets = patJets.clone(jetSource = cms.InputTag("akVs3CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs3Calocorr")),
                                               genJetMatch = cms.InputTag("akVs3Calomatch"),
                                               genPartonMatch = cms.InputTag("akVs3Caloparton"),
                                               jetIDMap = cms.InputTag("akVs3CaloJetID"),
                                               addBTagInfo         = False,
                                               addTagInfos         = False,
                                               addDiscriminators   = False,
                                               addAssociatedTracks = False,
                                               addJetCharge        = False,
                                               addJetID            = True,
                                               getJetMCFlavour     = False,
                                               addGenPartonMatch   = True,
                                               addGenJetMatch      = True,
                                               embedGenJetMatch    = True,
                                               embedGenPartonMatch = True,
                                               embedCaloTowers     = False,
				            )

akVs3CaloAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs3CalopatJets"),
                                                             genjetTag = 'ak3HiGenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs3CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("hiGeneralTracks"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akVs3CaloJetSequence_mc = cms.Sequence(akVs3Calomatch
                                                  *
                                                  akVs3Caloparton
                                                  *
                                                  akVs3Calocorr
                                                  *
                                                  akVs3CalopatJets
                                                  *
                                                  akVs3CaloAnalyzer
                                                  )

akVs3CaloJetSequence_data = cms.Sequence(akVs3Calocorr
                                                    *
                                                    akVs3CalopatJets
                                                    *
                                                    akVs3CaloAnalyzer
                                                    )

akVs3CaloJetSequence = cms.Sequence(akVs3CaloJetSequence_mc)
