{% include lib/mathjax.html %}
### MC vs TPS dose comparisons

A common problem involves comparing dose results from MC simulations with those obtained with a treatment planning system (TPS). In a real treatment, the final dose distribution (in absolute units, Gy) depends on the air-kerma strength of the source and on the treatment time. The idea is to use such TPS parameters to properly scale the MC dose distribution.

Given the air-kerma strengthn calculated with TOPAS $$S_K\_TOPAS$$, the MC dose distribution, in Gy, is calculated as follows.

$$
TOPAS\ (Gy/Bq\ s) = TOPAS\ (Gy/photon) * I (photon/Bq\ s),
$$

$$TOPAS\ (Gy/U\ s) =  \frac{TOPAS\ (Gy / Bq\ s)}{S_K\_TOPAS\ (U / Bq)},$$

$$TOPAS\ (Gy/s) = TOPAS\ (Gy/ U\ s) * S_K\_TPS\ (U),$$

$$TOPAS\ (Gy) = TOPAS\ (Gy/s) * treatment\ time\ (s),$$

where $I$ is the intensity given in photons per becquerel and its value depends on the isotope of the source. If the [Pydicom](https://pydicom.github.io/) library is used, the next piece of code shows how to scale a TOPAS RTDOSE DICOM file from Gy/photon to Gy.

First, load the needed libraries and define a function to read the DICOM file and scale it by the scaling factor attribute [(3004,000E)](https://dicom.innolitics.com/ciods/rt-dose/rt-dose/3004000e).

```python
import pydicom
import numpy as np

def get_dose_volume(dicom_path):
    dicom = pydicom.dcmread(dicom_path)
    scaling_factor = float(dicom[0x3004, 0x000E].value)
    return dicom.pixel_array*scaling_factor
```
Given a simulation with $$10^9$$ initial photons