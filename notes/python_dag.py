from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
	'owner': 'Jacques Sham',
	'retries': 5,
	'retry_delay': timedelta(minutes=5)
}

def greet(name, age):
	print(f"Hello World! My name is {name} and I am {age} years old")

with DAG(
	default_args=default_args,
	dag_id='1st_python_dag_v2',
	description='The first Python DAG using PythonOperator',
	start_date=datetime(2023,6,28),
	schedule_interval='@daily'
	) as dag:
	task1 = PythonOperator(
			task_id='greet',
			python_callable=greet,
			op_kwargs={'name':'Jacques', 'age': 21}
		)
	task1