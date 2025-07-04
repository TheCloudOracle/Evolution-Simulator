import torch
from torch import nn


class Brain(nn.Module):
    def __init__(self, input_size, hidden_units, output_size):
        super().__init__()
        layers = []
        last_size = input_size
        for size in hidden_units:
            layers.append(nn.Linear(in_features=last_size, out_features=size))
            layers.append(nn.Tanh())
            last_size = size
        layers.append(nn.Linear(in_features=last_size, out_features=output_size))
        layers.append(nn.Tanh())

        self.net = nn.Sequential(*layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)