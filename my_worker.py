from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

app = Celery('worker_demo', broker='redis://localhost:6379/0')


@app.task()
def basic_task(name: str):
    logger.info(f"Hello world, my name is {name}")
    print(f"Hello world, my name is {name}")

# celery -A my_worker worker -l info
# celery -A my_worker worker -l info -P  gevent
