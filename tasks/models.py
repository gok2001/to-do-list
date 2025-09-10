from django.db import models


class Task(models.Model):
    title = models.CharField(verbose_name='title', max_length=100)
    description = models.TextField(verbose_name='description', blank=True)
    completed = models.BooleanField(verbose_name='completed')
    created_at = models.DateTimeField(
        verbose_name='created at', auto_now=False, auto_now_add=False, blank=True)

    def __str__(self):
        return self.title