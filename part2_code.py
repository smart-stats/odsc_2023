import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import copy
import networkx as nx
import sklearn as skl
from sklearn.linear_model import LinearRegression

sns.set()


## Create a random intercept vector

def measurement1():
    n = 20
    m = 5
    u = np.repeat(np.random.normal(size = n), np.repeat(m, n))
    e = np.random.normal(size = n * m)
    y = u + e
    subject = np.repeat( np.array(range(n)), np.repeat(m, n))
    sns.scatterplot(x = subject, y = y);

def measurement2():
    n = 20
    m = 5
    u = np.repeat(np.random.normal(size = n), np.repeat(m, n)) * 10
    e = np.random.normal(size = n * m)
    y = u + e
    subject = np.repeat( np.array(range(n)), np.repeat(m, n))
    sns.scatterplot(x = subject, y = y);
    