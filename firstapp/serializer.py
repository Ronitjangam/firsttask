from rest_framework import serializers
from .models import Outsourcing




class OutsourcingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Outsourcing
        fields=['id','title','description','upload','skills','budget','payment','bids','time_reqd']