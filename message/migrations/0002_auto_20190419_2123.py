# Generated by Django 2.1.7 on 2019-04-19 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shareLife', '0003_post_sqft'),
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='postId',
        ),
        migrations.AddField(
            model_name='message',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Message_post', to='shareLife.Post'),
        ),
    ]
