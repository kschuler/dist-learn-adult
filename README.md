# Adult distributional learning experiment
Dist-learn-adult is a distributional learning experiment written in python.  This experiment is used when we want to expose learners to an artificial language and then test them on it. During the exposure phase, participants just listen to a stream of sentences - the screen is blank.  During the test phase, participants listen to a word or sentence and then are asked to rate it.

The experiment provided is a demo version. For more detailed information on running this experiment (including how to custimize it), see the [wiki](https://github.com/kschuler/dist-learn-adult/wiki).

## Running this experiment
Clone the repository:
```
git clone https://github.com/kschuler/dist-learn-adult
```
### Option 1: Run in standalone PsychoPy
Open 'experiment.py' in the *Coder view* of PsychoPy and run. (version 1.83.01 is known to work)

### Option 2: Run in a conda environment
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

