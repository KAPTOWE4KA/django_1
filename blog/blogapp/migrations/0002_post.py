# Generated by Django 4.0.6 on 2022-07-28 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('text', models.TextField()),
                ('edited', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blogapp.category')),
            ],
        ),
    ]