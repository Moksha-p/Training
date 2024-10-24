# Generated by Django 5.1.2 on 2024-10-24 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ManyToManyField(related_name='project', to='modelapp.employee'),
        ),
        migrations.AlterField(
            model_name='project',
            name='team_lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='led_projects', to='modelapp.employee'),
        ),
    ]
