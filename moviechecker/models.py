from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    times = models.TextField()

    def __str__(self):
        return self.title

    def get_times(self):
        return self.times
