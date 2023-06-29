# Notes on the Basics

## Basics
Here are some core concepts in the Airflow Structure:
<ul>
	<li>DAG (Directed Acyclic Graph): The workflow you manage to the collection of tasks you wish to perform, as the name directed acyclic graph suggested, tasks are perform one way without going back</li>
	<li>Task: Unit of work within a DAG</li>
	<li>Operator: The method of task, like Bash or Python operator</li>
	<li>Execution Date: The launch date/time of DAG</li>
	<li>Task Instance: The date/time the task is executed</li>
	<li>DAG run: The date/time the DAG is executed</li>
	<li>Task Lifecycle: Status of the tasks of a DAG run</li>
	<li></li>
</ul>

<br><br>
We would work with the followiing operators:
<ul>
	<li>BashOperator</li>
	<li>PythonOperator</li>
	<li></li>
	<li></li>
	<li></li>
</ul>
<br>
<b>Even there are many operators, all the operators are written in Python</b>. Each DAG would be written in one Python script and import the operators from the library, and define the task in the script.
<br><br>
All scripts should be saved in the DAG folder.

## Basic Syntax
In each DAG, you should at least include the following syntax:
<ul>
	<li>Importing DAG, operators from Airflow</li>
	<li>Default Arguement</li>
	<li>Metadata of the DAG</li>
	<li>Task Instruction</li>
	<li>Workflow of the task</li>
</ul>
<br>
An example of a script with BashOperator and PythonOperator

```
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


default_args = {
	'owner': 'Jacques Sham',
	'retries': 5,
	'retry_delay': timedelta(minutes=2)
}

def greet(name, age):
	print(f"Hello World! My name is {name} and I am {age} years old")

with DAG(
	dag_id='first_dag_v3',
	description='This is the first DAG',
	default_args = default_args,
	start_date=datetime(2023,6,28,23,15),
	schedule_interval='@daily'

) as dag:
	task1 = BashOperator(
		task_id='first_task',
		bash_command='echo Hello World!'
		)
	task2 = BashOperator(
		task_id='second_task',
		bash_command='echo I am executing Task 2 after saying hello!'
		)
	= PythonOperator(
			task_id='greet',
			python_callable=greet,
			op_kwargs={'name':'Jacques', 'age': 21}
		)
	task1.set_downstream(task2)
	task1 >> task3
```
<br>
Using the <b>with</b> syntax, you may define all the tasks in this DAG and the workflow. Note that you may set downstream with two ways:
<ul>
	<li>task1.set_downstream(task3)</li>
	<li>task1 >> task3</li>
</ul>

<br><br>
Coming soon...

## Reference
YouTuber <b>coder2j</b> - <a href="https://www.youtube.com/watch?v=K9AnJ9_ZAXE">Airflow Tutorial for Beginners - Full Course in 2 Hours 2022</a>