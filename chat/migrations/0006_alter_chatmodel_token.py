# Generated by Django 5.0.2 on 2024-02-19 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_chatmodel_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmodel',
            name='token',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]