# Generated by Django 4.0.6 on 2022-08-01 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_alter_post_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]