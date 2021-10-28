{% include lib/mathjax.html %}
### MC vs TPS dose comparisons

A common problem involves comparing dose results from MC simulations with those obtained with a treatment planning system (TPS). In a real treatment, the final dose distribution (in absolute units, Gy) depends on the air-kerma strength of the source and on the treatment time. The idea is to use such TPS parameters to properly scale the MC dose distribution.

Given the air-kerma strengthn calculated with TOPAS, the MC dose distribution, in Gy, is calculated as follows.

$$
TOPAS\ (Gy/Bq\ s) = TOPAS\ (Gy/photon) * I (photon/Bq\ s),
$$

$$TOPAS\ (Gy/\ U\s) =  TOPAS\ (Gy / Bq\ s) / S_K\_TOPAS (U / Bq),$$

$$TOPAS\ (Gy/s) = TOPAS\ (Gy/ U s) * S_K\_TPS (U),$$

$$TOPAS\ (Gy) = TOPAS\ (Gy/s) * treatment\ time\ (s).$$
