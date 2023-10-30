import random
import matplotlib.pyplot as plt

# Parameters
population_size = 500  # True population size
marked_fish = 100  # Number of fish marked in the first sample
second_sample_size = 70  # Size of the second sample
num_simulations = 1000  # Number of simulations

estimated_population_sizes = []

# Simulate the capture-recapture process multiple times
for _ in range(num_simulations):
    # Create a population of fish with marked individuals
    population = [1] * marked_fish + [0] * (population_size - marked_fish)
    random.shuffle(population)
    # Perform the second sample
    second_sample = random.sample(population, second_sample_size)
    
    # Count the number of marked fish in the second sample
    marked_in_second_sample = second_sample.count(1)+1
    
    # Estimate the population size using the capture-recapture method
    estimated_population = (marked_fish * second_sample_size) / marked_in_second_sample
    estimated_population_sizes.append(estimated_population)

# Plot a histogram of estimated population sizes
plt.hist(estimated_population_sizes, bins=30, alpha=0.75, color='b', edgecolor='black')
plt.axvline(x=population_size, color='r', linestyle='--', label='True Population Size')
plt.xlabel('Estimated Population Size')
plt.ylabel('Frequency')
plt.legend()
plt.title('Capture-Recapture Population Estimation')
display(plt)






#### The ICC example

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from pyodide.http import open_url

os.chdir('/home')
visit1=pd.read_csv(open_url("https://raw.githubusercontent.com/smart-stats/odsc_2023/main/assets/visit1_mricloud.csv"))
visit2=pd.read_csv(open_url("https://raw.githubusercontent.com/smart-stats/odsc_2023/main/assets/visit2_mricloud.csv"))

csf1 = visit1[(visit1['Type'] == 1) & (visit1['Level'] == 1) 
              & (visit1['Object'] == 'CSF')]['Volume']
csf2 = visit2[(visit2['Type'] == 1) & (visit2['Level'] == 1) 
              & (visit2['Object'] == 'CSF')]['Volume']
plt.scatter(csf1, csf2);
display(plt)

csfdf1 = visit1[(visit1['Type'] == 1) & (visit1['Level'] == 1) 
                & (visit1['Object'] == 'CSF')]
csfdf2 = visit2[(visit2['Type'] == 1) & (visit2['Level'] == 1) 
                & (visit2['Object'] == 'CSF')]

csfdf = pd.concat( [csfdf1, csfdf2] )
csfdf['logvolume'] = np.log(csfdf['Volume'])
md = smf.mixedlm("logvolume ~ 1", csfdf, groups=csfdf["ID"]).fit()
print("The summary is:\n",md.summary())
