# 🌟 **ML Learning Journey – Machine Learning, API Development & Cloud Deployment**
Dieses Projekt dokumentiert meine komplette Lernreise durch Data Science, Machine Learning, API-Entwicklung und produktionsreifes Deployment.  
Von den Grundlagen bis zur öffentlich erreichbaren ML-API in der Cloud.

Es umfasst:

- Data Science Basics (NumPy, Pandas, Matplotlib)  
- Feature Engineering & Modelltraining  
- FastAPI-Backend mit ML-Modell  
- Docker Deployment auf Render  
- GitHub CI/CD Automation  
- Logging, Monitoring & Load Testing  

---

# 📁 **Projektstruktur**

```
ML-LEARNING/
│
├── .github/workflows/
│   └── ci.yml                # GitHub Actions CI-Pipeline
│
├── api/
│   ├── app.py                # FastAPI ML API
│   ├── requirements.txt      # Dependencies
│   ├── Dockerfile            # Docker Image für Render Dep
│   ├── housing_pipeline.pkl  # Produktionsmodell (Scikit-Learn)
│   └── __init__.py
│
├── notebooks/
│   ├── model_training_and_api_demo.ipynb
│   ├── HousingAPI_Render_Test.ipynb
│   ├── NumPy-Basics.ipynb
│   ├── Pandas-Basics.ipynb
│   ├── Matplotlib-Seaborn.ipynb
│   ├── ScikitLearn.ipynb
│   └── weitere Analysen
│
├── tests/
│   ├── test_api.py           # Pytest: Testet Live-/Local API
│   └── load_test.ipynb       # Load Test: 100 Requests
│
├── data/
│
├── README.md
└── .gitignore
```

---

# 📚 **Woche 1 – Data Basics**

- NumPy: Arrays, Broadcasting, mathematische Operationen  
- Pandas: DataFrames, Filtering, GroupBy, Missing Values  
- Matplotlib & Seaborn  
- Explorative Analysen mit:
  - Sales.csv  
  - Students.csv  
  - Titanic.csv

---

# 🤖 **Woche 2 – Feature Engineering & Machine Learning**

- Feature Scaling, OneHotEncoding  
- Train/Test Split  
- Vergleich mehrerer ML-Modelle  
- Erstellung einer kompletten **Scikit-Learn Pipeline**  
- Modell gespeichert als `housing_pipeline.pkl`  
- Feature Engineering (z. B. rooms_per_household)  
- Modellinterpretation:
  - Feature Importance
  - SHAP Values

---

# ⚙️ **Woche 3 – FastAPI ML Backend**

- Aufbau einer REST API mit FastAPI  
- Pydantic für Input Validation  
- Laden des ML-Modells via joblib  
- Endpoint `/predict`  
- Rückgabe als JSON  
- Error Handling (422, 500, Validierungsfehler)  
- Testing über `requests` & Notebooks  
- Starten mit Uvicorn

---

# 🚀 **Woche 4 – CI/CD & Cloud Deployment (Render + GitHub Actions)**

### **CI mit GitHub Actions (`ci.yml`):**

- Automatisches Ausführen von Tests bei jedem Push  
- Python 3.11 Setup  
- Dependencies installieren  
- Pytest ausführen  

### **Docker Deployment auf Render:**

- Dockerfile erstellt  
- Render Service eingerichtet  
- Build Context richtig gesetzt  
- Auto-Deploy aktiviert  
- Fehler analysiert und gelöst:  
  - Model not found  
  - Dockerfile Path  
  - Gitignore Regeln  

➡️ **API jetzt öffentlich verfügbar**

---

# 🏭 **Woche 5 – Production Patterns: Logging, Monitoring, Fehlerhandling**

### Logging
- Strukturierte Logs (Zeit, Level, Nachricht)  
- Logging bei:
  - Request-Eingang  
  - Erfolgreichen Vorhersagen  
  - Fehlern (Exceptions)

### Monitoring
Ein eigener Monitoring-Endpoint:

**`GET /metrics`**
- Anzahl Requests  
- Durchschnittliche Latenz  

### Healthcheck
**`GET /health`**  
Wird von Render genutzt, um sicherzustellen, dass die API läuft.

---

# 🧪 **Woche 6 – Load Testing (100 Requests)**

Notebook: `tests/load_test.ipynb`

- Simuliert echte Nutzung der API  
- Sendet 100 POST-Requests  
- Misst:
  - Latenz pro Request  
  - Fehler  
  - Durchschnittliche Antwortzeit  
- Visualisiert:
  - Latenzverlauf (Line Plot)
  - Verteilung (Histogramm)
  - Ausreißer via Boxplot  

**Beispielwerte:**
- Durchschnittliche Latenz: ~0.12–0.20s  
- Minimale Latenz: ~0.07s  
- Maximale Latenz: ~0.38s  
- 0 Fehler (API stabil)

---

# 🔌 **API Endpoints**

### **GET /**  
Infos über API + verfügbare Endpoints

### **GET /health**  
Health Check (für Render)

### **POST /predict**  
ML-Vorhersage  
Input: JSON Feature-Set  
Output: predicted_price + latency_sec

---

# 🏠 **Projekt lokal starten**

### 1. Virtual Environment erstellen

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 2. Dependencies installieren
```bash
pip install -r api/requirements.txt
```

### 3. API starten
```bash
uvicorn api.app:app --reload
```

---

# 🛠 **Technologien**

- Python 3.11  
- NumPy, Pandas  
- Scikit-Learn  
- Matplotlib, Seaborn  
- FastAPI  
- Uvicorn  
- Docker  
- Render.com  
- GitHub Actions  
- Pytest  
- Jupyter Notebook  

---
