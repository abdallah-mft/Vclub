from rest_framework import serializers
from .models import Club, ClubRequest
from users.models import CustomUser

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club # This tells django to work with this model
        fields = '__all__' # serialize all of them
        read_only_fields = ['slug', 'is_active'] # We can read these fields via Response but we cannot create them or edit them via requests DRF will ignore them

class ClubRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubRequest
        fields = '__all__'
        read_only_fields = ['status', 'reviewed_by'] # Same here 

    def get_president_details(self,obj):
        if obj.president:
            return {
                'id': obj.president.id,
                'username': obj.president.username
            }
        return None 
    
    def get_vice_president_details(self, obj):
        if obj.vice_president:
            return {
                'id': obj.vice_president.id,
                'username': obj.vice_president.username
            }
        return None

    def validate(self, data):
        if data['president'] == data['vice_president']:
            raise serializers.ValidationError("President and Vice President must be different users.")
        return data
    


class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username']
