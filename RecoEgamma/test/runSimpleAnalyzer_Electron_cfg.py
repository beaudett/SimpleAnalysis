import FWCore.ParameterSet.Config as cms

process = cms.Process("validation")

process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("SimpleAnalysis.RecoEgamma.simpleElectronAnalyzer_cff")
process.load('DQMOffline.Configuration.DQMOffline_cff')

process.source = cms.Source("PoolSource",
#    debugVerbosity = cms.untracked.uint32(1),
#    debugFlag = cms.untracked.bool(True),
    fileNames = cms.untracked.vstring(        
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/707b1791-513e-4e1b-89ab-9ae18beabf28.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/a748dd7c-9204-4a73-af42-9253c22c9d4a.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/6bd153e2-aaca-45d1-ba8d-58e36b80fcdc.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/6923b188-fda4-43df-a6d4-5f38e42ace2b.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/e56b06ff-dd60-4e3f-95d8-0a3a4a64a48a.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/7c68efc0-f880-4511-8d82-c3c065936b04.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/572bf936-bee8-4e4e-9fbe-9ad2acc355a6.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/670f5cbd-2a61-4447-bea3-e1ffc785c9e5.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/f7579b73-a499-497b-bac8-e706be2b4c30.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/2de9cd80-c9b3-4a42-85a6-2320fcb891d8.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/7925ca36-5264-41d8-b619-608efb98d8ab.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/dd3c6c31-5a30-408e-87d3-645096839b61.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/82d7123d-542c-4018-a70a-cd49135365f3.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/ce0ca91d-2f3a-49fc-8db7-d4893c795ccb.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/d0bb2b59-5faa-49f1-b4e7-81d00ed39fc8.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/ac2711af-f0e7-4410-af03-35e5318f76c6.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/030f74f3-987c-46c2-9127-a4501630aaa6.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/3d1e4a72-9c4a-4cac-be0a-85fe6bd09f2d.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/bccf38f7-e334-48b8-96f5-ebb28fa8648e.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/95f08b50-db2a-485b-92c8-ea7be88720c9.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/3227f7d5-e429-460f-8561-53d44b696dfe.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/151fdaf1-58ab-4724-980c-909296bfac5c.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/3a10fac2-910a-4903-9a0b-be6f8d2eb167.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/cef5e1f5-aaf3-4cd3-92c1-183aead79d3e.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/0fd14eee-d4b6-492b-8767-31b025c980dc.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/1c6d2653-4173-4676-a6b4-b0a52b281fd0.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/48ed2c42-a287-4430-a8e6-472b6c879ea1.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/2ede38c4-02ae-4de4-9651-7bc28d4f6d9d.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/b535785f-454d-4026-ae1e-0a3673a27d84.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/72c2cdd4-760d-4796-b34d-fa229d0bc37b.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/1b06ee9e-6a29-4d60-9e9f-697b3bb8eda7.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/c6f49a77-cf45-4406-b22e-a7d19db0ae2b.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/2caa7c5c-f43e-443a-b003-3ee61e2a754f.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/11f8d5c4-42d2-4169-b87d-9d1908df52fb.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/4e3bbdad-47d6-4881-938c-c8dd796dbafc.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/bfb947b4-0ab0-495f-9a0e-476e393e5d62.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/1c54bbfc-9446-458d-9ff2-fe7bdb3be8d4.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/a27df9ab-44f9-4a7b-aa82-8e314fb8b281.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/2cb24d05-9be5-499c-bfc1-be7ecd556455.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/25abaf48-ff7a-47a2-8722-5c22edae1bd3.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/335634dc-38cf-424d-a0af-a59f90f73d74.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/5152905a-b91b-42ac-a69b-f38fe5a2d6d5.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/4b65cca4-2429-457b-8517-20f287fcd15d.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/d4539d74-8cae-44f3-9152-cb3468464e35.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/f86253bf-7fe9-49a3-9a71-46fc87f1c453.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/f12256c8-5481-4143-9d13-6497ce4d870d.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/56e402a6-db3e-48ec-8e11-3a28cff99ecb.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/d135ed22-e68e-4c7e-943e-b9c485149b15.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/231a91e1-88fc-4aae-b0b3-d75bff3f917b.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/2f6827d5-d6ee-4b21-897c-fa0440842da0.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/e68f2d1f-ce1e-46c0-b26e-0151c5504be2.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/fee78409-3aa5-4c0d-a4bf-c0218cc4251c.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/c88838ca-f414-4055-8f4f-10487c61fb8b.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/bff9d7d1-25d3-4652-a994-a8947c437778.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/1fea0460-ae95-40b5-ba0f-8bb3376e1512.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/a898d73c-e19e-4260-ad4e-4d8491600b30.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/0bceea45-3415-4df2-82f7-dc17214c9047.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/b50561af-c9b9-4c29-8f00-b4d0724c7c1a.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/83e96de6-7cba-419c-baa1-33073153921c.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/2d721f35-3086-4e4a-bfd2-eadc6b467041.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/0379886e-21a3-448a-b414-71f9e7dfac3f.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/71b85236-5d59-4131-b878-ec24523c810f.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/e83d36d2-1ba4-4cf9-bbfe-618bcd30358c.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/d00ddf35-6ece-409f-9dfb-77a76b85b180.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/4d3c35c6-5250-46dc-9c36-6b51f31fa2a4.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/ce6aee62-f533-4b73-9d98-96156c1ba778.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/70bbb1ae-c415-4a19-aa84-3b40fb3dac2b.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/d5a99aab-3ffd-4cba-a2e2-3118d891532d.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/b2340a6e-d428-4714-b837-b74cb34c532c.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/37384b49-74b9-4216-b2a5-6d80b2dd1ed2.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/8fdef345-d97a-4b04-a122-b34095d99fdc.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/a16f513a-f927-4f52-92b6-d526f36efb54.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/cc374749-cbc6-4b9c-a339-7d5d7fea6538.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/8d0ee2aa-a1f0-4fc7-a3a7-37f4f7f0feb2.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/4b88f1b8-18a4-4f8f-8774-8e4ba382eb3f.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/b8d2b4a2-249f-4b30-a13a-7d80d1778663.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/06f14a67-a252-4152-af9c-d4a1ba329861.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/e1efde74-3d2e-4ddb-8f4e-90fae9ce5d3a.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/d692364c-6f27-4737-80f1-cd02567d0095.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/844bc709-4e91-4ccf-b5b2-58b3e849db31.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/e36d9523-42cb-486b-96bc-68022759caa6.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/ce763d1e-8ed4-46b9-a3ee-acbb91b21410.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/e8f62bdf-9a9a-4535-89c0-0bd89125dfb2.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/5cfb76ba-d3d7-4f43-bdfc-b078f139b245.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/f835aa02-3b20-4e45-a479-dd6bcedbbb52.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/33e02526-2700-49c2-8a36-3da857246d9a.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_14_0_0_pre1/RelValZEE_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/87aa306c-8366-46aa-8a18-60feed4cbb49.root'
       )
    )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
    )


process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string('electrons.root')
                                   )

process.simpleAnalyzerPath = cms.EndPath(process.simpleElectronAnalyzerSequence)

#process.p = cms.Path(process.mySimpleAnalyzerSequence)
process.schedule = cms.Schedule(process.simpleAnalyzerPath)

process.outpath = cms.EndPath()


