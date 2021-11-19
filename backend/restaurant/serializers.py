from rest_framework import serializers
from restaurant.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    """Serializer for Restaurant model"""

    class Meta:
        model = Restaurant
        fields = '__all__'
