# Airflow Monitoring

A sample to show how Airflow can be configured to export metrics, logs and distributed tracing.

## Contents

Topics covered are monitoring, logging, etc. An accompanying Docker Compose setup was built for demonstration purposes. This includes:

- Airflow (webserver, scheduler, and Celery workers)
- PostgreSQL database for Airflow metastore
- Prometheus, for scraping and storing metrics
- Grafana, for visualizing metrics
- StatsD exporter to expose metrics

## Usage

To get started with the code examples, adapt your environment variables in `docker-compose.yml` if needed, then start Airflow with Docker Compose with the following command:

```bash
docker-compose up -d
```

The webserver initializes a few things, so wait for a few seconds, and you should be able to access the
Airflow webserver at http://localhost:8081.

To stop running the examples, run the following command:

```bash
docker-compose down -v
```

### Run DAGs

* Login to Airflow `http://localhost:8080` with credentials `admin/admin`.
* Enable the DAG and start. No need to pass any configurations.

### View Grafana dashboard

Now, it is time to view the dashboard
* Login to Grafana dashboards `http://localhost:3000/dashboards` using credentials `admin/admin`.
* Click on the dashboard `Airflow` to view the simple DAG and task.