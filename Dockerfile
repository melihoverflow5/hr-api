# syntax=docker/dockerfile:1.4
FROM python:3.9.16-buster

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app
RUN target=/root/.cache/pip \
    pip3 install -r requirements.txt
# RUN pip install --index-url https://pypi.python.org/simple --upgrade pip
# RUN pip install --index-url https://pypi.python.org/simple -r requirements.txt
COPY . /app
EXPOSE 5000
EXPOSE 8000
CMD ["gunicorn", "-c", "/app/gunicorn.py", "run:app"]
