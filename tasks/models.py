from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    STATUS_CHOISES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completado', 'Completado'),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField()

    status = models.CharField(max_length = 20, choices = STATUS_CHOISES, default = 'pending')

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'tasks')

    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
