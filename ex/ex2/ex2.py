import os
from datetime import datetime, timedelta
import csv
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from ex2.etl import *


default_args = {
	'owner': 'Jacques Sham',
	'retries': 5,
	'retry_delay': timedelta(minutes=5)
}


with DAG(
	default_args=default_args,
	dag_id='ex1_v1',
	start_date=datetime(2023,7,1),
	schedule_interval='0 4 * * Mon-Fri'
	) as dag:
	task1 = PostgresOperator(
		task_id='create_table',
		postgres_conn_id='postgres_airflow_docker',
		sql=get_pwd()+'/ex2/create_salarytable.sql'
		)
	task2 = PythonOperator(
		task_id='etl',
		python_callable=etl
		)
	task3 = PostgresOperator(
		task_id='update_log',
		postgres_conn_id='postgres_airflow_docker',
		sql="""
			insert into dag_runs (dt, dag_id) values ('{{ ds }}', '{{ dag.dag_id}}')
		"""
		)

	task1 >> task2 >> task3
