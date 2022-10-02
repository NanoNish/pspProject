from django.conf import settings
from django.db import models

class ImageData(models.Model):
    Folder = models.CharField(max_length=200, null=False)
    PNG = models.CharField(max_length=200, null=False)
    Time = models.CharField(max_length=200, null=False)