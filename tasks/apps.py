from django.apps import AppConfig

class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'

    def ready(self):
        from django.contrib.auth import get_user_model
        User = get_user_model()

        # 既に存在するなら何もしない
        if User.objects.filter(username="raguna").exists():
            return

        # 一度だけ作る
        User.objects.create_superuser(
            username="raguna",
            email="pasupoto17@gmail.com",
            password="kaibasensei"
        )
