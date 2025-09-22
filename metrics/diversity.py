import numpy as np

def compute_diversity(sampled_seqs):
    diversity = []
    for a in range(len(sampled_seqs)):
        for b in range(a + 1, len(sampled_seqs)):
            seq1 = sampled_seqs[a]
            seq2 = sampled_seqs[b]
            different = 0
            identical = 0
            for i in range(len(seq1)):
                aa = seq1[i]
                if aa != 'X':
                    if seq1[i] == seq2[i]:
                        identical += 1
                    else:
                        different += 1
            diversity.append(different / (identical + different))
    diversity = np.mean(diversity)
    return diversity