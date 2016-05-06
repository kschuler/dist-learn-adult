# Adult distributional learning experiment
Dist-learn-adult is a distributional learning experiment written in python.  This experiment is used when we want to expose learners to a an artificial language and then test them (via a rating test) on words or sentences that came (or did not come) from the language. Participants just listen to a stream of sentences during the exposure phase - the screen is blank.  During the test phase, participants listen to one word or sentence, then respond on a simple rating scale (the screen contains the rating scale and optional additional instructions).

The experiment provided is a demo version. For more detailed information on running this experiment (including how to custimize it), see the [wiki](https://github.com/kschuler/dist-learn-adult/wiki).

## Quick Start
Clone the repository:
```
git clone https://github.com/kschuler/dist-learn-adult
```
#### Run in standalone PsychoPy
Download standalone PscyhoPy (dist-learn-adult has been tested on version 1.83.04)
```
curl -O https://github.com/psychopy/psychopy/releases/download/1.83.04/StandalonePsychoPy-1.83.04-OSX_64bit.dmg
```
Open `experiment.py` in the *Coder View* of PsychoPy
Press the green run button or [Cmd+R]

#### Run in a conda environment
The repository contains an `environment.yml` file.  If you use Anaconda, you can create an environment with the approriate packages using
```
conda env create -f environment.yml
```
See the [wiki](https://github.com/kschuler/dist-learn-adult/wiki) page for more information on using Anaconda.
