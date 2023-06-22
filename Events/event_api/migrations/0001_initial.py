# Generated by Django 4.1.4 on 2023-06-21 06:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('tagline', models.CharField(max_length=255)),
                ('schedule', models.DateTimeField()),
                ('description', models.TextField()),
                ('moderator', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('sub_category', models.CharField(max_length=255)),
                ('rigor_rank', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='event_images/')),
                ('attendees', models.ManyToManyField(related_name='events_attending', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]