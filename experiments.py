'''This file contains functions used to perform the experiments
described in the dissertation.'''

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
#  Test protocols function
# ===============================================================

# testProtocols(n, top, trials, rounds) - executes the five 
#                protocols on a set topology and number of agents
# Parameters: n - number of agents
#             top - network topology (complete, incomplete, dynamic)
#             trials - int, number of trials
#             rounds - boolean, dictates if calls are made in 
#                      rounds (true) or not (false)
# Returns - dictionary, contains all results for set n

def testProtocols(n, top, trials, rounds = False):
    # Case where calls are made sequentially
    if (not rounds):
        # Intialise results dictionary
        results = {'ANY':{'execLengths':[], 'execTimes':[], 'avgTime': 0,
                          'avgLength': 0, 'sNumber': 0, 'fNumber': 0,
                          'tNumber': 0}, 
                   'CO':{'execLengths':[], 'execTimes':[], 'avgTime': 0,
                         'avgLength': 0, 'sNumber': 0, 'fNumber': 0,
                         'tNumber': 0},
                   'LNS':{'execLengths':[], 'execTimes':[], 'avgTime': 0,
                          'avgLength': 0, 'sNumber': 0, 'fNumber': 0,
                          'tNumber': 0}, 
                   'TOK':{'execLengths':[], 'execTimes':[], 'avgTime': 0,
                          'avgLength': 0, 'sNumber': 0, 'fNumber': 0,
                          'tNumber': 0},
                   'SPI':{'execLengths':[], 'execTimes':[], 'avgTime': 0,
                          'avgLength': 0, 'sNumber': 0, 'fNumber': 0,
                          'tNumber': 0}}
        
        # For set number of trials
        for _ in range(trials):
            # Generate graph
            if (top == 'complete'):
                G = completeGraph(n)
            elif (top == 'incomplete'):
                G = incompleteGraph(n)
            elif (top == 'dynamic'):
                G = diGraph(n)
            
            # Create copy of graph
            H = copy.deepcopy(G)
            
            # Run each protocol on H and record results
            # (number of successes, failures and timeouts)
            #ANY
            (c, timer, success, failure, timeout) = executeProtocol(H, ANY)
            if (success):
                results['ANY']['execLengths'].append(c)
                results['ANY']['execTimes'].append(timer)
                results['ANY']['sNumber'] += 1
            elif (failure):
                results['ANY']['fNumber'] += 1
            elif (timeout):
                results['ANY']['tNumber'] += 1
            # CO
            H = copy.deepcopy(G)
            (c, timer, success, failure, timeout) = executeProtocol(H, CO)
            if (success):
                results['CO']['execLengths'].append(c)
                results['CO']['execTimes'].append(timer)
                results['CO']['sNumber'] += 1
            elif (failure):
                results['CO']['fNumber'] += 1
            elif (timeout):
                results['CO']['tNumber'] += 1
            # LNS
            H = copy.deepcopy(G)
            (c, timer, success, failure, timeout) = executeProtocol(H, LNS)
            if (success):
                results['LNS']['execLengths'].append(c)
                results['LNS']['execTimes'].append(timer)
                results['LNS']['sNumber'] += 1
            elif (failure):
                results['LNS']['fNumber'] += 1
            elif (timeout):
                results['LNS']['tNumber'] += 1
            # TOK
            H = copy.deepcopy(G)
            (c, timer, success, failure, timeout) = executeProtocol(H, TOK)
            if (success):
                results['TOK']['execLengths'].append(c)
                results['TOK']['execTimes'].append(timer)
                results['TOK']['sNumber'] += 1
            elif (failure):
                results['TOK']['fNumber'] += 1
            elif (timeout):
                results['TOK']['tNumber'] += 1
            # SPI
            H = copy.deepcopy(G)
            (c, timer, success, failure, timeout) = executeProtocol(H, SPI)
            if (success):
                results['SPI']['execLengths'].append(c)
                results['SPI']['execTimes'].append(timer)
                results['SPI']['sNumber'] += 1
            elif (failure):
                results['SPI']['fNumber'] += 1
            elif (timeout):
                results['SPI']['tNumber'] += 1
                
        # Calculate averages and success rates
        # ANY
        if (len(results['ANY']['execLengths']) > 0):
            results['ANY']['avgLength'] = sum(
                results['ANY']['execLengths'])/results['ANY']['sNumber']
            results['ANY']['avgTime'] = sum(
                results['ANY']['execTimes'])/results['ANY']['sNumber']
        else:
            results['ANY']['avgLengths'] = None
            results['ANY']['avgTime'] = None
        results['ANY']['sRate'] = results['ANY']['sNumber']/trials
        results['ANY']['fRate'] = results['ANY']['fNumber']/trials
        results['ANY']['tRate'] = results['ANY']['tNumber']/trials
        # CO
        if (len(results['CO']['execLengths']) > 0):
            results['CO']['avgLength'] = sum(
                results['CO']['execLengths'])/results['CO']['sNumber']
            results['CO']['avgTime'] = sum(
                results['CO']['execTimes'])/results['CO']['sNumber']
        else:
            results['ANY']['avgLengths'] = None
            results['ANY']['avgTime'] = None
        results['CO']['sRate'] = results['CO']['sNumber']/trials
        results['CO']['fRate'] = results['CO']['fNumber']/trials
        results['CO']['tRate'] = results['CO']['tNumber']/trials
        # LNS
        if (len(results['LNS']['execLengths']) > 0):
            results['LNS']['avgLength'] = sum(
                results['LNS']['execLengths'])/results['LNS']['sNumber']
            results['LNS']['avgTime'] = sum(
                results['LNS']['execTimes'])/results['LNS']['sNumber']
        else:
            results['LNS']['avgLengths'] = None
            results['LNS']['avgTime'] = None
        results['LNS']['sRate'] = results['LNS']['sNumber']/trials
        results['LNS']['fRate'] = results['LNS']['fNumber']/trials
        results['LNS']['tRate'] = results['LNS']['tNumber']/trials
        # TOK
        if (len(results['TOK']['execLengths']) > 0):
            results['TOK']['avgLength'] = sum(
                results['TOK']['execLengths'])/results['TOK']['sNumber']
            results['TOK']['avgTime'] = sum(
                results['TOK']['execTimes'])/results['TOK']['sNumber']
        else:
            results['TOK']['avgLengths'] = None
            results['TOK']['avgTime'] = None
        results['TOK']['sRate'] = results['TOK']['sNumber']/trials
        results['TOK']['fRate'] = results['TOK']['fNumber']/trials
        results['TOK']['tRate'] = results['TOK']['tNumber']/trials
        # SPI
        if (len(results['SPI']['execLengths']) > 0):
            results['SPI']['avgLength'] = sum(
                results['SPI']['execLengths'])/results['SPI']['sNumber']
            results['SPI']['avgTime'] = sum(
                results['SPI']['execTimes'])/results['SPI']['sNumber']
        else:
            results['SPI']['avgLengths'] = None
            results['SPI']['avgTime'] = None
        results['SPI']['sRate'] = results['SPI']['sNumber']/trials
        results['SPI']['fRate'] = results['SPI']['fNumber']/trials
        results['SPI']['tRate'] = results['SPI']['tNumber']/trials
        
    # Case where calls are made in rounds
    if (rounds):
        # Intialise results dictionary
        results = {'ANY':{'rounds':[], 'avgRounds': 0,
                          'times':[], 'avgTime': 0, 'sNumber': 0,
                          'fNumber': 0, 'tNumber': 0}, 
                   'CO':{'rounds':[], 'avgRounds': 0,
                         'times':[], 'avgTime': 0, 'sNumber': 0,
                         'fNumber': 0, 'tNumber': 0},
                   'LNS':{'rounds':[], 'avgRounds': 0,
                          'times':[], 'avgTime': 0, 'sNumber': 0,
                          'fNumber': 0, 'tNumber': 0}, 
                   'TOK':{'rounds':[], 'avgRounds': 0,
                          'times':[], 'avgTime': 0, 'sNumber': 0,
                          'fNumber': 0, 'tNumber': 0},
                   'SPI':{'rounds':[], 'avgRounds': 0,
                          'times':[], 'avgTime': 0, 'sNumber': 0,
                          'fNumber': 0, 'tNumber': 0}}
        
        # For set number of trials
        for _ in range(trials):
            # Generate graph
            if (top == 'complete'):
                G = completeGraph(n)
            elif (top == 'incomplete'):
                G = incompleteGraph(n)
            elif (top == 'dynamic'):
                G = diGraph(n)
            
            # Create copy of graph
            H = copy.deepcopy(G)
            
            # Run each protocol on H and record results
            # (number of successes, failures and timeouts)
            #ANY
            (r, timer, success, failure, timeout) = executeRounds(H, ANY)
            if (success):
                results['ANY']['rounds'].append(r)
                results['ANY']['times'].append(timer)
                results['ANY']['sNumber'] += 1
            elif (failure):
                results['ANY']['fNumber'] += 1
            elif (timeout):
                results['ANY']['tNumber'] += 1
            # CO
            H = copy.deepcopy(G)
            (r, timer, success, failure, timeout) = executeRounds(H, CO)
            if (success):
                results['CO']['rounds'].append(r)
                results['CO']['times'].append(timer)
                results['CO']['sNumber'] += 1
            elif (failure):
                results['CO']['fNumber'] += 1
            elif (timeout):
                results['CO']['tNumber'] += 1
            # LNS
            H = copy.deepcopy(G)
            (r, timer, success, failure, timeout) = executeRounds(H, LNS)
            if (success):
                results['LNS']['rounds'].append(r)
                results['LNS']['times'].append(timer)
                results['LNS']['sNumber'] += 1
            elif (failure):
                results['LNS']['fNumber'] += 1
            elif (timeout):
                results['LNS']['tNumber'] += 1
            # TOK
            H = copy.deepcopy(G)
            (r, timer, success, failure, timeout) = executeRounds(H, TOK)
            if (success):
                results['TOK']['rounds'].append(r)
                results['TOK']['times'].append(timer)
                results['TOK']['sNumber'] += 1
            elif (failure):
                results['TOK']['fNumber'] += 1
            elif (timeout):
                results['TOK']['tNumber'] += 1
            # SPI
            H = copy.deepcopy(G)
            (r, timer, success, failure, timeout) = executeRounds(H, SPI)
            if (success):
                results['SPI']['rounds'].append(r)
                results['SPI']['times'].append(timer)
                results['SPI']['sNumber'] += 1
            elif (failure):
                results['SPI']['fNumber'] += 1
            elif (timeout):
                results['SPI']['tNumber'] += 1
                
        # Calculate averages and success rates
        # ANY
        if (len(results['ANY']['rounds']) > 0):
            results['ANY']['avgRounds'] = sum(
                results['ANY']['rounds'])/results['ANY']['sNumber']
            results['ANY']['avgTime'] = sum(
                results['ANY']['times'])/results['ANY']['sNumber']
        else:
            results['ANY']['avgRounds'] = None
            results['ANY']['avgTime'] = None
        results['ANY']['sRate'] = results['ANY']['sNumber']/trials
        results['ANY']['fRate'] = results['ANY']['fNumber']/trials
        results['ANY']['tRate'] = results['ANY']['tNumber']/trials
        # CO
        if (len(results['CO']['rounds']) > 0):
            results['CO']['avgRounds'] = sum(
                results['CO']['rounds'])/results['CO']['sNumber']
            results['CO']['avgTime'] = sum(
                results['CO']['times'])/results['CO']['sNumber']
        else:
            results['CO']['avgRounds'] = None
            results['CO']['avgTime'] = None
        results['CO']['sRate'] = results['CO']['sNumber']/trials
        results['CO']['fRate'] = results['CO']['fNumber']/trials
        results['CO']['tRate'] = results['CO']['tNumber']/trials
        # LNS
        if (len(results['LNS']['rounds']) > 0):
            results['LNS']['avgRounds'] = sum(
                results['LNS']['rounds'])/results['LNS']['sNumber']
            results['LNS']['avgTime'] = sum(
                results['LNS']['times'])/results['LNS']['sNumber']
        else:
            results['LNS']['avgRounds'] = None
            results['LNS']['avgTime'] = None
        results['LNS']['sRate'] = results['LNS']['sNumber']/trials
        results['LNS']['fRate'] = results['LNS']['fNumber']/trials
        results['LNS']['tRate'] = results['LNS']['tNumber']/trials
        # TOK
        if (len(results['TOK']['rounds']) > 0):
            results['TOK']['avgRounds'] = sum(
                results['TOK']['rounds'])/results['TOK']['sNumber']
            results['TOK']['avgTime'] = sum(
                results['TOK']['times'])/results['TOK']['sNumber']
        else:
            results['TOK']['avgRounds'] = None
            results['TOK']['avgTime'] = None
        results['TOK']['sRate'] = results['TOK']['sNumber']/trials
        results['TOK']['fRate'] = results['TOK']['fNumber']/trials
        results['TOK']['tRate'] = results['TOK']['tNumber']/trials
        # SPI
        if (len(results['SPI']['rounds']) > 0):
            results['SPI']['avgRounds'] = sum(
                results['SPI']['rounds'])/results['SPI']['sNumber']
            results['SPI']['avgTime'] = sum(
                results['SPI']['times'])/results['SPI']['sNumber']
        else:
            results['SPI']['avgRounds'] = None
            results['SPI']['avgTime'] = None
        results['SPI']['sRate'] = results['SPI']['sNumber']/trials
        results['SPI']['fRate'] = results['SPI']['fNumber']/trials
        results['SPI']['tRate'] = results['SPI']['tNumber']/trials
        
    return results

# ===============================================================
#  Experiment function
# ===============================================================

# experiment(maxN, top, trials) - produces results up to maxN agents
# Parameters: maxN - maximum number of agents to test for 
#                    (agents given in multiples of 5)
#             top - network topology (complete, incomplete, dynamic)
#             trials - int, number of trials for each value of n
#             rounds - boolean, dictates if calls are made in rounds 
#                      (true) or not (false)
#             minN - minimum number of agents to test for 
#                   (must be multiple of 5)
# Returns - dictionary - contains all results for all n

def experiment(maxN, top, trials, rounds = False, minN = 5):
    # Case where calls are made sequentially
    if (not rounds):
        # Execution lengths
        elANY, elCO, elLNS, elTOK, elSPI = [],[],[],[],[]
        # Execution times
        etANY, etCO, etLNS, etTOK, etSPI = [],[],[],[],[]
        # Success rates
        srANY, srCO, srLNS, srTOK, srSPI = [],[],[],[],[]
        # Failure rates
        frANY, frCO, frLNS, frTOK, frSPI = [],[],[],[],[]
        # Timeout rates
        trANY, trCO, trLNS, trTOK, trSPI = [],[],[],[],[]
    
        # Produce results for all values of 5n up to maxN
        for n in range(minN, maxN+1, 5):
            # Calculate execution length, time e.t.c.
            results = testProtocols(n, top, trials, rounds)
            print("Progress: "+str(n)+" agents complete.")
            
            # Record ANY results
            if (len(results['ANY']['execLengths']) > 0):
                elANY.append(results['ANY']['avgLength'])
                etANY.append(results['ANY']['avgTime'])
                srANY.append(results['ANY']['sRate'])
                frANY.append(results['ANY']['fRate'])
                trANY.append(results['ANY']['tRate'])
            else:
                elANY.append(None)
                etANY.append(None)
                srANY.append(results['ANY']['sRate'])
                frANY.append(results['ANY']['fRate'])
                trANY.append(results['ANY']['tRate'])
    
            # Record CO results    
            if (len(results['CO']['execLengths']) > 0):
                elCO.append(results['CO']['avgLength'])
                etCO.append(results['CO']['avgTime'])
                srCO.append(results['CO']['sRate'])
                frCO.append(results['CO']['fRate'])
                trCO.append(results['CO']['tRate'])
            else:
                elCO.append(None)
                etCO.append(None)
                srCO.append(results['CO']['sRate'])
                frCO.append(results['CO']['fRate'])
                trCO.append(results['CO']['tRate'])
            
            # Record LNS results  
            if (len(results['LNS']['execLengths']) > 0):
                elLNS.append(results['LNS']['avgLength'])
                etLNS.append(results['LNS']['avgTime'])
                srLNS.append(results['LNS']['sRate'])
                frLNS.append(results['LNS']['fRate'])
                trLNS.append(results['LNS']['tRate'])
            else:
                elLNS.append(None)
                etLNS.append(None)
                srLNS.append(results['LNS']['sRate'])
                frLNS.append(results['LNS']['fRate'])
                trLNS.append(results['LNS']['tRate'])
            
            # Record TOK results  
            if (len(results['TOK']['execLengths']) > 0):
                elTOK.append(results['TOK']['avgLength'])
                etTOK.append(results['TOK']['avgTime'])
                srTOK.append(results['TOK']['sRate'])
                frTOK.append(results['TOK']['fRate'])
                trTOK.append(results['TOK']['tRate'])
            else:
                elTOK.append(None)
                etTOK.append(None)
                srTOK.append(results['TOK']['sRate'])
                frTOK.append(results['TOK']['fRate'])
                trTOK.append(results['TOK']['tRate'])
            
            # Record SPI results
            if (len(results['SPI']['execLengths']) > 0):
                elSPI.append(results['SPI']['avgLength'])
                etSPI.append(results['SPI']['avgTime'])
                srSPI.append(results['SPI']['sRate'])
                frSPI.append(results['SPI']['fRate'])
                trSPI.append(results['SPI']['tRate'])
            else:
                elSPI.append(None)
                etSPI.append(None)
                srSPI.append(results['SPI']['sRate'])
                frSPI.append(results['SPI']['fRate'])
                trSPI.append(results['SPI']['tRate'])
        
        # Compile results into a dictionaries
        executionLengths = {'ANY': elANY, 'CO': elCO, 'LNS': elLNS,
                            'TOK': elTOK, 'SPI': elSPI}
        executionTimes = {'ANY': etANY, 'CO': etCO, 'LNS': etLNS,
                          'TOK': etTOK, 'SPI': etSPI}
        successRates = {'ANY': srANY, 'CO': srCO, 'LNS': srLNS,
                        'TOK': srTOK, 'SPI': srSPI}
        failureRates = {'ANY': frANY, 'CO': frCO, 'LNS': frLNS,
                        'TOK': frTOK, 'SPI': frSPI}
        timeoutRates = {'ANY': trANY, 'CO': trCO, 'LNS': trLNS,
                        'TOK': trTOK, 'SPI': trSPI}
    
        # Final results
        finalResults = (executionLengths, executionTimes, successRates, 
                       failureRates, timeoutRates)
        
    # Case where calls are made in rounds
    if (rounds):
        # Round lengths
        rlANY, rlCO, rlLNS, rlTOK, rlSPI = [],[],[],[],[]
        # Times
        tANY, tCO, tLNS, tTOK, tSPI = [],[],[],[],[]
        # Success rates
        srANY, srCO, srLNS, srTOK, srSPI = [],[],[],[],[]
        # Failure rates
        frANY, frCO, frLNS, frTOK, frSPI = [],[],[],[],[]
        # Timeout rates
        trANY, trCO, trLNS, trTOK, trSPI = [],[],[],[],[]
        
        # Produce results for all values of 5n up to maxN
        for n in range(minN, maxN+1, 5):
            # Calculate execution length, time e.t.c.
            results = testProtocols(n, top, trials, rounds)
            print("Progress: "+str(n)+" agents complete.")
            
            # Record ANY results
            if (len(results['ANY']['rounds']) > 0):
                rlANY.append(results['ANY']['avgRounds'])
                tANY.append(results['ANY']['avgTime'])
                srANY.append(results['ANY']['sRate'])
                frANY.append(results['ANY']['fRate'])
                trANY.append(results['ANY']['tRate'])
            else:
                rlANY.append(None)
                tANY.append(None)
                srANY.append(results['ANY']['sRate'])
                frANY.append(results['ANY']['fRate'])
                trANY.append(results['ANY']['tRate'])
            
            # Record CO results
            if (len(results['CO']['rounds']) > 0):
                rlCO.append(results['CO']['avgRounds'])
                tCO.append(results['CO']['avgTime'])
                srCO.append(results['CO']['sRate'])
                frCO.append(results['CO']['fRate'])
                trCO.append(results['CO']['tRate'])
            else:
                rlCO.append(None)
                tCO.append(None)
                srCO.append(results['CO']['sRate'])
                frCO.append(results['CO']['fRate'])
                trCO.append(results['CO']['tRate'])
            
            # Record LNS results
            if (len(results['LNS']['rounds']) > 0):
                rlLNS.append(results['LNS']['avgRounds'])
                tLNS.append(results['LNS']['avgTime'])
                srLNS.append(results['LNS']['sRate'])
                frLNS.append(results['LNS']['fRate'])
                trLNS.append(results['LNS']['tRate'])
            else:
                rlLNS.append(None)
                tLNS.append(None)
                srLNS.append(results['LNS']['sRate'])
                frLNS.append(results['LNS']['fRate'])
                trLNS.append(results['LNS']['tRate'])
            
            # Record TOK results
            if (len(results['TOK']['rounds']) > 0):
                rlTOK.append(results['TOK']['avgRounds'])
                tTOK.append(results['TOK']['avgTime'])
                srTOK.append(results['TOK']['sRate'])
                frTOK.append(results['TOK']['fRate'])
                trTOK.append(results['TOK']['tRate'])
            else:
                rlTOK.append(None)
                tTOK.append(None)
                srTOK.append(results['TOK']['sRate'])
                frTOK.append(results['TOK']['fRate'])
                trTOK.append(results['TOK']['tRate'])
            
            # Record SPI results
            if (len(results['SPI']['rounds']) > 0):
                rlSPI.append(results['SPI']['avgRounds'])
                tSPI.append(results['SPI']['avgTime'])
                srSPI.append(results['SPI']['sRate'])
                frSPI.append(results['SPI']['fRate'])
                trSPI.append(results['SPI']['tRate'])
            else:
                rlSPI.append(None)
                tSPI.append(None)
                srSPI.append(results['SPI']['sRate'])
                frSPI.append(results['SPI']['fRate'])
                trSPI.append(results['SPI']['tRate'])
        
        # Compile results into a dictionaries
        roundLengths = {'ANY': rlANY, 'CO': rlCO, 'LNS': rlLNS,
                        'TOK': rlTOK, 'SPI': rlSPI}
        times = {'ANY': tANY, 'CO': tCO, 'LNS': tLNS,
                 'TOK': tTOK, 'SPI': tSPI}
        successRates = {'ANY': srANY, 'CO': srCO, 'LNS': srLNS,
                        'TOK': srTOK, 'SPI': srSPI}
        failureRates = {'ANY': frANY, 'CO': frCO, 'LNS': frLNS,
                        'TOK': frTOK, 'SPI': frSPI}
        timeoutRates = {'ANY': trANY, 'CO': trCO, 'LNS': trLNS,
                        'TOK': trTOK, 'SPI': trSPI}
        
        # Final results
        finalResults = (roundLengths, times, successRates, 
                           failureRates, timeoutRates)
    
    return finalResults