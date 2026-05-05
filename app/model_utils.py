
# model_utils.py

import torch.nn as nn


def encode(text, vocab):
    return [vocab.get(word.lower(), 0) for word in text.split()]


def pad(seq, max_len=10):
    return seq[:max_len] + [0] * (max_len - len(seq))


class SimpleModel(nn.Module):
    def __init__(self, vocab_size, embed_dim):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.fc = nn.Linear(embed_dim, 1)

    def forward(self, x):
        x = self.embedding(x)        # (batch, seq, embed)
        x = x.mean(dim=1)
        x = self.fc(x)               # (batch, 1)
        return x
