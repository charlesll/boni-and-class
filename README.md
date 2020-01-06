# boni-and-class
Classification of boninite magmas based on major and trace elements.

Supplementary code to the article:

Valetich, Le Losq, Arculus, Umino and Mavrogenes, 2019, Compositions and classification of fractionated boninite series melts from the Izu-Bonin-Mariana arc, Journal of Petrology.

# Requirements
 - Python 3.6 or higher
 - Jupyter notebooks
 - scikit learn
 - numpy
 - pandas
 - matplotlib
 - boninites (this repo) , install needed, this is a small wrapper around scikit learn for making it even easier to use

# Data
Necessary data provided in csv files are available from the following studies:
 - Valetich et al. 2019, Compositions and classification of fractionated boninite series melts from the Izu-Bonin-Mariana arc, Journal of Petrology.
 - Umino et al. 2015, Thermal and chemical evolution of the subarc mantle revealed by spinel-hosted melt inclusions in boninite from the Ogasawara (Bonin), Geology
 43 (2): 151-154. [https://doi.org/10.1130/G36191.1](https://doi.org/10.1130/G36191.1)
 - Umino et al. 2018, Did boninite originate from the heterogeneous mantle with recycled ancient slab? Island Arc 27, e12221. [https://doi.org/10.1111/iar.12221](https://doi.org/10.1111/iar.12221)
 - Coulthard 2018, Subduction initiation and igneous petrogenesis: characterizing melt generation at a new convergent boundary through the geochemical analysis of volcanic glass, Master thesis of the University of Iowa. [https://ir.uiowa.edu/etd/6398](https://ir.uiowa.edu/etd/6398)

# Usage
1. Download the current repository and unzip it somewhere;
2. Install a Python distribution with Jupyter notebooks; see for instance https://www.anaconda.com/distribution/ and related documentation;
3. Launch your Jupyter server (read [Jupyter documentation](https://jupyter-notebook.readthedocs.io/en/stable/)). Open the Jupyter notebook and run the code. Further specific documentation is provided for boninites.boninite(), call help(boninites.boninite) in a Python REPL or Jupyter cell.

# Licence
See LICENCE.md

# Authors
- Charles Le Losq, Australian National University
- Matthew Valetich, Australian National University
