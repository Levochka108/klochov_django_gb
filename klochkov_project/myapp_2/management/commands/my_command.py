from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Описание вашей команды здесь'

    def add_arguments(self, parser):
        parser.add_argument('arg_name', nargs='+', type=str,
                            help='Описание аргументов команды')

    def handle(self, *args, **options):
        arg_value = options['arg_name']
        # Ваш код обработки команды здесь
        self.stdout.write(self.style.SUCCESS(
            f'Команда успешно выполнена с аргументами: {arg_value}'))
