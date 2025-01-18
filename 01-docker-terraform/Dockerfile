FROM python:3.13

RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app
COPY nytaxi.py nytaxi.py

ENTRYPOINT ["python", "nytaxi.py"]