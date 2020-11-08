from django.shortcuts import render,HttpResponse
from .models import Outsourcing
from .serializer import OutsourcingSerializer

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.
class CreateOutsourcing(ListCreateAPIView):
    queryset=Outsourcing.objects.all()
    serializer_class=OutsourcingSerializer

class RetriveOutsourcing(RetrieveUpdateDestroyAPIView):
    queryset=Outsourcing.objects.all()
    serializer_class=OutsourcingSerializer
