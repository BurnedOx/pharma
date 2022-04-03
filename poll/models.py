from enum import Enum
from django.db import models

# Create your models here.

MEDIA_CHOICES = (
    ('image', 'image'),
    ('video', 'video'),
)


class Event(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="events")
    medias = models.ManyToManyField('Media', blank=True)
    scheduled_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    ticket_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

    def scheduled_date_formated(self):
        return self.scheduled_date.strftime("%d/%m/%Y %H:%M")

    class Meta:
        ordering = ["-scheduled_date", "-created"]


class Media(models.Model):
    title = models.CharField(max_length=250)
    src = models.FileField(upload_to="media")
    src_type = models.CharField(
        max_length=10, choices=MEDIA_CHOICES, default='image')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]


class Member(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to="members")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created"]


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " - " + self.subject

    class Meta:
        ordering = ["created"]
