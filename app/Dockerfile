FROM python:3.11-slim

# Small base image to reduce attack surface and startup time
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 8080

# Simple process model (one process per container)
CMD ["python", "main.py"]