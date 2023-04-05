# Generated by Django 4.1.7 on 2023-03-12 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_posts_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='msg',
        ),
        migrations.AddField(
            model_name='posts',
            name='body',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='name',
            field=models.CharField(default='Jane Doe', max_length=20, verbose_name='Name'),
        ),
    ]
