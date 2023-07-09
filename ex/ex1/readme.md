# Ex 1 - Find the Person who has the Highest Salary
In this exercise, we will try to use Airflow to read a CSV file which contains the information of the candidates and try to find the person who has the highest salary. The exercise is a hands-on to try to use the BashOperator and PythonOperator.

## Plan
In this exercise, we would do the following tasks:
<ol>
	<li>Print an introduction on command line</li>
	<li>Read CSV file</li>
	<li>Print how many candidates are there</li>
	<li>Find the person who has the highest salary</li>
	<li>Calculate how many times he may go to Japan</li>
</ol>

<br>
The DAG will looks like this:
<img src=ex1_dag.png>

<br><br>
Therefore, the task order should be the following:

```
task1 >> task2 >> [task3, task4]
task4 >> task5
```

<br><br>
Note: The formula used to calculate how many times he may go to Japan is not a accurate formula, its purpose is simply add some fun into the context. The major goal is to demostrate a task in this DAG.

## Script
The filename of the script is <i>ex1_v1.py</i> along with the dataset <i>salary.csv</i>. Both files are expected to be saved under the <i>dags</i> folder in your Airflow folder. 
<br><br>
This script is written in basic operator syntax. You may find the <i>ex1_v2.py</i> for the script with Taskflow APIs syntax.
<br><br>
Note that the script is run in the Docker enviornment, the directory does not work the same way as reading locally. Add an extra step to state the current directory in the Docker folder, and add it with the filename like below:

```
import os
...
AIRFLOW_HOME = os.getenv('AIRFLOW_HOME')
df = pd.read_csv(AIRFLOW_HOME+'/dags/salary.csv')
```

<br><br>
<b>The scripts are designed to used for Docker hosted Airflow.</b>

### ex1_v1.py
The script will execute the task with the mixture of BashOperators and Python Operator, as well as 4 helper functions <i>load_data()</i>, <i>print_num_candidates()</i>, <i>print_highest()</i>, and <i>calculate_trips()</i> to be called for Task 2-5. It will Task instance to pass the data among tasks.


### ex1_v2.py
The script is the same script as <i>ex1_v1.py</i>, except it is written in the Taskflow API style syntax.

