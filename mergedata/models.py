from unittest import defaultTestLoader
from django.conf import settings
from django.db import models
from django.utils import timezone
from numpy import NaN

class Data(models.Model):
    Time = models.CharField(max_length=200, null=False)
    HelioDist = models.FloatField(default=NaN, null=True)
    HGILat = models.FloatField(default=NaN, null=True)
    HGILon = models.FloatField(default=NaN, null=True)
    BR = models.FloatField(default=NaN, null=True)
    BT = models.FloatField(default=NaN, null=True)
    BN = models.FloatField(default=NaN, null=True)
    B = models.FloatField(default=NaN, null=True)
    VR = models.FloatField(default=NaN, null=True)
    VT = models.FloatField(default=NaN, null=True)
    VN = models.FloatField(default=NaN, null=True)
    Speed = models.FloatField(default=NaN, null=True)
    FlowEle = models.FloatField(default=NaN, null=True)
    FlowAng = models.FloatField(default=NaN, null=True)
    Density = models.FloatField(default=NaN, null=True)
    Temp = models.FloatField(default=NaN, null=True)
    isBNaN = models.FloatField(default=NaN, null=True)
    isSpeedNaN = models.FloatField(default=NaN, null=True)
