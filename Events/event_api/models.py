from django.db import models
from django.conf import settings

class Event(models.Model):

    EVENT_TYPE_CHOICES = [
        ('event1', 'event1'),
        ('event2', 'event2'),
        ('event3', 'event3'),
        # Add more event type choices here if needed
    ]

    name = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    schedule = models.DateTimeField()
    description = models.TextField()
    moderator = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255)
    rigor_rank = models.IntegerField()
    attendees = models.IntegerField(default=0)
    # attendees = models.ManyToManyField('User', related_name='attended_events')
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    types = models.CharField(max_length=255, choices=EVENT_TYPE_CHOICES, default='event')
    
    def __str__(self):
        return self.name



# class User(models.Model):
#     name = models.CharField(max_length=255)