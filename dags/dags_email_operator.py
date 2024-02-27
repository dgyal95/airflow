from airflow import DAG
import pendulum
import datetime
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    send_email_task = EmailOperator(
        task_id='send_email_task', # 객체명과  task_id는 동일하게 만들자
        to='v_lilac@naver.com',
        #cc='v_lilac@naver.com',
        subject='Airflow 테스트 메일',
        html_content='Airflow 작업이 완료되었습니다'
    )