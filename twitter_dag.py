from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from Tweets_Scrape import twitter_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 6, 27),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='My first DAG with ETL',
    schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='tweets_etl',
    python_callable=twitter_etl,
    dag=dag, 
)

run_etl
