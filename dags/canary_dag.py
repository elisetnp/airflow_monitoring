from datetime import datetime
from urllib import request

import airflow.utils.dates
from airflow import DAG
from airflow.operators.python import PythonOperator


# Dag definition
dag = DAG(
    dag_id="canary_dag",
    start_date=airflow.utils.dates.days_ago(10),
    schedule_interval="0 5 * * *",  # "*/1 * * * *"
    catchup=False,
)
dag.doc_md = __doc__


def check_time(**kwargs) -> None:
    """Get the last runtime of DAG.

    Temporarily doing nothing useful as we use sla above.
    """
    from airflow.models import DagRun
    dag_id = "canary_dag"
    current_time = datetime.now()
    dag_runs = DagRun.find(dag_id=dag_id)
    dag_runs.sort(key=lambda x: x.logical_date, reverse=True)


task_compute_metric = PythonOperator(
    task_id="check_last_run_time",
    dag=dag,
    python_callable=check_time
)
