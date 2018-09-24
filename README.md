Sheriff
========

The solution to all of your bandit related issues.

## Introduction

Sheriff is a bandit testing project based on much of the code that accompanied the paper [A Tutorial on Thompson Sampling](https://web.stanford.edu/~bvr/pubs/TS_Tutorial.pdf). While much of the code may seem similar, much has changed. It's been upgraded to python3, it's been dockerized, and it has a whole slew of new features that integrate with commcare and a bunch of other things!

## Setup

If you're interested in messing around with thompson sampling stuff, I have provided an iPython notebook which runs a test using simulated data. To set up the notebook, create a python3 virtual env like below

```bash
pip install virtualenv
virtualenv -p python3 venv
./venv/bin/activate
```

Once you have a virtualenv, install the jupyter requirements with `pip install jupyter-requirements.txt`

And lastly, `cd src` and start the notebook with `jupyter notebook`.

### Web Services, Scripts, etc

For our web framework we are using the Falcon python microframework for doing basic API work and caching our commcare API data in mongo for easy access. Using a recent version of `docker-compose` simply run `docker-compose up --build` and the server should start


The below is still forked from the original repository as it still applies here.

## Code structure

Our code is meant to be as simple as possible, optimizing for ease of use rather than speed.

We break the experiments/algorithms into three key parts:

- `agent`: handles learning + action selection of a bandit algorithm.
- `environment`: evaluates rewards/outcomes from an action.
- `experiment`: contains agent, environment and seed.

We create an abstract skeleton for these classes in `src/base` and implement separate children classes in each of the `src/finite_arm`, `src/cascading`, `src/ensemble_nn`, `src/pricing` and `src/graph` subfolders.

To run large sweeps over many agents and seeds we define a `config` file.
The config decribes the selection of agents, environments and seeds that we want to run.
`batch_runner.py` will run a specific element of the `config` sweep that is specified by the `job_id` = the unique integer identifier for the parameter combination.
For example,
```
ipython batch_runner.py --config finite_arm.config_simple --job_id 0 --save_path /tmp/
```

runs the first experiment from `finite_arm/config_simple`, job_id=0 corresponds to (agent='greedy', seed=0) on a 3-armed bandit problem.
It then saves the results to `/tmp/exp=finite_simple|id=0.csv`, you can recover the parameters for job_id=0 (and any other integer) by looking in `/tmp/exp=finite_simple|params.csv`, which is also generated automatically.

This script (`batch_runner.py`) is designed to be used in a distributed computation framework.
In this way, each job can be run on separate machines and the resulting output can be saved to a shared file system.
The code in `base/plot.py` is designed to collate the resulting `.csv` files from many different job_id's and produce the plots from the paper.
An example of this use case can be found in `batch_analysis.py`.



## Playing around with code locally

If you are just playing around with the code locally (and happy to run fewer seeds) you may find `local_runner.py` to be better for your needs than `batch_runner.py`, since it keeps all data in memory rather than writing to .csv file.

Researchers or students who want to get a better feel for the underlying code might use this as a starting point for exploring new methods and approaches.


