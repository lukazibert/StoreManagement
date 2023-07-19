# Generated by Django 3.2 on 2023-07-19 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
        ('employes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='stores.store'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1),
        ),
    ]
