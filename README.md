# RemoteFoldSet: Benchmarking Structural Awareness of Protein Language Models

This repository provides the dataset, metrics, and analysis code for **RemoteFoldSet**.  

Read the [paper](#) (link coming soon).  


## Introduction
  - In this work, we constructed RemoteFoldSet, a dataset of proteins with high structural similarity but low sequence identity. The dataset comprising 90 protein sets of diverse folds with alternative, low-identity sequences generated via ProteinMPNN and filtered for foldability using AlphaFold3.

  - Together with the dataset, we introduced the Structural Awareness (SA) score and the SA distance ratio, a pair of new metrics to assess pLM embeddings that is model-agnostic, unsupervised, and training-free.

  - Based on these, we benchmarked widely used protein language models (pLMs), including UniRep, ProGen2, CARP, ESM, and ProtTrans.  

## Dataset generation
<img src="figs/workflow_ai4s_new.png" alt="workflow" width="1600">

To ensure that the selected starting structures were distributed across the known structural space, we sampled proteins from clusters of the [CATH dataset](https://www.cathdb.info/). As shown in the workflow, we then used [ProteinMPNN](https://github.com/dauparas/ProteinMPNN) to generate diverse alternative sequences for each selected structure, and refolded these generated sequences using [AlphaFold3](https://github.com/google-deepmind/alphafold3) to ensure that they could fold back into the originally selected structure. Finally, we performed a [`greedysearch.ipynb`](/home/zim003/mygithubrepos/RemoteFoldSet/notebooks/greedysearch.ipynb) to optimize the diversity within each retained protein sequence set.