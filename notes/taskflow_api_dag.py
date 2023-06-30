from datetime import datetime, timedelta
from airflow.decorators import dag, task


default_args = {
	'owner': 'Jacques Sham',
	'retries': 5,
	'retry_delay': timedelta(minutes=5)
}

@dag(dag_id='dag_with_taskflow_api_v01',
	default_args=default_args,
	start_date=datetime(2023,6,28),
	schedule_interval='@daily'
	)
def hello_world_etl():
	@task(multiple_outputs=True)
	def get_name():
		return {
			'first_name':'Rodney',
			'last_name':'Wong'
		}
	@task()
	def get_age():
		return 21
	@task()
	def greet(first_name, last_name, age):
		print(f"Hello World! My name is {first_name} {last_name}" 
			  f" and I am {age} years old!")
	name = get_name()
	age = get_age()
	greet(first_name=name['first_name'], last_name=name['last_name'], age=age)

greet_dag = hello_world_etl()