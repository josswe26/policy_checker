FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . /app

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
