# Generated by Django 4.1.5 on 2023-02-03 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0001_initial'),
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nomination',
            name='election',
        ),
        migrations.RemoveField(
            model_name='nomination',
            name='nominee',
        ),
        migrations.RemoveField(
            model_name='nomination',
            name='portfolio',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='createdBy',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='election',
        ),
        migrations.AlterField(
            model_name='voting',
            name='election',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.election'),
        ),
        migrations.DeleteModel(
            name='Election',
        ),
        migrations.DeleteModel(
            name='Nomination',
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
    ]
