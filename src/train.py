from src.model import NeuralNet
from src.data_loader import load_data
import torch

# Load Data
train_loader, test_loader = load_data()

# Initialize Model
model = NeuralNet()

# Training Loop
for epoch in range(5):  # Train for 5 epochs
    for images, labels in train_loader:
        # Your training logic here
        pass
    print(f"Epoch {epoch+1} completed.")

print("Training Done!")
