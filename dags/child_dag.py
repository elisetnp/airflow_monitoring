# """
# Documentation of pageview format: https://wikitech.wikimedia.org/wiki/Analytics/Data_Lake/Traffic/Pageviews
# """
from datetime import datetime
from urllib import request

import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

dag = DAG(
    dag_id="child_dag_id",
    start_date=datetime(2021, 10, 1),
    schedule_interval="0 18 * * *",
    template_searchpath="/tmp",
    max_active_runs=1,
)


def _task_1():
    print('Doing task 1')


def _task_2():
    print('Doing task 2')


task_1 = PythonOperator(
    task_id="task_1",
    python_callable=_task_1,
    dag=dag,
)

task_2 = PythonOperator(
    task_id="task_2",
    python_callable=_task_2,
    dag=dag,
)

task_1 >> task_2
