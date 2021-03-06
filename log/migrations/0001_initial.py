# Generated by Django 3.0 on 2020-05-06 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('s_num', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.CharField(max_length=100)),
                ('end_time', models.CharField(max_length=100)),
                ('s_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='user.UsersMan')),
            ],
            options={
                'db_table': 'log',
                'managed': True,
            },
        ),
    ]
