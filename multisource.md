<button onclick="window.location.href='https://fberumenm.github.io/TOPAS_tutorial_brachytherapy/';">HOME</button>
<button onclick="window.location.href='https://fberumenm.github.io/TOPAS_tutorial_brachytherapy/basic_tutorial';">TUTORIAL</button>
<button onclick="window.location.href='https://fberumenm.github.io/TOPAS_tutorial_brachytherapy/multisource';">MULTISOURCE</button>
<button onclick="window.location.href='https://fberumenm.github.io/TOPAS_tutorial_brachytherapy/mc_tps';">MC vs TPS</button>
<button onclick="window.location.href='https://github.com/fberumenm/TOPAS_tutorial_brachytherapy';">FILES</button>

### Multisource example

 In the [brachytherapy package for TOPAS](https://topas.readthedocs.io/en/latest/examples-docs/Brachytherapy/index.html), single-seed geometries are presented as separated files. Such files can be used as a template to generate the parameters for a multi-seed brachytherapy implant. 
 
The idea is to generate the source parameters in a loop and iterate over seed positions. Let's consider the example of 3 SelectSeeds sources. For positions consider the simple 3 vectors (1,1,1), (2,2,2), and (3,3,3), that indicate the seed positions in cm.

The first step is to create a group component that will be the parent of all 3 seeds. We can add a translation of the whole seed group component. Using [Python](https://www.python.org/), we can simply print the parameters as shown below, users can print text directly to a txt file as well. Note that the group component must be parallel to insert the seeds implant in a patient geometry [(layered mass geometry method)](https://topas.readthedocs.io/en/latest/parameters/geometry/parallel_world.html).

```python
# Translation of the whole seeds group
TransX = 0
TransY = 0
TransZ = 0

print("""
s:Ge/GroupOfSeeds/Type              = "Group"
s:Ge/GroupOfSeeds/Parent            = "World"
b:Ge/GroupOfSeeds/IsParallel        = "True"
s:Ge/GroupOfSeeds/ParallelWorldName = "SeedsWorld"
d:Ge/GroupOfSeeds/TransX            = {0} mm
d:Ge/GroupOfSeeds/TransY            = {1} mm
d:Ge/GroupOfSeeds/TransZ            = {2} mm
""".format(TransX,TransY,TransZ))

```
The next step is to generate the parameters defining the seeds.  As before, we need to define the positional arguments of the string.format method to account for the seed position (x,y,z), and the seed number. Particularly, consider only the parameters of the Titanium Tube. Note that the full list of parameters should follow a similar structure.


```python
# Number of seeds
seeds = 3

# Create an array with the seeds positions
# In this example, we used the vectors (1,1,1), (2,2,2), (3,3,3) 
PosX = np.arange(start = 1, stop = 4, step = 1)
PosY = np.arange(start = 1, stop = 4, step = 1)
PosZ = np.arange(start = 1, stop = 4, step = 1)
```
Note that each seed is a group component itself and must follow the corrrect seed number indicator (iterable value or something similar).

```python
# Print parameters of SelectSeed
# Only the parameters of the Titanium tube are shown
for i in range (seeds):
    print("""
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
s:Ge/TitaniumTube{0}/DrawingStyle = "Solid"
b:Ge/TitaniumTube{0}/IsParallel        = "True"
s:Ge/TitaniumTube{0}/ParallelWorldName = "SeedsWorld"

""".format(i,PosX[i],PosY[i],PosZ[i]))
```
In conclusion, with the given parameter files which are included in the brachytherapy package for TOPAS, multi-seed simulations are possible by taking those files as a template and looping over for each seed position.


 