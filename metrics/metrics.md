## Diversity

Let \( m \) be the number of generated sequences, each of length \( n \). Let \( r_{i,k} \) denote the residue at position \( k \) in the \( i \)-th sequence, where \( 1 \le i \le m \) and \( 1 \le k \le n \). We compute diversity as the average pairwise mismatch ratio between all sequence pairs:

$$
\mathrm{Diversity} = \frac{2}{m(m-1)} \sum_{1 \le i < j \le m} \frac{1}{n} \sum_{k=1}^{n} \mathbb{1}(r_{i,k} \ne r_{j,k})
$$


## SA distance ratio

For each structural set \( S_g = \{x_i\}_{i=1}^{16} \), the model \( f \) produces sequence embeddings \( z_i = f(x_i) \), which are first mean-centered to remove global bias.
Let \( G \) denote the total number of sets, and define the group mean embedding as \( \mu_g\).  
Using the distance as one minus cosine similarity, we compute the average intra- and inter-group distances, and take their ratio as the SA distance ratio:


$$
\mathrm{SA\_distance\_intra}(S) 
= \frac{2}{|S|(|S|-1)} \sum_{i<j} \Bigl( 1 - \frac{\langle z_i, z_j \rangle}{\|z_i\| \, \|z_j\|} \Bigr)
$$

$$
\mu_g = \frac{1}{|S|} \sum_{i=1}^{|S|} z_i
$$

$$
\mathrm{SA\_distance\_inter}(g) 
= \frac{1}{G-1} \sum_{h \neq g} \Bigl( 1 - \frac{\langle \mu_g, \mu_h \rangle}{\|\mu_g\| \, \|\mu_h\|} \Bigr)
$$

$$
\mathrm{SA\_distance\_ratio}(S_g) 
= \frac{\mathrm{SA\_distance\_intra}(S_g)}{\mathrm{SA\_distance\_inter}(g) + \varepsilon},
\quad \varepsilon = 10^{-12}
$$