

import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *

akPu6PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu6PFJets"),
    matched = cms.InputTag("ak6HiGenJetsCleaned")
    )

akPu6PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPu6PFJets"),
                                                        matched = cms.InputTag("hiGenParticles")
                                                        )

akPu6PFcorr = patJetCorrFactors.clone(
    useNPV = False,
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akPu6PFJets"),
    payload = "AK6PF_hiIterativeTracks"
    )

akPu6PFpatJets = patJets.clone(jetSource = cms.InputTag("akPu6PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu6PFcorr")),
                                               genJetMatch = cms.InputTag("akPu6PFmatch"),
                                               genPartonMatch = cms.InputTag("akPu6PFparton"),
                                               jetIDMap = cms.InputTag("akPu6PFJetID"),
                                               addBTagInfo         = False,
                                               addTagInfos         = False,
                                               addDiscriminators   = False,
                                               addAssociatedTracks = False,
                                               addJetCharge        = False,
                                               addJetID            = False,
                                               getJetMCFlavour     = False,
                                               addGenPartonMatch   = True,
                                               addGenJetMatch      = True,
                                               embedGenJetMatch    = True,
                                               embedGenPartonMatch = True,
                                               embedCaloTowers     = False,
                                               embedPFCandidates = False
				            )

akPu6PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu6PFpatJets"),
                                                             genjetTag = 'ak6HiGenJetsCleaned',
                                                             rParam = 0.6,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akPu6CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("hiGeneralTracks"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )

akPu6PFJetSequence_mc = cms.Sequence(
						  akPu6PFmatch
                                                  *
                                                  akPu6PFparton
                                                  *
                                                  akPu6PFcorr
                                                  *
                                                  akPu6PFpatJets
                                                  *
                                                  akPu6PFJetAnalyzer
                                                  )

akPu6PFJetSequence_data = cms.Sequence(akPu6PFcorr
                                                    *
                                                    akPu6PFpatJets
                                                    *
                                                    akPu6PFJetAnalyzer
                                                    )

akPu6PFJetSequence = cms.Sequence(akPu6PFJetSequence_mc)
