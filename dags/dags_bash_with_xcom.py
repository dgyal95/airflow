from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_with_xcom",
    schedule="10 0 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    # push
    bash_push = BashOperator(
    task_id='bash_push',
    bash_command="echo START && "
                 "echo XCOM_PUSHED "
                 "{{ ti.xcom_push(key='bash_pushed',value='first_bash_message') }} && " # bash_pushed 에 저장
                 "echo COMPLETE"  # bash_command 마지막 출력문은 자동으로 return_value 에 저장
    )

    # pull
    bash_pull = BashOperator(
        task_id='bash_pull',
        env={'PUSHED_VALUE':"{{ ti.xcom_pull(key='bash_pushed') }}",    # bash_pushed 키의 value
            'RETURN_VALUE':"{{ ti.xcom_pull(task_ids='bash_push') }}"}, # task_ids만 지정하면 return_value 
        bash_command="echo $PUSHED_VALUE && echo $RETURN_VALUE ",
        do_xcom_push=False  # bash_command 마지막 출력문이 자동으로 Xcom에 들어가는데 그걸 하지 마라고 주는 옵션
    )

    bash_push >> bash_pull