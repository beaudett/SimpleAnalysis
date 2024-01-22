import FWCore.ParameterSet.Config as cms

from SimpleAnalysis.RecoEgamma.simpleElectronAnalyzer_cfi import *

simpleElectronAnalyzerSequence = cms.Sequence(electronValidation)