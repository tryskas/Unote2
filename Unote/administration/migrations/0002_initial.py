# Generated by Django 5.0.6 on 2024-06-07 07:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administration', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='grade',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(related_name='users_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.group'),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='presence',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='session',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.course'),
        ),
        migrations.AddField(
            model_name='session',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.room'),
        ),
        migrations.AddField(
            model_name='presence',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.session'),
        ),
        migrations.AddField(
            model_name='grade',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.subject'),
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.subject'),
        ),
        migrations.AddField(
            model_name='ue',
            name='subjects',
            field=models.ManyToManyField(related_name='ues', to='administration.subject'),
        ),
        migrations.AddField(
            model_name='group',
            name='ues',
            field=models.ManyToManyField(related_name='groups', to='administration.ue'),
        ),
    ]
