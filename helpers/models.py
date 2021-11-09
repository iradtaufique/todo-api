from django.db import models
from django.db.models.expressions import OrderBy

"""model which save date the model created and when it was updated"""
class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True
        ordering = ('-created_at', )