import os
from datetime import datetime, timedelta
import csv
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook


default_args = {
	'owner': 'Jacques Sham',
	'retries': 5,
	'retry_delay': timedelta(minutes=5)
}

def save_data():
	psql_hook = PostgresHook(postgres_conn_id='postgres_airflow_docker')
	conn = psql_hook.get_conn()
	cursor = conn.cursor()
	cursor.execute("select * from public.dag_runs")
	AIRFLOW_HOME = os.getenv('AIRFLOW_HOME')
	new_filename = AIRFLOW_HOME+'/dags/log.csv'
	with open(new_filename, 'w') as f:
		csv_writer = csv.writer(f)
		csv_writer.writerow([i[0] for i in cursor.description])
		csv_writer.writerows(cursor)
	cursor.close()
	conn.close()


with DAG(
	default_args=default_args,
	dag_id='hook_postgres_v1',
	start_date=datetime(2023,7,1),
	schedule_interval='@daily'
	) as dag:
	task1 = PythonOperator(
		task_id='get_csv',
		python_callable=save_data
		)