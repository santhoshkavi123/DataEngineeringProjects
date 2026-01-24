from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator
import pandas as pd
from typing import List
import logging


import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("pyspark-ml") \
    .config() \
    .getOrCreate()


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
files = [SONGS_FILE_PATH, USERS_FILE_PATH, STREAMS_FILE_PATH]

# Check if all the required files are present or not
def file_check_task():
    file_status = {}
    for s_file in files:
        try:
            data = spark.read.csv(s_file, inferSchema = True, header = True)
            logging.info(f"SUCCESS - WHILE LOADING THE FILE")
        except Exception as e:
            logging.error(f"ERROR - WHILE LOADING THE FILE: {e}")
        else:
            file_status[s_file] =  True if data.count() > 0 else False
    
    return file_status

# Branch Task
def branch_task(ti):
    file_status_v = ti.xcom_pull(task_ids = "file_status_check")
    
    if all(file_status_v):
        return ""
    else:
        return "end_dag"

# Success Task
def success_task():
    return "success"


with DAG('DATA_CHECK_KPI_COMPUTATION', default_args = default_args, schedule = '@daily') as dag:

    # Check if all the files are present and it contains atleast one record 
    file_status_check = PythonOperator(
        task_id = "file_status_check", 
        python_callable = file_check_task
    )

    # Branch Tag checks whether to end tag or processed with computing metrics
    branch_tag = BranchPythonOperator(
        task_id = "branch_tag",
        python_callable = branch_task
    )

    end_dag = EmptyOperator(
        task_id = "end_dag"
    )

    success_tag= PythonOperator(
        task_id = "success_tag", 
        python_callable = success_task
    )

    file_status_check >> branch_tag >> [success_tag, end_dag]
    