# Generated by Django 5.0.6 on 2024-07-05 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meet', '0002_alter_meeting_meeting_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='meeting_end',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meeting_start',
            field=models.CharField(max_length=75),
        ),
    ]
