from .models import ImageData
from rest_framework import serializers


class ImageDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImageData
        fields = ['url', 'Folder', 'PNG', 'Time']
