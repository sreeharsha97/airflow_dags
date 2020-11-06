from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow'
}

def sample_python_function(**kwargs):
    """
    Insert arbitrary python function here
    """
    print("Dummy Function Test")

dag = DAG('example_python_operator_airflow',
            max_active_runs=3,
            catchup=True,
            schedule_interval=None,
            start_date=days_ago(2),
            default_args=default_args)

with dag:

    start = DummyOperator(task_id='start')

    for i in range(0,2):

        t1 = PythonOperator( 
            task_id='python_function_af_{0}'.format(i),
            python_callable=sample_python_function,
            dag=dag)

        start >> t1
