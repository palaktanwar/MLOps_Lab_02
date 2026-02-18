# Docker Lab 02 - Breast Cancer Classification with KNN

## Overview
This lab demonstrates how to containerize a Machine Learning model using Docker. The project trains a K-Nearest Neighbors (KNN) classifier on the Breast Cancer dataset and saves the trained model.

## Project Structure
```
lab_02/
├── Dockerfile
├── ReadMe.md
├── output.txt
└── src/
    ├── main.py
    └── requirements.txt
```

## Files Description
| File | Description |
|------|-------------|
| `Dockerfile` | Instructions to build the Docker image |
| `src/main.py` | Python script that trains the KNN model |
| `src/requirements.txt` | Python dependencies (scikit-learn, joblib) |
| `output.txt` | Proof of successful Docker container execution |

## What the Code Does
1. Loads the Breast Cancer dataset from scikit-learn
2. Splits data into training (70%) and testing (30%) sets
3. Trains a K-Nearest Neighbors classifier (k=5)
4. Evaluates model accuracy on test data
5. Saves the trained model as `cancer_knn_model.pkl`

## How to Run

### Step 1: Build the Docker Image
```bash
docker build -t lab1:v1 .
```

### Step 2: Run the Container
```bash
docker run lab1:v1
```

### Expected Output
```
KNN model training successful! Accuracy: 92.98%
```

## Docker Concepts Used
| Concept | Description |
|---------|-------------|
| **Dockerfile** | A text file with instructions to build an image |
| **Image** | A read-only template containing the application and dependencies |
| **Container** | A running instance of an image |

## Dockerfile Explanation
```dockerfile
FROM python:3.10           # Base image with Python 3.10
WORKDIR /app               # Set working directory inside container
COPY src/ .                # Copy source code into container
RUN pip install -r requirements.txt  # Install dependencies
CMD ["python", "main.py"]  # Command to run when container starts
```
