from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    temple = ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)