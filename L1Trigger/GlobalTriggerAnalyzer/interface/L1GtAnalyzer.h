#ifndef GlobalTriggerAnalyzer_L1GtAnalyzer_h
#define GlobalTriggerAnalyzer_L1GtAnalyzer_h

/**
 * \class L1GtAnalyzer
 * 
 * 
 * Description: test analyzer to illustrate various methods for L1 GT trigger.
 *
 * Implementation:
 *    <TODO: enter implementation details>
 *   
 * \author: Vasile Mihai Ghete - HEPHY Vienna
 * 
 *
 */

// system include files
#include <memory>
#include <string>

// user include files

#include "DataFormats/Common/interface/ConditionsInEdm.h"

#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerObjectMapRecord.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerObjectMaps.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GtTriggerMenuLite.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/EDGetToken.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "L1Trigger/GlobalTriggerAnalyzer/interface/L1GtUtils.h"
#include "L1Trigger/GlobalTriggerAnalyzer/interface/L1RetrieveL1Extra.h"

#include "TH2D.h"

// class declaration

class L1GtAnalyzer: public edm::EDAnalyzer {

public:
    explicit L1GtAnalyzer(const edm::ParameterSet&);
    ~L1GtAnalyzer();

private:

    /// analyze: decision and decision word
    ///   bunch cross in event BxInEvent = 0 - L1Accept event
    virtual void analyzeDecisionReadoutRecord(const edm::Event&, const edm::EventSetup&);

    /// analyze: usage of L1GtUtils
    ///   for tests, use only one of the following methods

    /// full analysis of an algorithm or technical trigger

    /// analyze: object map product

    /// analyze: usage of L1GtTriggerMenuLite

    /// analyze: usage of ConditionsInEdm
    ///
    /// to be used in beginRun
    /// to be used in beginLuminosityBlock
    /// to be used in analyze/produce/filter

    /// print the output stream to the required output, given by m_printOutput
    void printOutput(std::ostringstream&);

    /// analyze each event: event loop over various code snippets
    virtual void analyze(const edm::Event&, const edm::EventSetup&);

    /// end section

    /// end of job

private:

    // L1Extra collections

    /// print output
    int m_printOutput;


    /// enable / disable various analysis methods
    //

private:

    /// input tags for GT DAQ product
    edm::InputTag m_l1GtDaqReadoutRecordInputTag;
    edm::EDGetTokenT<L1GlobalTriggerReadoutRecord> m_l1GtDaqReadoutRecordToken;

    /// input tags for GT lite product

    /// input tags for GT object map collection L1GlobalTriggerObjectMapRecord

    /// input tags for GT object map collection L1GlobalTriggerObjectMaps

    /// input tag for muon collection from GMT

    /// input tag for L1GtTriggerMenuLite

    /// input tag for ConditionInEdm products

    /// an algorithm trigger (name or alias) or a technical trigger name

    /// a condition in the algorithm trigger to test the object maps

    /// a bit number to retrieve the name and the alias

    /// L1 configuration code for L1GtUtils

    /// if true, use methods in L1GtUtils with the input tag for L1GtTriggerMenuLite
    /// from provenance

    /// if true, use methods in L1GtUtils with the given input tags
    /// for L1GlobalTriggerReadoutRecord and / or L1GlobalTriggerRecord from provenance

    /// if true, configure (partially) L1GtUtils in beginRun using getL1GtRunCache
    
    /// expression to test the L1GtUtils methods to retrieve L1 trigger decisions, 
    ///   prescale factors and masks for logical expressions

private:


    TH2D *hBx;
    TH2D *hAlgoBx;

};

#endif /*GlobalTriggerAnalyzer_L1GtAnalyzer_h*/
