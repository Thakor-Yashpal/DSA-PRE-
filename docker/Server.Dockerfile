# Multi-stage Dockerfile supporting Node.js or Python projects.
# Build Node image:   docker build -t myapp:node --target node -f app.dockerfile .
# Build Python image: docker build -t myapp:py   --target python -f app.dockerfile .

# ---------- Node stage ----------
FROM node:20-alpine AS node
WORKDIR /app

# Install npm deps only if package.json exists
COPY package*.json ./
RUN if [ -f package.json ]; then npm ci --production; fi

# Copy app sources
COPY . .

# Expose a common port; override as needed
EXPOSE 3000

# Default command (adjust to your app entrypoint)
CMD ["node", "index.js"]

# ---------- Python stage ----------
FROM python:3.11-slim AS python
WORKDIR /app

# Install pip deps only if requirements.txt exists
COPY requirements.txt ./
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Copy app sources
COPY . .

EXPOSE 8000

# Default command (adjust to your app entrypoint)
CMD ["python", "app.py"]