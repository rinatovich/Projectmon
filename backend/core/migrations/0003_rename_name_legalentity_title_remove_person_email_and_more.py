# Generated by Django 5.0.1 on 2024-02-13 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_document_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='legalentity',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
        migrations.RemoveField(
            model_name='person',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия'),
        ),
    ]
