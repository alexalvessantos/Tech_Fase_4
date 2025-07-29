FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Comando correto para iniciar com gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "api.main:app"]
