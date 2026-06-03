from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "Homer Simpson",
    "start_date": datetime(2020, 5, 20, 11, 0, 0),
}


def hello_world_loop():
    for palabra in ["El uso de Airflow en la universidad de Springfield",
                    "El otro día mi hija me dijo que Airflow no se utilizaba en la universidad de Springfield, y yo le dije: qué no Lisa? qué no?",
                    "Púdrete Flanders"]:
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