import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

class EthicalModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(EthicalModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return self.sigmoid(out)

def train_model(model, X_train, y_train, epochs=100):
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    
    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(X_train)
        loss = criterion(outputs, y_train.unsqueeze(1))
        loss.backward()
        optimizer.step()
        
    return model

def predict_outcome(model, input_features):
    """
    Predicts risk score based on input features.
    """
    model.eval()
    with torch.no_grad():
        prediction = model(input_features)
    return prediction.item()
