
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akVs7PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs7PFJets"),
    matched = cms.InputTag("ak7HiGenJets")
    )

akVs7PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVs7PFJets"),
                                                        matched = cms.InputTag("hiGenParticles")
                                                        )

akVs7PFcorr = patJetCorrFactors.clone(
    useNPV = False,
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akVs7PFJets"),
    payload = "AK7PF_hiIterativeTracks"
    )

akVs7PFpatJets = patJets.clone(jetSource = cms.InputTag("akVs7PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs7PFcorr")),
                                               genJetMatch = cms.InputTag("akVs7PFmatch"),
                                               genPartonMatch = cms.InputTag("akVs7PFparton"),
                                               jetIDMap = cms.InputTag("akVs7PFJetID"),
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

akVs7PFAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs7PFpatJets"),
                                                             genjetTag = 'ak7HiGenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs7PFpatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("hiGeneralTracks"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akVs7PFJetSequence_mc = cms.Sequence(akVs7PFmatch
                                                  *
                                                  akVs7PFparton
                                                  *
                                                  akVs7PFcorr
                                                  *
                                                  akVs7PFpatJets
                                                  *
                                                  akVs7PFAnalyzer
                                                  )

akVs7PFJetSequence_data = cms.Sequence(akVs7PFcorr
                                                    *
                                                    akVs7PFpatJets
                                                    *
                                                    akVs7PFAnalyzer
                                                    )

akVs7PFJetSequence = cms.Sequence(akVs7PFJetSequence_mc)
