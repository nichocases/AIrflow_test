#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from google_drive_operator import GoogleDriveOperator

dag = DAG(
    dag_id='upload_to_drive',
    description='Create spare parts analysis sheet in Google Drive',
    schedule_interval='@daily',
    start_date=datetime(2022, 4, 19),
    end_date=datetime(2022, 12, 31)
)

create_file = BashOperator(
    task_id='create_file',
    bash_command=(
        'echo file created on {{ ds }}. > '
        '${AIRFLOW_HOME}/tmp/my_file_{{ ds }}.txt'
    ),
    dag=dag
)

upload_file = GoogleDriveOperator(
    task_id='upload_file',
    local_path='tmp/prueba_drive.txt',
    drive_folder='google-drive-operator',
    gcp_conn_id='airflow-to-drive',
    delegate_to='ing.nicaes@gmail.com',
    dag=dag
)

upload_file
