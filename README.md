# Sound Source Localization
Welcome to the git repository for my third-year dissertation. This repository contains all of the code, data, and documentation associated with my research. 


## Summary
The aim of this tool is to support a comparative study of an analytical and a learning-based model for estimating the azimuth direction of incoming sound in an indoors environment. 


## Features
By using the web platform, it is possible to:
- select environment
- select number of microphones used
- select sound source
- select prediction model based on MUSIC or TOPS
- analyse based on the statistics provided

By using the Jupyter Notebooks, it is possible to:
- create dataset of sound from multiple incomming angles
- observe the datapipeline
- test the MUSIC algorithm using the dataset
- train and test a simpler a more complex CNN arhitecture the dataset
- analyse based on the statistics provided
- perform a simple path planning exercise to test models further


## Structure
The repository is structured as follows:

```
Project
├──README.md 
|
├──frontend             # contains the GUI for the web interface
|
├──models               # contains the cnn model
|
├──notebooks            # contains all Jupyter Notebooks that were developed for testing
|
├──data                 # stores preprocessed data as .wav files
|   └───full_circle     # 360 degrees
|   └───half_circle     # 180 degrees
|
└──training_data        # contains .csv files used as input for the cnn
```

## Setup
To use this repository, you will need to have Git and a Python environment (version > 3.6) set up on your computer.

### Libraries
The following python modules are required:
- jupyter_client
- jupyter_core 
- scipy
- numpy
- pandas
- matplotlib
- pyroomacoustics
- sklearn
- keras
- visualkeras
- tensorflow
- itertools
- seaborn


## Usage
There are two different ways in which the analysis may be performed: a web-interface and Jupyter notebooks.

In order to run the web interface:
1. Run main.py
2. Go on a browser and search for


## Contributions
At the moment, no contributions, suggestions for improvement in data preprocessing, model architecture and performance metrics are allowed Proposed changes will be checked and potentially accepted after the submission of the project.