#!/usr/bin/env python
# coding: utf-8

# In[4]:


import itertools
import random

get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx


# In[5]:


p = 0.75

# Do this 10 times
for _ in range(10):
    r = random.random()
    if r < p:
        print('Heads')
    else:
        print('Tails')


# In[6]:


names = ['Alice', 'Bob', 'Cathy', 'Dan']
random.choice(names)


# In[8]:


G = nx.cycle_graph(5)
random.sample(G.nodes, 2)


# In[9]:


names = ['Alice', 'Bob', 'Carol']
tickets = [1, 3, 4]

for _ in range(10):
    print(random.choices(names, tickets))


# In[10]:


random.choices(names, tickets, k=10)


# In[11]:


elements = [0, 1, 2, 3, 4]
list(itertools.combinations(elements, 2))


# In[12]:


G = nx.Graph()
G.add_nodes_from(elements)

list(itertools.combinations(G.nodes, 2))


# In[20]:


def gnp_random_graph(N, p):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    
    for i, j in itertools.combinations(G.nodes, 2):
        r = random.random()
        if r < p:
            G.add_edge(i, j)
        # Do nothing if r >= p
        
    return G

G = gnp_random_graph(16, 0.15)
nx.draw(G)
print('Graph has', G.number_of_edges(), 'edges.')


# In[19]:


def gnm_random_graph(N, M):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    
    possible_edges = itertools.combinations(G.nodes, 2)
    edges_to_add = random.sample(list(possible_edges), M)
    G.add_edges_from(edges_to_add)
    
    return G

G = gnm_random_graph(16, 18)
nx.draw(G)


# In[21]:


N = 10
G = nx.cycle_graph(N)
nx.draw_circular(G, with_labels=True)


# In[22]:


k = 4

for n in G.nodes:
    for i in range(1, k // 2 + 1):
        left  = (n-i) % N
        right = (n+i) % N 
        G.add_edge(n, left)
        G.add_edge(n, right)

nx.draw_circular(G, with_labels=True)


# In[23]:


p = 0.1

for u, v in list(G.edges):
    if random.random() < p:
        not_neighbors = set(G.nodes) - set(G.neighbors(u))
        w = random.choice(list(not_neighbors))
        G.remove_edge(u, v)
        G.add_edge(u, w)

nx.draw_circular(G, with_labels=True)


# In[24]:


def watts_strogatz_graph(N, k, p):
   
    G = nx.cycle_graph(N)

   
    for n in G.nodes:
        for i in range(1, k // 2 + 1):
            left  = (n-i) % N
            right = (n+i) % N 
            G.add_edge(n, left)
            G.add_edge(n, right)
    
    for u, v in list(G.edges):
        if random.random() < p:
            not_neighbors = set(G.nodes) - set(G.neighbors(u)) - {u}
            w = random.choice(list(not_neighbors))
            G.remove_edge(u, v)
            G.add_edge(u, w)

    return G


# In[25]:


G = watts_strogatz_graph(16, 4, 0.2)
nx.draw_circular(G, with_labels=True)


# In[26]:


G = nx.star_graph(4)
degrees = [G.degree(n) for n in G.nodes]

print(degrees)
nx.draw(G, with_labels=True)


# In[27]:


def barabasi_albert_graph(N, m):
    G = nx.complete_graph(m + 1)
    for i in range(G.number_of_nodes(), N):
        new_neighbors = []
        possible_neighbors = list(G.nodes)
        for _ in range(m):
            degrees = [G.degree(n) for n in possible_neighbors]
            j = random.choices(possible_neighbors, degrees)[0]
            new_neighbors.append(j)
            possible_neighbors.remove(j)
        
        for j in new_neighbors:
            G.add_edge(i, j)

    return G

G = barabasi_albert_graph(30, 1)
nx.draw(G)


# In[ ]:




