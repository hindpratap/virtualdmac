# Generated by Django 2.2.7 on 2021-03-10 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmac', '0002_tablelist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lead',
        ),
        migrations.AddField(
            model_name='tablelist',
            name='query_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]