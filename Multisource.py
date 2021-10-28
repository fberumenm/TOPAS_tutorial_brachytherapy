import numpy as np

# Create the txt file
filename = 'mysources.txt'
open(filename, "w").close()

# Number of seeds
seeds = 10

# Translation of the whole seeds group
TransX = 0
TransY = 0
TransZ = 0

NumberHistoriesPerSeed = 100000

# Create an array with the seeds positions 
PosX = np.arange(start = 1, stop = 11, step = 1)
PosY = np.arange(start = 1, stop = 11, step = 1)
PosZ = np.arange(start = 1, stop = 11, step = 1)

# Print parameters in the file
print("""
# ====================================================== #
#                Iodine 125 - SelectSeeds                #
# ====================================================== #
includeFile = ../../../SeedMaterials.txt

s:Ge/GroupOfSeeds/Type              = "Group"
s:Ge/GroupOfSeeds/Parent            = "World"
b:Ge/GroupOfSeeds/IsParallel        = "True"
s:Ge/GroupOfSeeds/ParallelWorldName = "SeedsWorld"
d:Ge/GroupOfSeeds/TransX            = {0} mm
d:Ge/GroupOfSeeds/TransY            = {1} mm
d:Ge/GroupOfSeeds/TransZ            = {2} mm
""".format(TransX,TransY,TransZ),file=open(filename, "a"))

for i in range (seeds):
    print("""
ic:So/ActiveSource{0}/NumberOfHistoriesInRun    = {4}   

s:Ge/Seed{0}/Type              = "Group"
s:Ge/Seed{0}/Parent            = "GroupOfSeeds"
b:Ge/Seed{0}/IsParallel        = "True"
s:Ge/Seed{0}/ParallelWorldName = "SeedsWorld"
d:Ge/Seed{0}/TransX            = {1} mm
d:Ge/Seed{0}/TransY            = {2} mm
d:Ge/Seed{0}/TransZ            = {3} mm

##### TITANIUM TUBE
s:Ge/TitaniumTube{0}/Type         = "TsCylinder"
s:Ge/TitaniumTube{0}/Material     = "MatTitaniumTube"
s:Ge/TitaniumTube{0}/Parent       = "Seed{0}"
d:Ge/TitaniumTube{0}/RMin         = 0 mm
d:Ge/TitaniumTube{0}/RMax         = 0.4 mm
d:Ge/TitaniumTube{0}/HL           = 1.85 mm
d:Ge/TitaniumTube{0}/SPhi         = 0. deg
d:Ge/TitaniumTube{0}/DPhi         = 360. deg
s:Ge/TitaniumTube{0}/Color        = "transparentgray2"
s:Ge/TitaniumTube{0}/DrawingStyle = "Solid"
b:Ge/TitaniumTube{0}/IsParallel        = "True"
s:Ge/TitaniumTube{0}/ParallelWorldName = "SeedsWorld"

##### TITANIUM CAP L
s:Ge/TitaniumCapL{0}/Type         = "TsSphere"
s:Ge/TitaniumCapL{0}/Material     = "MatTitaniumTube"
s:Ge/TitaniumCapL{0}/Parent       = "Seed{0}"
d:Ge/TitaniumCapL{0}/RMin         = 0. mm
d:Ge/TitaniumCapL{0}/RMax         = 0.4 mm
d:Ge/TitaniumCapL{0}/SPhi         = 0. deg
d:Ge/TitaniumCapL{0}/DPhi         = 360. deg
d:Ge/TitaniumCapL{0}/STheta       = 0. deg
d:Ge/TitaniumCapL{0}/DTheta       = 90. deg
d:Ge/TitaniumCapL{0}/TransZ       = 1.85 mm
s:Ge/TitaniumCapL{0}/DrawingStyle = "Solid"
s:Ge/TitaniumCapL{0}/Color        = "transparentgray2"
b:Ge/TitaniumCapL{0}/IsParallel        = "True"
s:Ge/TitaniumCapL{0}/ParallelWorldName = "SeedsWorld"

##### TITANIUM CAP R
s:Ge/TitaniumCapR{0}/Type         = "TsSphere"
s:Ge/TitaniumCapR{0}/Material     = "MatTitaniumTube"
s:Ge/TitaniumCapR{0}/Parent       = "Seed{0}"
d:Ge/TitaniumCapR{0}/RMin         = 0. mm
d:Ge/TitaniumCapR{0}/RMax         = 0.4 mm
d:Ge/TitaniumCapR{0}/SPhi         = 0. deg
d:Ge/TitaniumCapR{0}/DPhi         = 360. deg
d:Ge/TitaniumCapR{0}/STheta       = 90. deg
d:Ge/TitaniumCapR{0}/DTheta       = 180. deg
d:Ge/TitaniumCapR{0}/TransZ       = -1.85 mm
s:Ge/TitaniumCapR{0}/DrawingStyle = "Solid"
s:Ge/TitaniumCapR{0}/Color        = "transparentgray2"
b:Ge/TitaniumCapR{0}/IsParallel        = "True"
s:Ge/TitaniumCapR{0}/ParallelWorldName = "SeedsWorld"

##### AIR
s:Ge/InsideAir{0}/Type         = "TsCylinder"
s:Ge/InsideAir{0}/Material     = "G4_AIR"
s:Ge/InsideAir{0}/Parent       = "TitaniumTube{0}"
d:Ge/InsideAir{0}/RMin         = 0 mm
d:Ge/InsideAir{0}/RMax         = Ge/TitaniumTube{0}/RMax - 0.05 mm
d:Ge/InsideAir{0}/HL           = 1.85 mm
d:Ge/InsideAir{0}/SPhi         = 0. deg
d:Ge/InsideAir{0}/DPhi         = 360. deg
s:Ge/InsideAir{0}/Color        = "transparentgray"
s:Ge/InsideAir{0}/DrawingStyle = "Solid"
b:Ge/InsideAir{0}/IsParallel        = "True"
s:Ge/InsideAir{0}/ParallelWorldName = "SeedsWorld"

##### RADIOACTIVE LAYER
s:Ge/RadioactiveLayer{0}/Type         = "TsCylinder"
s:Ge/RadioactiveLayer{0}/Material     = "MatRadioactiveLayer"
s:Ge/RadioactiveLayer{0}/Parent       = "InsideAir{0}"
d:Ge/RadioactiveLayer{0}/RMin         = 0 mm
d:Ge/RadioactiveLayer{0}/RMax         = 0.258 mm
d:Ge/RadioactiveLayer{0}/HL           = 1.703 mm
d:Ge/RadioactiveLayer{0}/SPhi         = 0. deg
d:Ge/RadioactiveLayer{0}/DPhi         = 360. deg
b:Ge/RadioactiveLayer{0}/Invisible    = "True" 
b:Ge/RadioactiveLayer{0}/IsParallel        = "True"
s:Ge/RadioactiveLayer{0}/ParallelWorldName = "SeedsWorld"

##### CYLINDRICAL SILVER ROD
s:Ge/SilverRod{0}/Type         = "TsCylinder"
s:Ge/SilverRod{0}/Material     = "MatSilverRod"
s:Ge/SilverRod{0}/Parent       = "RadioactiveLayer{0}"
d:Ge/SilverRod{0}/RMin         = 0 mm
d:Ge/SilverRod{0}/RMax         = Ge/RadioactiveLayer{0}/RMax - 0.003 mm
d:Ge/SilverRod{0}/HL           = Ge/RadioactiveLayer{0}/HL - 0.003 mm
d:Ge/SilverRod{0}/SPhi         = 0. deg
d:Ge/SilverRod{0}/DPhi         = 360. deg
s:Ge/SilverRod{0}/Color        = "White"
s:Ge/SilverRod{0}/DrawingStyle = "Solid"
b:Ge/SilverRod{0}/IsParallel        = "True"
s:Ge/SilverRod{0}/ParallelWorldName = "SeedsWorld"

s:So/ActiveSource{0}/Type                       = "Volumetric"
s:So/ActiveSource{0}/Component                  = "RadioactiveLayer{0}"
sc:So/ActiveSource{0}/ActiveMaterial            = "MatRadioactiveLayer"
s:So/ActiveSource{0}/BeamParticle               = "gamma"
ic:So/ActiveSource{0}/MaxNumberOfPointsToSample = 1000000000
s:So/ActiveSource{0}/BeamEnergySpectrumType    = "Discrete"

#### I-125 SPECTRUM ####
dv:So/ActiveSource{0}/BeamEnergySpectrumValues = 7 3.77 27.202 27.472 30.944 30.995 31.704 35.4922 keV
uv:So/ActiveSource{0}/BeamEnergySpectrumWeightsUnscaled = 7 0.149 0.401 0.740 0.0683 0.132 0.0380 0.0668
uv:So/ActiveSource{0}/BeamEnergySpectrumWeights = 0.626919 * So/ActiveSource{0}/BeamEnergySpectrumWeightsUnscaled
""".format(i,PosX[i],PosY[i],PosZ[i],NumberHistoriesPerSeed),file=open(filename, "a"))

print("""
iv:Gr/Color/transparentgray = 4 255 255 255 100
iv:Gr/Color/transparentgray2 = 4 200 200 200 100
""",file=open(filename, "a"))