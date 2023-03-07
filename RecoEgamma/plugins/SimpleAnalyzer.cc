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
#include "RecoEgamma/EgammaMCTools/interface/PhotonMCTruth.h"

#include "SimpleAnalysis/RecoEgamma/plugins/SimpleAnalyzer.h"


SimpleAnalyzer::SimpleAnalyzer(const edm::ParameterSet& pset)
:photonCollectionToken_(consumes<reco::PhotonCollection>(pset.getParameter<edm::InputTag>("photonCollection"))),
 pfCandidateCollectionToken_(consumes<reco::PFCandidateCollection>(pset.getParameter<edm::InputTag>("pfCandidateCollection"))),
 g4_simTk_Token_(consumes<edm::SimTrackContainer>(pset.getParameter<edm::InputTag>("simTracks"))),
 g4_simVtx_Token_(consumes<edm::SimVertexContainer>(pset.getParameter<edm::InputTag>("simVertices")))
 {
    usesResource(TFileService::kSharedResource);
    minPhoEtCut_ = pset.getParameter<double>("minPhoEtCut");
    barrelEtaLimit_ = pset.getParameter<double>("barrelEtaLimit");
    edm::Service<TFileService> fs;
    h_Pho_Eta_ = fs->make<TH1F>("EtaPhotons", "Eta photons", 100 , -2.5, 2.5);
    h_Pho_Eta_Barrel_ = fs->make<TH1F>("EtaPhotonsBarrel", "Eta photons barrel", 100 , -2.5, 2.5);
    h_EtaCheck_[0] = fs->make<TH1F>("EtaPhotonsCheckCentral", "Eta photons central", 100 , -2.5, 2.5);
    h_EtaCheck_[1] = fs->make<TH1F>("EtaPhotonsCheckEdge", "Eta photons edge", 100 , -2.5, 2.5);
    h_NeutralHadron_ = fs->make<TH1F>("NeutralHadronEta", "Eta neutral hadrons", 30 , -3., 3.)  ; 

    h_dRPhoPFcand_NeuHad_unCleaned_[0] = fs->make<TH1F>("dRPhoPFcand_all", "dR(pho,cand) Neutral Hadrons :  All Ecal", 50 , 0., 0.7);
    h_dRPhoPFcand_NeuHad_unCleaned_[1] = fs->make<TH1F>("dRPhoPFcand_Barrel", "dR(pho,cand) Neutral Hadrons :  Barrel", 50, 0., 0.7);
    h_dRPhoPFcand_NeuHad_unCleaned_[2] = fs->make<TH1F>("dRPhoPFcand_Endcap", "dR(pho,cand) Neutral Hadrons :  Endcap", 50, 0., 0.7);
    h_dRPhoPFcand_NeuHad_unCleaned_EtaRestricted_[0] = fs->make<TH1F>("dRPhoPFcand_Barrel_all", "dR(pho,cand) Neutral Hadrons :  Barrel ", 50 , 0., 0.7);
    h_dRPhoPFcand_NeuHad_unCleaned_EtaRestricted_[1] = fs->make<TH1F>("dRPhoPFcand_Barrel_EtaR", "dR(pho,cand) Neutral Hadrons :  Barrel central", 50, 0., 0.7);
    h_dRPhoPFcand_NeuHad_unCleaned_EtaRestricted_[2] = fs->make<TH1F>("dRPhoPFcand_Barrel_Edge", "dR(pho,cand) Neutral Hadrons :  Barrel edge", 50, 0., 0.7);
 }

SimpleAnalyzer::~SimpleAnalyzer() {}

void SimpleAnalyzer::beginJob() {
  thePhotonMCTruthFinder_ = std::make_unique<PhotonMCTruthFinder>();
}


void SimpleAnalyzer::analyze(const edm::Event& e, const edm::EventSetup& esup) {
  thePhotonMCTruthFinder_->clear();

  ///// Get the recontructed  photons
  edm::Handle<reco::PhotonCollection> photonHandle;
  e.getByToken(photonCollectionToken_, photonHandle);
  const reco::PhotonCollection photonCollection = *(photonHandle.product());
  if (!photonHandle.isValid()) {
    edm::LogError("PhotonProducer") << "Error! Can't get the Photon collection " << std::endl;
    return;
  }

  // Get the  PF refined cluster  collection
  edm::Handle<reco::PFCandidateCollection> pfCandidateHandle;
  e.getByToken(pfCandidateCollectionToken_, pfCandidateHandle);
  if (!pfCandidateHandle.isValid()) {
    edm::LogError("PhotonValidator") << "Error! Can't get the product pfCandidates " << std::endl;
  }

 //////////////////// Get the MC truth
  //get simtrack info
  std::vector<SimTrack> theSimTracks;
  std::vector<SimVertex> theSimVertices;
  edm::Handle<edm::SimTrackContainer> SimTk;
  edm::Handle<edm::SimVertexContainer> SimVtx;
  e.getByToken(g4_simTk_Token_, SimTk);
  e.getByToken(g4_simVtx_Token_, SimVtx);

  theSimTracks.insert(theSimTracks.end(), SimTk->begin(), SimTk->end());
  theSimVertices.insert(theSimVertices.end(), SimVtx->begin(), SimVtx->end());
  std::vector<PhotonMCTruth> mcPhotons = thePhotonMCTruthFinder_->find(theSimTracks, theSimVertices);
  float minDelta = 10000.;
  int iMatch = -1;
  bool matched=false;

  for (std::vector<PhotonMCTruth>::const_iterator mcPho = mcPhotons.begin(); mcPho != mcPhotons.end(); mcPho++) {
    if ((*mcPho).fourMomentum().et() < minPhoEtCut_)
      continue;
    float mcPhi = (*mcPho).fourMomentum().phi();
    mcPhi_ = phiNormalization(mcPhi);
    mcEta_ = (*mcPho).fourMomentum().pseudoRapidity();
    mcEta_ = etaTransformation(mcEta_, (*mcPho).primaryVertex().z());

    for (unsigned int iPho = 0; iPho < photonHandle->size(); ++iPho) {
      reco::PhotonRef aPho(reco::PhotonRef(photonHandle, iPho));
      float phiPho = aPho->phi();
      float etaPho = aPho->eta();
      
      float delta = deltaR(etaPho,phiPho,mcEta_,mcPhi_);
      if (delta < 0.1 && delta < minDelta) {
        minDelta = delta;
        iMatch = iPho;
        } 
      }  // end loop over reco photons
    if (iMatch > -1)
        matched = true;
      
    if (matched) {
      reco::PhotonRef matchingPho(reco::PhotonRef(photonHandle,iMatch));
      h_Pho_Eta_->Fill(matchingPho->eta());
      if(std::abs(mcEta_)<1.479 )
        h_Pho_Eta_Barrel_->Fill(matchingPho->eta());
      for (unsigned int lCand = 0; lCand < pfCandidateHandle->size(); lCand++) {
        reco::PFCandidateRef pfCandRef(reco::PFCandidateRef(pfCandidateHandle, lCand));
        if (pfCandRef->particleId()== reco::PFCandidate::h0)
          h_NeutralHadron_->Fill(pfCandRef->eta());
        float dR = deltaR(matchingPho->eta(), matchingPho->phi(), pfCandRef->eta(), pfCandRef->phi());
        if (dR < 0.4) {
          reco::PFCandidate::ParticleType type = pfCandRef->particleId();
        if (type == reco::PFCandidate::h0) {
          h_dRPhoPFcand_NeuHad_unCleaned_[0]->Fill(dR);
          if (matchingPho->isEB())
            h_dRPhoPFcand_NeuHad_unCleaned_[1]->Fill(dR);
          else
            h_dRPhoPFcand_NeuHad_unCleaned_[2]->Fill(dR);
          
          if (matchingPho->isEB() ) {
            h_dRPhoPFcand_NeuHad_unCleaned_EtaRestricted_[0]->Fill(dR);
            if (std::abs(mcEta_)<barrelEtaLimit_){
              h_dRPhoPFcand_NeuHad_unCleaned_EtaRestricted_[1]->Fill(dR);
              h_EtaCheck_[0]->Fill(mcEta_);
              }
           else {
              h_dRPhoPFcand_NeuHad_unCleaned_EtaRestricted_[2]->Fill(dR);          
              h_EtaCheck_[1]->Fill(mcEta_);
              }  
            }
          }
        } 
      }   
    } 
  }
}


float SimpleAnalyzer::etaTransformation(float EtaParticle, float Zvertex) {
  //---Definitions
  const float PI = 3.1415927;

  //---Definitions for ECAL
  const float R_ECAL = 136.5;
  const float Z_Endcap = 328.0;
  const float etaBarrelEndcap = 1.479;

  //---ETA correction

  float Theta = 0.0;
  float ZEcal = R_ECAL * sinh(EtaParticle) + Zvertex;

  if (ZEcal != 0.0)
    Theta = atan(R_ECAL / ZEcal);
  if (Theta < 0.0)
    Theta = Theta + PI;
  float ETA = -log(tan(0.5 * Theta));

  if (fabs(ETA) > etaBarrelEndcap) {
    float Zend = Z_Endcap;
    if (EtaParticle < 0.0)
      Zend = -Zend;
    float Zlen = Zend - Zvertex;
    float RR = Zlen / sinh(EtaParticle);
    Theta = atan(RR / Zend);
    if (Theta < 0.0)
      Theta = Theta + PI;
    ETA = -log(tan(0.5 * Theta));
  }
  //---Return the result
  return ETA;
  //---end
}

float SimpleAnalyzer::phiNormalization(float& phi) {
  //---Definitions
  const float PI = 3.1415927;
  const float TWOPI = 2.0 * PI;

  if (phi > PI) {
    phi = phi - TWOPI;
  }
  if (phi < -PI) {
    phi = phi + TWOPI;
  }

  return phi;
}
