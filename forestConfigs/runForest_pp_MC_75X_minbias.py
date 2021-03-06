#!/usr/bin/env python2
# Run the foresting configuration on PbPb in CMSSW_5_3_X, using the new HF/Voronoi jets
# Author: Alex Barbieri
# Date: 2013-10-15

import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')
process.options = cms.untracked.PSet(
    # wantSummary = cms.untracked.bool(True)
    #SkipEvent = cms.untracked.vstring('ProductNotFound')
)

#####################################################################################
# HiForest labelling info
#####################################################################################

process.load("HeavyIonsAnalysis.JetAnalysis.HiForest_cff")
process.HiForest.inputLines = cms.vstring("HiForest V3",)
import subprocess
version = subprocess.Popen(["(cd $CMSSW_BASE/src && git describe --tags)"], stdout=subprocess.PIPE, shell=True).stdout.read()
if version == '':
    version = 'no git info'
process.HiForest.HiForestVersion = cms.untracked.string(version)

#####################################################################################
# Input source
#####################################################################################

process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                            fileNames = cms.untracked.vstring(
    "file:step3_RAW2DIGI_L1Reco_RECO_1000_1_Rc8.root"
    ))

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10))


#####################################################################################
# Load Global Tag, Geometry, etc.
#####################################################################################

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('RecoHI.HiCentralityAlgos.CentralityBin_cfi')

process.load('FWCore.MessageService.MessageLogger_cfi')

# pp 75X MC
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc_HIon', '')

process.load("CondCore.DBCommon.CondDBCommon_cfi")
from CondCore.DBCommon.CondDBSetup_cfi import *
process.jec = cms.ESSource("PoolDBESSource",
      DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0)
        ),
      timetype = cms.string('runnumber'),
      toGet = cms.VPSet(
      cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v3_AK1Calo_offline'),
            label  = cms.untracked.string('AK1Calo_offline')
            ),
      cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v3_AK2Calo_offline'),
            label  = cms.untracked.string('AK2Calo_offline')
            ),
      cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v3_AK3Calo_offline'),
            label  = cms.untracked.string('AK3Calo_offline')
            ),
      cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v3_AK4Calo_offline'),
            label  = cms.untracked.string('AK4Calo_offline')
            ),
      cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v3_AK5Calo_offline'),
            label  = cms.untracked.string('AK5Calo_offline')
            ),
      cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v3_AK6Calo_offline'),
            label  = cms.untracked.string('AK6Calo_offline')
            ),
      cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v3_AK1PF_offline'),
            label  = cms.untracked.string('AK1PF_offline')
            ),
      cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v3_AK2PF_offline'),
            label  = cms.untracked.string('AK2PF_offline')
            ),
      cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v3_AK3PF_offline'),
            label  = cms.untracked.string('AK3PF_offline')
            ),
      cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v3_AK4PF_offline'),
            label  = cms.untracked.string('AK4PF_offline')
            ),
      cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v3_AK5PF_offline'),
            label  = cms.untracked.string('AK5PF_offline')
            ),
      cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v3_AK6PF_offline'),
            label  = cms.untracked.string('AK6PF_offline')
            ),
      ## here you add as many jet types as you need
      ## note that the tag name is specific for the particular sqlite file 
      ), 
      connect = cms.string('sqlite:HI_PythiaCUETP8M1_5020GeV_753p1_v3.db')
     # uncomment above tag lines and this comment to use MC JEC
     # connect = cms.string('sqlite:Summer12_V7_MC.db')
)
## add an es_prefer statement to resolve a possible conflict from simultaneous connection to a global tag
process.es_prefer_jec = cms.ESPrefer('PoolDBESSource','jec')


# process.GlobalTag.toGet = cms.VPSet(
# cms.PSet(record = cms.string('PTrackerParametersRcd'),
              # tag = cms.string('TKParameters_Geometry_Run2_Test02'),
              # connect = cms.string("sqlite_file:TrackerGeometryExtended2015.db")
              # ),
# )

# from HeavyIonsAnalysis.Configuration.CommonFunctionsLocalDB2015_cff import *
# overrideGT_pp2760(process)
# overrideJEC_pp5020(process)

process.HeavyIonGlobalParameters = cms.PSet(
    centralityVariable = cms.string("HFtowersTrunc"),
    nonDefaultGlauberModel = cms.string("Hijing"),
    centralitySrc = cms.InputTag("hiCentrality")
    )

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("HiForest.root"))

#####################################################################################
# Additional Reconstruction and Analysis: Main Body
#####################################################################################

process.load('Configuration.StandardSequences.Generator_cff')
process.load('RecoJets.Configuration.GenJetParticles_cff')

process.hiCentrality.producePixelhits = False
process.hiCentrality.producePixelTracks = False
process.hiCentrality.srcTracks = cms.InputTag("generalTracks")
process.hiCentrality.srcVertex = cms.InputTag("offlinePrimaryVerticesWithBS")

process.load('RecoHI.HiJetAlgos.HiGenJets_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak1PFJetSequence_pp_jec_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak1CaloJetSequence_pp_jec_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak2PFJetSequence_pp_jec_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak2CaloJetSequence_pp_jec_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak3PFJetSequence_pp_jec_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak3CaloJetSequence_pp_jec_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak4PFJetSequence_pp_jec_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak4CaloJetSequence_pp_jec_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak5PFJetSequence_pp_jec_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak5CaloJetSequence_pp_jec_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak6PFJetSequence_pp_jec_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak6CaloJetSequence_pp_jec_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu1PFJetSequence_pp_jec_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu1CaloJetSequence_pp_jec_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu2PFJetSequence_pp_jec_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu2CaloJetSequence_pp_jec_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu3PFJetSequence_pp_jec_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu3CaloJetSequence_pp_jec_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu4PFJetSequence_pp_jec_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_pp_jec_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu5PFJetSequence_pp_jec_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu5CaloJetSequence_pp_jec_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu6PFJetSequence_pp_jec_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu6CaloJetSequence_pp_jec_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs1PFJetSequence_pp_jec_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs1CaloJetSequence_pp_jec_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs2PFJetSequence_pp_jec_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs2CaloJetSequence_pp_jec_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs3PFJetSequence_pp_jec_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs3CaloJetSequence_pp_jec_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs4PFJetSequence_pp_jec_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs4CaloJetSequence_pp_jec_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs5PFJetSequence_pp_jec_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs5CaloJetSequence_pp_jec_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs6PFJetSequence_pp_jec_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs6CaloJetSequence_pp_jec_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.HiReRecoJets_pp_cff')


process.voronoiBackgroundPF.src = cms.InputTag("particleFlow")
process.PFTowers.src = cms.InputTag("particleFlow")


process.jetSequences = cms.Sequence(
                                    # process.akPu1PFJetSequence +
                                    # process.akPu1CaloJetSequence +
									
                                    # process.akPu2PFJetSequence +
                                    # process.akPu2CaloJetSequence +
									
                                    # process.akPu3PFJetSequence +
                                    # process.akPu3CaloJetSequence +
									
                                    # process.akPu4PFJetSequence +
                                    # process.akPu4CaloJetSequence +
									
                                    # process.akPu5PFJetSequence +
                                    # process.akPu5CaloJetSequence +
									
                                    # process.akPu6PFJetSequence +
                                    # process.akPu6CaloJetSequence +
                                    
                                    # process.ak1PFJetSequence +
                                    # process.ak1CaloJetSequence +
									
                                    # process.ak2PFJetSequence +
                                    # process.ak2CaloJetSequence +
									
                                    # process.ak3PFJetSequence +
                                    # process.ak3CaloJetSequence +
									
                                    process.ak4PFJetSequence +
                                    process.ak4CaloJetSequence 
									
                                    # process.ak5PFJetSequence +
                                    # process.ak5CaloJetSequence +
									
                                    # process.ak6PFJetSequence +
                                    # process.ak6CaloJetSequence 
                                    )
									

process.akPu1PFJetAnalyzer.doSubEvent = True 
process.akPu2PFJetAnalyzer.doSubEvent = True
process.akPu3PFJetAnalyzer.doSubEvent = True
process.akPu4PFJetAnalyzer.doSubEvent = True
process.akPu5PFJetAnalyzer.doSubEvent = True
process.akPu6PFJetAnalyzer.doSubEvent = True

process.ak1PFJetAnalyzer.doSubEvent = True 
process.ak2PFJetAnalyzer.doSubEvent = True
process.ak3PFJetAnalyzer.doSubEvent = True
process.ak4PFJetAnalyzer.doSubEvent = True
process.ak5PFJetAnalyzer.doSubEvent = True
process.ak6PFJetAnalyzer.doSubEvent = True

process.akPu1CaloJetAnalyzer.doSubEvent = True  
process.akPu2CaloJetAnalyzer.doSubEvent = True
process.akPu3CaloJetAnalyzer.doSubEvent = True
process.akPu4CaloJetAnalyzer.doSubEvent = True
process.akPu5CaloJetAnalyzer.doSubEvent = True
process.akPu6CaloJetAnalyzer.doSubEvent = True

process.ak1CaloJetAnalyzer.doSubEvent = True 
process.ak2CaloJetAnalyzer.doSubEvent = True
process.ak3CaloJetAnalyzer.doSubEvent = True
process.ak4CaloJetAnalyzer.doSubEvent = True
process.ak5CaloJetAnalyzer.doSubEvent = True
process.ak6CaloJetAnalyzer.doSubEvent = True


process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_mc_cfi')
process.load('HeavyIonsAnalysis.JetAnalysis.HiGenAnalyzer_cfi')

process.hiEvtAnalyzer.Vertex = cms.InputTag("offlinePrimaryVerticesWithBS")


#####################################################################################
# To be cleaned

process.load('HeavyIonsAnalysis.JetAnalysis.ExtraTrackReco_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.TrkAnalyzers_MC_cff')
process.load("HeavyIonsAnalysis.TrackAnalysis.METAnalyzer_cff")
process.load("HeavyIonsAnalysis.JetAnalysis.pfcandAnalyzer_pp_cfi")
process.load('HeavyIonsAnalysis.JetAnalysis.rechitanalyzer_pp_cfi')
# process.rechitAna = cms.Sequence(process.rechitanalyzer+process.pfTowers)
process.pfcandAnalyzer.skipCharged = False
process.pfcandAnalyzer.pfPtMin = 0
process.pfcandAnalyzer.pfCandidateLabel = cms.InputTag("particleFlow")
process.pfcandAnalyzer.doVS = cms.untracked.bool(False)
process.pfcandAnalyzer.doUEraw_ = cms.untracked.bool(False)
process.pfcandAnalyzer.genLabel = cms.InputTag("genParticles")

#####################################################################################

#########################
# Track Analyzer
#########################
process.hiTracks.cut = cms.string('quality("highPurity")')

#########################
# Track Analyzer
#########################
process.ppTrack.qualityStrings = cms.untracked.vstring(['highPurity','tight','loose'])

process.hiTracks.cut = cms.string('quality("highPurity")')

# set track collection to iterative tracking
process.ppTrack.trackSrc = cms.InputTag("generalTracks")
process.ppTrack.mvaSrc = cms.string("generalTracks")
 
process.ppTrack.doSimVertex = False
process.ppTrack.doSimTrack = False

process.load("SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cff")
process.tpRecoAssocGeneralTracks = process.trackingParticleRecoTrackAsssociation.clone()
process.tpRecoAssocGeneralTracks.label_tr = cms.InputTag("generalTracks")
process.quickTrackAssociatorByHits.ComponentName = cms.string('quickTrackAssociatorByHits')
process.quickTrackAssociatorByHits.SimToRecoDenominator = cms.string('reco')
process.quickTrackAssociatorByHits.Cut_RecoToSim = cms.double(0.75)
process.quickTrackAssociatorByHits.Quality_SimToReco = cms.double(0.5)


#####################
# photons 
######################
process.load('RecoJets.Configuration.GenJetParticles_cff')
process.genParticlesForJets.ignoreParticleIDs += cms.vuint32( 12,14,16)

process.load('HeavyIonsAnalysis.PhotonAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.gsfElectronLabel   = cms.InputTag("gedGsfElectrons")
process.ggHiNtuplizer.useValMapIso       = cms.bool(False)
process.ggHiNtuplizer.VtxLabel           = cms.InputTag("offlinePrimaryVerticesWithBS")
process.ggHiNtuplizer.particleFlowCollection = cms.InputTag("particleFlow")
process.ggHiNtuplizer.doVsIso            = cms.bool(False)
process.ggHiNtuplizer.doGenParticles = False
process.ggHiNtuplizerGED = process.ggHiNtuplizer.clone(recoPhotonSrc = cms.InputTag('gedPhotons'))

process.akHiGenJets = cms.Sequence(
                             process.genParticlesForJets +
                             # process.ak1HiGenJets +
                             # process.ak2HiGenJets +
                             # process.ak3HiGenJets +
                             process.ak4HiGenJets 
                             # process.ak5HiGenJets +
                             # process.ak6HiGenJets
							 )
						
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')

process.HiGenParticleAna.genParticleSrc = cms.untracked.InputTag("genParticles")
process.HiGenParticleAna.doHI = False

process.ana_step = cms.Path(process.hltanalysis *
                            process.HiGenParticleAna*
                            process.PFTowers +
                            # process.hiReRecoPFJets+
                            # process.hiReRecoCaloJets+
						               	process.akHiGenJets  +
                            process.jetSequences +
                            process.ggHiNtuplizer +
                            process.ggHiNtuplizerGED +
                            # process.pfcandAnalyzer +
   						              process.quickTrackAssociatorByHits +
							              # process.tpRecoAssocGeneralTracks +
                            process.HiForest +
                            process.ppTrack
							)


process.load("HeavyIonsAnalysis.VertexAnalysis.PAPileUpVertexFilter_cff")

process.pVertexFilterCutG = cms.Path(process.pileupVertexFilterCutG)
process.pVertexFilterCutGloose = cms.Path(process.pileupVertexFilterCutGloose)
process.pVertexFilterCutGtight = cms.Path(process.pileupVertexFilterCutGtight)
process.pVertexFilterCutGplus = cms.Path(process.pileupVertexFilterCutGplus)
process.pVertexFilterCutE = cms.Path(process.pileupVertexFilterCutE)
process.pVertexFilterCutEandG = cms.Path(process.pileupVertexFilterCutEandG)


# Customization

process.pAna = cms.EndPath(process.skimanalysis)