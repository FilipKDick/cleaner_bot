# Generated by Django 3.2.15 on 2022-10-04 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0003_many_to_many_group_page'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chore',
            old_name='completion_period',
            new_name='completion_frequency',
        ),
    ]
