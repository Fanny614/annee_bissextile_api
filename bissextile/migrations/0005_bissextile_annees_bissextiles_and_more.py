# Generated by Django 5.1.3 on 2024-12-09 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bissextile', '0004_alter_bissextile_annee'),
    ]

    operations = [
        migrations.AddField(
            model_name='bissextile',
            name='annees_bissextiles',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bissextile',
            name='is_bissextile',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
