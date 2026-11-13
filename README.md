# ML Engineering Journey --- Backend, APIs & Machine Learning Infrastructure

This repository documents practical experience building machine learning
systems from experimentation to deployable backend services.

The focus is on the engineering aspects around ML systems:

-   Data processing and model development
-   Backend API design with FastAPI
-   Containerised deployment
-   Automated testing and CI/CD
-   Performance evaluation and monitoring

The repository demonstrates the transition from ML experimentation
towards reliable and reproducible software systems.

## Engineering Focus

This project focuses on building software systems around machine
learning models.

Key engineering areas:

-   Designing backend services for ML inference
-   Building reproducible development environments
-   Containerising applications with Docker
-   Testing APIs automatically
-   Evaluating application performance
-   Applying software engineering practices to ML workflows

## Backend Engineering with FastAPI

The project includes a machine learning inference API built with
FastAPI.

The backend provides:

-   REST API endpoints
-   Request validation using Pydantic
-   ML model loading using joblib
-   JSON responses
-   Error handling
-   API testing

## Containerisation & Deployment

The API is containerised using Docker.

The Docker setup provides:

-   Reproducible environments
-   Dependency isolation
-   Consistent execution across systems

## Performance Testing & API Evaluation

The project includes load testing to evaluate API behaviour.

Measured metrics:

-   Request latency
-   Average response time
-   Errors
-   Performance variation

## Continuous Integration

GitHub Actions is used to automatically validate changes by:

-   Installing dependencies
-   Running automated tests
-   Checking application stability

## Deep Learning Foundations

The repository also contains practical PyTorch experiments covering:

-   Tensor operations
-   Training loops
-   Neural networks
-   CNN architectures

## Running Locally

Install dependencies:

``` bash
pip install -r api/requirements.txt
```

Start API:

``` bash
uvicorn api.app:app --reload
```

Run tests:

``` bash
pytest
```

## Technologies

### Backend & Infrastructure

-   Python
-   FastAPI
-   REST APIs
-   Docker
-   GitHub Actions
-   Pytest

### Machine Learning

-   Scikit-Learn
-   Pandas
-   NumPy
-   PyTorch
-   Torchvision

## Engineering Lessons

This project provided practical experience with:

-   Building backend services around ML models
-   Designing REST APIs
-   Containerising applications
-   Automating testing workflows
-   Measuring application performance

## Author

Nirosh

Software Engineering student interested in:

-   Backend systems
-   Data infrastructure
-   Distributed systems
-   Performance engineering
-   AI/ML infrastructure
