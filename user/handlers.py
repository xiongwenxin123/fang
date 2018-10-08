"""
Django信号机制的钩子程序(暂时没有用上)
"""
# from uuid import uuid1
#
# from django.dispatch import receiver
# from django.db.models.signals import pre_save
#
# from common.models import User
# from common.utils import to_md5_hex
#
#
# @receiver(signal=pre_save, sender=User)
# def handle_before_user_save(sender, **kwargs):
#     user = kwargs['instance']
#     user.password = to_md5_hex(user.password)
#     user.token = uuid1().hex
