FROM python:3.12-slim

WORKDIR /app

# Optional, aber empfohlen: pip aktualisieren
RUN pip install --upgrade pip

# Anforderungen direkt installieren (schneller & sicher)
RUN pip install fastapi uvicorn[standard] pandas joblib scikit-learn

# Rest des Codes kopieren
COPY . .

# Startbefehl
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

