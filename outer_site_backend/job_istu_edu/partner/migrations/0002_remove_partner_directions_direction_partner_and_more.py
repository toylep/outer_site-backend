# Generated by Django 4.2.7 on 2023-11-13 02:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='directions',
        ),
        migrations.AddField(
            model_name='direction',
            name='partner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='partner.partner'),
        ),
        migrations.AddField(
            model_name='partner',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
