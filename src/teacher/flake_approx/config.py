'''
Config file for the frozen lake teacher

other files should import the constants defined here
'''


# Map name from src/envs/frozen_lake/frozen_maps.py
# The paper used 'small'
MAP_NAME = '16x16'


# Number of trials (students trained per mode) to get a good average during mode evaluation
# This might not incude the bandit policy, see `compare_teachers.run_bandits`
# The paper used 10
NUMBER_OF_TRIALS = 10


# Number of (curriculum) steps
# Training is done for N_STEPS+1, to account for the zeroth step
# The paper used 10
N_STEPS = 10


# Interventions / modes
# The paper used ['Trained', 'SR1', 'SR2', 'HR', 'Original', 'Bandit']
# Custom modes: ['Halfway', 'Incremental']
INTERVENTION_MODES = ['Halfway', 'Trained', 'Incremental', 'SR1', 'SR2', 'HR', 'Original', 'Bandit']
