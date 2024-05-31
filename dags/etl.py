from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta

default_args = {
    'owner': 'ashish',
    'start_date': datetime(2024, 5, 31),  # should be start_date instead of start_time
    'retry_delay': timedelta(minutes=5),
    'retries': 0
}

def extract_fun():
    print("this is extract function")
    return_val = "this is demo airflow"
    return return_val

def transform_fun(t1, ti):
    xcom_pull_obj = ti.xcom_pull(task_ids="EXTRACT")
    if xcom_pull_obj:
        extract_value = xcom_pull_obj[0]
    else:
        extract_value = None
    print(f'the value of xcom from EXTRACT is {extract_value}')
    print(f'value of t1={t1}')
    return 10

def load_fun(o1, o2, ti):
    xcom_pull_obj = ti.xcom_pull(task_ids="TRANSFORM")
    if xcom_pull_obj:
        transform_value = xcom_pull_obj
    else:
        transform_value = None
    print(f'the value of xcom from TRANSFORM is {transform_value}')
    print(f'value of o1={o1} value of o2={o2}')

dag = DAG(
    dag_id='etl_2',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['etl1_with_xcoms', 'etl_demo']
)

start = DummyOperator(task_id='START', dag=dag)

extract = PythonOperator(
    task_id='EXTRACT',
    python_callable=extract_fun,
    do_xcom_push=True,
    dag=dag
)

transform = PythonOperator(
    task_id='TRANSFORM',
    python_callable=transform_fun,
    op_args=["learning airflow"],
    do_xcom_push=True,
    dag=dag
)

load = PythonOperator(
    task_id='LOAD',
    python_callable=load_fun,
    op_kwargs={"o1": "first value", "o2": "2nd value"},
    dag=dag
)

# Define task dependencies
start >> extract >> transform >> load
