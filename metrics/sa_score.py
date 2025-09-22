import numpy as np
from itertools import combinations

def cosine_similarity(u, v):
    u = np.asarray(u)
    v = np.asarray(v)
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

def group_homogeneity(embedding_list, group_size=16):
    embedding_array = np.array(embedding_list)
    num_full_groups = len(embedding_array) // group_size
    homogeneity_scores = []
    
    for i in range(num_full_groups):
        group = embedding_array[i * group_size : (i + 1) * group_size]
        sims = []
        for u_idx, v_idx in combinations(range(group_size), 2):
            u = group[u_idx]
            v = group[v_idx]
            sim = cosine_similarity(u, v)
            sims.append(sim)
        avg_sim = np.mean(sims)
        homogeneity_scores.append(avg_sim)
    
    return homogeneity_scores