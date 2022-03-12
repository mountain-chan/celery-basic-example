# Celery Basic Example

* Link documents: [First Steps with Celery](https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html)

## Broker: redis
* Redis for Windows: [https://github.com/tporadowski/redis/releases](https://github.com/tporadowski/redis/releases)

## Running the Celery worker server
* Ubuntu
```commandline
celery -A my_worker worker --loglevel=INFO
```

* Windows
```commandline
celery -A my_worker worker -l info -P  gevent
```

## Calling the task
```commandline
python main.py
```