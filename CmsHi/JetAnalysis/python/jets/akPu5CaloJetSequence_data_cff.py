
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akPu5Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu5CaloJets"),
    matched = cms.InputTag("ak5HiGenJets")
    )

akPu5Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPu5CaloJets"),
                                                        matched = cms.InputTag("hiGenParticles")
                                                        )

akPu5Calocorr = patJetCorrFactors.clone(
    useNPV = False,
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akPu5CaloJets"),
    payload = "AK5Calo_hiIterativeTracks"
    )

akPu5CalopatJets = patJets.clone(jetSource = cms.InputTag("akPu5CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu5Calocorr")),
                                               genJetMatch = cms.InputTag("akPu5Calomatch"),
                                               genPartonMatch = cms.InputTag("akPu5Caloparton"),
                                               jetIDMap = cms.InputTag("akPu5CaloJetID"),
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

akPu5CaloAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu5CalopatJets"),
                                                             genjetTag = 'ak5HiGenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akPu5CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("hiGeneralTracks"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akPu5CaloJetSequence_mc = cms.Sequence(akPu5Calomatch
                                                  *
                                                  akPu5Caloparton
                                                  *
                                                  akPu5Calocorr
                                                  *
                                                  akPu5CalopatJets
                                                  *
                                                  akPu5CaloAnalyzer
                                                  )

akPu5CaloJetSequence_data = cms.Sequence(akPu5Calocorr
                                                    *
                                                    akPu5CalopatJets
                                                    *
                                                    akPu5CaloAnalyzer
                                                    )

akPu5CaloJetSequence = cms.Sequence(akPu5CaloJetSequence_data)
