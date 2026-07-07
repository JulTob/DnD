     # syntax=docker/dockerfile:1
     FROM python:3.11-slim

     ENV PYTHONUNBUFFERED=1 \
         PIP_NO_CACHE_DIR=1

     WORKDIR /app
     COPY requirements.txt .
     RUN pip install --no-deps -r requirements.txt

     COPY . .
     ENV PORT=8080
     EXPOSE 8080

     CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
