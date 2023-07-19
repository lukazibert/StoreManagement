# Generated by Django 3.2 on 2023-07-19 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employes', '0004_alter_employee_store'),
        ('stores', '0002_store_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='employees',
            field=models.ManyToManyField(related_name='employes', to='employes.Employee'),
        ),
    ]
