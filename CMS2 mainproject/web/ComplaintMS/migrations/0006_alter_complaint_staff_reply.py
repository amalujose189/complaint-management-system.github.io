# Generated by Django 3.2.2 on 2023-04-24 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComplaintMS', '0005_alter_complaint_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='staff_reply',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
