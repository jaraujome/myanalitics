class AnaliticsRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read analitics models go to default.
        """
        if model._meta.app_label == 'analitics':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write analitics models go to default.
        """
        if model._meta.app_label == 'analitics':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the analitics app is involved.
        """
        if obj1._meta.app_label == 'analitics' or \
           obj2._meta.app_label == 'analitics':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the analitics app only appears in the 'default'
        database.
        """
        if app_label == 'analitics':
            return db == 'default'
        return None