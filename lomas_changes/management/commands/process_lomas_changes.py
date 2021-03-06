from datetime import datetime, timedelta

import django_rq
from django.core.management.base import BaseCommand, CommandError
from dateutil.relativedelta import relativedelta

from lomas_changes.models import Period
from lomas_changes.tasks import sentinel1, sentinel2
from lomas_changes.tasks.predict_rf import predict
from lomas_changes.tasks.load_data import load_data


class Command(BaseCommand):
    help = 'Starts processing pipeline for generating a change map'

    date_to = datetime.now().replace(day=1)
    date_from = date_to - relativedelta(months=1)

    def add_arguments(self, parser):
        parser.add_argument('--date-from',
                            type=lambda s: datetime.strptime(s, '%Y-%m-%d'),
                            default=self.date_from)
        parser.add_argument('--date-to',
                            type=lambda s: datetime.strptime(s, '%Y-%m-%d'),
                            default=self.date_to)

    def handle(self, *args, **options):
        date_from = options['date_from'].date()
        date_to = options['date_to'].date()
        period, _ = Period.objects.get_or_create(date_from=date_from,
                                                 date_to=date_to)
        #sentinel1.process_all(period)
        #sentinel2.process_all(period)
        #predict(period)
        load_data(period)
