FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY . .

#CMD ["python", "api/main.py"]
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "api.main:app"]

