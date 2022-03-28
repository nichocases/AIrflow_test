FROM apache/airflow:2.2.4
CMD docker-compose build && docker-compose up

