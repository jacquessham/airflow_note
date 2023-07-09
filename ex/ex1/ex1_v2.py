import os
from datetime import datetime, timedelta
import pandas as pd
from airflow.decorators import dag, task


default_args = {
    'owner': 'Jacques Sham',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

@dag(dag_id='ex1_v2',
    default_args=default_args,
    start_date=datetime(2023,6,1),
    schedule_interval='0 13 * * Mon-Fri'
    )
def candidate_etl():
    @task()
    def greet():
        print(f"Hello! Let us look at our candidates:")
    @task(multiple_outputs=True)

    def load_data():
        AIRFLOW_HOME = os.getenv('AIRFLOW_HOME')
        df = pd.read_csv(AIRFLOW_HOME+'/dags/salary.csv')
        candidates = df['name'].tolist()
        max_candidate = df[df['salary']==df['salary'].max()].to_dict('records')[0]
        return {
            'candidates': candidates,
            'max_candidate': max_candidate
        }
    @task()
    def print_num_candidates(candidates):
        print(f"We have {len(candidates)} candidates in the pool...")
    @task()
    def print_highest(max_candidate):
        print(f"{max_candidate['name']} has the highest salary!"
              f" Making ${max_candidate['salary']}")
    @task()
    def calculate_trips(max_candidate):
        dispo_salary = max_candidate['salary']*0.55
        if dispo_salary < 50000:
            num_trips = 0
        else:
            num_trips = int(dispo_salary/5000)
        print(f"{max_candidate['name']} may go to Japan up to {num_trips}"
              f" times!")
    greet()
    candidates_results = load_data()
    print_num_candidates(candidates_results['candidates'])
    print_highest(candidates_results['max_candidate'])
    calculate_trips(candidates_results['max_candidate'])

ex1_dag = candidate_etl()

