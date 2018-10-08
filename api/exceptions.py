"""
自定义DRF的异常处理器
"""
import logging

from django.db import DatabaseError
from redis.exceptions import RedisError

from rest_framework import status
from rest_framework import views
from rest_framework.response import Response


# 获取在配置文件中定义的logger来记录日志
logger = logging.getLogger('django')


def exception_handler(ex, ctx):
    """
    自定义异常处理
    :param ex: 异常对象
    :param ctx: 抛出异常的上下文对象
    :return: 响应对象
    """
    resp = views.exception_handler(ex, ctx)

    if resp is None:
        if isinstance(ex, DatabaseError) or isinstance(ex, RedisError):
            logger.error(f'{ctx["view"]}: {ex}')
            resp = Response({'code': 500, 'message': '服务器升级维护中请稍后重试'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return resp
