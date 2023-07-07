import os
import pandas as pd
from airflow.providers.postgres.hooks.postgres import PostgresHook


def get_pwd():
    return os.getenv('AIRFLOW_HOME')+'/dags'

def declare_conn():
    psql_hook = PostgresHook(postgres_conn_id='postgres_airflow_docker')
    conn = psql_hook.get_conn()
    cursor = conn.cursor()
    return conn, cursor

def close_conn(conn):
    conn.close()

def getstr_insert_into(table, row):
    if table == 'df_person':
        query = (f"insert into ex2.person"
                f"(person_id, name, school, major) "
                f"values ({row['person_id']}, '{row['name']}', "
                f"'{row['school']}', '{row['major']}');")
    elif table == 'df_salary':
        query = (
            f"insert into ex2.salary"
            f"(tran_id, person_id, salary)"
            f"values ({row['tran_id']}, {row['person_id']},"
            f"{row['salary']})"
        )
    else:
        query = ''
    print(query)
    return query

def etl():
    pwd = os.getenv('AIRFLOW_HOME')
    df_salary = pd.read_csv(pwd+'/dags/salary.csv')
    df_salary['tran_id'] = range(1,df_salary.shape[0]+1) 
    df_salary['person_id'] = range(1,df_salary.shape[0]+1) 

    df_person = df_salary[['person_id','name','school','major']]
    df_salary = df_salary[['tran_id','person_id','salary']]

    conn, cursor = declare_conn()

    # Delete all records before insert due to duplicated PK
    # Since we never declare IDs dynamically
    cursor.execute('delete from ex2.person')
    for i, row in df_person.iterrows():
        cursor.execute(getstr_insert_into('df_person', row))

    # Delete all records before insert due to duplicated PK
    # Since we never declare IDs dynamically
    cursor.execute('delete from ex2.salary')
    for i, row in df_salary.iterrows():
        cursor.execute(getstr_insert_into('df_salary', row))

    close_conn(conn)
