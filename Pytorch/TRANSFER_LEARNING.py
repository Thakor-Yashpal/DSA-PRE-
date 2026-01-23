import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import torchvision.transforms as T
import torchvision.models as models

device = "cuda" if torch.cuda.is_available() else "cpu"

df = pd.read_csv("Pytorch/data/fmnist_small.csv")

X = df.iloc[:, 1:].values
y = df.iloc[:, 0].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

train_transform = T.Compose([
    T.ToPILImage(),
    T.Resize((224, 224)),
    T.RandomHorizontalFlip(),
    T.ToTensor(),
    T.Lambda(lambda x: x.repeat(3, 1, 1)),  # 1 → 3 channels
    T.Normalize(mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225])
])

test_transform = T.Compose([
    T.ToPILImage(),
    T.Resize((224, 224)),
    T.ToTensor(),
    T.Lambda(lambda x: x.repeat(3, 1, 1)),
    T.Normalize(mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225])
])

class FMNISTDataset(Dataset):
    def __init__(self, X, y, transform=None):
        self.X = X
        self.y = y
        self.transform = transform

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        img = self.X[idx].reshape(28, 28).astype("uint8")
        label = self.y[idx]

        if self.transform:
            img = self.transform(img)

        return img, label

train_loader = DataLoader(
    FMNISTDataset(X_train, y_train, train_transform),
    batch_size=32,
    shuffle=True
)

test_loader = DataLoader(
    FMNISTDataset(X_test, y_test, test_transform),
    batch_size=32,
    shuffle=False
)

model = models.resnet18(pretrained=True)

# Freeze backbone
for param in model.parameters():
    param.requires_grad = False

# Replace classifier
model.fc = nn.Linear(model.fc.in_features, 10)

model = model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.fc.parameters(), lr=1e-3)
epochs = 15

train_losses = []
train_accuracies = []
test_accuracies = []

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

for epoch in range(epochs):
    model.train()
    correct, total, loss_sum = 0, 0, 0

    for x, y in train_loader:
        x, y = x.to(device), y.to(device)

        optimizer.zero_grad()
        outputs = model(x)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()

        loss_sum += loss.item() * x.size(0)
        _, preds = torch.max(outputs, 1)
        correct += (preds == y).sum().item()
        total += y.size(0)

    train_loss = loss_sum / total
    train_acc = correct / total

    # NEW
    train_losses.append(train_loss)
    train_accuracies.append(train_acc)

    # -------- Validation --------
    model.eval()
    correct, total = 0, 0
    all_preds = []
    all_labels = []

    with torch.no_grad():
        for x, y in test_loader:
            x, y = x.to(device), y.to(device)
            outputs = model(x)
            _, preds = torch.max(outputs, 1)

            correct += (preds == y).sum().item()
            total += y.size(0)

            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(y.cpu().numpy())

    test_acc = correct / total
    test_accuracies.append(test_acc)

    print(
        f"Epoch [{epoch+1}/{epochs}] "
        f"Loss: {train_loss:.4f} "
        f"Train Acc: {train_acc:.4f} "
        f"Test Acc: {test_acc:.4f}"
    )

plt.figure(figsize=(14, 5))

# ---- Loss ----
plt.subplot(1, 2, 1)
plt.plot(train_losses, marker="o")
plt.title("Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)

# ---- Accuracy ----
plt.subplot(1, 2, 2)
plt.plot(train_accuracies, label="Train Accuracy", marker="o")
plt.plot(test_accuracies, label="Test Accuracy", marker="x")
plt.title("Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Confusion Matrix (Matplotlib)

cm = confusion_matrix(all_labels, all_preds)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=[str(i) for i in range(10)]
)

plt.figure(figsize=(8, 8))
disp.plot(cmap="Blues", values_format="d")
plt.title("Confusion Matrix")
plt.show()
