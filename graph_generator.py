'''This file contains three functions in order to generate
complete, incomplete, and dynamic gossip (di)graphs.'''

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
#  Complete (gossip) graph generator
# ===============================================================

# completeGraph(n, plot) - generate a complete gossip graph on 
#                          n vertices
# Parameters: n - number of agents/nodes
#             plot - boolean, dicates if final network is plotted
# Returns - complete (gossip) graph object with n nodes

def completeGraph(n, plot = False):
    # Initialise complete graph using nx
    G = nx.complete_graph(n)
    # Indicate G is an initial gossip graph
    G.graph['initial'] = True
    
    # Add attributes to nodes (agents)
    for agent in list(range(n)):
        # Initial secret
        G.nodes[agent]['secrets'] = {agent}
        # Contact list (initially empty)
        G.nodes[agent]['contacts'] = set()
        # Token (boolean initially set to true)
        G.nodes[agent]['token'] = True
        # Initial list of known numbers
        G.nodes[agent]['numbers'] = set(G.adj[agent]).union({agent})
    
    # Plot the graph 
    if (plot):
        options = {'node_color': 'lightblue',
                   'node_size': 1000,
                   'width': 3,
                   'with_labels' : True,
                   'font_weight' : 'bold',
                   'font_size' : 20
                   }
        nx.draw_circular(G, **options)
    
    # Return the graph
    return G


# ===============================================================
#  Random incomplete (gossip) graph generator
# ===============================================================

# incompleteGraph(n) - generate a random incomplete gossip graph 
#                      on n vertices
# Parameters: n - number of agents/nodes
#             plot - boolean, dicates if final network is plotted
# Returns - graph object with n nodes

def incompleteGraph(n, plot = False):
    # Generate initial random tree using nx
    G = nx.random_tree(n)
    # Indicate G is an initial gossip graph
    G.graph['initial'] = True
    
    # Calculate maximum number of extra edges to add
    nC2 = factorial(n)/(2 * factorial(n - 2))
    epsilon = nC2 - (n-1)
    
    # Generate random number of edges to add
    r = random.randint(0, epsilon)
    
    # Add edges to G until limit reached
    while (G.number_of_edges() < (n-1) + r):
        # Pick random pair of nodes in G
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        
        # Add edge (i,j) to G if edge doesn't already exist
        if (((i,j) not in G.edges) and (i != j)):
            G.add_edge(*(i,j))
    
    # Add attributes to nodes
    for agent in list(range(n)):
        # Initial secret
        G.nodes[agent]['secrets'] = {agent}
        # Contact list (initially empty)
        G.nodes[agent]['contacts'] = set()
        # Token (boolean initially set to true)
        G.nodes[agent]['token'] = True
        # Initial list of known numbers
        G.nodes[agent]['numbers'] = set(G.adj[agent]).union({agent})
    
    # Plot the graph
    if (plot):
        options = {'node_color': 'lightblue',
                   'node_size': 1000,
                   'width': 3,
                   'with_labels' : True,
                   'font_weight' : 'bold',
                   'font_size' : 20
                   }
        nx.draw_circular(G, **options)
    
    # Return the graph
    return G


# ===============================================================
#  Random (gossip) digraph generator
# ===============================================================

# diGraph(n) - generate a random gossip digraph on n vertices
# Parameters: n - number of agents/nodes
#             plot - boolean, dicates if final network is plotted
# Returns - graph object with n nodes

def diGraph(n, plot = False):
    # Generate intial random tree
    G = nx.random_tree(n)
    
    # Create digraph using the edges of G (each edge becomes two arcs)
    G = nx.DiGraph(G)
    
    # Fetch adjacency matrix of G
    A = np.array(nx.adjacency_matrix(G).todense())
    
    # Loop through all pairs of vertices
    for i in list(range(n)):
        for j in list(range(i)):
            # Check if an arc exists between nodes i and j 
            # (and hence vice versa)
            if (A[i,j] == 1):
                # If so, remove either arc (i,j) or (j,i) (at random)
                rand = random.randint(0,1)
                if (rand == 0):
                    A[i,j] = 0
                else:
                    A[j,i] = 0
    
    # Convert matrix back into NetwrokX digraph object
    G = nx.convert_matrix.from_numpy_matrix(A, create_using=(nx.DiGraph))
    # Indicate G is an initial gossip graph
    G.graph['initial'] = True
    
    # Calculate maximum number of extra arcs to add (restricted)
    nC2 = factorial(n)/(2 * factorial(n - 2))
    epsilon = int(((2 * nC2) - (n-1))/10)
    
    # Generate random number of arcs to add
    r = random.randint(0, epsilon)
    
    # Add arcs to G until limit reached
    while (G.number_of_edges() < (n-1) + r):
        # Pick random pair of nodes in G
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        
        # Add arc (i,j) to G if arc doesn't already exist
        if (((i,j) not in G.edges) and (i != j)):
            G.add_edge(*(i,j))
    
    # Add additional attributes to nodes
    for agent in list(range(n)):
        # Initial secret
        G.nodes[agent]['secrets'] = {agent}
        # Contact list (initially empty)
        G.nodes[agent]['contacts'] = set()
        # Token (boolean initially set to true)
        G.nodes[agent]['token'] = True
        # Initial list of known numbers
        G.nodes[agent]['numbers'] = set(G.adj[agent]).union({agent})
    
    # Plot graph
    if (plot):
        options = {'node_color': 'lightblue',
                   'node_size': 1000,
                   'width': 3,
                   'with_labels' : True,
                   'font_weight' : 'bold',
                   'font_size' : 20
                   }
        nx.draw_circular(G, **options)
    
    # Return the graph
    return G



