import pandas as pd
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import optuna

device = "cuda" if torch.cuda.is_available() else "cpu"

df = pd.read_csv('Pytorch\data\fmnist_small.csv')

fig,axes = plt.subplots(2,5, figsize=(12,5))
for i, ax in enumerate(axes.flatten()):
    img = df.iloc[i,1:].values.reshape(28,28)
    ax.imshow(img, cmap='gray')
    ax.set_title(f"Label: {df.iloc[i,0]}")
    ax.axis('off')
    
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

X = df.iloc[:, 1:].values
y = df.iloc[:, 0].values

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Normalize
X_train = X_train / 255.0
X_test = X_test / 255.0


class custom_dataset(Dataset):
    def __init(Self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.long)
        
    def __len__(self):
        
        return len(self.y)
    
    def __getitem__(self, index):
        
        return self.X[index], self.y[index]
    
train_dataset = custom_dataset(X_train, y_train)
test_dataset = custom_dataset(X_test, y_test)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)


class ANN_Model(nn.Module): #this our model
    def __init__(self, input_dim, output_dim, num_hidden_layers, neurons_per_layer, dropout_rate):
        super(ANN_Model, self).__init__()
        
        layers = []
        
        layers.append(nn.Linear(input_dim, neurons_per_layer))
        layers.append(nn.batchnorm1d(neurons_per_layer))
        layers.append(nn.ReLU())
        layers.append(nn.Dropout(dropout_rate))
        input_dim = neurons_per_layer
        
        layers.append(nn.Linear(input_dim, output_dim))
        
        self.model = nn.Sequential(*layers)
        
    def forward(self, x):
        return self.model(x)

model = ANN_Model(input_dim=784, 
                  output_dim=10, 
                  num_hidden_layers=1, 
                  neurons_per_layer=128, 
                  dropout_rate=0.2)
model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
num_epochs = 20


train_losses = []
test_losses = []

for epoch in range(num_epochs):
    model.train()
    running_train_loss = 0.0

    for inputs, labels in train_loader:
        inputs, labels = inputs.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_train_loss += loss.item() * inputs.size(0)

    train_loss = running_train_loss / len(train_loader.dataset)
    train_losses.append(train_loss)

    model.eval()
    running_test_loss = 0.0

    with torch.no_grad():
        for inputs, labels in test_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            running_test_loss += loss.item() * inputs.size(0)

    test_loss = running_test_loss / len(test_loader.dataset)
    test_losses.append(test_loss)

    print(
        f"Epoch [{epoch+1}/{num_epochs}] "
        f"Train Loss: {train_loss:.4f} | Test Loss: {test_loss:.4f}"
    )

# Loss Curves
plt.figure(figsize=(8, 5))
plt.plot(train_losses, label="Train Loss")
plt.plot(test_losses, label="Test Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training vs Validation Loss")
plt.legend()
plt.show()