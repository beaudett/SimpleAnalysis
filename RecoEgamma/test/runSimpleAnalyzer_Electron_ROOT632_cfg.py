import FWCore.ParameterSet.Config as cms

process = cms.Process("validation")

process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("SimpleAnalysis.RecoEgamma.simpleElectronAnalyzer_cff")
process.load('DQMOffline.Configuration.DQMOffline_cff')

# 
process.source = cms.Source("PoolSource",
#    debugVerbosity = cms.untracked.uint32(1),
#    debugFlag = cms.untracked.bool(True),
    fileNames = cms.untracked.vstring(
'/store/relval/CMSSW_14_1_0_pre6_ROOT632/RelValTTbar_14TeV/GEN-SIM-RECO/140X_mcRun3_2024_realistic_v15_2024_KITFARM_ROOT632_SpecialRV-v1/130000/03f145b9-8402-403a-a48c-4a891f5a5743.root',
'/store/relval/CMSSW_14_1_0_pre6_ROOT632/RelValTTbar_14TeV/GEN-SIM-RECO/140X_mcRun3_2024_realistic_v15_2024_KITFARM_ROOT632_SpecialRV-v1/130000/ce07489f-7037-41ca-bec5-fe047fe49176.root',
'/store/relval/CMSSW_14_1_0_pre6_ROOT632/RelValTTbar_14TeV/GEN-SIM-RECO/140X_mcRun3_2024_realistic_v15_2024_KITFARM_ROOT632_SpecialRV-v1/130000/b90f94c8-2678-4e0e-a93a-78f9f94abf6d.root',
'/store/relval/CMSSW_14_1_0_pre6_ROOT632/RelValTTbar_14TeV/GEN-SIM-RECO/140X_mcRun3_2024_realistic_v15_2024_KITFARM_ROOT632_SpecialRV-v1/130000/28d2d4c9-a54c-48f8-90d7-75d3a15348e5.root'
#'/store/relval/CMSSW_14_1_0_pre6_ROOT632/RelValZpToEE_m6000_14TeV/GEN-SIM-RECO/140X_mcRun3_2024_realistic_v15_2024_KITFARM_ROOT632_SpecialRV-v1/120000/013c8501-a496-43c3-b98a-0edda3697838.root',
#'/store/relval/CMSSW_14_1_0_pre6_ROOT632/RelValZpToEE_m6000_14TeV/GEN-SIM-RECO/140X_mcRun3_2024_realistic_v15_2024_KITFARM_ROOT632_SpecialRV-v1/120000/c7f0e6bf-fce4-4fc7-a83c-4f6ffcff2cba.root',
#'/store/relval/CMSSW_14_1_0_pre6_ROOT632/RelValZpToEE_m6000_14TeV/GEN-SIM-RECO/140X_mcRun3_2024_realistic_v15_2024_KITFARM_ROOT632_SpecialRV-v1/120000/455bc7c5-56f2-4c22-90a5-0d20b6be3ce3.root',
#'/store/relval/CMSSW_14_1_0_pre6_ROOT632/RelValZpToEE_m6000_14TeV/GEN-SIM-RECO/140X_mcRun3_2024_realistic_v15_2024_KITFARM_ROOT632_SpecialRV-v1/120000/258b638e-eac5-4838-83b6-fdf33f925503.root'
       )
    )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )


process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string('electrons632.root')
                                   )

process.simpleAnalyzerPath = cms.EndPath(process.simpleElectronAnalyzerSequence)

#process.p = cms.Path(process.mySimpleAnalyzerSequence)
process.schedule = cms.Schedule(process.simpleAnalyzerPath)

process.outpath = cms.EndPath()


