# Sound Source Localization
Welcome to the git repository for my third-year dissertation. This repository contains all of the code, data, and documentation associated with my research. 


## Summary
The aim of this tool is to allow for a simpler comparison between analytical and machine learning models of identifying the location of a sound in an indoor environment.  


## Features
In order to run a simulation, you can:
- select environment
- select type and number of microphones used
- select sound source
- select prediction model
- analyse based on the statistics provided

## Demo
TODO


## Structure
The repository is structured as follows:

```
Project
├──README.md 
|
├──frontend             # contains the GUI for the web interface
|
├──models               # contains history from the cnn training
|
├──notebooks            # contains all Jupyter Notebooks that were developed
|
├──data                 # stores preprocessed data as .wav files
|   └───full_circle     # 360 degrees
|   └───half_circle     # 180 degrees
|
└──training_data        # contains .csv files used for the cnn
```

## Usage
To use this repository, you will need to have Git and a Python environment set up on your computer.

## Setup
The following steps have to be followed to set-up the project:
TODO 


## Libraries
Install the following python packages:
- scipy
- pyroomacoustics
- sklearn
- keras
- tensorflow

## Build with


## License
The development of the environment is currently based on pyroomacoustics.


## Contributions
At the moment, no contributions, suggestions for improvement in data preprocessing, model architecture and performance metrics are allowed Proposed changes will be checked and potentially accepted after the submission of the project.