# contains serializers to prepare the objects into json requests

from rest_framework import serializers
from .models import user, bank

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = ('name', 'balance','birthday')
        # specifies json fields
