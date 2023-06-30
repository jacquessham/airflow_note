from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
	'owner': 'Jacques Sham',
	'retries': 5,
	'retry_delay': timedelta(minutes=2)
}

with DAG(
	dag_id='cron_dag_v2',
	default_args = default_args,
	start_date=datetime(2023,6,15),
	schedule_interval='0 4 * * *'
	) as dag:
	task1 = BashOperator(
		task_id='task1',
		bash_command="echo dag with cron expression!"
		)
	task1