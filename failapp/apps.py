from django.apps import AppConfig


class FailappConfig(AppConfig):
    name = 'failapp'

    def ready(self):
        print('in failapp apps, about to import TF')
        import tensorflow as tf
        print('TF imported successfully')

