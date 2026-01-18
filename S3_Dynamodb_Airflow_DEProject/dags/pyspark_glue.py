from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator, BashOperator
from airlfow.operators.empty import EmptyOperator
import pandas as pd
import logging

default_args = {
    'owner' : 'sans', 
    'depends_on_past' : False, 
    'start_date' : datetime(2026, 1, 18),
    'email_on_failure' : False, 
    'email_on_retry' : False, 
    'retries' : 1, 
    'retry_delay' : timedelta(minutes = 5)
}

SONGS_FILE_PATH = "/opt/airflow/data/songs.csv"
USERS_FILE_PATH = "/opt/airflow/data/users.csv"
STREAMS_FILE_PATH = "/opt/airflow/data/streams/"

def file_check():
    try:
        pass
    except Exception as e:
        pass


    
with DAG('DATA_CHECK_KPI_COMPUTATION', default_args = default_args, schedule = '@daily') as dag:


