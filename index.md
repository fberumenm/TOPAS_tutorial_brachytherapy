### Tutorial of brachytherapy simulations using TOPAS
TOPAS is a toolkit that performs advanced Monte Carlo simulations of all forms of radiation therapy setups. The volumetric source enables accurate brachytherapy simulations. The following 4 clips show how to use such source and some common simulation setups as well.





Brachytherapy package for TOPAS
===============================

This package has been developed by the Medical Physics Research Group at Laval University [https://physmed.fsg.ulaval.ca](https://physmed.fsg.ulaval.ca) with the close collaboration of the TOPAS developer team.

Collaborators:

* Francisco Berumen
* Audran Poher
* Yunzhi Ma
* Jose Ramos Mendez
* Joseph Perl
* Luc Beaulieu

For any presentation or publication using the track-length estimator or brachytherapy related calculation, please cite the following published works:

* Francisco Berumen, Yunzhi Ma, José Ramos-Méndez, Joseph Perl, and Luc Beaulieu. "Validation of the TOPAS Monte Carlo toolkit for HDR brachytherapy simulations", Brachytherapy (2021) https://doi.org/10.1016/j.brachy.2020.12.007
* Audran Poher, Francisco Berumen, Yunzhi Ma, Joseph Perl, and Luc Beaulieu. "Characterization of LDR brachytherapy sources using the TOPAS Monte Carlo toolkit", COMP annual meeting 2021.

The Brachytherapy TOPAS package includes 4 examples:

* DoseTLE.txt
* HDRSource.txt
* HDRSourceInApplicator.txt
* LDRSource.txt

These examples in turn use sources and seeds found in topas/examples/LDR and topas/examples/HDR:

* 3 HDR sources (Flexisource, TG186, MicroSelectronV2)
* 12 LDR sources (IsoRay CS-1 Rev2, Bard STM1251, Best 2301, IsoAid IAI-125A, OncoSeed 6711, selectSeed 130.002, SL-125, Theragenics AgX100, Best 2335, IsoAid IAPd-103A, TheraSeed 200 Heavy, TheraSeed 200 Light)

Note that for each source a self-contained parameter file is provided. In such a way, the desired source can be imported with the includeFile method. For some sources, the layered mass geometry method was used, and the corresponding physics parameter is also given at the end.

HDRsource.txt and LDRSource.txt files provide a quick example on how to import a single source and visualize it, comment/uncomment the includeFile line accordingly.

For both Theraseed200 models, the user can define the materials of left and right caps.

The HDRSourceInApplicator.txt file presents the TG186 source inside the TG186 applicator. 

The DoseTLE.txt file scores the dose of the previous setup using the TLE. The TLE requires the mass absorption coefficients which are given to TOPAS in the InputFile parameter "Muen.dat". 


You can use the [editor on GitHub](https://github.com/fberumenm/TOPAS_tutorial_brachytherapy/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

<iframe width="560" height="315" src="https://www.youtube.com/embed/cNhewJFxeSE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/fberumenm/TOPAS_tutorial_brachytherapy/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
