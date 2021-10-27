### Monte Carlo Simulations for Brachytherapy using the TOPAS toolkit
_Overview_ 

Monte Carlo (MC) techniques use randomized mathematical methods to determine estimates of numerical quantities according to appropriate probability distributions and rules. In the specific case of radiation transport, mechanisms of radiation interaction with matter are governed by probability distributions. More precisely, discrete interaction processes are described by the relevant cross sections. In that sense, the MC method is fully applicable to radiation transport problems. 

In the field of medical physics, the MC method is mostly used to study the interaction of radiation with the patient, imaging devices, treatment sources/units, and radiation detectors. In such a way, complex scenarios can be simulated. These educational resources are focused on brachytherapy, a form of radiation therapy, in which sealed sources are inserted into the patient to closely treat lesions.

[TOPAS](http://www.topasmc.org/) is a toolkit that performs advanced Monte Carlo simulations of all forms of radiation therapy setups. The toolkit allows users to set up complex simulations through simple text files which in turn indicate a series of parameters. This parameter system is fully described in the official [TOPAS documentation](https://topas.readthedocs.io/en/latest/getting-started/intro.html) site. To account for an accurate brachytherapy source modeling, TOPAS includes a volumetric source that randomly samples positions, in a given geometry component, to generate particles.


The TOPAS version 3.7 includes a brachytherapy package of source models and a track-length estimator for dose scoring [(link)](https://topas.readthedocs.io/en/latest/examples-docs/Brachytherapy/index.html). Such package was developed by the [Medical Physics Research Group at Université Laval](https://physmed.fsg.ulaval.ca).This tutorial gives some insights on how the sources are modeled and some common simulation setups (for example, the TG-43 parameters setup). Additionally, the TOPAS Time Feature System is described and used to simulate a prostate case. A couple of advanced examples (a multi-source setup, and a MC vs TPS comparison) are described as well.

For any presentation or publication using the track-length estimator or brachytherapy related calculation, please cite the following published works:

* Francisco Berumen, Yunzhi Ma, José Ramos-Méndez, Joseph Perl, and Luc Beaulieu. "Validation of the TOPAS Monte Carlo toolkit for HDR brachytherapy simulations", Brachytherapy (2021) [(link)](https://doi.org/10.1016/j.brachy.2020.12.007)
* Audran Poher, Francisco Berumen, Yunzhi Ma, Joseph Perl, and Luc Beaulieu. "Characterization of LDR brachytherapy sources using the TOPAS Monte Carlo toolkit", COMP annual meeting 2021.



