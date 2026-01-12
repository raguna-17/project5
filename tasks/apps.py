from django.apps import AppConfig

class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'

    def ready(self):
        from django.contrib.auth import get_user_model
        User = get_user_model()
        if not User.objects.filter(username="raguna").exists():
            User.objects.create_superuser("raguna", "pasupoto17@gmail.com", "kaibasensei")
