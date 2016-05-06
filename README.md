# Adult distributional learning experiment
Dist-learn-adult is a distributional learning experiment written in python.  This experiment is used when we want to expose learners to a an artificial language and then test them (via a rating test) on words or sentences that came (or did not come) from the language. Participants just listen to a stream of sentences during the exposure phase - the screen is blank.  During the test phase, participants listen to one word or sentence, then respond on a simple rating scale (the screen contains the rating scale and optional additional instructions).

The experiment provided is a demo version. For more detailed information on running this experiment (including how to custimize it), see the [wiki](https://github.com/kschuler/dist-learn-adult/wiki).

## Running this experiment
Clone the repository:
```
git clone https://github.com/kschuler/dist-learn-adult
```
#### Run in standalone PsychoPy
Open 'experiment.py' in the *Coder view* of PsychoPy (version 1.83.01 is known to work) and run.

#### Run in a conda environment
Create a conda environment with the `environment.yml` file.  
```
conda env create -f environment.yml
```
Navigate to your local copy of this repo and activate the environment
```
source activate psychopyenv
```
Run the `experiment.py` file with pythonw
```
pythonw experiment.py
```

