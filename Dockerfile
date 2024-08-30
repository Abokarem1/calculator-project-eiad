# Välj en basbild som har Python installerat
FROM python:3.9-slim

# Ställ in arbetskatalogen i containern
WORKDIR /app

# Kopiera requirements.txt till arbetskatalogen
COPY requirements.txt .

# Installera Python-beroenden
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera applikationsfilerna till arbetskatalogen
COPY . .

# Specificera hur applikationen ska köras när containern startas
ENTRYPOINT ["python", "calculator.py"]
