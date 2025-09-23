## Diversity

Let \( m \) be the number of generated sequences, each of length \( n \). Let \( r_{i,k} \) denote the residue at position \( k \) in the \( i \)-th sequence, where \( 1 \le i \le m \) and \( 1 \le k \le n \). We compute diversity as the average pairwise mismatch ratio between all sequence pairs:

$$
\mathrm{Diversity} = \frac{2}{m(m-1)} \sum_{1 \le i < j \le m} \frac{1}{n} \sum_{k=1}^{n} \mathbbm{1}(r_{i,k} \ne r_{j,k})
$$