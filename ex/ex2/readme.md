# Ex 2 - Build a Simple ETL Pipeline
In this exercise, we will build a simple ETL to ingest a csv file, transform, and upload to a Postgres databse.

## Plan
In this exercise, we would do the following:
<ol>
	<li>Read a SQL script and create table</li>
	<li>Read data via Pandas</li>
	<li>Normalize the data into one fact table and one attribute table</li>
	<li>Upload the data to the respective tables</li>
	<li>Upload the log record</li>
</ol>

<br>
The DAG will looks like this:
<img src=ex2_dag.png>
<br><br>
Under each task, we will:
<ul>
	<li>create_table: 1</li>
	<li>etl: 2, 3, 4</li>
	<li>update_log: 5</li>
</ul>

## Logical Model
The logical model of this use case should be:
<img src=ex2_ldm.png>

## Script
The file <i>ex2.py</i> will be the main Python script to run this DAG, along <i>salary.csv</i> is saved under the same directory. A folder <i>ex2</i> contains <i>etl.py</i>, <i>create_salarytable.sql</i>.
<br><br>
The main script will create table with Postgres Operator first. Then it will import the functions from <i>etl.py</i> to ingest data, transform, and utilize Postgres Hook to upload data to the database. And finally use Postgres Operator to upload log records.
<br><br>
<b>The scripts are designed to used for Docker hosted Airflow.</b>

### ex2_v1.py
This is the main script to construct the DAG, which includes 3 tasks mentioned in the Plan section. It will execute the DDL script, <i>create_salarytable.sql</i> to create tables according to the logical model. For Task 2, it will call the function <i>etl()</i> from <i>etl.py</i> for instruction of each task. And it will upload the log data by extracting from the Airflow Macro.

### etl.py
This script includes the major function <i>etl()</i> to read <i>salary.csv</i> with Pandas and insert transformed data. <i>etl()</i> will utilize helper functions like <i>getstr_insert_into()</i> to organize the SQL insert syntax, as well as <i>get_pwd()</i>, <i>declare_conn()</i>, and <i>close_conn(conn)</i> to handle directory and consor object (for connecting database with Python).

### create_salarytable.sql
The SQL script, or DDL, creates a schema called <i>ex2</i> and tables <i>person</i> and <i>salary</i> according to the logical model.

