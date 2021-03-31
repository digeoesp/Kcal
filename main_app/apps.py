from django.apps import AppConfig


class MainAppConfig(AppConfig):
    name = 'main_app'
    def ready(self): #new
        import main_app.signals #new
