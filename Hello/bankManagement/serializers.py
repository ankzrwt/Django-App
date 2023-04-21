# from   import serializers

from models import Customer

# # class CustomerSerializer(serializers.ModelSerializer):
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=(
            'customerId','name','phone'
        )
