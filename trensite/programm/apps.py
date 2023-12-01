from django.apps import AppConfig


class ProgrammConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'programm'
    verbose_name = 'Заказ'
    verbose_name_plural = 'Заказы'
