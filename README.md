# Airflow ETL DAG Example

This project demonstrates a simple ETL (Extract, Transform, Load) workflow using Apache Airflow. The workflow consists of three main tasks: `EXTRACT`, `TRANSFORM`, and `LOAD`, which are orchestrated using Airflow's Directed Acyclic Graph (DAG) capabilities.

## DAG Structure

The DAG is defined in the `etl.py` file and consists of the following tasks:
- `START`: A dummy task to mark the beginning of the workflow.
- `EXTRACT`: A Python task that simulates extracting data.
- `TRANSFORM`: A Python task that transforms the extracted data.
- `LOAD`: A Python task that loads the transformed data.

## Files

- `etl.py`: Contains the DAG definition and task functions.
- `README.md`: This file, providing an overview of the project.

## Requirements

- Apache Airflow

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Set up Airflow:**
   
   Follow the official [Apache Airflow installation guide](https://airflow.apache.org/docs/apache-airflow/stable/installation.html) to set up Airflow on your machine.

3. **Copy the DAG file:**

    Copy the `etl.py` file to your Airflow DAGs folder. The default location is usually `~/airflow/dags/`.

    ```bash
    cp etl.py ~/airflow/dags/
    ```

## Running the DAG

1. **Start the Airflow web server and scheduler:**

    ```bash
    airflow webserver --port 8080
    airflow scheduler
    ```

2. **Trigger the DAG:**

    Go to the Airflow web interface at `http://localhost:8080`, find the DAG named `etl_2`, and trigger it manually.

## DAG Code

 the code for the DAG in the repo
