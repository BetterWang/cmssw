import FWCore.ParameterSet.Config as cms

from L1Trigger.GlobalTriggerAnalyzer.L1ExtraInputTagSet_cff import *

l1GtAnalyzer = cms.EDAnalyzer("L1GtAnalyzer",
         
    # non-keyed parameter sets first                           
    # input tags for L1Extra collections
    # used by: 
    #    analyzeTrigger
    
    # print output
    #   0 std::cout
    #   1 LogTrace
    #   2 LogVerbatim
    #   3 LogInfo
    PrintOutput = cms.untracked.int32(3),

    # enable/disable various analyses
    #

    # input tag for L1GlobalTriggerReadoutRecord (L1 GT DAQ readout record) 
    #     GT emulator, GT unpacker:  gtDigis  
    # used by: 
    #    analyzeDecisionReadoutRecord
    #    L1GtUtils methods with input tags explicitly given
    #        analyzeL1GtUtilsEventSetup
    #        analyzeL1GtUtils
    #        analyzeTrigger
    L1GtDaqReadoutRecordInputTag = cms.InputTag("gtDigis"),
    
    # input tag for L1GlobalTriggerRecord 
    #     L1GlobalTriggerRecord record producer:  l1GtRecord  
    # used by: 
    #    analyzeDecisionReadoutRecord
    #    L1GtUtils methods with input tags explicitly given, if L1GtDaqReadoutRecordInputTag product does not exist
    #        analyzeL1GtUtilsEventSetup
    #        analyzeL1GtUtils
    #        analyzeTrigger
    
    # input tag for GT object map collection L1GlobalTriggerObjectMapRecord
    #     only the L1 GT emulator produces it,
    #     no map collection is produced by hardware
    #    
    #     GT emulator:  gtDigis
    # used by: 
    #    analyzeObjectMap
    #    analyzeTrigger

    # input tag for GT object map collection L1GlobalTriggerObjectMaps
    #     no map collection is produced by hardware
    #    
    #     L1Reco producer:  l1L1GtObjectMap
    # used by: 
    #    analyzeObjectMap
    #    analyzeTrigger

    # input tag for GMT readout collection: not used
    #     gmtDigis = GMT emulator
    #     gtDigis  = GT unpacker (common GT/GMT unpacker)
    
    # input tag for L1GtTriggerMenuLite
    # used by: 
    #    analyzeL1GtTriggerMenuLite (always)
    #    L1GtUtils methods, if L1GtTmLInputTagProv is set to False    
    #        analyzeL1GtUtilsMenuLite
    #        analyzeL1GtUtils
    #        analyzeTrigger
    
    # input tag for input tag for ConditionInEdm products
    # used by: 
    #    analyzeConditionsInRunBlock
    #    analyzeConditionsInLumiBlock
    #    analyzeConditionsInEventBlock    

    # an algorithm trigger name or alias, or a technical trigger name
    # used by: 
    #    analyzeL1GtUtilsEventSetup
    #    analyzeL1GtUtilsMenuLite
    #    analyzeL1GtUtils
    #    analyzeTrigger
    #    analyzeObjectMap (relevant for algorithm triggers only)
    # from provenance
    # used by: 
    #    analyzeL1GtUtilsEventSetup
    #    analyzeL1GtUtilsMenuLite
    #    analyzeL1GtUtils
    #    analyzeTrigger
    # L1GtUtilsLogicalExpression = cms.string("8 OR 25")
    # L1GtUtilsLogicalExpression = cms.string("(L1_HTT150  OR L1_HTT175 OR L1_DoubleJetC56 OR L1_SingleJet128) AND L1_NotInMenu")
    # L1GtUtilsLogicalExpression = cms.string("(6 OR 40 OR 25) AND 65 AND (NOT 34)" )
    # L1GtUtilsLogicalExpression = cms.string("(8 OR L1_HTT150 AND INVALID_KEYWORD 65 AND (NOT 34)" )
   
)


