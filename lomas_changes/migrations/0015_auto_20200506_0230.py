# Generated by Django 3.0.6 on 2020-05-06 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lomas_changes', '0014_auto_20200506_0028'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='period',
            unique_together={('date_from', 'date_to')},
        ),
    ]
