# Adult distributional learning experiment
Dist-learn-adult is a distributional learning experiment written in python.  This experiment is used when we want to expose learners to a an artificial language and then test them (via a rating test) on words or sentences that came (or did not come) from the language. Participants just listen to a stream of sentences during the exposure phase - the screen is blank.  During the test phase, participants listen to one word or sentence, then respond on a simple rating scale (the screen contains the rating scale and optional additional instructions).

The experiment provided is a demo version. For information on how to custimize this experiment, see the [wiki](https://github.com/kschuler/dist-learn-adult/wiki).

## Quick Start
To get this experiment up and running quickly, follow these instructions.  For more detailed instructions, refer to the [wiki](https://github.com/kschuler/dist-learn-adult/wiki).

### Get this repository
The first step is to clone this repository.
```
git clone https://github.com/kschuler/dist-learn-adult
```

### Run the experiment
There are two options for running this experiment.  The first is to run it using the standalone distribution of PsychoPy - a standalone app for running neuroscience and pyschology experiments.

#### Run in standalone PsychoPy
1. Download standalone PscyhoPy (dist-learn-adult has been tested on version 1.83.04)
```
curl -O https://github.com/psychopy/psychopy/releases/download/1.83.04/StandalonePsychoPy-1.83.04-OSX_64bit.dmg
```
2. Open `experiment.py` in the *Coder View* of PsychoPy
3. Press the green run button or [Cmd+R]
