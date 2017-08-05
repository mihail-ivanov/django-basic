
import subprocess

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError


class Command(BaseCommand):
    help = 'Rebuilds webpack assets'

    def add_arguments(self, parser):
        parser.add_argument(
            '--debug',
            action='store_true',
            dest='debug',
            default=False,
            help='Displays debug information while building the assets',
        )

    def handle(self, *args, **options):
        command = './node_modules/.bin/webpack {} --config webpack.config.js'
        if options['debug']:
            command = command.format('--display-modules')
        else:
            command = command.format('')

        response = subprocess.call(command, shell=True)

        self.stdout.write(self.style.SUCCESS('Assets build finished'))
