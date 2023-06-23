from rest_framework import serializers
from hi.models import Post

class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
