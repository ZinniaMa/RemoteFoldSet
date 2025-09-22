import numpy as np

def cosine_similarity(u, v):
    u = np.asarray(u)
    v = np.asarray(v)
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

def group_distance_ratio(embedding_list, group_size=16):
    embedding_array = np.array(embedding_list)
    num_full_groups = len(embedding_array) // group_size
    scores = []

    # group-level mean embeddings
    group_embeddings = []
    for i in range(num_full_groups):
        group = embedding_array[i*group_size:(i+1)*group_size]
        group_embeddings.append(group.mean(axis=0))
    group_embeddings = np.array(group_embeddings)

    for i in range(num_full_groups):
        # within-group distance
        group = embedding_array[i*group_size:(i+1)*group_size]
        within_dists = [
            1 - cosine_similarity(group[u], group[v])
            for u in range(group_size) for v in range(u+1, group_size)
        ]
        avg_within_dist = np.mean(within_dists)

        # between-group distance
        target = group_embeddings[i]
        other_embs = np.delete(group_embeddings, i, axis=0)
        between_dists = [1 - cosine_similarity(target, other) for other in other_embs]
        avg_between_dist = np.mean(between_dists)

        ratio = avg_within_dist / (avg_between_dist + 1e-12)
        scores.append(ratio)

    return scores