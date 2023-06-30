# Ex 1 - Find the Person who has the Highest Salary
In this exercise, we will try to use Airflow to read a CSV file which contains the information of the candidates and try to find the person who has the highest salary. The exercise is a hands-on to try to use the BashOperator and PythonOperator.

## Plan
In this exercise, we would do the following:
<ul>
	<li>Print an introduction on command line</li>
	<li>Read CSV file</li>
	<li>Print how many candidates are there</li>
	<li>Find the person who has the highest salary</li>
	<li>Calculate how many times he may go to Japan</li>
</ul>

<br>
The DAG will looks like this:
<img src=ex1_dag.png>

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

### ex1_v1.py
Coming Soon...

### ex1_v2.py
Coming Soon...
