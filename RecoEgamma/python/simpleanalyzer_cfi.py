import FWCore.ParameterSet.Config as cms


photonValidation = cms.EDAnalyzer('SimpleAnalyzer',
    photonCollection = cms.InputTag('gedPhotons'),
    pfCandidateCollection = cms.InputTag('particleFlow'),
    simTracks = cms.InputTag('g4SimHits'),
    simVertices = cms.InputTag('g4SimHits'),
    barrelEtaLimit = cms.double(1.),
    minPhoEtCut = cms.double(10.),
 
)


