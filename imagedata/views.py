from rest_framework import viewsets
from .serializers import ImageDataSerializer
from .models import ImageData

class ImageDataViewSet(viewsets.ModelViewSet):
    queryset = ImageData.objects.all()
    serializer_class = ImageDataSerializer

def bruh(request):
    print("HI")
    return
