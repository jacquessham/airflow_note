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

### ex2_v1.py
Coming Soon...

### etl.py
Coming Soon...

### create_salarytable.sql
The SQL script creates a schema called <i>ex2</i> and tables <i>person</i> and <i>salary</i> according to the logical model.