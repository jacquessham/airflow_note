from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.amazon.aws.sensor.s3_key import S3KeySensor


default_args = {
	'owner': 'Jacques Sham',
	'retries': 5,
	'retry_delay': timedelta(minutes=2)
}

with DAG(
	dag_id='connect_s3_sensor_v1',
	default_args = default_args,
	start_date=datetime(2023,7,1),
	schedule_interval='0 4 * * *'
	) as dag:
	task1 = S3KeySensor(
		task_id='sensor_minio_s3',
		bucket_name='airflow',
		bucket_key='data.csv', # The file you want to load
		aws_conn_id='minio_s3_airflow',
		mode='poke',
		poke_interval=5
		)
	task1