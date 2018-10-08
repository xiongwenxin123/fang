"""
数据库路由规则
"""


class AuthAdminDbRouter:
    """Auth数据库的路由"""

    def db_for_read(self, model, **hints):
        if model._meta.app_label in ('auth', 'admin'):
            return 'auth_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in ('auth', 'admin'):
            return 'auth_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in ('auth', 'admin') or \
                obj2._meta.app_label in ('auth', 'admin'):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'auth':
            return db == 'auth_db'
        return None


class MasterSlaveDbRouter:
    """主从复制的路由"""

    def db_for_read(self, model, **hints):
        # return random.choice(('slave1', 'slave2'))
        return 'slave1'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        db_list = ('default', 'slave1')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
