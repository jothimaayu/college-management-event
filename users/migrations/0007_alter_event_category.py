# Generated by Django 5.1.2 on 2025-02-28 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_registration_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Sports', 'Sports'), ('Cultural', 'Cultural'), ('Gaming', 'Gaming'), ('Education', 'Education')], max_length=20),
        ),
    ]
