#include <iostream>
#include <memory>

//
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "SimpleAnalysis/RecoEgamma/plugins/SimpleAnalyzerElectron.h"


SimpleAnalyzerElectron::SimpleAnalyzerElectron(const edm::ParameterSet& pset)
:electronCollectionToken_(consumes<reco::GsfElectronCollection>(pset.getParameter<edm::InputTag>("electronCollection")))
 {
    edm::Service<TFileService> fs;
    h_HoE_ = fs->make<TH1F>("HoE_all", "H/E", 100 , 0. , 1.);
    h_HoEvsEta_ = fs->make<TH2F>("HoEvsETa", "H/E vs Eta", 30 , -3., 3.,100,0,1.)  ; 
 }

SimpleAnalyzerElectron::~SimpleAnalyzerElectron() {}

void SimpleAnalyzerElectron::beginJob() {
;
}


void SimpleAnalyzerElectron::analyze(const edm::Event& e, const edm::EventSetup& esup) {

  ///// Get the recontructed  photons
  edm::Handle<reco::GsfElectronCollection> electronHandle;
  e.getByToken(electronCollectionToken_, electronHandle);
  const reco::GsfElectronCollection electronCollection = *(electronHandle.product());
  if (!electronHandle.isValid()) {
    edm::LogError("SimpleAnalyzerElectron") << "Error! Can't get the Electron collection " << std::endl;
    return;
  }


  for (unsigned int iE = 0; iE < electronHandle->size(); ++iE) {
    const reco::GsfElectron & cand = (*electronHandle)[iE];
    h_HoE_->Fill(cand.hcalOverEcal());
    h_HoEvsEta_->Fill(cand.eta(),cand.hcalOverEcal());
  }
}


