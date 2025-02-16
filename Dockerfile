FROM python:3.10-slim

# Set environment variables to ensure Python doesn't write .pyc files and buffers stdout/stderr.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["gunicorn", "django_appstore_project.wsgi:application", "--bind", "0.0.0.0:8000"]

