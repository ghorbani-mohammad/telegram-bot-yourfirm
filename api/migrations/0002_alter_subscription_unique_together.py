# Generated by Django 4.0.2 on 2022-08-18 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together={('profile', 'term')},
        ),
    ]