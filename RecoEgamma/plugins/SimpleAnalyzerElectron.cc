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
:electronBarrelCollectionToken_(consumes<reco::GsfElectronCollection>(pset.getParameter<edm::InputTag>("electronBarrelCollection"))),
electronEndcapCollectionToken_(consumes<reco::GsfElectronCollection>(pset.getParameter<edm::InputTag>("electronEndcapCollection")))
 {
    edm::Service<TFileService> fs;
    h_HoE_[0] = fs->make<TH1F>("HoE_all", "H/E all ", 100 , 0. , 0.5);
    h_HoE_[1] = fs->make<TH1F>("HoE_barrel", "H/E barrel", 100 , 0. , 0.5);
    h_HoE_[2] = fs->make<TH1F>("HoE_endcaps", "H/E endcaps", 100 , 0. , 0.5);

    h_HoEvsEta_[0] = fs->make<TH2F>("HoEvsEta_all", "H/E vs Eta", 30 , -3., 3.,100,0,0.5)  ; 
    h_HoEvsEta_[1] = fs->make<TH2F>("HoEvsEta_barrel", "H/E vs Eta", 30 , -3., 3.,100,0,0.5)  ; 
    h_HoEvsEta_[2] = fs->make<TH2F>("HoEvsEta_endcaps", "H/E vs Eta", 30 , -3., 3.,100,0,0.5)  ; 

 }

SimpleAnalyzerElectron::~SimpleAnalyzerElectron() {}

void SimpleAnalyzerElectron::beginJob() {
;
}


void SimpleAnalyzerElectron::analyze(const edm::Event& e, const edm::EventSetup& esup) {

  ///// Get the recontructed  electrons in the barrel
  edm::Handle<reco::GsfElectronCollection> electronBarrelHandle;
  e.getByToken(electronBarrelCollectionToken_, electronBarrelHandle);
  const reco::GsfElectronCollection electronBarrelCollection = *(electronBarrelHandle.product());
  if (!electronBarrelHandle.isValid()) {
    edm::LogError("SimpleAnalyzerElectron") << "Error! Can't get the Electron collection " << std::endl;
    return;
  }


  for (unsigned int iE = 0; iE < electronBarrelHandle->size(); ++iE) {
    const reco::GsfElectron & cand = (*electronBarrelHandle)[iE];
    h_HoE_[0]->Fill(cand.hcalOverEcal());
    h_HoEvsEta_[0]->Fill(cand.eta(),cand.hcalOverEcal());
    h_HoE_[1]->Fill(cand.hcalOverEcal());
    h_HoEvsEta_[1]->Fill(cand.eta(),cand.hcalOverEcal());
  }

  ///// Get the recontructed  electrons in the endcaps
  edm::Handle<reco::GsfElectronCollection> electronEndcapHandle;
  e.getByToken(electronEndcapCollectionToken_, electronEndcapHandle);
  const reco::GsfElectronCollection  electronEndcapCollection = *(electronEndcapHandle.product());
  if (!electronEndcapHandle.isValid()) {
    edm::LogError("SimpleAnalyzerElectron") << "Error! Can't get the Electron collection " << std::endl;
    return;
  }
  for (unsigned int iE = 0; iE < electronEndcapHandle->size(); ++iE) {
    const reco::GsfElectron & cand = (*electronEndcapHandle)[iE];
    h_HoE_[0]->Fill(cand.hcalOverEcal());
    h_HoEvsEta_[0]->Fill(cand.eta(),cand.hcalOverEcal());
    h_HoE_[2]->Fill(cand.hcalOverEcal());
    h_HoEvsEta_[2]->Fill(cand.eta(),cand.hcalOverEcal());
  }

}


