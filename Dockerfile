FROM python:3.11.3-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir gunicorn==20.1.0

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir /db
RUN mkdir /static

WORKDIR /usr/src/app
COPY src/. .

RUN ./manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "conf.wsgi:application", "--bind", "0.0.0.0:8000"]
