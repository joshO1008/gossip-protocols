'''This file contains:
    - Prerequisite functions to check for an all-expert state
      and to check if an individual call is permitted
    - Functions to execute a chosen protocol sequentially and
      in rounds
    - Five indivdual protocol functions used to return 
      permitted calls'''

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
#  Useful tools
# ===============================================================

# experts(G) - checks if all agents of G are experts
# Parameters: G - graph object, generated in "graph_generator.py"
# Returns: s - boolean, true if all agents experts, false otherwise

def experts(G):
    # Fetch number of nodes
    n = G.number_of_nodes()
    
    # Intialise s as true
    s = True
    
    # Loop through all nodes of G
    for agent in list(range(n)):
        # If an agent does not know all secrets, 
        # set s to false and break
        if(len(G.nodes[agent]['secrets']) < n):
            s = False
            break
    
    return s
        

# pPermitted(G, P, caller, callee) - checks if (caller, callee) is a P 
#                                 permitted call
# Parameters: G - graph object,
#             P - predefined protocol function,
#             caller - int, index of caller agent
#             callee - int, index of callee agent
# Returns: boolean - true if call is permitted, false otherwise

def pPermitted(G, P, caller, callee):
    # ANY - always p permitted
    if (P == ANY):
        return True
    # CO - p permitted if agents have not been in contact
    elif (P == CO):
        if (caller not in G.nodes[callee]['contacts']):
            return True
    # LNS - p permitted if caller does not know callee's secret
    elif (P == LNS):
        if (callee not in G.nodes[caller]['secrets']):
            return True
    # TOK and SPI - p permitted if caller has a token
    elif (P == TOK or P == SPI):
        if (G.nodes[caller]['token']):
            return True
    return False


# ===============================================================
#  Protocol execution function
# ===============================================================

# executeProtocol(G, P, breakdown) - executes protocol P on graph G
# Parameters: G - graph object, generated in "graph_generator.py"
#             P - function,  returns list of P permitted calls
#             breakdown - boolean, if true a breakdown of calls made and
#                         available calls at each stage given 
# Returns: c - execution length
#          timer - execution time
#          success - boolean, indicates if all agents are experts 
#                    at termination
#          failure - boolean, indicates if protocol has failed
#          timeout - boolean, indicates if protocol has timed out

def executeProtocol(G, P, breakdown = False):
    # Intitialise number of calls and success boolean
    c, success = 0, False
    # Initialise timeout and failure booleans
    timeout, failure = False, False
    
    # Initialise list of available calls and newest call
    calls = []
    newcall = 0
    
    # Record initial time
    initTime = time.perf_counter()
    
    # Execute protocol (each loop corresponds to one call or termination)
    while (True):
        # Check if all agents are experts
        if (experts(G)):
            success = True
            break
        
        # Fetch list of available calls
        calls = P(G, newcall, calls)
        
        if (breakdown):
            print("Stage "+str(c + 1))
            print("Available calls: "+str(calls))
        
        # If calls is non-empty
        if (len(calls) != 0):
            # Select random call
            newcall = random.choice(calls)
            
            if (breakdown):
                print("New call: "+str(newcall)+"\n")
            # i is the caller, j is the callee
            i, j = newcall[0], newcall[1]
            
            # Execute new call
            
            # Exchange secrets
            G.nodes[i]['secrets'] = G.nodes[i]['secrets'].union(
                                    G.nodes[j]['secrets'])
            G.nodes[j]['secrets'] = G.nodes[i]['secrets']
            
            # Add each agent to each others past contacts
            G.nodes[i]['contacts'].add(j)
            G.nodes[j]['contacts'].add(i)
            
            # Exchange tokens
            # TOK
            if (P == TOK):
                G.nodes[i]['token'] = False
                G.nodes[j]['token'] = True
            # SPI
            if (P == SPI):
                G.nodes[j]['token'] = False
            
            # Increment call counter
            c += 1
            
            # Indicate G is no longer an initial gossip graph
            G.graph['initial'] = False
            
            # Update arcs of G in dynamic case
            if (type(G) == nx.classes.digraph.DiGraph):
                # Update phone number lists
                G.nodes[i]['numbers'] = G.nodes[i]['numbers'].union(
                                        G.nodes[j]['numbers'])
                G.nodes[j]['numbers'] = G.nodes[i]['numbers']
                
                # Add relevant arcs to graph
                # Loop through known numbers of caller
                for number in G.nodes[i]['numbers']:
                    # Add any new arcs to G
                    if (((i, number) not in G.edges) and (i != number)):
                        G.add_edge(i, number)
                        # Add new P permitted calls to calls
                        if pPermitted(G, P, i, number):
                            calls.append((i, number))
                
                # Similarly for the callee
                for number in G.nodes[j]['numbers']:
                    if (((j, number) not in G.edges) and (j != number)):
                        G.add_edge(j, number)
                        # Add new P permitted calls to calls
                        if pPermitted(G, P, j, number):
                            calls.append((j, number))
            
        # Else if calls is empty, break from loop
        elif (len(calls) == 0):
            failure = True
            break
        
        # Record current time 
        curTime = time.perf_counter()
        # Time elapsed
        timer = curTime - initTime
        
        # Timeout
        if (timer > G.number_of_nodes()/10):
            timeout = True
            break
        
    return (c, timer, success, failure, timeout)


# ===============================================================
#  Protocol execution function (rounds variant)
# ===============================================================

# executeRounds(G, P) - executes protocol P on gossip graph G 
#                      (in rounds of calls)
# Parameters: G - graph object, generated in "graph_generator.py"
#             P - function,  returns list of P permitted calls
#             breakdown - boolean, if true function will return 
#                         breakdown of calls made in each round
# Returns: r - number of rounds performed
#          timer - execution time
#          success - boolean, indicates if all agents are experts 
#                    at termination
#          failure - boolean, indicates if protocol has failed
#          timeout - boolean, indicates if protocol has timed out

def executeRounds(G, P, breakdown=False):
    # Intitialise number of rounds and success boolean
    r, success = 0, False
    # Initialise failure and timeout booleans
    failure, timeout = False, False
    
    # Initialise list of available calls and newest call
    newcall = 0
    calls = []
    calls = P(G, newcall, calls)
    
    # Record initial time
    initTime = time.perf_counter()
    
    # Execute protocol (each loop corresponds to one round)
    while (True):
        # Check if all agents are experts
        if (experts(G)):
            success = True
            break
        
        # If calls is empty, break from loop
        if (len(calls) == 0):
            failure = True
            break
        
        if (breakdown):
            print("Round "+str(r + 1))
            print("Possible calls for this round: "+str(calls))
        
        # Create copy of available calls
        roundCalls = copy.deepcopy(calls)
        # Initialise set of agents that have participated 
        # in this round
        participants = set()
        
        if (breakdown):
            print("Calls chosen this round:")
        
        # Perform calls whilst list of round calls in non-empty
        while (len(roundCalls) != 0 and len(participants) < 
               (G.number_of_nodes() - 1)):
            # Select random call
            newcall = random.choice(roundCalls)
            
            # i is the caller, j is the callee
            i, j = newcall[0], newcall[1]
            # If i or j already participated, remove (i,j) from calls 
            # and select new pair
            if ((i in participants) or (j in participants)):
                roundCalls.remove(newcall)
                continue
            # Else execute new call
            else:
                participants.add(i)
                participants.add(j)
                if (breakdown):
                    print(newcall)
            
            # Exchange secrets
            G.nodes[i]['secrets'] = G.nodes[i]['secrets'].union(
                                    G.nodes[j]['secrets'])
            G.nodes[j]['secrets'] = G.nodes[i]['secrets']
            
            # Add each agent to each others past contacts
            G.nodes[i]['contacts'].add(j)
            G.nodes[j]['contacts'].add(i)
            
            # Exchange tokens
            # TOK
            if (P == TOK):
                G.nodes[i]['token'] = False
                G.nodes[j]['token'] = True
            # SPI
            if (P == SPI):
                G.nodes[j]['token'] = False
            
            # Indicate G is no longer an initial gossip graph
            G.graph['initial'] = False
            
            # Update initial list of calls for next round
            calls = P(G, newcall, calls)
            
            # Update arcs of G in dynamic case
            if (type(G) == nx.classes.digraph.DiGraph):
                # Update phone number lists
                G.nodes[i]['numbers'] = G.nodes[i]['numbers'].union(
                                        G.nodes[j]['numbers'])
                G.nodes[j]['numbers'] = G.nodes[i]['numbers']
                
                # Add relevant arcs to graph
                # Loop through known numbers of caller
                for number in G.nodes[i]['numbers']:
                    # Add any new arcs to G
                    if (((i, number) not in G.edges) and (i != number)):
                        G.add_edge(i, number)
                        # Add new P permitted calls to calls
                        if pPermitted(G, P, i, number):
                            calls.append((i, number))
                
                # Similarly for the callee
                for number in G.nodes[j]['numbers']:
                    if (((j, number) not in G.edges) and (j != number)):
                        G.add_edge(j, number)
                        # Add new P permitted calls to calls
                        if pPermitted(G, P, j, number):
                            calls.append((j, number))
            
        if (breakdown):
            print("\n")
    
        # Increment round counter
        r += 1
        
        # Record current time 
        curTime = time.perf_counter()
        # Time elapsed
        timer = curTime - initTime
        
        # Timeout
        if (timer > G.number_of_nodes()/10):
            timeout = True
            break
        
    return (r, timer, success, failure, timeout)
                


# ===============================================================
#  Individual protocol functions
# ===============================================================

# ANY(G, newcall, calls) - returns ANY permitted calls for graph G
# Parameters: G - graph object, generated in "graph_generator.py"
#             newcall - tuple, latest call made
#             calls - list of permitted calls in the previous step
# Returns - calls, updated list of permitted calls

def ANY(G, newcall, calls):
    
    # If G is an initial gossip graph, add all edges/arcs from G
    if (G.graph['initial'] or newcall == 0):
        H = copy.deepcopy(G)
        H = nx.DiGraph(H)
        calls = list(H.edges)
        
    return calls




# CO(G, newcall, calls) - returns CO permitted calls for graph G
# Parameters: G - graph object, generated in "graph_generator.py"
#             newcall - tuple, latest call made
#             calls - list of permitted calls in the previous step
# Returns - calls, updated list of permitted calls

def CO(G, newcall, calls):
    
    # If G is an initial gossip graph, add all edges/arcs from G
    if (G.graph['initial'] or newcall == 0):
        H = copy.deepcopy(G)
        H = nx.DiGraph(H)
        calls = list(H.edges)
    
    # Latest call is (i,j)
    # If G not initial, remove (i,j) and (j,i) from calls
    else:
        calls.remove(newcall)
        if (newcall[::-1] in calls):
            calls.remove(newcall[::-1])
        
    return calls



# LNS(G, newcall, calls) - returns LNS permitted calls for graph G
# Parameters: G - graph object, generated in "graph_generator.py"
#             newcall - tuple, latest call made
#             calls - list of permitted calls in the previous step
# Returns - calls, updated list of permitted calls

def LNS(G, newcall, calls):
    
    # If G is an initial gossip graph, add all edges/arcs from G
    if (G.graph['initial'] or newcall == 0):
        H = copy.deepcopy(G)
        H = nx.DiGraph(H)
        calls = list(H.edges)
    
    # Say the latest call is (i,j)
    # If G not initial, remove calls (i,k) where i knows k's secret 
    # Similarly remove calls (j,k) such that j knows k's secret 
    else:
        i = newcall[0]
        # For each secret k that i knows
        for secret in G.nodes[i]['secrets']:
            # Check if (i,k) in calls and remove if so
            if ((i, secret) in calls):
                calls.remove((i, secret))
                
        j = newcall[1]
        # For each secret k that j knows
        for secret in G.nodes[j]['secrets']:
            # Check if (j,k) in calls and remove if so
            if ((j, secret) in calls):
                calls.remove((j, secret)) 
        
    return calls
    
    

# TOK(G, newcall, calls) - returns TOK permitted calls for graph G
# Parameters: G - graph object, generated in "graph_generator.py"
#             newcall - tuple, latest call made
#             calls - list of permitted calls in the previous step
# Returns - calls, updated list of permitted calls

def TOK(G, newcall, calls):
    
    # If G is an initial gossip graph, add all edges/arcs from G
    if (G.graph['initial'] or newcall == 0):
        H = copy.deepcopy(G)
        H = nx.DiGraph(H)
        calls = list(H.edges)
    
    # Say the latest call is (i.j)
    # If G not initial, remove calls (i,k) where i knows k's number
    # and add calls (j, k) such that j knows k's number
    else:
        i, j = newcall[0], newcall[1]
        
        # For each neighbour k of i, remove call (i,k) if it exists
        for neighbour in G.adj[i]:
            if ((i, neighbour) in calls):
                calls.remove((i, neighbour))
                
        # For each neighbour k of j, add new calls (j,k)
        for neighbour in G.adj[j]:
            if ((j, neighbour) not in calls):
                calls.append((j, neighbour))
        
    return calls


# SPI(G, newcall, calls) - returns SPI permitted calls for gossip graph G
# Parameters: G - graph object, generated in "graph_generator.py"
#             newcall - tuple, latest call made
#             calls - list of permitted calls in the previous step
# Returns - calls, updated list of permitted calls

def SPI(G, newcall, calls):
    
    # If G is an initial gossip graph, add all edges/arcs from G
    if (G.graph['initial'] or newcall == 0):
        H = copy.deepcopy(G)
        H = nx.DiGraph(H)
        calls = list(H.edges)
    
    # Say the latest call is (i.j)
    # If G not initial, remove calls (j,k) such that j knows k's number
    else:
        j = newcall[1]
        # For each neighbour k of j, remove call (j,k) if it exists
        for neighbour in G.adj[j]:
            if ((j, neighbour) in calls):
                calls.remove((j, neighbour))
        
    return calls

    
    
    