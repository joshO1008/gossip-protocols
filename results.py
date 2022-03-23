'''This file contains code that utilises the experiment functions
to produce and plot the desired results. Note that running this file
will attempt to save the results to the current working directory.'''

# Install modules
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["figure.dpi"] = 150
import numpy as np
from math import factorial
from math import log
import random
import time
import copy
import pickle

# =============================================================================
#  Complete Topology Results
# =============================================================================

# 100 agents max, complete topology, 10 trials for each value of n
completeResults = experiment(100, 'complete', 10)

# Save data to file
pickle.dump(completeResults, open("completeResults.data", "wb"))

# Load data from file
completeResults = pickle.load(open("completeResults.data", "rb"))
completeExecutionLengths = completeResults[0]
completeExecutionTimes = completeResults[1]
completeSuccessRates = completeResults[2]
completeFailureRates = completeResults[3]
completeTimeoutRates = completeResults[4]

# Execution lengths
(elANY, elCO, elLNS, elTOK, elSPI) = (completeExecutionLengths['ANY'], completeExecutionLengths['CO'],
                                   completeExecutionLengths['LNS'], completeExecutionLengths['TOK'],
                                   completeExecutionLengths['SPI'])
# Execution times
(etANY, etCO, etLNS, etTOK, etSPI) = (completeExecutionTimes['ANY'], completeExecutionTimes['CO'],
                                   completeExecutionTimes['LNS'], completeExecutionTimes['TOK'],
                                   completeExecutionTimes['SPI'])
# Success rates
(srANY, srCO, srLNS, srTOK, srSPI) = (completeSuccessRates['ANY'], completeSuccessRates['CO'],
                                   completeSuccessRates['LNS'], completeSuccessRates['TOK'],
                                   completeSuccessRates['SPI'])
# Failure rates
(frANY, frCO, frLNS, frTOK, frSPI) = (completeFailureRates['ANY'], completeFailureRates['CO'],
                                   completeFailureRates['LNS'], completeFailureRates['TOK'],
                                   completeFailureRates['SPI'])
# Timeout rates
(trANY, trCO, trLNS, trTOK, trSPI) = (completeTimeoutRates['ANY'], completeTimeoutRates['CO'],
                                   completeTimeoutRates['LNS'], completeTimeoutRates['TOK'],
                                   completeTimeoutRates['SPI'])

# Plot results
nRange = list(range(5,101,5))

# Expectation of ANY
ANYexp = []
for n in nRange:
    ANYexp.append((3/2) * n * log(n))

# Expectation of LNS
LNSexp = []
for n in nRange:
    LNSexp.append(((1.0976) * n * log(n)) - 1.1330)

plt.plot(nRange, elANY, '-o', c='r', label='ANY')
plt.plot(nRange, elCO, '-o', c='b', label='CO')
plt.plot(nRange, elLNS, '-o', c='g', label='LNS')
plt.plot(nRange, elTOK, '-o', c='y', label='TOK')
plt.plot(nRange, elSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Average Execution Length')
plt.title('Execution Length: Complete Topology')
plt.legend()
plt.show()

nRange = list(range(5,101,5))
plt.plot(nRange, etANY, '-o', c='r', label='ANY')
plt.plot(nRange, etCO, '-o', c='b', label='CO')
plt.plot(nRange, etLNS, '-o', c='g', label='LNS')
plt.plot(nRange, etTOK, '-o', c='y', label='TOK')
plt.plot(nRange, etSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Average Execution Time (s)')
plt.title('Execution Time: Complete Topology')
plt.legend()
plt.show()

nRange = list(range(5,101,5))
plt.plot(nRange, srANY, '-o', c='r', label='ANY')
plt.plot(nRange, srCO, '-o', c='b', label='CO')
plt.plot(nRange, srLNS, '-o', c='g', label='LNS')
plt.plot(nRange, srTOK, '-o', c='y', label='TOK')
plt.plot(nRange, srSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Success Rate')
plt.title('Success Rate: Complete Topology')
plt.legend()
plt.show()

plt.plot(nRange, elANY, '-o', c='r', label='ANY')
plt.plot(nRange, ANYexp, '-o', c='k', label='ANY expectation')
plt.xlabel('n')
plt.ylabel('Average Execution Length')
plt.title('Execution Length: Complete Topology')
plt.legend()
plt.show()

plt.plot(nRange, elLNS, '-o', c='g', label='LNS')
plt.plot(nRange, LNSexp, '-o', c='k', label='LNS expectation')
plt.xlabel('n')
plt.ylabel('Average Execution Length')
plt.title('Execution Length: Complete Topology')
plt.legend()
plt.show()



# =============================================================================
#  Incomplete Topology Results
# =============================================================================
        
# 100 agents max, incomplete topology, 10 trials for each value of n
incompleteResults = experiment(100, 'incomplete', 10)

# Save data to file
pickle.dump(incompleteResults, open("incompleteResults.data", "wb"))

# Load data from file
incompleteResults = pickle.load(open("incompleteResults.data", "rb"))
incompleteExecutionLengths = incompleteResults[0]
incompleteExecutionTimes = incompleteResults[1]
incompleteSuccessRates = incompleteResults[2]
incompleteFailureRates = incompleteResults[3]
incompleteTimeoutRates = incompleteResults[4]

# Execution lengths
(elANY, elCO, elLNS, elTOK, elSPI) = (incompleteExecutionLengths['ANY'], incompleteExecutionLengths['CO'],
                                   incompleteExecutionLengths['LNS'], incompleteExecutionLengths['TOK'],
                                   incompleteExecutionLengths['SPI'])
# Execution times
(etANY, etCO, etLNS, etTOK, etSPI) = (incompleteExecutionTimes['ANY'], incompleteExecutionTimes['CO'],
                                   incompleteExecutionTimes['LNS'], incompleteExecutionTimes['TOK'],
                                   incompleteExecutionTimes['SPI'])
# Success rates
(srANY, srCO, srLNS, srTOK, srSPI) = (incompleteSuccessRates['ANY'], incompleteSuccessRates['CO'],
                                   incompleteSuccessRates['LNS'], incompleteSuccessRates['TOK'],
                                   incompleteSuccessRates['SPI'])
# Failure rates
(frANY, frCO, frLNS, frTOK, frSPI) = (incompleteFailureRates['ANY'], incompleteFailureRates['CO'],
                                   incompleteFailureRates['LNS'], incompleteFailureRates['TOK'],
                                   incompleteFailureRates['SPI'])
# Timeout rates
(trANY, trCO, trLNS, trTOK, trSPI) = (incompleteTimeoutRates['ANY'], incompleteTimeoutRates['CO'],
                                   incompleteTimeoutRates['LNS'], incompleteTimeoutRates['TOK'],
                                   incompleteTimeoutRates['SPI'])
        

# Plot results
nRange = list(range(5,101,5))
plt.plot(nRange, elANY, '-o', c='r', label='ANY')
plt.plot(nRange, elCO, '-o', c='b', label='CO')
plt.plot(nRange, elLNS, '-o', c='g', label='LNS')
plt.plot(nRange, elTOK, '-o', c='y', label='TOK')
plt.plot(nRange, elSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Average Execution length')
plt.title('Execution Length: Incomplete Topology')
plt.legend()
plt.show()

nRange = list(range(5,101,5))
plt.plot(nRange, etANY, '-o', c='r', label='ANY')
plt.plot(nRange, etCO, '-o', c='b', label='CO')
plt.plot(nRange, etLNS, '-o', c='g', label='LNS')
plt.plot(nRange, etTOK, '-o', c='y', label='TOK')
plt.plot(nRange, etSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Average Execution Time (s)')
plt.title('Execution Time: Incomplete Topology')
plt.legend()
plt.show()

nRange = list(range(5,101,5))
plt.plot(nRange, srANY, '-o', c='r', label='ANY')
plt.plot(nRange, srCO, '-o', c='b', label='CO')
plt.plot(nRange, srLNS, '-o', c='g', label='LNS')
plt.plot(nRange, srTOK, '-o', c='y', label='TOK')
plt.plot(nRange, srSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Success Rate')
plt.title('Success Rate: Incomplete Topology')
plt.legend()
plt.show()

nRange = list(range(5,101,5))
plt.plot(nRange, trANY, '-o', c='r', label='ANY')
plt.plot(nRange, trCO, '-o', c='b', label='CO')
plt.plot(nRange, trLNS, '-o', c='g', label='LNS')
plt.plot(nRange, trTOK, '-o', c='y', label='TOK')
plt.plot(nRange, trSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Timeout Rate')
plt.title('Timeout Rate: Incomplete Topology')
plt.legend()
plt.show()

nRange = list(range(5,101,5))
plt.plot(nRange, frANY, '-o', c='r', label='ANY')
plt.plot(nRange, frCO, '-o', c='b', label='CO')
plt.plot(nRange, frLNS, '-o', c='g', label='LNS')
plt.plot(nRange, frTOK, '-o', c='y', label='TOK')
plt.plot(nRange, frSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Failure Rate')
plt.title('Failure Rate: Incomplete Topology')
plt.legend()
plt.show()


# =============================================================================
#  Dynamic Topology Results
# =============================================================================

# 100 agents max, digraph (dynamic) topology, 10 trials for each value of n
dynamicResults = experiment(100, 'dynamic', 10)

# Save data to file
pickle.dump(dynamicResults, open("dynamicResults.data", "wb"))

# Load data from file
dynamicResults = pickle.load(open("dynamicResults.data", "rb"))
dynamicExecutionLengths = dynamicResults[0]
dynamicExecutionTimes = dynamicResults[1]
dynamicSuccessRates = dynamicResults[2]
dynamicFailureRates = dynamicResults[3]
dynamicTimeoutRates = dynamicResults[4]

# Execution lengths
(elANY, elCO, elLNS, elTOK, elSPI) = (dynamicExecutionLengths['ANY'], dynamicExecutionLengths['CO'],
                                   dynamicExecutionLengths['LNS'], dynamicExecutionLengths['TOK'],
                                   dynamicExecutionLengths['SPI'])
# Execution times
(etANY, etCO, etLNS, etTOK, etSPI) = (dynamicExecutionTimes['ANY'], dynamicExecutionTimes['CO'],
                                   dynamicExecutionTimes['LNS'], dynamicExecutionTimes['TOK'],
                                   dynamicExecutionTimes['SPI'])
# Success rates
(srANY, srCO, srLNS, srTOK, srSPI) = (dynamicSuccessRates['ANY'], dynamicSuccessRates['CO'],
                                   dynamicSuccessRates['LNS'], dynamicSuccessRates['TOK'],
                                   dynamicSuccessRates['SPI'])
# Failure rates
(frANY, frCO, frLNS, frTOK, frSPI) = (dynamicFailureRates['ANY'], dynamicFailureRates['CO'],
                                   dynamicFailureRates['LNS'], dynamicFailureRates['TOK'],
                                   dynamicFailureRates['SPI'])
# Timeout rates
(trANY, trCO, trLNS, trTOK, trSPI) = (dynamicTimeoutRates['ANY'], dynamicTimeoutRates['CO'],
                                   dynamicTimeoutRates['LNS'], dynamicTimeoutRates['TOK'],
                                   dynamicTimeoutRates['SPI'])

# Plot results
nRange = list(range(5,101,5))
plt.figure(dpi=300)
plt.plot(nRange, elANY, '-o', c='r', label='ANY')
plt.plot(nRange, elCO, '-o', c='b', label='CO')
plt.plot(nRange, elLNS, '-o', c='g', label='LNS')
plt.plot(nRange, elTOK, '-o', c='y', label='TOK')
plt.plot(nRange, elSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Average Execution length')
plt.title('Execution Length: Dynamic Gossip')
plt.legend()
plt.show()

nRange = list(range(5,101,5))
plt.plot(nRange, etANY, '-o', c='r', label='ANY')
plt.plot(nRange, etCO, '-o', c='b', label='CO')
plt.plot(nRange, etLNS, '-o', c='g', label='LNS')
plt.plot(nRange, etTOK, '-o', c='y', label='TOK')
plt.plot(nRange, etSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Average Execution Times')
plt.title('Execution Time: Dynamic Gossip')
plt.legend()
plt.show()

nRange = list(range(5,101,5))
plt.plot(nRange, srANY, '-o', c='r', label='ANY')
plt.plot(nRange, srCO, '-o', c='b', label='CO')
plt.plot(nRange, srLNS, '-o', c='g', label='LNS')
plt.plot(nRange, srTOK, '-o', c='y', label='TOK')
plt.plot(nRange, srSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Success Rate')
plt.title('Success Rate: Dynamic Gossip')
plt.legend()
plt.show()
        
nRange = list(range(5,101,5))
plt.plot(nRange, frANY, '-o', c='r', label='ANY')
plt.plot(nRange, frCO, '-o', c='b', label='CO')
plt.plot(nRange, frLNS, '-o', c='g', label='LNS')
plt.plot(nRange, frTOK, '-o', c='y', label='TOK')
plt.plot(nRange, frSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Failure Rate')
plt.title('Failure Rate: Dynamic Gossip')
plt.legend()
plt.show()

nRange = list(range(5,101,5))
plt.plot(nRange, trANY, '-o', c='r', label='ANY')
plt.plot(nRange, trCO, '-o', c='b', label='CO')
plt.plot(nRange, trLNS, '-o', c='g', label='LNS')
plt.plot(nRange, trTOK, '-o', c='y', label='TOK')
plt.plot(nRange, trSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Timeout Rate')
plt.title('Timeout Rate: Dynamic Gossip')
plt.legend()
plt.show()


# =============================================================================
#  Complete Topology Results (Rounds)
# =============================================================================

completeRoundResults = experiment(100, 'complete', 10, True)

# Save data to file
pickle.dump(completeRoundResults, open("completeRoundResults.data", "wb"))

# Load data from file
completeRoundResults = pickle.load(open("completeRoundResults.data", "rb"))
completeRoundLengths = completeRoundResults[0]
completeTimes = completeRoundResults[1]
completeSuccessRates = completeRoundResults[2]
completeFailureRates = completeRoundResults[3]
completeTimeoutRates = completeRoundResults[4]

# Round lengths
(rlANY, rlCO, rlLNS, rlTOK, rlSPI) = (completeRoundLengths['ANY'], completeRoundLengths['CO'],
                                   completeRoundLengths['LNS'], completeRoundLengths['TOK'],
                                   completeRoundLengths['SPI'])

# Times
(tANY, tCO, tLNS, tTOK, tSPI) = (completeTimes['ANY'], completeTimes['CO'],
                                   completeTimes['LNS'], completeTimes['TOK'],
                                   completeTimes['SPI'])
                            
# Success rates
(srANY, srCO, srLNS, srTOK, srSPI) = (completeSuccessRates['ANY'], completeSuccessRates['CO'],
                                   completeSuccessRates['LNS'], completeSuccessRates['TOK'],
                                   completeSuccessRates['SPI'])
# Failure rates
(frANY, frCO, frLNS, frTOK, frSPI) = (completeFailureRates['ANY'], completeFailureRates['CO'],
                                   completeFailureRates['LNS'], completeFailureRates['TOK'],
                                   completeFailureRates['SPI'])
# Timeout rates
(trANY, trCO, trLNS, trTOK, trSPI) = (completeTimeoutRates['ANY'], completeTimeoutRates['CO'],
                                   completeTimeoutRates['LNS'], completeTimeoutRates['TOK'],
                                   completeTimeoutRates['SPI'])
        

# Plot results
nRange = list(range(5,101,5))
plt.plot(nRange, rlANY, '-o', c='r', label='ANY')
plt.plot(nRange, rlCO, '-o', c='b', label='CO')
plt.plot(nRange, rlLNS, '-o', c='g', label='LNS')
plt.plot(nRange, rlTOK, '-o', c='y', label='TOK')
plt.plot(nRange, rlSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Average Round Number')
plt.title('Round Number: Complete Topology')
plt.legend()
plt.show()

# Plot results
nRange = list(range(5,101,5))
plt.plot(nRange, rlANY, '-o', c='r', label='ANY')
plt.plot(nRange, rlCO, '-o', c='b', label='CO')
plt.plot(nRange, rlLNS, '-o', c='g', label='LNS')
plt.xlabel('n')
plt.ylabel('Average Round Number')
plt.title('Round Number: Complete Topology')
plt.legend()
plt.show()

nRange = list(range(5,101,5))
plt.plot(nRange, srANY, '-o', c='r', label='ANY')
plt.plot(nRange, srCO, '-o', c='b', label='CO')
plt.plot(nRange, srLNS, '-o', c='g', label='LNS')
plt.plot(nRange, srTOK, '-o', c='y', label='TOK')
plt.plot(nRange, srSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Success Rate')
plt.title('Success Rate: Complete Topology (Rounds)')
plt.legend()
plt.show()

# Plot round lenghts without TOK and SPI for closer comparison
nRange = list(range(5,101,5))
plt.plot(nRange, rlANY, '-o', c='r', label='ANY')
plt.plot(nRange, rlCO, '-o', c='b', label='CO')
plt.plot(nRange, rlLNS, '-o', c='g', label='LNS')
plt.xlabel('n')
plt.ylabel('Average Round Number')
plt.title('Round Number: Complete Topology')
plt.legend()
plt.show()

# =============================================================================
#  Incomplete Topology Results (Rounds)
# =============================================================================
        
incompleteRoundResults = experiment(100, 'incomplete', 10, True)

# Save data to file
pickle.dump(incompleteRoundResults, open("incompleteRoundResults.data", "wb"))

# Load data from file
incompleteRoundResults = pickle.load(open("incompleteRoundResults.data", "rb"))
incompleteRoundLengths = incompleteRoundResults[0]
incompleteTimes = incompleteRoundResults[1]
incompleteSuccessRates = incompleteRoundResults[2]
incompleteFailureRates = incompleteRoundResults[3]
incompleteTimeoutRates = incompleteRoundResults[4]

# Execution lengths
(rlANY, rlCO, rlLNS, rlTOK, rlSPI) = (incompleteRoundLengths['ANY'], incompleteRoundLengths['CO'],
                                   incompleteRoundLengths['LNS'], incompleteRoundLengths['TOK'],
                                   incompleteRoundLengths['SPI'])

# Times
(tANY, tCO, tLNS, tTOK, tSPI) = (incompleteTimes['ANY'], incompleteTimes['CO'],
                                   incompleteTimes['LNS'], incompleteTimes['TOK'],
                                   incompleteTimes['SPI'])
                            
# Success rates
(srANY, srCO, srLNS, srTOK, srSPI) = (incompleteSuccessRates['ANY'], incompleteSuccessRates['CO'],
                                   incompleteSuccessRates['LNS'], incompleteSuccessRates['TOK'],
                                   incompleteSuccessRates['SPI'])
# Failure rates
(frANY, frCO, frLNS, frTOK, frSPI) = (incompleteFailureRates['ANY'], incompleteFailureRates['CO'],
                                   incompleteFailureRates['LNS'], incompleteFailureRates['TOK'],
                                   incompleteFailureRates['SPI'])
# Timeout rates
(trANY, trCO, trLNS, trTOK, trSPI) = (incompleteTimeoutRates['ANY'], incompleteTimeoutRates['CO'],
                                   incompleteTimeoutRates['LNS'], incompleteTimeoutRates['TOK'],
                                   incompleteTimeoutRates['SPI'])
        

# Plot results
nRange = list(range(5,101,5))
plt.plot(nRange, rlANY, '-o', c='r', label='ANY')
plt.plot(nRange, rlCO, '-o', c='b', label='CO')
plt.plot(nRange, rlLNS, '-o', c='g', label='LNS')
plt.plot(nRange, rlTOK, '-o', c='y', label='TOK')
plt.plot(nRange, rlSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Average Round Number')
plt.title('Round Number: Incomplete Topology')
plt.legend()
plt.show()

# Plot results
nRange = list(range(5,101,5))
plt.plot(nRange, rlANY, '-o', c='r', label='ANY')
plt.plot(nRange, rlCO, '-o', c='b', label='CO')
plt.plot(nRange, rlLNS, '-o', c='g', label='LNS')
plt.xlabel('n')
plt.ylabel('Average Round Number')
plt.title('Round Number: Incomplete Topology')
plt.legend()
plt.show()

nRange = list(range(5,101,5))
plt.plot(nRange, srANY, '-o', c='r', label='ANY')
plt.plot(nRange, srCO, '-o', c='b', label='CO')
plt.plot(nRange, srLNS, '-o', c='g', label='LNS')
plt.plot(nRange, srTOK, '-o', c='y', label='TOK')
plt.plot(nRange, srSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Success Rate')
plt.title('Success Rate: Incomplete Topology (Rounds)')
plt.legend()
plt.show()


# =============================================================================
#  Dynamic Topology Results (Rounds)
# =============================================================================

dynamicRoundResults = experiment(100, 'dynamic', 10, True)

# Save data to file
pickle.dump(dynamicRoundResults, open("dynamicRoundResults.data", "wb"))

# Load data from file
dynamicRoundResults = pickle.load(open("dynamicRoundResults.data", "rb"))
dynamicRoundLengths = dynamicRoundResults[0]
dynamicTimes = dynamicRoundResults[1]
dynamicSuccessRates = dynamicRoundResults[2]
dynamicFailureRates = dynamicRoundResults[3]
dynamicTimeoutRates = dynamicRoundResults[4]

# Execution lengths
(rlANY, rlCO, rlLNS, rlTOK, rlSPI) = (dynamicRoundLengths['ANY'], dynamicRoundLengths['CO'],
                                   dynamicRoundLengths['LNS'], dynamicRoundLengths['TOK'],
                                   dynamicRoundLengths['SPI'])

# Times
(tANY, tCO, tLNS, tTOK, tSPI) = (dynamicTimes['ANY'], dynamicTimes['CO'],
                                   dynamicTimes['LNS'], dynamicTimes['TOK'],
                                   dynamicTimes['SPI'])
                            
# Success rates
(srANY, srCO, srLNS, srTOK, srSPI) = (dynamicSuccessRates['ANY'], dynamicSuccessRates['CO'],
                                   dynamicSuccessRates['LNS'], dynamicSuccessRates['TOK'],
                                   dynamicSuccessRates['SPI'])
# Failure rates
(frANY, frCO, frLNS, frTOK, frSPI) = (dynamicFailureRates['ANY'], dynamicFailureRates['CO'],
                                   dynamicFailureRates['LNS'], dynamicFailureRates['TOK'],
                                   dynamicFailureRates['SPI'])
# Timeout rates
(trANY, trCO, trLNS, trTOK, trSPI) = (dynamicTimeoutRates['ANY'], dynamicTimeoutRates['CO'],
                                   dynamicTimeoutRates['LNS'], dynamicTimeoutRates['TOK'],
                                   dynamicTimeoutRates['SPI'])
        

# Plot results
nRange = list(range(5,101,5))
plt.plot(nRange, rlANY, '-o', c='r', label='ANY')
plt.plot(nRange, rlCO, '-o', c='b', label='CO')
plt.plot(nRange, rlLNS, '-o', c='g', label='LNS')
plt.plot(nRange, rlTOK, '-o', c='y', label='TOK')
plt.plot(nRange, rlSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Average Round Number')
plt.title('Round Number: Dynamic Gossip')
plt.legend()
plt.show()

nRange = list(range(5,101,5))
plt.plot(nRange, srANY, '-o', c='r', label='ANY')
plt.plot(nRange, srCO, '-o', c='b', label='CO')
plt.plot(nRange, srLNS, '-o', c='g', label='LNS')
plt.plot(nRange, srTOK, '-o', c='y', label='TOK')
plt.plot(nRange, srSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Success Rate')
plt.title('Success Rate: Dynamic Gossip (Rounds)')
plt.legend()
plt.show()

nRange = list(range(5,101,5))
plt.plot(nRange, frANY, '-o', c='r', label='ANY')
plt.plot(nRange, frCO, '-o', c='b', label='CO')
plt.plot(nRange, frLNS, '-o', c='g', label='LNS')
plt.plot(nRange, frTOK, '-o', c='y', label='TOK')
plt.plot(nRange, frSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Failure Rate')
plt.title('Failure Rate: Dynamic Gossip (Rounds)')
plt.legend()
plt.show()

nRange = list(range(5,101,5))
plt.plot(nRange, trANY, '-o', c='r', label='ANY')
plt.plot(nRange, trCO, '-o', c='b', label='CO')
plt.plot(nRange, trLNS, '-o', c='g', label='LNS')
plt.plot(nRange, trTOK, '-o', c='y', label='TOK')
plt.plot(nRange, trSPI, '-o', c='c', label='SPI')
plt.xlabel('n')
plt.ylabel('Timeout Rate')
plt.title('Timeout Rate: Dynamic Gossip (Rounds)')
plt.legend()
plt.show()

# Plot round lenghts without TOK and SPI for closer comparison
nRange = list(range(5,101,5))
plt.plot(nRange, rlANY, '-o', c='r', label='ANY')
plt.plot(nRange, rlCO, '-o', c='b', label='CO')
plt.plot(nRange, rlLNS, '-o', c='g', label='LNS')
plt.xlabel('n')
plt.ylabel('Average Round Number')
plt.title('Round Number: Dynamic Gossip (Rounds)')
plt.legend()
plt.show()