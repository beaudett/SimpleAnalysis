import FWCore.ParameterSet.Config as cms

process = cms.Process("validation")

process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("SimpleAnalysis.RecoEgamma.simpleanalyzer_cff")
process.load('DQMOffline.Configuration.DQMOffline_cff')

process.source = cms.Source("PoolSource",
#    debugVerbosity = cms.untracked.uint32(1),
#    debugFlag = cms.untracked.bool(True),
    fileNames = cms.untracked.vstring(
        'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/7475d28b-ae6a-4851-bf8b-3d8474855326.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/25f18918-9e4f-410c-b05f-e90b7ee43847.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/268a32e4-aca0-4d7d-a778-eeff6c2f040b.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/9b5c08e3-94f1-411a-9196-a4b1305c0c9d.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/9aa4ddf5-b429-4ece-8b73-13b8a5e1bef7.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/a50e94e5-e525-491c-aa17-d5b4fe037d8c.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/9a7b615c-5f8c-48a3-bf4e-165aa0a14f97.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/7f2134e0-dffe-4829-95c1-1d93bc328e17.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/7ced6445-1ade-4d84-9472-f112013a8b79.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/f196a223-3ae2-4904-a48b-f084e45cfe81.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/f54a43b0-fd43-410f-813d-b45b69695255.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/fed50f68-29b5-4f06-9607-ddec052ae5db.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/e548d79b-f275-4d91-b4d6-1acbac3c0788.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/c483ecb2-7c36-480f-8cd9-e8028cdb9f5a.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/8b40ef33-8fe1-49d3-a8ce-67d7fffc794a.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/222ebbb6-b09e-424b-a284-205f65564c3a.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/23664a9d-c739-4205-8d31-1f77873d0cea.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/31257d04-3d53-4493-84f7-0237a3a83c70.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/a53b7ece-c754-4165-bf38-a5973ce65166.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/5e1754d8-636e-48fa-bc84-713fcf223c67.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/ebe252b7-a713-41fc-a60e-1b70a41eed52.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/bf070595-badb-41a3-a60c-ac9b8cfbc7eb.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/d04c8573-0e62-40fb-8b5d-c59b9b075289.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/c0f39a9f-1d0b-4c0e-aa58-d35720de9fbd.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/58e3c5da-2c09-4993-9ea1-b1bc8d46f820.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/d9cba56e-fb02-4e18-8a4b-a44ce1f88ff7.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/96e96289-f616-4683-8d78-d762380c58b7.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/74959a35-1935-4387-afae-0c6d3daef36e.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/06e485b4-79bb-43a8-a8c5-03a4ff18b147.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/7fc2aed9-fea8-4a0f-9ca9-5b22760717d8.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/ceddf7da-d98b-4c02-a3ac-ddae5922f728.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/350b003d-cd6d-4a44-9199-768f9c399898.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/189b3c1b-acdd-4170-8caa-42ff6e0db0bb.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/e9df5b44-b636-4182-9d8c-5fabbba20bf8.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/4be4b99a-0ee8-4da7-907a-edff3c8d885d.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/24330984-30a0-45f4-b880-4239b44a61c1.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/17908940-3031-4f9f-9518-267e637a0c6b.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/dc7aab25-5f3f-46ef-b23c-0f69980ea15f.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/c506dfb2-5bf7-483e-81db-4723b862536b.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/b2ea494f-90ed-4a0b-8250-2d54852f8c58.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/7fd7fb1d-7759-48f1-8acc-a0229dd091e1.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/a9210bfa-1bf8-40aa-b227-8ddab5dc6b87.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/33aadd69-1875-4b29-8cbd-95d8a552119a.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/b757f042-9d3f-492f-bb12-b72941e40d41.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/e644dbed-0034-40d0-9b56-f1b37420a5d8.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/e16c7834-87c0-49b9-bc0f-f808a11eb87c.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/7a568c95-d2e6-440e-90cf-f7c1d118287e.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/933fe69a-9887-4737-82e9-b2e0a81130de.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/89cd97a5-a7da-42bf-bf2b-589bb0c74f1b.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/9a652ec1-54d4-4c73-8379-3bc2152d4a77.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/6b194bb6-def2-4455-9066-a38ccaa1d3d7.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/bbc28c9d-46b9-4cfe-a454-9d5d29b4aa3d.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/cb83b649-0985-4bcf-81c7-177b1c85d34a.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/1d6a2bb1-be59-486b-a9b8-5d260216bf55.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/d105ef83-c0ef-4946-9696-b3ef4af78973.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/c2855a45-5ef1-43e4-a641-6d9b4213c7e3.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/a6efc21e-8c56-415e-b9a5-724e54aa336d.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/a2f4a4c7-3ffa-4eca-9355-c0b51a925cb7.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/88e8c9cb-4c33-4e86-a1e6-3e42788c3017.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/3fc9e595-de7c-4495-8c0c-3107266918b1.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/c4604c4d-4303-4f77-ae03-4a2943591b1e.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/25d73242-0c8a-445c-aa1e-33683c1998c1.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/3f11b3e6-684a-4691-b97f-5370227f6729.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/b82b6ded-9ba0-47e6-af58-9c0ece23b6b1.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/384685a8-0f97-401f-bf4e-dd4c5cf8e9dc.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/0430adf2-5655-44df-bbc5-e9ab076f09fd.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/dc6babff-5b70-401d-932b-ec5566e53021.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/5e65ec2e-2861-4a78-878b-40bb3f024e1d.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/6eadbb9c-bd87-40bd-a89c-d44f76fc4a36.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/dd02f761-6e13-49c4-a840-e323bb3fcf00.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/46cad31f-6127-421d-a3bf-7b19244c69cf.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/61a33d28-587e-40e1-a47d-1bcf794c5dcf.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/b49e282f-6b47-4d3a-9d8a-da895b048899.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/a09a9677-6937-4b8b-be16-b020e21890b7.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/3dfdb891-7b7a-42f3-bf58-e57d640bcaae.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/bc769ac6-bf8a-44e8-b0b4-15cc543e4222.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/693a67ff-9c02-467e-9d5c-76c2b8b1d94c.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/750f94d4-6983-475d-a2ce-73fedf5737e7.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/1453d11a-3947-4539-8ea6-c2be15e85cd1.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/26d4f136-09a8-46ef-bee3-8fe571eeb221.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/7efccf13-eccb-4b66-9139-bc4869a916ea.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/28954de6-d5d2-4b42-b029-2e08c4712dd5.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/05c5bbb6-bc95-4648-b598-8e19e8197b6d.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/1875a007-9c06-43ca-8348-ab7ff2b5e83e.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/47089572-ef8a-4c83-9a16-3087afd62bf5.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/1b541557-751c-4ddf-b697-d230d19ac053.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/e696c63e-8554-4854-b632-267d0753362f.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/4c6338df-8e50-4ead-88ac-702a447b0d27.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/6758314d-69f8-4cf4-95da-d8c5f348272a.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/de9eb239-5089-4c83-8b78-f83e981aac3a.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/b1469ebc-7808-4d1b-8071-de35a6f6010a.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/e0fbd7cb-e055-4432-88fb-fcfc7ab7f2dd.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/079cdd6e-81af-48f2-bd83-001ec44a429d.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/ca133cf2-2d78-4d46-9a76-25f8de7088c6.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/3ac306df-519a-4c7c-b078-a62f07eb9c82.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/32bb05ef-034c-4c7e-a62b-f12cb0a960be.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/260d3eef-d7d7-47e5-b562-e280038bad80.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/1513dae1-bac7-4a3a-b09e-cb3e1556e41c.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/1776a8a6-752d-465b-924d-5a3fa87f4a18.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/7771537c-4f51-4b96-b30e-da4723efe32b.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/e87d4f61-5564-4058-8a08-d97f4a7a51bc.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/7e0c7c5a-7565-4ecd-ab91-bc3a37820132.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/2a7f2e16-d56f-4bdb-808e-8ce452c18806.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/763f78f4-264e-4e87-9b77-cf5a920b6303.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/14188da9-2462-49b3-874b-91276b52ecbc.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/f53eda67-23d1-4cee-a6f0-04c0f2d1221b.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/f44eb9cc-bb6b-4dbc-bc4b-49e96a3d31e6.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/fc2a6da3-1fc2-4346-a6a8-da0c3766c6e8.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/e0a6d6c1-b0a6-4b69-84f3-4189721ca1f5.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/57ccec27-4bfb-488a-ba02-e3d6204d36e5.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/e5694590-1d38-4ea0-8c34-ed9a4281f06e.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/909330ab-cf85-47da-94ba-4a6ac882247f.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/7d52c66f-9fa8-4fbd-84a4-15e8e490769d.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/13a5acfe-2d35-404f-ad7b-d136209824ad.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/72356876-1c84-4d6c-87bd-0665ccecd766.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/9de61632-aea2-47c8-b068-a2fc5cde9b26.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/ea4f3914-d6c6-4f25-b3e0-e366443b9db8.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/e4c0fca8-9c39-485a-b808-fb0f2882308c.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/ea06a87d-9e21-45d5-8a51-c81bacb646ed.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/d985dab9-4400-443d-867c-a2071fcf0f55.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/8bde1cd3-a0bd-46ef-8a8a-42b07d472781.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/625fac5d-5afe-4770-a22a-81fcbbd7b2bc.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/409e5498-8b87-4ca4-ad90-0288faeb5a1e.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/8ba2e01f-96c4-4d48-aa3c-e3b0cec17cff.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/e39597b9-7b06-4ac7-bbc7-1f8cdf8bbe50.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/4a572c7e-2317-4534-8b49-4ff2eb9b29b6.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/6add57c0-3b33-47c8-9361-70d4f4ac11eb.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/af9dce4b-d1ed-4ba8-88bb-56957e4787ff.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/19cdaa6d-1376-409b-bba9-9fac3b93b243.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/7d6e897a-ec52-4521-b08d-82198565346d.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/a74ec2b9-bd70-4fda-8da3-d7bcdeb19521.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/cb19bd2b-c46f-4206-b9f8-ebd453551327.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/cdd76e27-3625-4057-adb0-292d764412f1.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/d5db5832-e27f-45a1-a8e5-c4a6f1cdb0b1.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/e494c224-0fdc-44d0-a335-35904b7ce11a.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/d349c4f8-5a85-4e29-985e-9f18d4112081.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/ae275991-f7d1-40d3-95cd-892931252bf2.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/7d1b6df8-5909-4859-a277-ca1499a83f9d.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/931c0e64-9165-48c1-8e08-b227e3e1b189.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/957bf90b-4f43-4cd7-9c70-56113e097989.root',
'root://xrootd-cms.infn.it///store/relval/CMSSW_12_6_0_pre2/RelValH125GGgluonfusion_14/GEN-SIM-RECO/PU_125X_mcRun4_realistic_v2_2026D88PU200_ReProd-v1/00000/c6b60202-101b-47b3-8b1c-f14b296104ed.root'))    

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string('histodemo_pre2.root')
                                   )

process.simpleAnalyzerPath = cms.EndPath(process.simpleAnalyzerSequence)

#process.p = cms.Path(process.mySimpleAnalyzerSequence)
process.schedule = cms.Schedule(process.simpleAnalyzerPath)

process.outpath = cms.EndPath()


