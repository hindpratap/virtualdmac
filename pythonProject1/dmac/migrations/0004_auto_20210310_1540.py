# Generated by Django 2.2.7 on 2021-03-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmac', '0003_auto_20210310_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeEmails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_id', models.IntegerField(blank=True, default=0)),
                ('table1', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Tablelist',
        ),
    ]