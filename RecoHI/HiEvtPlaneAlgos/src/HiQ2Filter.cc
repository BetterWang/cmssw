/*
 * Author: Quan Wang 
 * Date : Mar 2015
 */

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/HeavyIonEvent/interface/EvtPlane.h"
#include "RecoHI/HiEvtPlaneAlgos/interface/HiEvtPlaneList.h"

class HiQ2Filter : public edm::EDFilter {

public:
	HiQ2Filter(const edm::ParameterSet&);
	~HiQ2Filter() {};
	virtual bool filter(edm::Event&, edm::EventSetup const&);
	virtual void beginJob() {};
	virtual void endJob() {};
private:
	int level_;
	int idx_;
	double q2_low;
	double q2_high;
};

HiQ2Filter::HiQ2Filter(const edm::ParameterSet& ps) :
	level_(ps.getParameter<int>("level")),
	idx_(ps.getParameter<int>("EPidx")),
	q2_low(ps.getParameter<double>("q2_low")),
	q2_high(ps.getParameter<double>("q2_high"))
{

}

bool HiQ2Filter::filter(edm::Event& evt, edm::EventSetup const& es)
{
	return true;
}

DEFINE_FWK_MODULE(HiQ2Filter);
