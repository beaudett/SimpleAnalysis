import FWCore.ParameterSet.Config as cms


electronValidation = cms.EDAnalyzer('SimpleAnalyzerElectron',
    electronCollection = cms.InputTag('gedGsfElectrons'),
    
)


