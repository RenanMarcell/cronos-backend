FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . .
RUN chmod +x wait-for
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get -q update && apt-get -qy install netcat

EXPOSE 8000
