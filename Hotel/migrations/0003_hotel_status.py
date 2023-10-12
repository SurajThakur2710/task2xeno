# Generated by Django 4.1.7 on 2023-05-06 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0002_auto_20211011_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='status',
            field=models.IntegerField(choices=[(1, 'APPROVED'), (3, 'DISAPPROVED'), (2, 'PENDING')], default=2),
        ),
    ]