import os

import celery
import pymysql

from django.conf import settings
from fang import tasks

pymysql.install_as_MySQLdb()

# 项目名称
# project_name = 'fang'
# project_settings = '%s.settings' % project_name

# 注册环境变量 - 让Celery能够读取项目的配置文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fang.settings')

# 创建Celery实例 - 指定访问消息队列服务的URL
app = celery.Celery('fang',
                    backend='amqp://luohao:123123@120.77.222.217:5672/vhost1',
                    broker='amqp://luohao:123123@120.77.222.217:5672/vhost1')


# 从默认的配置文件读取配置信息
app.config_from_object('django.conf:settings')

# Celery加载所有注册的应用
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# 添加定时任务
# 下面的方式比较麻烦可以使用更简单的periodic_task装饰器
# app.conf.update(
#     timezone=settings.TIME_ZONE,
#     enable_utc=True,
#     beat_schedule={
#         'task1': {
#             'task': 'tasks.foo',
#             'schedule': crontab(),
#             'args': ('你妈喊你回家吃饭啦', )
#         },
#     },
# )
