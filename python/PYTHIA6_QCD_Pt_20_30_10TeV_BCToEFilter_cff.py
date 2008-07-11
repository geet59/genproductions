import FWCore.ParameterSet.Config as cms

# in the source below you should add all option necessary for the generation of your physics channel. The example below is for Upsilon production (taken from Configuration/Spring08Production/python/iCSA08_Upsilon_cff.py)

from Configuration.GenProduction.PythiaUESettings_cfi import *
source = cms.Source("PythiaSource",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.00048),
    crossSection = cms.untracked.double(400000000.),
    comEnergy = cms.untracked.double(10000.0),  # center of mass energy in GeV
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring('MSEL=1                 ! QCD high pT processes',
                                        'CKIN(3)=20.          ! minimum pt hat for hard interactions',
                                        'CKIN(4)=30.          ! maximum pt hat for hard interactions'
                                        ),
        parameterSets = cms.vstring('pythiaUESettings', 
                                    'processParameters')
        )
                    )

# if you need some filter modules define and configure them here
genParticlesForFilter = cms.EDProducer("GenParticleProducer",
    saveBarCodes = cms.untracked.bool(True),
    src = cms.InputTag("source"),
    abortOnUnknownPDGCode = cms.untracked.bool(True)
)

bctoefilter = cms.EDFilter("BCToEFilter",
                           filterAlgoPSet = cms.PSet(eTThreshold = cms.double(10),
                                                     genParSource = cms.InputTag("genParticlesForFilter")
                                                     )
                           )


# enter below the configuration metadata (only a description is needed, the rest is filled in by cvs)
configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: $'),
    name = cms.untracked.string('$Source: $'),
    annotation = cms.untracked.string('b/c->e filtered QCD pthat 20-30, 10 TeV')
)

# add your filters to this sequence
ProductionFilterSequence = cms.Sequence(genParticlesForFilter + bctoefilter)
