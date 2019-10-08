from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=200)
    note = models.TextField()
    created_time = models.DateTimeField(default=timezone.now())
    begin_time = models.DateField()
    end_time = models.DateField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title