#ifndef SimpleAnalyzer_H
#define SimpleAnalyzer_H

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "DataFormats/EgammaCandidates/interface/PhotonFwd.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
#include "SimDataFormats/Track/interface/SimTrackContainer.h"
#include "SimDataFormats/Vertex/interface/SimVertexContainer.h"

#include "RecoEgamma/EgammaMCTools/interface/PhotonMCTruthFinder.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1.h"
#include "TH2.h"

class SimpleAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
public:
  //
  explicit SimpleAnalyzer(const edm::ParameterSet&);
  ~SimpleAnalyzer() override;

  void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void beginJob();


private:
  //
  float etaTransformation(float a, float b);
  float phiNormalization(float& phi) ;


  edm::EDGetTokenT<reco::PhotonCollection> photonCollectionToken_;
  edm::EDGetTokenT<reco::PFCandidateCollection> pfCandidateCollectionToken_;
  edm::EDGetTokenT<edm::SimTrackContainer> g4_simTk_Token_;
  edm::EDGetTokenT<edm::SimVertexContainer> g4_simVtx_Token_;

  std::unique_ptr<PhotonMCTruthFinder> thePhotonMCTruthFinder_;

  double minPhoEtCut_;
  double barrelEtaLimit_;
  double mcPhi_;
  double mcEta_;

  TH1F* h_dRPhoPFcand_NeuHad_unCleaned_[3];
  TH1F* h_dRPhoPFcand_NeuHad_unCleaned_EtaRestricted_[3];
  TH1F* h_EtaCheck_[2];
  TH1F * h_Pho_Eta_; 
  TH1F * h_Pho_Eta_Barrel_;
  TH1F * h_NeutralHadron_; 
  TH2F * h_NeutralHadronEtaPt_;
  TH1F * h_NeutralHadronConeMultiplicity_[3];
};

#endif 