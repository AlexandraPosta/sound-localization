# Sound Source Localization (SSL)
Welcome to the git repository for my third-year dissertation. This repository contains all of the code, data, and documentation associated with my project. 


## Summary
The aim of this tool is to support a comparative study of an analytical and a learning-based model for estimating the azimuth direction of incoming sound in an indoors environment. 

The project takes advantage of a simulated environment to normalize the training and testing conditions. Two microphones and a single sound source are placed in a cuboid room using the Pyroomacoustics library. The sound sources are audio files from the CMU_ARCTIC database. In terms of model development, the analytical multiple signal classification technique (MUSIC) and a convolutional neural network (CNN) are employed. 

Data was collected from two scenarios: one with sound sources forming a 180-degree arch on one side of the microphones, and another with sound sources forming a full circle around the microphones. 
![Alt text](./images/room.png?raw=true "Room")


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
sound-localisation
├──README.md 
|
├──frontend             # contains the GUI for the web interface
|
├──models               # contains the cnn model
|
├──notebooks            # contains all Jupyter Notebooks that were used for development
|
├──data                 # stores preprocessed data as .wav files
|   └───full_circle     # 360 degrees
|   └───half_circle     # 180 degrees
|   └───original        # the original audio files that were processed
|
├──training_data        # contains .csv files used as input for the 
|
├──comparison           # contains .csv files that hold the spectrum response of models
|
└──images               # contains images used for the README file
```

## Setup
To use this repository, a Python environment (version > 3.6) has to be set up on the personal device.

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


### Usage
There are two different ways in which the analysis may be performed: a web-interface and Jupyter notebooks. The web interface automates the process of generating a room and allows for a fast check of the analytic models. The Jupyter notebooks allow for an in-depth analysis of the data pipeline and model construction.

In order to run the web interface:
1. Run main.py
2. Go on a browser and search for http://localhost:8000/
3. Specify the 
    - room width, length in meters
    - sound location 
    - microphone's location 
4. Press "Apply"
![Alt text](./images/web_1.png?raw=true "Apply")
5. Select an analytical model and press "Run model"
![Alt text](./images/web_2.png?raw=true "Run model")
6. Check the spectrum response
7. Repeat by selecting a different model

To run the notebooks and perform the full data pipeline:
1.	Use the Explore.ipynb to learn the basics
2.	Run SimulateData.ipynb
    -	Get the data for training, validation and testing.
    -	Data is saved under ./data/full_circle or ./data/half_circle
3.	Run Dataframes.ipynb
    -	This will generate .csv files under /training_data using for the CNN
4.	Run DoaMUSIC.ipynb
    -	Perform the estimation using an analytical model (MUSIC) 
    -	In case further comparison is needed, make sure to set GENERATE_DATA_FOR_COMPARISON to True. In this case, uncomment " if 'test' in file]" to run the algorithm for a single file
5.	Run DoaCNN.ipynb
    -	Perform the estimation using a learning-based model (CNN)
    -	In case further comparison is needed, make sure to set GENERATE_DATA_FOR_COMPARISON to True
6.	Run Comparion.ipynb
    -	Compare the MUSIC and CNN models in the same graphs
    -	Make sure that the comparison folder contains MUSIC_data, CNN_data and CNN_spectrum
    -	If a half_circle file is tested, set the GRID to 180; if a full circle file is testing, set the GRID to 360
7.	Run PathPlanning.ipynb
    -	make sure that the CNN model is saved inside ./models/


## Contributions
At the moment, no contributions, suggestions for improvement in data preprocessing, model architecture and performance metrics are allowed Proposed changes will be checked and potentially accepted after the submission of the project.