from django.db import models
from serenesiri.models import BaseModel


class SereneModel(BaseModel):
    name = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.name