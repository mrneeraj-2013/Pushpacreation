# Generated by Django 4.2.3 on 2023-07-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pihu', '0003_alter_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
