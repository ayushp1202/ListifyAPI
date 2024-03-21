from django.db import models

class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True ## I don't want to create new instances using this model as it is very generic.  
        ordering =('-created_at',)
