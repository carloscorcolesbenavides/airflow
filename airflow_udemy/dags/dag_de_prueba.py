from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "javier_lopez",
    "start_date": datetime(2020, 5, 20, 11, 0, 0),
}


def hello_world_loop():
    for palabra in ["hello", "world"]:
        print(palabra)


with DAG(
    dag_id="dag_prueba",
    default_args=default_args,
    schedule="@daily",
    catchup=False,
) as dag:

    start = EmptyOperator(
        task_id="start"
    )

    prueba_python = PythonOperator(
        task_id="prueba_python",
        python_callable=hello_world_loop,
    )

    prueba_bash = BashOperator(
        task_id="prueba_bash",
        bash_command="echo prueba_bash",
    )

    start >> prueba_python >> prueba_bash