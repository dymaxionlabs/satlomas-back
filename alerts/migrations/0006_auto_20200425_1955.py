# Generated by Django 3.0.5 on 2020-04-25 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('alerts', '0005_fix_unique_constraint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoperule',
            name='measurement_content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'lomas_changes'), ('model', 'coveragemeasurement')), models.Q(('app_label', 'vi_lomas_changes'), ('model', 'coveragemeasurement')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='scopetyperule',
            name='measurement_content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'lomas_changes'), ('model', 'coveragemeasurement')), models.Q(('app_label', 'vi_lomas_changes'), ('model', 'coveragemeasurement')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]
