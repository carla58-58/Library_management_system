# Dockerfile for Django app (production)
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app


# Copy requirements.txt first, then the rest of the app
COPY pythonProject1/requirements.txt /app/
COPY pythonProject1/ /app/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Collect static files (will be used with S3 in production)
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]
