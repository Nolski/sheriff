"""Run an simple experiment locally without using config file.

This file is presented as a very simple entry point to code.
For running any meaningful experiments, we suggest `batch_runner.py` or
`local_runner.py`.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys

import numpy as np
import pandas as pd

from base.experiment import BaseExperiment
from finite_arm.agent_finite import FiniteBernoulliBanditTS, DriftingFiniteBernoulliBanditTS
from finite_arm.env_finite import DriftingFiniteArmedBernoulliBandit as FiniteArmedBernoulliBandit

sys.path.append(os.getcwd())

##############################################################################
# Running a single experiment

n_arm = 3
probs = [0.7, 0.8, 0.9]
n_steps = 1000
seed = 0

# agent = FiniteBernoulliBanditTS(n_arm)
agent = DriftingFiniteBernoulliBanditTS(n_arm)
env = FiniteArmedBernoulliBandit(3)
experiment = BaseExperiment(agent, env, n_steps=1000,
                            seed=seed, unique_id='example')

experiment.run_experiment()
