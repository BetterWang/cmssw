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

// this class header
#include "L1Trigger/GlobalTriggerAnalyzer/interface/L1GtAnalyzer.h"

// system include files
#include <memory>
#include <iomanip>

// user include files
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutSetupFwd.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutSetup.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerRecord.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerObjectMap.h"

#include "DataFormats/L1GlobalMuonTrigger/interface/L1MuGMTReadoutCollection.h"

#include "L1Trigger/GlobalTrigger/interface/L1GlobalTriggerPSB.h"
#include "L1Trigger/GlobalTrigger/interface/L1GlobalTriggerGTL.h"
#include "L1Trigger/GlobalTrigger/interface/L1GlobalTriggerFDL.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"

#include "CondFormats/L1TObjects/interface/L1GtTriggerMenu.h"
#include "CondFormats/DataRecord/interface/L1GtTriggerMenuRcd.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
// constructor(s)
L1GtAnalyzer::L1GtAnalyzer(const edm::ParameterSet& parSet) :

            m_printOutput(parSet.getUntrackedParameter<int>("PrintOutput", 3)),
            m_l1GtDaqReadoutRecordInputTag(parSet.getParameter<edm::InputTag>(
                    "L1GtDaqReadoutRecordInputTag"))

{
    m_l1GtDaqReadoutRecordToken = consumes<L1GlobalTriggerReadoutRecord>(m_l1GtDaqReadoutRecordInputTag);

    edm::Service<TFileService> fs;
    hBx = fs->make<TH2D>("hBx", "bit vs Bx;Bx;bits", 3600, -0.5, 3599.5, 64, -0.5, 63.5);
    hAlgoBx = fs->make<TH2D>("hAlgoBx", "algo bit vs Bx;Bx;algo bits", 3600, -0.5, 3599.5, 128, -0.5, 127.5);
}

// destructor
L1GtAnalyzer::~L1GtAnalyzer() {
    // empty
}

// method called once each job just before starting event loop

// member functions

// analyze: decision and decision word
//   bunch cross in event BxInEvent = 0 - L1Accept event
void L1GtAnalyzer::analyzeDecisionReadoutRecord(const edm::Event& iEvent, const edm::EventSetup& evSetup)
{

    LogDebug("L1GtAnalyzer")
    << "\n**** L1GtAnalyzer::analyzeDecisionReadoutRecord ****\n"
    << std::endl;

    // define an output stream to print into
    // it can then be directed to whatever log level is desired
    std::ostringstream myCoutStream;

    // get L1GlobalTriggerReadoutRecord
    edm::Handle<L1GlobalTriggerReadoutRecord> gtReadoutRecord;
    iEvent.getByToken(m_l1GtDaqReadoutRecordToken, gtReadoutRecord);

    if (!gtReadoutRecord.isValid()) {

	    std::cout << "\nL1GlobalTriggerReadoutRecord with \n  "
                << m_l1GtDaqReadoutRecordInputTag
                << "\nrequested in configuration, but not found in the event."
                << "\nExit the method.\n" << std::endl;

        return;
    }
    myCoutStream << "!!!!!!" << std::endl;

    L1GtfeWord gtfeWord = gtReadoutRecord->gtfeWord();
    int bx = gtfeWord.bxNr();

    TechnicalTriggerWord twE = gtReadoutRecord->technicalTriggerWord(-2);
    TechnicalTriggerWord twF = gtReadoutRecord->technicalTriggerWord(-1);
    TechnicalTriggerWord tw = gtReadoutRecord->technicalTriggerWord(0);
    TechnicalTriggerWord tw1 = gtReadoutRecord->technicalTriggerWord(1);
    TechnicalTriggerWord tw2 = gtReadoutRecord->technicalTriggerWord(2);

    DecisionWord dwE = gtReadoutRecord->decisionWord(-2);
    DecisionWord dwF = gtReadoutRecord->decisionWord(-1);
    DecisionWord dw  = gtReadoutRecord->decisionWord(0);
    DecisionWord dw1 = gtReadoutRecord->decisionWord(1);
    DecisionWord dw2 = gtReadoutRecord->decisionWord(2);

    if (!tw.empty()) {
	    for (uint i = 0; i < tw.size(); ++i) {
		    if (twE[i]) {
			    hBx->Fill(bx-2, i);
		    }
		    if (twF[i]) {
			    hBx->Fill(bx-1, i);
		    }
		    if (tw[i]) {
			    hBx->Fill(bx, i);
		    }
		    if (tw1[i]) {
			    hBx->Fill(bx+1, i);
		    }
		    if (tw2[i]) {
			    hBx->Fill(bx+2, i);
		    }
	    }
    }

    if (!dw.empty() ) {
	    for ( uint i = 0; i < dw.size(); ++i ) {
		    if (dwE[i]) {
			    hAlgoBx->Fill(bx-2, i);
		    }
		    if (dwF[i]) {
			    hAlgoBx->Fill(bx-1, i);
		    }
		    if (dw[i]) {
			    hAlgoBx->Fill(bx, i);
		    }
		    if (dw1[i]) {
			    hAlgoBx->Fill(bx+1, i);
		    }
		    if (dw2[i]) {
			    hAlgoBx->Fill(bx+2, i);
		    }
	    }
    }

    // get Global Trigger decision and the decision word
//    bool gtDecision = gtReadoutRecord->decision();
//    DecisionWord gtDecisionWord = gtReadoutRecord->decisionWord();

    // print Global Trigger decision and the decision word
//    std::cout << "\n GlobalTrigger decision: " << gtDecision << std::endl;

    // print via supplied "print" function (
//    gtReadoutRecord->printGtDecision(myCoutStream);

    // print technical trigger word via supplied "print" function
//    gtReadoutRecord->printTechnicalTrigger(myCoutStream);
//    gtReadoutRecord->print(myCoutStream);

//    std::cout << " gtFdlVector.size() = " << gtReadoutRecord->gtFdlVector().size() << std::endl;
//    printOutput(myCoutStream);

}



void L1GtAnalyzer::printOutput(std::ostringstream& myCout) {

    switch (m_printOutput) {
        case 0: {

            std::cout << myCout.str() << std::endl;

        }

            break;
        case 1: {

            LogTrace("L1GtAnalyzer") << myCout.str() << std::endl;

        }
            break;

        case 2: {

            edm::LogVerbatim("L1GtAnalyzer") << myCout.str() << std::endl;

        }

            break;
        case 3: {

            edm::LogInfo("L1GtAnalyzer") << myCout.str();

        }

            break;
        default: {
            std::cout << "\n\n  L1GtAnalyzer: Error - no print output = "
                    << m_printOutput
                    << " defined! \n  Check available values in the cfi file."
                    << "\n" << std::endl;

        }
            break;
    }

    myCout.str("");
    myCout.clear();

}

// analyze each event: event loop
void L1GtAnalyzer::analyze(const edm::Event& iEvent,
        const edm::EventSetup& evSetup) {

    // analyze: decision and decision word
    //   bunch cross in event BxInEvent = 0 - L1Accept event
        analyzeDecisionReadoutRecord(iEvent, evSetup);

    // analyze: decision for a given algorithm using L1GtUtils functions
    //   for tests, use only one of the following methods
}


