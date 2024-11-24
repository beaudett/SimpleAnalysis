import FWCore.ParameterSet.Config as cms


electronValidation = cms.EDAnalyzer('SimpleAnalyzerElectron',
    electronBarrelCollection = cms.InputTag('gedGsfElectrons'),
    electronEndcapCollection = cms.InputTag('gedGsfElectrons'),
    photonCollection = cms.InputTag('gedPhotons'),
    superClusterCollection = cms.InputTag('uncleanedOnlyCorrectedHybridSuperClusters'),
    mcTruthCollection = cms.InputTag("genParticles"),
    MatchingID = cms.vint32(11,-11),
    MatchingMotherID = cms.vint32(23,24,-24,32)
)


