#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random

get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx


# In[12]:


G = nx.Graph()
nx.add_cycle(G,[0, 1, 2, 3])
nx.add_cycle(G,[4, 5, 6, 7])
G.add_edge(0, 7)

nx.draw(G, with_labels=True)


# In[13]:


partition = [
    {1, 2, 3},
    {4, 5, 6},
    {0, 7},
]


# In[14]:


nx.community.is_partition(G, partition)


# In[15]:


partition_map = {}
for idx, cluster_nodes in enumerate(partition):
    for node in cluster_nodes:
        partition_map[node] = idx

partition_map


# In[16]:


partition_map[0] == partition_map[7]


# In[17]:


node_colors = [partition_map[n] for n in G.nodes]
        
nx.draw(G, node_color=node_colors, with_labels=True)


# In[18]:


def modularity(G, partition):
    W = sum(G.edges[v, w].get('weight', 1) for v, w in G.edges)
    summation = 0
    for cluster_nodes in partition:
        s_c = sum(G.degree(n, weight='weight') for n in cluster_nodes)
        C = G.subgraph(cluster_nodes)
        W_c = sum(C.edges[v, w].get('weight', 1) for v, w in C.edges)
        summation += W_c - s_c ** 2 / (4 * W)
    
    return summation / W


# In[19]:


modularity(G, partition)


# In[20]:


partition_2 = [
    {0, 1, 2, 3},
    {4, 5, 6, 7},
]
modularity(G, partition_2)


# In[21]:


nx.community.quality.modularity(G, partition_2)


# In[22]:


K = nx.karate_club_graph()
nx.draw(K, with_labels=True)


# In[23]:


K.nodes[0]


# In[25]:


K.nodes[9]


# In[27]:


K = nx.karate_club_graph()
club_color = {
    'Mr. Hi': 'orange',
    'Officer': 'lightblue',
}
node_colors = [club_color[K.nodes[n]['club']] for n in K.nodes]
nx.draw(K, node_color=node_colors, with_labels=True)


# In[29]:


groups = {
    'Mr. Hi': set(),
    'Officer': set(),
}

for n in K.nodes:
    club = K.nodes[n]['club']
    groups[club].add(n)
    
groups


# In[30]:


empirical_partition = list(groups.values())
empirical_partition


# In[31]:


nx.community.is_partition(K, empirical_partition)


# In[32]:


nx.community.quality.modularity(K, empirical_partition)


# In[33]:


random_nodes = random.sample(K.nodes, 17)
random_partition = [set(random_nodes),
                    set(K.nodes) - set(random_nodes)]
random_partition


# In[34]:


random_node_colors = ['orange' if n in random_nodes else 'lightblue' for n in K.nodes]
nx.draw(K, node_color=random_node_colors)


# In[35]:


nx.community.quality.modularity(K, random_partition)


# In[36]:


G = nx.karate_club_graph()
nx.draw(G)


# In[37]:


nx.edge_betweenness_centrality(G)


# In[38]:


my_edge_betweenness = nx.edge_betweenness_centrality(G)
my_edge_betweenness[0, 1]


# In[39]:


max(my_edge_betweenness, key=my_edge_betweenness.get)


# In[40]:


max(G.edges(), key=my_edge_betweenness.get)


# In[42]:


my_edge_betweenness = nx.edge_betweenness_centrality(G)
most_valuable_edge = max(G.edges(), key=my_edge_betweenness.get)
G.remove_edge(*most_valuable_edge)
nx.connected_components(G)


# In[43]:


list(nx.connected_components(G))


# In[44]:


G = nx.karate_club_graph()
partition_sequence = []
for _ in range(G.number_of_edges()):
    my_edge_betweenness = nx.edge_betweenness_centrality(G)
    most_valuable_edge = max(G.edges(), key=my_edge_betweenness.get)
    G.remove_edge(*most_valuable_edge)
    my_partition = list(nx.connected_components(G))
    partition_sequence.append(my_partition)


# In[45]:


len(partition_sequence), nx.karate_club_graph().number_of_edges()


# In[46]:


len(partition_sequence[0])


# In[47]:


len(partition_sequence[-1]), nx.karate_club_graph().number_of_nodes()


# In[48]:


G = nx.karate_club_graph()
modularity_sequence = [modularity(G, p) for p in partition_sequence]
modularity_sequence


# In[49]:


import matplotlib.pyplot as plt
plt.plot(modularity_sequence)
plt.ylabel('Modularity')
plt.xlabel('Algorithm step')


# In[50]:


best_partition = max(partition_sequence, key=nx.community.quality.modularity)


# In[51]:


def my_modularity(partition):
    return nx.community.quality.modularity(G, partition)
best_partition = max(partition_sequence, key=my_modularity)


# In[52]:


best_partition


# In[53]:


def create_partition_map(partition):
    partition_map = {}
    for idx, cluster_nodes in enumerate(partition):
        for node in cluster_nodes:
            partition_map[node] = idx
    return partition_map

best_partition_map = create_partition_map(best_partition)

node_colors = [best_partition_map[n] for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors)


# In[54]:


nx.community.quality.modularity(G, best_partition)


# In[55]:


for partition in partition_sequence:
    if len(partition) == 2:
        two_cluster_partition = partition
        break

two_cluster_partition


# In[56]:


two_cluster_partition_map = create_partition_map(two_cluster_partition)

node_colors = [two_cluster_partition_map[n] for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors)


# In[57]:


nx.community.quality.modularity(G, two_cluster_partition)


# In[58]:


import matplotlib.pyplot as plt

pos = nx.layout.spring_layout(G)
fig = plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)
two_cluster_partition_map = create_partition_map(two_cluster_partition)
node_colors = [two_cluster_partition_map[n] for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors, pos=pos)
plt.title('Predicted communities')

plt.subplot(1, 2, 2)
node_colors = [G.nodes[n]['club'] == 'Officer' for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors, pos=pos)
plt.title('Actual communities')


# In[59]:


G.nodes[8]


# In[60]:


list(nx.community.girvan_newman(G))[:5]


# In[ ]:




