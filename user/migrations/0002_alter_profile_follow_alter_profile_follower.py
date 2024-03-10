# Generated by Django 5.0.2 on 2024-03-03 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(blank=True, related_name='takip', to='user.profile', verbose_name='Takip Edilenler'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='follower',
            field=models.ManyToManyField(blank=True, related_name='takipci', to='user.profile', verbose_name='Takipçiler'),
        ),
    ]
