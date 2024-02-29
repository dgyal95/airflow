from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator
from airflow.models import Variable # 전역변수 사용

with DAG(
    dag_id="dags_bash_with_variable",
    schedule="10 9 * * *",
    start_date=pendulum.datetime(2023, 4, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    # 1안) Variable 라이브러리 사용
    var_value = Variable.get("sample_key")

    bash_var_1 = BashOperator(
    task_id="bash_var_1",
    bash_command=f"echo variable:{var_value}"
    )

    # 2안) Jinja Template 이용, 오퍼레이터 내부에서 가져오기 (Airflow 권고)
    bash_var_2 = BashOperator(
    task_id="bash_var_2",
    bash_command="echo variable:{{var.value.sample_key}}"
    )
