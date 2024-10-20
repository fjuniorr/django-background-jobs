# Generated by Django 5.1.2 on 2024-10-20 18:51

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoey', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZProduct',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoey.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
