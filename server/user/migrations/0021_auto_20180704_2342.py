# Generated by Django 2.0.4 on 2018-07-05 03:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_rename_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='active',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='If the subscription is active, the datetime when it was last activated', null=True),
        ),
    ]