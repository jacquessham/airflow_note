from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
	'owner': 'Jacques Sham',
	'retries': 5,
	'retry_delay': timedelta(minutes=2)
}

with DAG(
	dag_id='first_dag_v3',
	description='This is the first DAG',
	default_args = default_args,
	start_date=datetime(2023,6,28,23,15),
	schedule_interval='@daily'

) as dag:
	task1 = BashOperator(
		task_id='first_task',
		bash_command='echo Hello World!'
		)
	task2 = BashOperator(
		task_id='second_task',
		bash_command='echo I am executing Task 2 after saying hello!'
		)
	task3 = BashOperator(
		task_id='third_task',
		bash_command='echo I have said hello world...'
		)
	task1.set_downstream(task2)
	task1 >> task3