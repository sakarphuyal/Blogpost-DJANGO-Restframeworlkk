# Generated by Django 3.2.3 on 2021-05-31 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='image/same.png', upload_to='images/'),
        ),
    ]