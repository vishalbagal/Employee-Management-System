# Generated by Django 5.0.1 on 2024-01-23 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_department_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='manager',
            field=models.CharField(max_length=255),
        ),
    ]