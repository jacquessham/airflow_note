from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator


default_args = {
	'owner': 'Jacques Sham',
	'retries': 5,
	'retry_delay': timedelta(minutes=2)
}

with DAG(
	dag_id='connect_psql_v3',
	default_args = default_args,
	start_date=datetime(2023,7,1),
	schedule_interval='0 4 * * *'
	) as dag:
	task1 = PostgresOperator(
		task_id='create_postgres_table',
		postgres_conn_id='postgres_airflow_docker',
		sql="""
			create table if not exists dag_runs(
				dt date,
				dag_id varchar(512),
				primary key (dt, dag_id)
			)
		"""
		)
	task2 = PostgresOperator(
		task_id='delete_from_table',
		postgres_conn_id='postgres_airflow_docker',
		sql="""
			delete from dag_runs 
			where dt = '{{ ds }}' and
				dag_id = '{{dag.dag_id}}'
		"""
		)
	task3 = PostgresOperator(
		task_id='insert_into_table',
		postgres_conn_id='postgres_airflow_docker',
		sql="""
			insert into dag_runs (dt, dag_id) values ('{{ ds }}', '{{ dag.dag_id}}')
		"""
		)
	
	task1 >> task2 >> task3