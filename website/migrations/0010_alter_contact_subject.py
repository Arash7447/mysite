# Generated by Django 5.0.2 on 2024-04-01 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
