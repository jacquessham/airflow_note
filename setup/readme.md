# Setup

## First Time User (via Docker, run locally)
<ol>
	<li>Download the Yaml file from Airflow</li>
	<li>Open the Yaml file, change from Celery Executor to Local Excutor, and delete the dependences</li>
	<li>Make the folders for dags, logs, plugins</li>
	<li>Initiate the Postgres database</li>
	<li>Run the container</li>
	<li>Open the broswer and head to <b>0.0.0.0:8080</b>, log in with username and password <b>airflow</b></li>
</ol>

```
# Download yaml file from Airflow
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.6.2/docker-compose.yaml'

# Initiate the Postgres db
docker-compose up airflow-init

# Run the container
docker-compose up
```


## Reference
YouTuber <b>coder2j</b> - <a href="https://www.youtube.com/watch?v=K9AnJ9_ZAXE">Airflow Tutorial for Beginners - Full Course in 2 Hours 2022</a>