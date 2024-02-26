import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(

    dag_id="dags_bash_operator",                          # dag_id : airflow에서 보이는 dag 이름
    schedule="0 0 * * *",                                 # cron 스케쥴  ex. 매일 0시 0분에 실행 (분 시 일 월 요일)
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),   # DAG이 언제부터 돌지 start 시간
    catchup=False,                                        # start_date가 과거일때 과거부터 모두 실행시켜놓을지

    #dagrun_timeout=datetime.timedelta(minutes=60), # 특정시간이 지나면 timeout 실패하게 설정
    #tags=["example", "example2"], # 분류태그
    #params={"example_key": "example_value"}, # 파라메터

) as dag:

    bash_t1 = BashOperator(     # task : operator를 통해서 만들어짐
        task_id="bash_t1",      # task_id : DAG내 보여질 task 이름 (이것도 Task명과 동일하게 주는게 좋음)
        bash_command="echo whoami",  # 어떤 shell script를 수행할 것인지
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2