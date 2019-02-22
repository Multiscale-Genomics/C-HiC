# CHi-C

[![Documentation Status](https://readthedocs.org/projects/capture-chi-c/badge/?version=latest)](https://capture-chi-c.readthedocs.io/en/latest/?badge=latest) [![Build Status](https://travis-ci.org/Multiscale-Genomics/CHi-C.svg?branch=VM_CR1)](https://travis-ci.org/Multiscale-Genomics/CHi-C)


This repository contains pipelines for analyzing capture Hi-C data. CHiCAGO algorithm is used for the normalization of chromatin contacts

# Requirements
- pyenv and pyenv-virtualenv
- Python 2.7.12
- Python Modules:
  - pylint
  - pytest
  - mg-tool-api
  - rpy2
  - matplotlib
  - pandas
  - rtree


- R >=3.1.2
-R Modules:
  -argparser
  -devtools
  -Chicago
- bedtools
- perl
- spatialindex
- bowtie2
- hicup
- BWA


Installation
------------

For a guide to the full installation procedure the see [ReadTheDocs](https://capture-chi-c.readthedocs.io/en/latest/?badge=latest)

Directly from GitHub:

.. code-block:: none
   :linenos:

   cd ${HOME}/code

   git clone -b VM_CR1 https://github.com/Multiscale-Genomics/CHi-C.git

   cd CHi-C

Create the Python environment

.. code-block:: none
   :linenos:

   pyenv-virtualenv 2.7.10 CHi-C
   pip install --editable .
  
Tests
-----

Tests must be runned from the top directory.
Test for single tools are runned with pytest, example: $pytest tests/test_rmap_tool.py
There is an order to run single tests:
  - test_rmap_tool.py
  - test_baitmap.py
  - test_design.py
  - test_hicup.py
  - test_bam2chicago.py
  - test_pyCHiC.py

To run all test type: $python tests/test_toolchains.py

IMPORTANT! From the top directory type ./tidy_data before running tests/test_toolchains.py

