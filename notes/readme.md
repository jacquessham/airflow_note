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
	<li>XCom: A mechanism that let tasks communicate, ie, passing values to downstream tasks. <b>Note: It may only take 48KB of data only!</b></li>
	<li>Task Instance (ti): The instance to allow you to pull values stored in XCom</li>
</ul>

<br><br>
We would work with the followiing operators:
<ul>
	<li>BashOperator</li>
	<li>PythonOperator</li>
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
	start_date=datetime(2023,6,28),
	schedule_interval='@daily', # You may change to cron expression
	catchup=False # By fault it is True
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
If you have multiple downstream or upstream tasks you may use an array to list it:

```
...
[task2, task3] >> task1

```

<br><br>
By default, DAG is set catchup to be True. It means if you set the a backdated starting date, DAG will automatically run the tasks between the interval of the starting date and today. You may set it to be False, and backfill manually on command line (See the video in the Reference Section).
<br>
Under schedule interval, we are using Airflow reserved word for interval, you may replaced it with cron expression, such as <b>0 4 * * Tue-Fri</b>.

## Python Operator
Instead of Bash command, you may utilize Python Operator to perform Python functions within a DAG. In the Operator argument, simply replace BashCommand to PythonCommand along a defined functions to be called in the command, like below:

```
def get_name():
	return 'Rodney'

...

	task2 = PythonOperator(
		task_id='get_name',
		python_callable=get_name
		)
...
task2 >> task1
```

You may utilize the XCom component in Airflow to pass arguement from one task to anthoer. Add a <b>ti</b> object in the function argument, then push or pull value into the object (Task Instance), like below:

```
...

def greet(ti):
	first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
	last_name = ti.xcom_pull(task_ids='get_name',key='last_name')
	age = ti.xcom_pull(task_ids='get_age',key='age')
	print(f"Hello World! My name is {first_name} {last_name} and I am {age} years old")

def get_name(ti):
	ti.xcom_push(key='first_name', value='Rodney')
	ti.xcom_push(key='last_name', value='Wong')
...


```

## Task APIs
Because tasks are isolated and rely XComs for communication, you may utilize Task APIs to overcome this constrain and have a clear code script. You may first declear a outer function which contains multiple task functions (Each task function includes <b>@task()</b> on top of the function declaration). An example is below:

```
...
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
```

You may find more the reasons and the advantage in this <a href="https://blog.xmartlabs.com/blog/taskflow-the-airflow-new-feature-you-should-know/">blog</a>

## Reference
YouTuber <b>coder2j</b> - <a href="https://www.youtube.com/watch?v=K9AnJ9_ZAXE">Airflow Tutorial for Beginners - Full Course in 2 Hours 2022</a>