ARG AIRFLOW_BASE_IMAGE="apache/airflow:2.2.2-python3.6"
FROM ${AIRFLOW_BASE_IMAGE}

RUN pip install --user --no-cache-dir \
    apache-airflow-providers-postgres==1.0.0 \
    apache-airflow[statsd]
