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
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SimpleAnalysis/RecoEgamma/plugins/SimpleAnalyzerElectron.h"
#include "DataFormats/GsfTrackReco/interface/GsfTrack.h"
#include "CLHEP/Units/GlobalPhysicalConstants.h"

SimpleAnalyzerElectron::SimpleAnalyzerElectron(const edm::ParameterSet& pset)
:electronBarrelCollectionToken_(consumes<reco::GsfElectronCollection>(pset.getParameter<edm::InputTag>("electronBarrelCollection"))),
electronEndcapCollectionToken_(consumes<reco::GsfElectronCollection>(pset.getParameter<edm::InputTag>("electronEndcapCollection"))),
photonCollectionToken_(consumes<reco::PhotonCollection>(pset.getParameter<edm::InputTag>("photonCollection"))),
superClusterCollectionToken_(consumes<reco::PhotonCollection>(pset.getParameter<edm::InputTag>("superClusterCollection"))),
mcTruthCollectionToken_(consumes<reco::GenParticleCollection>(pset.getParameter<edm::InputTag>("mcTruthCollection")))
 {
    edm::Service<TFileService> fs;
    h_RecEleNum_ = fs->make<TH1F>("RecEleNum","Number of electrons", 100,-0.5,99.5);
    h_HoE_[0] = fs->make<TH1F>("HoE_all", "H/E all ", 100 , 0. , 0.5);
    h_HoE_[1] = fs->make<TH1F>("HoE_barrel", "H/E barrel", 100 , 0. , 0.5);
    h_HoE_[2] = fs->make<TH1F>("HoE_endcaps", "H/E endcaps", 100 , 0. , 0.5);
    h_HoE_[3] = fs->make<TH1F>("HoE_centralbarrel", "H/E |eta|<1", 100 , 0. , 0.5);
    h_HoE_[4] = fs->make<TH1F>("HoE_centralbarrelHighPT", "H/E |eta|<1 Et >10 ", 100 , 0. , 0.5);

    h_HoEPhotons_ = fs->make<TH1F>("HoEPhotons", "H/E Photons |eta|<1", 100 , 0. , 0.5);
    h_EtaHighHoE_ = fs->make<TH1F>("EtaHighHoE", "Eta H>E>0.2", 30 , -3., 3.);
    h_Eta_ = fs->make<TH1F>("Eta_barrel", "Eta barrel", 30 , -3., 3.);
    h_HoESC_ = fs->make<TH1F>("Eta_SC", "Eta SC barrel", 30 , -3., 3.);
    h_PtCentralElectronBarrel_ = fs->make<TH1F>("Pt_electrons", "Pt electron barrel", 80 , 0, 40.);
    h_PtCentralPhotonBarrel_ = fs->make<TH1F>("Pt_photons ", "Pt photon barrel", 80 , 0, 40.);
    h_H_ = fs->make<TH1F>("H", "H central barrel", 50 , 0, 10.);
    h_E_ = fs->make<TH1F>("E", "E central barrel", 50 , 0, 10.);


    h_HoEvsEta_[0] = fs->make<TH2F>("HoEvsEta_all", "H/E vs Eta", 30 , -3., 3.,100,0,0.5)  ; 
    h_HoEvsEta_[1] = fs->make<TH2F>("HoEvsEta_barrel", "H/E vs Eta", 30 , -3., 3.,100,0,0.5)  ; 
    h_HoEvsEta_[2] = fs->make<TH2F>("HoEvsEta_endcaps", "H/E vs Eta", 30 , -3., 3.,100,0,0.5)  ; 
    h_HoEvsPt_[0] = fs->make<TH2F>("HoEvsPt_all", "H/E vs Pt", 80 , 0, 40.,100,0,0.5)  ; 
    h_HoEvsPt_[1] = fs->make<TH2F>("HoEvsPt_barrel", "H/E vs Pt barrel]", 80 , 0, 40.,100,0,0.5)  ; 
    h_HoEvsPt_[2] = fs->make<TH2F>("HoEvsPt_endcaps", "H/E vs Pt endcaps", 80 , 0, 40.,100,0,0.5)  ; 
    h_HoEvsPt_[3] = fs->make<TH2F>("HoEvsPt_central_barrel", "H/E vs Pt central barrel", 80 , 0, 40.,100,0,0.5)  ; 
    h_EvsPt_ = fs->make<TH2F>("EvsPt_central_barrel", "E vs Pt central barrel", 80 , 0, 40.,50,0,10.)  ;
    h_HvsPt_ = fs->make<TH2F>("HvsPt_central_barrel", "H vs Pt central barrel", 80 , 0, 40.,50,0,10.)  ;
    h_GsfPtoGenvsEta_ = fs->make<TH2F>("GsfPtoGenvsEta", "Track pT/Gen vs eta", 90 , -3., 3.,50,0.,1.5)  ;
    h_GsfPtoGenvsAbsEta_ = fs->make<TH2F>("GsfPtoGenvsAbsEta", "Track pT/Gen vs |eta|", 90 , 0., 3.,50,0.,1.5)  ;
    h_EoPvsEta_ = fs->make<TH2F>("EoPvsEta","E/p vs eta",90,-3,3.,50,0,1.5);
    h_EoPvsAbsEta_ = fs->make<TH2F>("EoPvsAbsEta","E/p vs |eta|",90,0,3.,50,0,1.5);
    h_GsfPtoGenvsEtaLR_ = fs->make<TH2F>("GsfPtoGenvsEtaLR", "Track pT/Gen vs eta", 90 , -3., 3.,500,0.,15)  ;
    h_GsfPtoGenvsAbsEtaLR_ = fs->make<TH2F>("GsfPtoGenvsAbsEtaLR", "Track pT/Gen vs |eta|", 90 , 0., 3.,500,0.,15)  ;
    h_EoPvsEtaLR_ = fs->make<TH2F>("EoPvsEtaLR","E/p vs eta",90,-3,3.,500,0,15);
    h_EoPvsAbsEtaLR_ = fs->make<TH2F>("EoPvsAbsEtaLR","E/p vs |eta|",90,0,3.,500,0,15);
    h_EoPExtended_ = fs->make<TH1F>("EoPExt", "E/p 2.5<|eta|<3", 80 , 0, 20.);
    h_EoPExtendedNeg_ = fs->make<TH1F>("EoPExtNeg", "E/p -3 <eta< -2.5", 80 , 0, 20.);
    h_EoPExtendedPos_ = fs->make<TH1F>("EoPExtPos", "E/p 2.5< eta <3", 80 , 0, 20.);
    h_EoPvsEtaProf_ = fs->make<TProfile>("EoPvsEtaProf","E/p vs eta",50,-3,3.);
    h_EoPvsEtaProfEoPMax_ = fs->make<TProfile>("EoPvsEtaProfMax","E/p vs eta E/p<5",50,-3,3.);;
    matchingIDs_ = pset.getParameter<std::vector<int> >("MatchingID");
    matchingMotherIDs_ = pset.getParameter<std::vector<int> >("MatchingMotherID");
    std::cout << " Created histograms " << std::endl;
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
  h_RecEleNum_->Fill(electronBarrelHandle->size());
  for (unsigned int iE = 0; iE < electronBarrelHandle->size(); ++iE) {
    const reco::GsfElectron & cand = (*electronBarrelHandle)[iE];
   // if (cand.pt()<20) continue;
    h_HoE_[0]->Fill(cand.hcalOverEcal());
    h_HoEvsPt_[0]->Fill(cand.pt(),cand.hcalOverEcal());
    h_HoEvsPt_[1]->Fill(cand.pt(),cand.hcalOverEcal());
    h_HoEvsEta_[0]->Fill(cand.eta(),cand.hcalOverEcal());
    h_HoE_[1]->Fill(cand.hcalOverEcal());
    h_HoEvsEta_[1]->Fill(cand.eta(),cand.hcalOverEcal());
    h_Eta_->Fill(cand.eta());
    if(std::abs(cand.eta())<1.) {
      float energy=cand.superCluster()->energy();
      float h = cand.hcalOverEcal()*energy;
      h_HoE_[3]->Fill(cand.hcalOverEcal());
      h_E_->Fill(energy);
      h_H_->Fill(h);
      h_HvsPt_->Fill(cand.pt(),h);
      h_EvsPt_->Fill(cand.pt(),energy);
      h_HoEvsPt_[3]->Fill(cand.pt(),cand.hcalOverEcal());
      h_PtCentralElectronBarrel_->Fill(cand.pt());
      if (cand.pt()>10.)
        h_HoE_[4]->Fill(cand.hcalOverEcal());
    }
    if (cand.hcalOverEcal()>0.2) 
      h_EtaHighHoE_->Fill(cand.eta());
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
//    if (cand.pt()<20) continue;
    h_HoE_[0]->Fill(cand.hcalOverEcal());
    h_HoEvsEta_[0]->Fill(cand.eta(),cand.hcalOverEcal());
    h_HoEvsPt_[0]->Fill(cand.pt(),cand.hcalOverEcal());
    h_HoEvsPt_[2]->Fill(cand.pt(),cand.hcalOverEcal());
    h_HoE_[2]->Fill(cand.hcalOverEcal());
    h_HoEvsEta_[2]->Fill(cand.eta(),cand.hcalOverEcal());
  }

 ///// Get the recontructed  photons
  edm::Handle<reco::PhotonCollection> photonHandle;
  e.getByToken(photonCollectionToken_, photonHandle);
  const reco::PhotonCollection photonCollection = *(photonHandle.product());
  if (!photonHandle.isValid()) {
    edm::LogError("SimpleAnalyzerElectron") << "Error! Can't get the Photon collection " << std::endl;
    return;
  }
  for (unsigned int iPho = 0; iPho < photonHandle->size(); ++iPho) {
    const reco::Photon & cand= (*photonHandle)[iPho];
    if (cand.pt()>0 && std::abs(cand.eta())<1) {
      h_PtCentralPhotonBarrel_->Fill(cand.pt());
      h_HoEPhotons_->Fill(cand.hcalOverEcal());
    }
  }

  bool matchingID, matchingMotherID;

  edm::Handle<reco::GenParticleCollection> mcParticlesHandle;  
  e.getByToken(mcTruthCollectionToken_,mcParticlesHandle);
  reco::GenParticleCollection::const_iterator mcIter;
  for (mcIter = mcParticlesHandle->begin(); mcIter != mcParticlesHandle->end(); mcIter++) {
    // select requested matching gen particle
    matchingID = false;
    for (unsigned int i = 0; i < matchingIDs_.size(); i++) {
      if (mcIter->pdgId() == matchingIDs_[i]) {
        matchingID = true;
      }
    }
    if (matchingID) {
        // select requested mother matching gen particle
        // always include single particle with no mother
      const reco::Candidate *mother = mcIter->mother();
      matchingMotherID = false;
   //   std::cout << " Mother PID " << mother->pdgId()  << std::endl;
      for (unsigned int i = 0; i < matchingMotherIDs_.size(); i++) {
     //   std::cout << " Testing MotherPID "<< matchingMotherIDs_[i] << std::endl;
        if (mother == nullptr) {
          matchingMotherID = true;
          } else if (mother->pdgId() == matchingMotherIDs_[i]) {
            if (mother->numberOfDaughters() <= 2) {
              matchingMotherID = true;
            }
          }  // end of mother if test
        }
        if (matchingMotherID) {
          if (std::abs(mcIter->eta()) > 4.) {
            continue;
          }
          bool okGsfFound = false;
          double gsfOkRatio = 999999.;
          // find best matched electron
          reco::GsfElectron bestGsfElectron;
          for (unsigned int iE = 0; iE < electronEndcapHandle->size(); ++iE) {
          const reco::GsfElectron & cand = (*electronEndcapHandle)[iE];        
          double dphi = cand.phi() - mcIter->phi();
          if (std::abs(dphi) > CLHEP::pi) {
            dphi = dphi < 0 ? (CLHEP::twopi) + dphi : dphi - CLHEP::twopi;            
          }
          double deltaR2 = (cand.eta() - mcIter->eta()) * (cand.eta() - mcIter->eta()) + dphi * dphi;
          if (deltaR2 < 0.0025) {
            double tmpGsfRatio = cand.p() / mcIter->p();
            if (std::abs(tmpGsfRatio - 1) < std::abs(gsfOkRatio - 1)) {
              gsfOkRatio = tmpGsfRatio;
              bestGsfElectron = cand;
              okGsfFound = true;
              }
            }     // DeltaR3
            if (okGsfFound && bestGsfElectron.pt() < 100 ){
              h_GsfPtoGenvsEta_->Fill(mcIter->eta(),bestGsfElectron.gsfTrack()->innerMomentum().R()/mcIter->p());
              h_GsfPtoGenvsAbsEta_->Fill(std::abs(mcIter->eta()),bestGsfElectron.gsfTrack()->innerMomentum().R()/mcIter->p());
              h_EoPvsEta_->Fill(bestGsfElectron.eta(),bestGsfElectron.eSuperClusterOverP());
              h_EoPvsEtaProf_->Fill(bestGsfElectron.eta(),bestGsfElectron.eSuperClusterOverP());
              if(bestGsfElectron.eSuperClusterOverP() < 5.)
                h_EoPvsEtaProfEoPMax_->Fill(bestGsfElectron.eta(),bestGsfElectron.eSuperClusterOverP());
              h_EoPvsAbsEta_->Fill(std::abs(bestGsfElectron.eta()),bestGsfElectron.eSuperClusterOverP());
              h_GsfPtoGenvsEtaLR_->Fill(mcIter->eta(),bestGsfElectron.gsfTrack()->innerMomentum().R()/mcIter->p());
              h_GsfPtoGenvsAbsEtaLR_->Fill(std::abs(mcIter->eta()),bestGsfElectron.gsfTrack()->innerMomentum().R()/mcIter->p());
              h_EoPvsEtaLR_->Fill(bestGsfElectron.eta(),bestGsfElectron.eSuperClusterOverP());
              h_EoPvsAbsEtaLR_->Fill(std::abs(bestGsfElectron.eta()),bestGsfElectron.eSuperClusterOverP());
              if (std::abs(bestGsfElectron.eta())>2.5 && std::abs(bestGsfElectron.eta())<3.)
                h_EoPExtended_->Fill(bestGsfElectron.eSuperClusterOverP());
              if (bestGsfElectron.eta() <-2.5 && bestGsfElectron.eta()>-3.)
                h_EoPExtendedNeg_->Fill(bestGsfElectron.eSuperClusterOverP());
              if (bestGsfElectron.eta() > 2.5 && bestGsfElectron.eta() < 3.)
                h_EoPExtendedPos_->Fill(bestGsfElectron.eSuperClusterOverP());
            }
          } //loop on EE electrons
        } //matching motherID 
    } // loop on gen particles  
  } //loop on MC particles



 ///// Get the SuperClusters
 // edm::Handle<reco::SuperClusterCollection> scHandle;
 // e.getByToken(superClusterCollectionToken_, scHandle);
 // const reco::SuperClusterCollection scCollection = *(scHandle.product());
 // if (!scHandle.isValid()) {
 //   edm::LogError("SimpleAnalyzerElectron") << "Error! Can't get the SC collection " << std::endl;
 //   return;
 // }
 // for (unsigned int iSC = 0; iSC < scHandle->size(); ++iSC) {
 //   const reco::SuperCluster & cand= (*scHandle)[iSC];
 //   if (cand.pt()>0 && std::abs(cand.eta())<1)
 // }

}


