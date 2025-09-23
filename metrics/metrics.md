## Diversity

Let \( m \) be the number of generated sequences, each of length \( n \). Let \( r_{i,k} \) denote the residue at position \( k \) in the \( i \)-th sequence, where \( 1 \le i \le m \) and \( 1 \le k \le n \). We compute diversity as the average pairwise mismatch ratio between all sequence pairs:

```

Diversity = (2 / (m(m - 1))) \* sum\_{1 ≤ i < j ≤ m} (1 / n) \* sum\_{k = 1}^{n} 𝟙(r\_{i,k} ≠ r\_{j,k})

```

---

## SA score

For each structural set \( S_g = \{x_i\}_{i=1}^{16} \), the model \( f \) produces sequence embeddings \( z_i = f(x_i) \), which are first mean-centered to remove global bias.  
After mean-centering, we compute the pairwise cosine similarities and take their average as the SA score for that set:

```

SA(S) = (2 / (|S|(|S| - 1))) \* sum\_{i < j} ( ⟨z\_i, z\_j⟩ / (‖z\_i‖‖z\_j‖) )

```

---

## SA distance ratio

Let \( G \) denote the total number of sets, and define the group mean embedding as \( \mu_g \).  
Using the distance as one minus cosine similarity, we compute the average intra- and inter-group distances, and take their ratio as the SA distance ratio:

**Intra-group distance**
```

SA\_distance\_intra(S) = (2 / (|S|(|S| - 1))) \* sum\_{i < j} (1 - ⟨z\_i, z\_j⟩ / (‖z\_i‖‖z\_j‖))

```

**Group mean**
```

μ\_g = (1 / |S|) \* sum\_{i = 1}^{|S|} z\_i

```

**Inter-group distance**
```

SA\_distance\_inter(g) = (1 / (G - 1)) \* sum\_{h ≠ g} (1 - ⟨μ\_g, μ\_h⟩ / (‖μ\_g‖‖μ\_h‖))

```

**Final ratio**
```

SA\_distance\_ratio(S\_g) = SA\_distance\_intra(S\_g) / (SA\_distance\_inter(g) + ε)
ε = 10^{-12}

```
```
