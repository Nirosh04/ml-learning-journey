# 🌟 ML Learning Journey -- Machine Learning, API Development & Cloud Deployment

This project documents my complete learning journey through Data
Science, Machine Learning, API development, and production-ready cloud
deployment.\
From fundamentals to a fully deployed, publicly accessible ML API.

It includes:

-   Data Science basics (NumPy, Pandas, Matplotlib)\
-   Feature engineering & model training\
-   FastAPI backend with ML model\
-   Docker deployment on Render\
-   GitHub CI/CD automation\
-   Logging, monitoring & load testing

------------------------------------------------------------------------

# 📁 Project Structure

    ML-LEARNING/
    │
    ├── .github/workflows/
    │   └── ci.yml                # GitHub Actions CI pipeline
    │
    ├── api/
    │   ├── app.py                # FastAPI ML API
    │   ├── requirements.txt      # Dependencies
    │   ├── Dockerfile            # Docker image for Render deployment
    │   ├── housing_pipeline.pkl  # Production-ready ML model
    │   └── __init__.py
    │
    ├── notebooks/
    │   ├── model_training_and_api_demo.ipynb
    │   ├── HousingAPI_Render_Test.ipynb
    │   ├── NumPy-Basics.ipynb
    │   ├── Pandas-Basics.ipynb
    │   ├── Matplotlib-Seaborn.ipynb
    │   ├── ScikitLearn.ipynb
    │   └── additional analyses
    │
    ├── tests/
    │   ├── test_api.py           # Pytest: tests live/local API
    │   └── load_test.ipynb       # Load test: 100 requests
    │
    ├── data/
    │
    ├── README.md
    └── .gitignore

------------------------------------------------------------------------

# 📚 Week 1 -- Data Basics

-   NumPy: arrays, broadcasting, mathematical operations\
-   Pandas: DataFrames, filtering, groupby, handling missing values\
-   Matplotlib & Seaborn for visualization\
-   Exploratory analysis on:
    -   sales.csv\
    -   students.csv\
    -   titanic.csv

------------------------------------------------------------------------

# 🤖 Week 2 -- Feature Engineering & Machine Learning

-   Feature scaling, OneHotEncoding\
-   Train/test split\
-   Comparison of multiple machine learning models\
-   Building a complete **Scikit-Learn pipeline**\
-   Saving the model as `housing_pipeline.pkl`\
-   Custom feature engineering (e.g., rooms_per_household)\
-   Model interpretation:
    -   Feature importance\
    -   SHAP values

------------------------------------------------------------------------

# ⚙️ Week 3 -- FastAPI ML Backend

-   Developing a REST API with FastAPI\
-   Input validation using Pydantic\
-   Loading the ML model via joblib\
-   `/predict` endpoint\
-   JSON responses\
-   Error handling (422, 500, validation errors)\
-   Testing via `requests` and notebooks\
-   Running with Uvicorn

------------------------------------------------------------------------

# 🚀 Week 4 -- CI/CD & Cloud Deployment (Render + GitHub Actions)

## CI with GitHub Actions (`ci.yml`):

-   Automatically runs tests on every push\
-   Python 3.11 setup\
-   Installing dependencies\
-   Running Pytest

## Docker Deployment on Render:

-   Created a Dockerfile\
-   Configured Render service\
-   Correct build context\
-   Enabled auto-deploy\
-   Debugged and resolved issues such as:
    -   Model not found\
    -   Wrong Dockerfile path\
    -   Gitignore exclusions

➡️ **The API is now publicly deployed**

------------------------------------------------------------------------

# 🏭 Week 5 -- Production Patterns: Logging, Monitoring & Error Handling

## Logging

-   Structured logs (timestamp, level, message)\
-   Logging events for:
    -   Incoming requests\
    -   Successful predictions\
    -   Errors (exceptions)

## Monitoring

Custom monitoring endpoint:

### `GET /metrics`

-   Total number of requests\
-   Average latency

## Healthcheck

### `GET /health`

Used by Render to verify that the API is running.

------------------------------------------------------------------------

# 🧪 Week 6 -- Load Testing (100 Requests)

Notebook: `tests/load_test.ipynb`

-   Simulates real API usage\
-   Sends 100 POST requests\
-   Measures:
    -   Latency per request\
    -   Errors\
    -   Average response time\
-   Visualizes:
    -   Latency over time (line plot)\
    -   Distribution (histogram)\
    -   Outliers (boxplot)

### Example Results

-   Average latency: \~0.12--0.20s\
-   Minimum latency: \~0.07s\
-   Maximum latency: \~0.38s\
-   0 errors (API stable)

------------------------------------------------------------------------

# 🔌 API Endpoints

### **GET /**

Returns basic API information and a list of available endpoints.

### **GET /health**

Health check (used by Render).

### **POST /predict**

Runs ML prediction.\
Input: JSON feature set\
Output: `predicted_price` + `latency_sec`

------------------------------------------------------------------------

# 🏠 Running the Project Locally

## 1. Create a Virtual Environment

``` bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scriptsctivate         # Windows
```

## 2. Install Dependencies

``` bash
pip install -r api/requirements.txt
```

## 3. Start the API

``` bash
uvicorn api.app:app --reload
```

------------------------------------------------------------------------

# 🛠 Technologies Used

-   Python 3.11\
-   NumPy, Pandas\
-   Scikit-Learn\
-   Matplotlib, Seaborn\
-   FastAPI\
-   Uvicorn\
-   Docker\
-   Render.com\
-   GitHub Actions\
-   Pytest\
-   Jupyter Notebook