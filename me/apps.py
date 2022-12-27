from django.apps import AppConfig


class MeConfig(AppConfig):
    
    name = 'me'
    def ready(self):
        import me.signals