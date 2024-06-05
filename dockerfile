FROM python:3.11

WORKDIR /app

COPY . .

RUN pip3 install --upgrade pip

RUN pip3 install -r /requirements.txt

EXPOSE 8080/tcp

CMD ["gunicorn", "--config", "gunicorn_config.py", "main:app"]