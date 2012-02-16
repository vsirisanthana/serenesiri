from django.db import models


class BaseModel(models.Model):
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return 'hello world'