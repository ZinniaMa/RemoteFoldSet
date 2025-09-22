# RemoteFoldSet: Benchmarking Structural Awareness of Protein Language Models

This repository provides the dataset, metrics, and analysis code for **RemoteFoldSet**.  

Read the [paper](#) (link coming soon).  


## Introduction
  - In this work, we constructed RemoteFoldSet, a dataset of proteins with high structural similarity but low sequence identity. The dataset comprising 90 protein sets of diverse folds with alternative, low-identity sequences generated via ProteinMPNN and filtered for foldability using AlphaFold3.

  - Together with the dataset, we introduced the Structural Awareness (SA) score and the SA distance ratio, a pair of new metrics to assess pLM embeddings that is model-agnostic, unsupervised, and training-free.

  - Based on these, we benchmarked widely used pLMs, including UniRep, ProGen2, CARP, ESM, and ProtTrans.  
