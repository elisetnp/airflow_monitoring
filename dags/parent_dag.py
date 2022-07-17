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
from airflow.sensors.external_task_sensor import ExternalTaskSensor

dag = DAG(
    dag_id="parent_dag_id",
    start_date=datetime(2021, 10, 1),
    schedule_interval="0 18 L * *",
    template_searchpath="/tmp",
    max_active_runs=1,
)


def _last_parent_task():
    print('Doing _last_parent_task')


def _initial_parent_task():
    print('Doing initial_parent_task')


initial_parent_task = PythonOperator(
    task_id="initial_parent_task",
    python_callable=_initial_parent_task,
    dag=dag,
)

last_parent_task = PythonOperator(
    task_id="last_parent_task",
    python_callable=_last_parent_task,
    dag=dag,
)

sensor = ExternalTaskSensor(task_id='dag_sensor', external_dag_id='child_dag_id', external_task_id=None,
                            dag=dag, mode='reschedule')

initial_parent_task >> sensor >> last_parent_task
