from django.apps import AppConfig


class InstagraAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'instagra_app'

# updated the user
class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
