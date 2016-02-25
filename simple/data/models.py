from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=64, unique=True)
    item_processed = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s'%(self.item_name)
