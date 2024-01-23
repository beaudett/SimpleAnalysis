import FWCore.ParameterSet.Config as cms


electronValidation = cms.EDAnalyzer('SimpleAnalyzerElectron',
    electronBarrelCollection = cms.InputTag('gedGsfElectrons'),
    electronEndcapCollection = cms.InputTag('ecalDrivenGsfElectronsHGC')   
)


