 # GPT Language Model

This repo contains PyTorch code to implement a GPT language model from scratch using Python. 

## Model Overview

This implementation includes:

- CUDA implementation
- Token and position embeddings
- Multi-head self attention layers
- Feedforward layers  (LM, ReLU, LM)
- Layer normalization (Post-Norm)
- Residual connections (MA, KQP)
- Language modeling head

The model is trained to predict the next token (character) in a sequence, using a cross-entropy loss function.

## Introduction

The main model code is contained in `gpt-v1.ipynb`. To train the model:

1. Specify hyperparameters like number of layers, heads, embedding size etc.(Depends on GPU)
2. Load and preprocess text data
3. Instantiate GPT model
4. Define dataloaders, optimizer and training loop 
5. Train model and monitor loss

The trained model can be used to generate text by sampling tokens autoregressively.

## Requirements

- Python 3.x 
- PyTorch
- cuda (Graphics Required)
- numpy
- jupyter notebook 

## References

The GPT model architecture is based on the original Paper, Analysis of Large Language Models and FreeCodeCamp
