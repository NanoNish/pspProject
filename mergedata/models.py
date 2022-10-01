from unittest import defaultTestLoader
from django.conf import settings
from django.db import models
from django.utils import timezone
from numpy import NaN


class Data(models.Model):
    HelioDist = models.FloatField(default=NaN)
    HGILat = models.FloatField(default=NaN)
    HGILon = models.FloatField(default=NaN)
    BR = models.FloatField(default=NaN)
    BT = models.FloatField(default=NaN)
    BN = models.FloatField(default=NaN)
    B = models.FloatField(default=NaN)
    VR = models.FloatField(default=NaN)
    VT = models.FloatField(default=NaN)
    VN = models.FloatField(default=NaN)
    Speed = models.FloatField(default=NaN)
    FlowEle = models.FloatField(default=NaN)
    FlowAng = models.FloatField(default=NaN)
    Density = models.FloatField(default=NaN)
    Temp = models.FloatField(default=NaN)
    isBNaN = models.FloatField(default=NaN)
    isSpeedNaN = models.FloatField(default=NaN)
