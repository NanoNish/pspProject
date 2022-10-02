from .models import Data
from rest_framework import serializers

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ['url', 'HelioDist', 'HGILat', 'HGILon', 'BR', 'BT', 'BN', 'B', 'VR', 'VT', 'VN', 'Speed',
        'FlowEle', 'FlowAng', 'Density', 'Temp', 'isBNaN', 'isSpeedNaN']
