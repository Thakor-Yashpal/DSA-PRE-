import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from torch.optim.lr_scheduler import StepLR

# =====================
# Device
# =====================
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

# =====================
# Load Data
# =====================
df = pd.read_csv("Pytorch/data/fmnist_small.csv")

X = df.iloc[:, 1:].values / 255.0
y = df.iloc[:, 0].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# =====================
# Dataset
# =====================
class CustomDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32).view(-1, 1, 28, 28)
        self.y = torch.tensor(y, dtype=torch.long)

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

train_loader = DataLoader(CustomDataset(X_train, y_train), batch_size=32, shuffle=True)
test_loader = DataLoader(CustomDataset(X_test, y_test), batch_size=32)

# =====================
# CNN Model
# =====================
class MyNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 32, 3, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(32),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, 3, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(64),
            nn.MaxPool2d(2)
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Dropout(0.25),
            nn.Linear(64 * 7 * 7, 128),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        return self.classifier(self.features(x))

model = MyNN().to(device)

# =====================
# Training Setup
# =====================
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3, weight_decay=1e-4)
scheduler = StepLR(optimizer, step_size=10, gamma=0.5)

epochs = 50
train_accuracies, test_accuracies, losses = [], [], []

# =====================
# Training Loop
# =====================
for epoch in range(epochs):
    model.train()
    correct, total, running_loss = 0, 0, 0

    for x, y in train_loader:
        x, y = x.to(device), y.to(device)

        optimizer.zero_grad()
        outputs = model(x)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * x.size(0)
        _, preds = torch.max(outputs, 1)
        correct += (preds == y).sum().item()
        total += y.size(0)

    train_acc = correct / total
    train_loss = running_loss / total
    train_accuracies.append(train_acc)
    losses.append(train_loss)

    # ---- Test ----
    model.eval()
    correct, total = 0, 0
    with torch.no_grad():
        for x, y in test_loader:
            x, y = x.to(device), y.to(device)
            outputs = model(x)
            _, preds = torch.max(outputs, 1)
            correct += (preds == y).sum().item()
            total += y.size(0)

    test_acc = correct / total
    test_accuracies.append(test_acc)

    scheduler.step()

    print(f"Epoch [{epoch+1}/{epochs}] "
          f"Loss: {train_loss:.4f} "
          f"Train Acc: {train_acc:.4f} "
          f"Test Acc: {test_acc:.4f}")

plt.figure(figsize=(14,5))

plt.subplot(1,2,1)
plt.plot(losses)
plt.title("Training Loss")

plt.subplot(1,2,2)
plt.plot(train_accuracies, label="Train")
plt.plot(test_accuracies, label="Test")
plt.legend()
plt.title("Accuracy")

plt.show()
