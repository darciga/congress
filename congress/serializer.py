from rest_framework import serializers
from .models import Applicants


class AplicantsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Applicants
        fields = ('name','lastName','email')