from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'workwave.apps.users'

    def ready(self):
        import workwave.apps.users.signals 