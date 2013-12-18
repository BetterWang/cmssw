

import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *

akPu7PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu7PFJets"),
    matched = cms.InputTag("ak7HiGenJetsCleaned")
    )

akPu7PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPu7PFJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akPu7PFcorr = patJetCorrFactors.clone(
    useNPV = False,
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akPu7PFJets"),
    payload = "AK7PF_generalTracks"
    )

akPu7PFpatJets = patJets.clone(jetSource = cms.InputTag("akPu7PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu7PFcorr")),
                                               genJetMatch = cms.InputTag("akPu7PFmatch"),
                                               genPartonMatch = cms.InputTag("akPu7PFparton"),
                                               jetIDMap = cms.InputTag("akPu7PFJetID"),
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

akPu7PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu7PFpatJets"),
                                                             genjetTag = 'ak7HiGenJetsCleaned',
                                                             rParam = 0.7,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akPu7CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("generalTracks"),
                                                             fillGenJets = False,
                                                             isMC = False,
                                                             genParticles = cms.untracked.InputTag("genParticles")
                                                             )

akPu7PFJetSequence_mc = cms.Sequence(
						  akPu7PFmatch
                                                  *
                                                  akPu7PFparton
                                                  *
                                                  akPu7PFcorr
                                                  *
                                                  akPu7PFpatJets
                                                  *
                                                  akPu7PFJetAnalyzer
                                                  )

akPu7PFJetSequence_data = cms.Sequence(akPu7PFcorr
                                                    *
                                                    akPu7PFpatJets
                                                    *
                                                    akPu7PFJetAnalyzer
                                                    )

akPu7PFJetSequence = cms.Sequence(akPu7PFJetSequence_data)
