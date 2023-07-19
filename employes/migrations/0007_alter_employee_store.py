# Generated by Django 3.2 on 2023-07-19 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0005_alter_store_employees'),
        ('employes', '0006_alter_employee_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.store'),
        ),
    ]
