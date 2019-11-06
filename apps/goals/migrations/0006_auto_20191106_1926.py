# Generated by Django 2.2.7 on 2019-11-06 18:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0005_auto_20191106_1720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goal',
            options={'ordering': ['-match'], 'verbose_name': 'Goal', 'verbose_name_plural': 'Goals'},
        ),
        migrations.AddField(
            model_name='goal',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
    ]
