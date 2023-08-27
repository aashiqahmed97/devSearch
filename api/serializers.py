from rest_framework import serializers
from projects.models import project, tag , Review
from users.models import profile

class reviewserializer (serializers.ModelSerializer):
    class Meta:
        model= Review
        fields = '__all__'

class profileserializer (serializers.ModelSerializer):
    class Meta:
        model= profile
        fields = '__all__'

class tagserializer (serializers.ModelSerializer):
    class Meta:
        model= tag
        fields = '__all__'        



class projectserializer (serializers.ModelSerializer):
    owner = profileserializer(many=False)
    tags = tagserializer(many=True)
    reviews = serializers.SerializerMethodField()


    class Meta:
        model= project
        fields = '__all__'
    def get_reviews(self,obj):
        reviews = obj.review_set.all()
        serializer = reviewserializer(reviews , many=True)
        return serializer.data 
