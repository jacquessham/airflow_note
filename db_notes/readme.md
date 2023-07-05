# Notes on the Database Connections

## Connections
### Relational Databases
We will connect Postgres database via Docker, port at 3489 as stated in the Yaml file in the <a href="https://github.com/jacquessham/airflow_notes/tree/main/setup">Setup</a> folder. Before getting into the script, spin the database running first, connect with your SQL Client, and Aiflow. You may go to the homepage of Airflow -> Admin -> Connection, and click on the + sign to add new database connection. Fill in all the login info and credentials. 
<br><br>
If your Docker is running via Docker, the host should be <b>host.docker.internal</b> if your OS is MacOS, whereas it is fine to fill in <i>localhost</i> if it is not running via Docker.
<br><br>
An example of a operator that execute SQL code with Airflow Macro:

```
task_id='insert_into_table',
		postgres_conn_id='postgres_airflow_docker',
		sql="""
			insert into dag_runs (dt, dag_id) values ('{{ ds }}', '{{ dag.dag_id}}')
		"""
```
<br><br>
You may find <i>connect_postgres.py</i> to find the sample code.
<br><br>
Alternatively, you may use a Postgres Hook to execute SQL query in SQLalchemy syntax style. You may find <i>hook_postgres.py</i> to find the sample code.

### S3 Bucket
We will be using <a href="https://min.io/docs/minio/container/index.html">Minio</a> as a S3 bucket sensor (The sensor will trigger the DAG run while new file is uploaded to S3 bucket). Then under Connection section, fill in all login info and credentials like you did in the last section. An extra step is to fill in a dictionary of extra credentials, including S3 access and sceret key and host. Then you may connect your S3 bucket via Minio in your Python script.
<br><br>
In the operator object, you may set the <i>mode</i> to <b>poke</b> and the time for <i>poke_interval</i>. If you set time interval as 5 seconds, it means the DAG would check whether the <i>bucket_key</i> is presented in the bucket every 5 seconds. It is not presented, it would fail and check every 5 seconds until it finds it.
<br><br>
You may find <i>connect_s3_sensor.py</i> for the sample code.

### NoSQL Database
The format of the syntax for connecting NoSQL database and executing NoSQL query is the same as the syntax for relational databases. First, add a collection like you did for Postgres before writing your Python script. An example of the MongoOperator is:

```
# Coming soon...
```
