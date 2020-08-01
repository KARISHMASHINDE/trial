from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tag,Posts



class RegistrationSerializer(serializers.ModelSerializer):
    
	password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = User
		fields = ['email', 'username', 'password', 'password2']
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self,validated_data):

		user = User(
					email=self.validated_data['email'],
					username=self.validated_data['username']
				)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		user.set_password(password)
		user.save()
		return user



class PostsSerializer(serializers.ModelSerializer):
    Author_id = serializers.CharField(source='Author_id.username', read_only=True)
    class Meta:
        model=Posts
        fields='__all__'
        
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'
    
