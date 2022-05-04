#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx

G = nx.gnm_random_graph(20, 50)
nx.draw(G)


# In[2]:


def initial_state(G):
    state = {}
    for node in G.nodes:
        state[node] = 'asleep'
    return state


initial_state(G)


# In[3]:


import random

P_AWAKEN = 0.2
def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        if current_state[node] == 'asleep':
            if random.random() < P_AWAKEN:
                next_state[node] = 'awake'
    return next_state



test_state = initial_state(G)
state_transition(G, test_state)


# In[4]:


from simulation import Simulation

sim = Simulation(G, initial_state, state_transition, name='Simple Sim')


# In[5]:



sim.state()


# In[6]:


sim.draw()


# In[8]:


sim.run()


sim.steps


# In[9]:


sim.draw(with_labels=True)


# In[10]:


sim.state()


# In[11]:


sim.run(10)

sim.steps


# In[12]:


sim.draw(with_labels=True)


# In[13]:


sim.plot()


# In[14]:


sim.draw(4, with_labels=True)


# In[15]:


sim.state(4)


# In[16]:


sim.plot(min_step=2, max_step=8)


# In[17]:


get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx

G = nx.gnm_random_graph(20, 50)
nx.draw(G)


# In[18]:


import random
import string

def initial_state(G):
    state = {}
    for node in G.nodes:
        state[node] = random.choice('ABCD')
    return state


initial_state(G)


# In[19]:


def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        # Caveat: what if the node has no neighbors?
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            next_state[node] = current_state[neighbor]
    return next_state


test_state = initial_state(G)
state_transition(G, test_state)


# In[20]:


import matplotlib.pyplot as plt

sim = Simulation(G, initial_state, state_transition, name='Voter Model')

sim.draw()


# In[21]:


sim.run(40)

sim.draw()


# In[22]:


sim.plot()


# In[23]:


import random

def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            next_state[node] = current_state[neighbor]
    return next_state


# In[24]:


def state_transition_async(G, current_state):
    for node in G.nodes:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            current_state[node] = current_state[neighbor]
    return current_state


# In[25]:


def state_transition_async(G, current_state):
    nodes_to_update = list(G.nodes)
    random.shuffle(nodes_to_update)
    for node in nodes_to_update:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            current_state[node] = current_state[neighbor]
    return current_state


sim = Simulation(G, initial_state, state_transition_async, name='Async Voter Model')
sim.run(40)
sim.plot()


# In[27]:


def stop_condition(G, current_state):
    unique_state_values = set(current_state.values())
    is_stopped = len(unique_state_values) <= 1
    return is_stopped


sim = Simulation(G, initial_state, state_transition, stop_condition, name='Voter model')
sim.run(100)





# In[28]:


sim.steps


# In[29]:


sim.plot()


# In[30]:


def state_transition_async_rewiring(G, current_state):
    nodes_to_update = list(G.nodes)
    random.shuffle(nodes_to_update)
    for node in nodes_to_update:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            current_state[node] = current_state[neighbor]
            neighbor = random.choice(list(G.neighbors(node)))
            if current_state[node] != current_state[neighbor]:
                G.remove_edge(node, neighbor)
            
    return current_state

sim = Simulation(G, initial_state, state_transition_async_rewiring, stop_condition,
                 name='Voter Model with rewiring')
sim.draw()


# In[31]:


sim.run(40)
sim.draw()


# In[32]:


sim.plot()


# In[33]:


get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx

G = nx.gnm_random_graph(20, 50)
nx.draw(G)


# In[35]:


import random

def initial_state(G):
    state = {}
    for node in G.nodes:
        state[node] = 'S'
    
    patient_zero = random.choice(list(G.nodes))
    state[patient_zero] = 'I'
    return state

initial_state(G)


# In[36]:


MU = 0.1
BETA = 0.1

def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        if current_state[node] == 'I':
            if random.random() < MU:
                next_state[node] = 'S'
        else:
            for neighbor in G.neighbors(node):
                if current_state[neighbor] == 'I':
                    if random.random() < BETA:
                        next_state[node] = 'I'

    return next_state


test_state = initial_state(G)
state_transition(G, test_state)


# In[37]:


sim = Simulation(G, initial_state, state_transition, name='SIS model')

sim.draw()


# In[38]:


sim.run(25)

sim.draw()


# In[39]:


sim.plot()


# In[ ]:




