# Generated by Django 4.2.7 on 2023-11-21 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_delete_marksheet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='class_name',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='grade',
        ),
    ]
