# Generated by Django 3.0.5 on 2020-04-15 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0007_delete_measure'),
        ('alerts', '0002_add_created_updated_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameterrule',
            name='station',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='stations.Station'),
        ),
    ]
