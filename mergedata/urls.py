from django.urls import path
from mergedata.views import default

urlpatterns = [
    path('', default),
]