#ifndef SimpleAnalyzerElectron_H
#define SimpleAnalyzerElectron_H

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "DataFormats/EgammaCandidates/interface/PhotonFwd.h"
#include "DataFormats/EgammaReco/interface/SuperCluster.h"
#include "DataFormats/EgammaReco/interface/SuperClusterFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1.h"
#include "TH2.h"
#include "TProfile.h"

class SimpleAnalyzerElectron : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
public:
  //
  explicit SimpleAnalyzerElectron(const edm::ParameterSet&);
  ~SimpleAnalyzerElectron() override;

  void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void beginJob();


private:
  //
  edm::EDGetTokenT<reco::GsfElectronCollection> electronBarrelCollectionToken_;
  edm::EDGetTokenT<reco::GsfElectronCollection> electronEndcapCollectionToken_;
  edm::EDGetTokenT<reco::PhotonCollection> photonCollectionToken_;
  edm::EDGetTokenT<reco::PhotonCollection> superClusterCollectionToken_;
  edm::EDGetTokenT<reco::GenParticleCollection> mcTruthCollectionToken_;                  // genParticles
  std::vector<int> matchingIDs_;
  std::vector<int> matchingMotherIDs_;

  TH1F * h_RecEleNum_;
  TH2F * h_HoEvsEta_[3];
  TH2F * h_HoEvsPt_[4];
  TH1F * h_HoE_[5];
  TH1F * h_EtaHighHoE_; 
  TH1F * h_Eta_;
  TH1F * h_HoEPhotons_;
  TH1F * h_HoESC_;
  TH1F * h_PtCentralElectronBarrel_;
  TH1F * h_PtCentralPhotonBarrel_;
  TH1F * h_H_;
  TH1F * h_E_;
  TH2F * h_HvsPt_;
  TH2F * h_EvsPt_;
//  TProfile * h_GsfPtoGenvsEta_;
//  TProfile * h_GsfPtoGenvsAbsEta_;
//  TProfile * h_EoPvsEta_;
//  TProfile * h_EoPvsAbsEta_;
  TH2F * h_GsfPtoGenvsEta_;
  TH2F * h_GsfPtoGenvsAbsEta_;
  TH2F * h_EoPvsEta_;
  TH2F * h_EoPvsAbsEta_;
  TH2F * h_GsfPtoGenvsEtaLR_;
  TH2F * h_GsfPtoGenvsAbsEtaLR_;
  TH2F * h_EoPvsEtaLR_;
  TH2F * h_EoPvsAbsEtaLR_;
  TH1F * h_EoPExtended_;
  TH1F * h_EoPExtendedNeg_;
  TH1F * h_EoPExtendedPos_;
  TProfile * h_EoPvsEtaProf_;
  TProfile * h_EoPvsEtaProfEoPMax_;
};

#endif 