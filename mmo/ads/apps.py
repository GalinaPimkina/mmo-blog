from django.apps import AppConfig


class AdsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ads'
    verbose_name = "Объявления авантюристов"

    def ready(self):
        import ads.signals

