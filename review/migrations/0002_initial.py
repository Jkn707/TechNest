# Generated by Django 4.2.12 on 2024-08-11 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='reviewingClient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.client'),
        ),
    ]
