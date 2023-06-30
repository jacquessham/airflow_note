import os
from datetime import datetime, timedelta
import pandas as pd
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'Jacques Sham',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def load_data(ti):
    AIRFLOW_HOME = os.getenv('AIRFLOW_HOME')
    df = pd.read_csv(AIRFLOW_HOME+'/dags/salary.csv')
    candidates = df['name'].tolist()
    max_candidate = df[df['salary']==df['salary'].max()].to_dict('records')[0]
    ti.xcom_push(key='candidates',value=candidates)
    ti.xcom_push(key='max_candidate',value=max_candidate)

def print_num_candidates(ti):
    candidates = ti.xcom_pull(task_ids='load_data',key='candidates')
    print(f"We have {len(candidates)} candidates in the pool...")

def print_highest(ti):
    max_candidate = ti.xcom_pull(task_ids='load_data',key='max_candidate')
    print(f"{max_candidate['name']} has the highest salary!"
          f" Making ${max_candidate['salary']}")

def calculate_trips(ti):
    max_candidate = ti.xcom_pull(task_ids='load_data',key='max_candidate')
    dispo_salary = max_candidate['salary']*0.55
    if dispo_salary < 50000:
        num_trips = 0
    else:
        num_trips = int(dispo_salary/5000)
    print(f"{max_candidate['name']} may go to Japan up to {num_trips} times!")

with DAG(
    default_args=default_args,
    dag_id='ex1_v1',
    description='The first Airflow pipeline',
    start_date=datetime(2023,6,1),
    schedule_interval='0 13 * * Mon-Fri'
    ) as dag:
    task1 = BashOperator(
            task_id='greet',
            bash_command='echo Hello! Let us look at our candidates:'
        )
    task2 = PythonOperator(
        task_id='load_data',
        python_callable=load_data
        )
    task3 = PythonOperator(
        task_id='print_highest',
        python_callable=print_highest
        )
    task4 = PythonOperator(
        task_id='print_num_candidates',
        python_callable=print_num_candidates
        )
    task5 = PythonOperator(
        task_id='calculate_trips',
        python_callable=calculate_trips
        )
    task1 >> task2 >> [task3, task4]
    task4 >> task5
    