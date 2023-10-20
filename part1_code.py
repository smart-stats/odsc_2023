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

n = 100
x = np.random.normal(size = n)
e = np.random.normal(size = n)
t = np.random.binomial(1, .5, n)

beta0 = 0
beta1 = 1
beta2 = 4

y = beta0 + beta1 * x + beta2 * t + e

def myplot(x, y, t):
    x1 = x[t == 1]
    x0 = x[t == 0]
    y1 = y[t == 1]
    y0 = y[t == 0]
    xm1 = np.mean(x1)
    xm0 = np.mean(x0)
    ym1 = np.mean(y1)
    ym0 = np.mean(y0)

    X = np.array([x, t]).transpose()
    out = LinearRegression().fit(X, y)
    b0hat = out.intercept_
    b1hat = out.coef_[0]
    b2hat = out.coef_[1]
    
    plt.scatter(x0, y0)
    plt.scatter(x1, y1)

    col = sns.color_palette()

    plt.axhline(y = ym0, c = col[0])
    plt.axhline(y = ym1, c = col[1])

    xlim = [np.min(x), np.max(x)]

    ylim0 = [z * b1hat + b0hat + b2hat for z in xlim]
    ylim1 = [z * b1hat + b0hat         for z in xlim]

    plt.plot( xlim, ylim1)
    plt.plot( xlim, ylim0) 

    plt.show()


def causal1():
    plt.figure(figsize=[3, 3])
    G = nx.DiGraph()
    G.add_node("X1",  pos = (0.5,   1) )
    G.add_node("X2",  pos = (0  ,   0) )
    G.add_node("X3",  pos =  (1 ,   0) )
    G.add_edges_from([  
      ["X1", "X2"],
      ["X1", "X3"],
      ["X2", "X3"],
    ] )

    nx.draw(G, 
            nx.get_node_attributes(G, 'pos'), 
            with_labels=True, 
            font_weight='bold', 
            node_size = 2000,
            node_color = "lightblue",
            linewidths = 3)
    ax= plt.gca()
    ax.collections[0].set_edgecolor("#000000")
    ax.set_xlim([-.3, 1.3])
    ax.set_ylim([-.3, 1.3])
    plt.show()

def causal2():
    plt.figure(figsize=[3, 3])
    G = nx.DiGraph()
    G.add_node("X1",  pos = (0,   0) )
    G.add_node("X2", pos = (0,   1) )
    G.add_node("X3", pos = (1, 1.5) )
    G.add_node("X4", pos = (1,  .5) )
    G.add_node("X5", pos = (2,   1) )
    G.add_node("X6",  pos = (2,   0) )
    G.add_edges_from([  
      ["X2", "X1" ], 
      ["X2", "X3"],
      ["X3", "X1" ],
      ["X3", "X4"],
      ["X4", "X6" ],
      ["X5", "X3"],
      ["X5", "X6" ]
    ] )

    nx.draw(G, 
            nx.get_node_attributes(G, 'pos'), 
            with_labels=True, 
            font_weight='bold', 
            node_size = 2000,
            node_color = "lightblue",
            linewidths = 3)
    ax= plt.gca()
    ax.collections[0].set_edgecolor("#000000")
    ax.set_xlim([-.3, 2.3])
    ax.set_ylim([-.3, 2.3])
    plt.show()
    
    
def berkson_plot():
    n = 1000
    x = np.random.normal(size = n) * 5
    e = np.random.normal(size = n) * 5

    y =  x + e

    admitted = (x > 0) & (y > 0)
    matricul = (x < 10) & (y < 10)

    sns.scatterplot(x = x, y = y);
    plt.plot( [-10, 5], [10, -20], color = "red");
    plt.plot( [-5, 10], [20, -10], color = "red");
    plt.show()
