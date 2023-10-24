import copy
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os
import pandas as pd
import seaborn as sns
import sklearn as skl
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import sys 

## The following reads in the raw data and processes it
## Stored ast visit1 and visit2_mricloud.csv
### Repo at https://github.com/MR-Biomarker-Resource/MRICloudPy
#sys.path.append("/home/jupyter-bcaffo/sandboxes/MRICloudPy/main")
#import mricloudpy
#import read
#example = "/home/jupyter-bcaffo/sandboxes/MRICloudPy/sample_data/"
#visit1 = mricloudpy.Data("assets/mricloud/visit1/").df
#visit2 = mricloudpy.Data("assets/mricloud/visit2/").df
#visit1.to_csv("assets/visit1_mricloud.csv")
#visit2.to_csv("assets/visit2_mricloud.csv")

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
    
    
