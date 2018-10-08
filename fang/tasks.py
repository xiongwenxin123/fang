from celery.schedules import crontab
from celery.task import periodic_task


@periodic_task(run_every=crontab())
def foo():
    print('刘强东，奶茶妹妹喊你回家吃饭啦!')
