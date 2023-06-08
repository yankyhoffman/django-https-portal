FROM python:3.11.3-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir /db
RUN mkdir /static

WORKDIR /usr/src/app
COPY src/. .

EXPOSE 8000

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
