import FWCore.ParameterSet.Config as cms

process = cms.Process("validation")

process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("SimpleAnalysis.RecoEgamma.simpleElectronAnalyzer_cff")
process.load('DQMOffline.Configuration.DQMOffline_cff')

#reference
process.source = cms.Source("PoolSource",
#    debugVerbosity = cms.untracked.uint32(1),
#    debugFlag = cms.untracked.bool(True),
    fileNames = cms.untracked.vstring(
        '/store/relval/CMSSW_14_1_0_pre6/RelValTTbar_14TeV/GEN-SIM-RECO/140X_mcRun3_2024_realistic_v15_2024_KITFARM_x86_SpecialRV-v1/130000/6023e0c6-4a51-41ef-a723-25d329aba766.root',
        '/store/relval/CMSSW_14_1_0_pre6/RelValTTbar_14TeV/GEN-SIM-RECO/140X_mcRun3_2024_realistic_v15_2024_KITFARM_x86_SpecialRV-v1/130000/8ae29446-90b9-440b-90e5-5e17cfad1818.root',
        '/store/relval/CMSSW_14_1_0_pre6/RelValTTbar_14TeV/GEN-SIM-RECO/140X_mcRun3_2024_realistic_v15_2024_KITFARM_x86_SpecialRV-v1/130000/a6a683a8-9b2b-4fdc-94dd-6156f67de9df.root',
        '/store/relval/CMSSW_14_1_0_pre6/RelValTTbar_14TeV/GEN-SIM-RECO/140X_mcRun3_2024_realistic_v15_2024_KITFARM_x86_SpecialRV-v1/130000/fd3605eb-e45a-49ce-933c-4cf4c7868152.root'
#'root://xrootd-cms.infn.it///store/relval/CMSSW_14_1_0_pre6/RelValZpToEE_m6000_14TeV/GEN-SIM-RECO/140X_mcRun3_2024_realistic_v15_2024_KITFARM_x86_SpecialRV-v1/130000/c25ddad4-b50e-4cc4-9ad4-2241405411db.root',
#'root://xrootd-cms.infn.it///store/relval/CMSSW_14_1_0_pre6/RelValZpToEE_m6000_14TeV/GEN-SIM-RECO/140X_mcRun3_2024_realistic_v15_2024_KITFARM_x86_SpecialRV-v1/130000/4026a0b3-2f00-4a8e-9fac-84789c4933a1.root',
#'root://xrootd-cms.infn.it///store/relval/CMSSW_14_1_0_pre6/RelValZpToEE_m6000_14TeV/GEN-SIM-RECO/140X_mcRun3_2024_realistic_v15_2024_KITFARM_x86_SpecialRV-v1/130000/48136ffa-f0fd-4ad3-be20-5ccf8a08cd12.root'
       )
    )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )


process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string('electrons.root')
                                   )

process.simpleAnalyzerPath = cms.EndPath(process.simpleElectronAnalyzerSequence)

#process.p = cms.Path(process.mySimpleAnalyzerSequence)
process.schedule = cms.Schedule(process.simpleAnalyzerPath)

process.outpath = cms.EndPath()


