# Generated by Django 3.2.11 on 2022-03-06 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviehub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='hgh', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
