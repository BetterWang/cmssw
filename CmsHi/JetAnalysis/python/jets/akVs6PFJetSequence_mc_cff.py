
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akVs6PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs6PFJets"),
    matched = cms.InputTag("ak6HiGenJets")
    )

akVs6PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVs6PFJets"),
                                                        matched = cms.InputTag("hiGenParticles")
                                                        )

akVs6PFcorr = patJetCorrFactors.clone(
    useNPV = False,
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akVs6PFJets"),
    payload = "AK6PF_hiIterativeTracks"
    )

akVs6PFpatJets = patJets.clone(jetSource = cms.InputTag("akVs6PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs6PFcorr")),
                                               genJetMatch = cms.InputTag("akVs6PFmatch"),
                                               genPartonMatch = cms.InputTag("akVs6PFparton"),
                                               jetIDMap = cms.InputTag("akVs6PFJetID"),
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

akVs6PFAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs6PFpatJets"),
                                                             genjetTag = 'ak6HiGenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs6PFpatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("hiGeneralTracks"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akVs6PFJetSequence_mc = cms.Sequence(akVs6PFmatch
                                                  *
                                                  akVs6PFparton
                                                  *
                                                  akVs6PFcorr
                                                  *
                                                  akVs6PFpatJets
                                                  *
                                                  akVs6PFAnalyzer
                                                  )

akVs6PFJetSequence_data = cms.Sequence(akVs6PFcorr
                                                    *
                                                    akVs6PFpatJets
                                                    *
                                                    akVs6PFAnalyzer
                                                    )

akVs6PFJetSequence = cms.Sequence(akVs6PFJetSequence_mc)
