import os
import sys
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator


def get_curr_pwd():
	return os.getenv('AIRFLOW_HOME')

sys.path.insert(0,get_curr_pwd()+"/dags/ex2")
from etl import *

default_args = {
	'owner': 'Jacques Sham',
	'retries': 5,
	'retry_delay': timedelta(minutes=5)
}

sql_query_dir = 'ex2/create_salarytable.sql'

with DAG(
	default_args=default_args,
	dag_id='ex2_v1',
	start_date=datetime(2023,7,1),
	schedule_interval='0 4 * * Mon-Fri'
	) as dag:
	task1 = PostgresOperator(
		task_id='create_table',
		postgres_conn_id='postgres_airflow_docker',
		sql=sql_query_dir
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
