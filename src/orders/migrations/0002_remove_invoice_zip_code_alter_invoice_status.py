# Generated by Django 4.0 on 2022-01-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='zip_code',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='New', max_length=10),
        ),
    ]
