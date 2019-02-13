# Generated by Django 2.1.5 on 2019-02-03 08:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190203_0638'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ('username',)},
        ),
        migrations.AlterModelOptions(
            name='flag',
            options={'ordering': ('flag',)},
        ),
        migrations.RemoveField(
            model_name='flag',
            name='solved_users',
        ),
        migrations.AddField(
            model_name='flag',
            name='solved_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]