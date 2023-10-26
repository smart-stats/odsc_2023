import random
import matplotlib.pyplot as plt

# Parameters
population_size = 200  # True population size
marked_fish = 50  # Number of fish marked in the first sample
second_sample_size = 30  # Size of the second sample
num_simulations = 100  # Number of simulations

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



###
import numpy as np
import matplotlib.pyplot as plt

# Simulate data for two independent variables, X and Y
n = 1000  # Number of data points
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)

# Simulate data for a dependent variable, Z, which depends on X and Y
# However, Z is only observed if X or Y are greater than a threshold
threshold = 0.5
Z = np.zeros(n)

for i in range(n):
    if X[i] > threshold or Y[i] > threshold:
        Z[i] = X[i] + Y[i]

# Create scatter plots to visualize the paradox
plt.figure(figsize=(12, 5))

# Scatter plot of Z vs. X
plt.subplot(1, 2, 1)
plt.scatter(X, Z, alpha=0.5)
plt.xlabel('X')
plt.ylabel('Z')
plt.title("Z vs. X")

# Scatter plot of Z vs. Y
plt.subplot(1, 2, 2)
plt.scatter(Y, Z, alpha=0.5)
plt.xlabel('Y')
plt.ylabel('Z')
plt.title("Z vs. Y")

plt.tight_layout()
display(plt)