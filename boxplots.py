'''This file contains code in order to produce boxplots of execution
lengths on randomly generated gossip graphs.'''

# Install modules
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["figure.dpi"] = 150
import numpy as np
from math import factorial
import random
import time
import copy
import pickle

# ===============================================================
#  Complete Topology Boxplots
# ===============================================================
# Complete topology, 50 agents
data = [[],[],[],[],[]]
n = 50
G = completeGraph(n)
trials = 50

(srANY, srCO, srLNS, srTOK, srSPI) = (0,0,0,0,0)

for trial in list(range(1,trials+1)):
    H = copy.deepcopy(G)
    test = executeProtocol(H, ANY, False)
    if (test[2]):
        data[0].append(test[0])
        srANY += 1
    
    H = copy.deepcopy(G)
    test = executeProtocol(H, CO, False)
    if (test[2]):
        data[1].append(test[0])
        srCO += 1
    
    H = copy.deepcopy(G)
    test = executeProtocol(H, LNS, False)
    if (test[2]):
        data[2].append(test[0])
        srLNS += 1
    
    H = copy.deepcopy(G)
    test = executeProtocol(H, TOK, False)
    if (test[2]):
        data[3].append(test[0])
        srTOK += 1
    
    H = copy.deepcopy(G)
    test = executeProtocol(H, SPI, False)
    if (test[2]):
        data[4].append(test[0])
        srSPI += 1
    
    print("Progress: "+str(trial))

srANY = srANY/n
srCO = srCO/n
srLNS = srLNS/n
srTOK = srTOK/n
srSPI = srSPI/n
    
fig = plt.figure()
fig.suptitle('Complete topology with '+str(n)+' agents and '+
             str(trials)+' trials.')

labels = ['ANY', 'CO', 'LNS', 'TOK', 'SPI']

labels[0] = labels[0] + ' ('+str(srANY)+')'
labels[1] = labels[1] + ' ('+str(srCO)+')'
labels[2] = labels[2] + ' ('+str(srLNS)+')'
labels[3] = labels[3] + ' ('+str(srTOK)+')'
labels[4] = labels[4] + ' ('+str(srSPI)+')'

ax = fig.add_subplot(111)
ax.boxplot(data, labels = labels)

ax.set_xlabel('Protocols (success rate)')
ax.set_ylabel('Execution Length')

plt.show()



# ===============================================================
#  Incomplete Topology Boxplots
# ===============================================================
# Incomplete topology, 50 agents
data = [[],[],[],[],[]]
n = 50
G = incompleteGraph(n)
trials = 50

(srANY, srCO, srLNS, srTOK, srSPI) = (0,0,0,0,0)

for trial in list(range(1,trials+1)):
    H = copy.deepcopy(G)
    test = executeProtocol(H, ANY, False)
    if (test[2]):
        data[0].append(test[0])
        srANY += 1
    
    H = copy.deepcopy(G)
    test = executeProtocol(H, CO, False)
    if (test[2]):
        data[1].append(test[0])
        srCO += 1
    
    H = copy.deepcopy(G)
    test = executeProtocol(H, LNS, False)
    if (test[2]):
        data[2].append(test[0])
        srLNS += 1
    
    H = copy.deepcopy(G)
    test = executeProtocol(H, TOK, False)
    if (test[2]):
        data[3].append(test[0])
        srTOK += 1
    
    H = copy.deepcopy(G)
    test = executeProtocol(H, SPI, False)
    if (test[2]):
        data[4].append(test[0])
        srSPI += 1
    
    print("Progress: "+str(trial))

srANY = srANY/n
srCO = srCO/n
srLNS = srLNS/n
srTOK = srTOK/n
srSPI = srSPI/n
    
fig = plt.figure()
fig.suptitle('Incomplete topology with '+str(n)+' agents and '
             +str(trials)+' trials.')

labels = ['ANY', 'CO', 'LNS', 'TOK', 'SPI']

labels[0] = labels[0] + ' ('+str(srANY)+')'
labels[1] = labels[1] + ' ('+str(srCO)+')'
labels[2] = labels[2] + ' ('+str(srLNS)+')'
labels[3] = labels[3] + ' ('+str(srTOK)+')'
labels[4] = labels[4] + ' ('+str(srSPI)+')'

ax = fig.add_subplot(111)
ax.boxplot(data, labels = labels)

ax.set_xlabel('Protocols (success rate)')
ax.set_ylabel('Execution Length')

plt.show()



# ===============================================================
#  Dynamic Topology Boxplots
# ===============================================================
# Dynamic topology, 50 agents
data = [[],[],[],[],[]]
n = 50
G = diGraph(n)
trials = 50

(srANY, srCO, srLNS, srTOK, srSPI) = (0,0,0,0,0)

for trial in list(range(1,trials+1)):
    H = copy.deepcopy(G)
    test = executeProtocol(H, ANY, False)
    if (test[2]):
        data[0].append(test[0])
        srANY += 1
    
    H = copy.deepcopy(G)
    test = executeProtocol(H, CO, False)
    if (test[2]):
        data[1].append(test[0])
        srCO += 1
    
    H = copy.deepcopy(G)
    test = executeProtocol(H, LNS, False)
    if (test[2]):
        data[2].append(test[0])
        srLNS += 1
    
    H = copy.deepcopy(G)
    test = executeProtocol(H, TOK, False)
    if (test[2]):
        data[3].append(test[0])
        srTOK += 1
    
    H = copy.deepcopy(G)
    test = executeProtocol(H, SPI, False)
    if (test[2]):
        data[4].append(test[0])
        srSPI += 1
    
    print("Progress: "+str(trial))

srANY = srANY/n
srCO = srCO/n
srLNS = srLNS/n
srTOK = srTOK/n
srSPI = srSPI/n
    
fig = plt.figure()
fig.suptitle('Dynamic topology with '+str(n)+' agents and '
             +str(trials)+' trials.')

labels = ['ANY', 'CO', 'LNS', 'TOK', 'SPI']

labels[0] = labels[0] + ' ('+str(srANY)+')'
labels[1] = labels[1] + ' ('+str(srCO)+')'
labels[2] = labels[2] + ' ('+str(srLNS)+')'
labels[3] = labels[3] + ' ('+str(srTOK)+')'
labels[4] = labels[4] + ' ('+str(srSPI)+')'

ax = fig.add_subplot(111)
ax.boxplot(data, labels = labels)

ax.set_xlabel('Protocols (success rate)')
ax.set_ylabel('Execution Length')

plt.show()
