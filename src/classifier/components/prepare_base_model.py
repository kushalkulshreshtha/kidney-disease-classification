import os
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
from classifier.entity.config_entity import BaseModelConfig

class PrepareBaseModel:
    def __init__(self, config: BaseModelConfig):
        self.config = config

    def get_base_model(self):
        model = models.resnet18(weights=self.config.params_weight)
        optimizer = torch.optim.Adam(model.parameters(), lr = self.config.params_learning_rate)
        for param in model.parameters():
            param.requires_grad = False
        num_ftrs = model.fc.in_features
        # Here the size of each output sample is set to 2.
        model.fc = nn.Linear(num_ftrs, 2)
        self.model = model
        self.optimizer = optimizer

        self.save_model()


    def save_model(self):
        # create_directories([self.config.base_model_path])
        torch.save({
            'epoch': 0,
            'model_state_dict': self.model.state_dict(),
            'optimizer_state_dict': self.optimizer.state_dict()

            }, self.config.base_model_path)