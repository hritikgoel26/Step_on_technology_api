from .models import Parents,Child
from rest_framework import serializers

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model=Child
        fields=['id','number_of_children','family_number']

class ParentsSerializer(serializers.ModelSerializer):
    number_of_children= serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=Parents
        fields=['id','family_number','number_of_children']        

