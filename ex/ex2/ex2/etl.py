def get_pwd():
	return os.getenv('AIRFLOW_HOME')

def declare_conn():
	psql_hook = PostgresHook(postgres_conn_id='postgres_airflow_docker')
	conn = psql_hook.get_conn()
	cursor = conn.cursor()
	return conn, cursor

def close_conn(conn):
	conn.close()

def etl():
	df_salary = pd.read_csv(get_pwd()+'/salary.csv')
	df_salary['tran_id'] = range(1,df_salary.shape[0]+1) 
	df_salary['person_id'] = range(1,df_salary.shape[0]+1) 

	df_person = df_salary[['person_id','name','school','major']]
	df_salary = df_salary[['tran_id','person_id','salary']]

	conn, cursor = declare_conn

	for i, row in df_person.iterrows():
		cursor.execute()

	for i, row in df_salary.iterrows():
		cursor.execute()

	close_conn(conn)