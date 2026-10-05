from rest_framework import serializers
from ...models import Service, Category


class ServiceSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMetaclass()
    tags = serializers.SerializerMethodField()
    specials = serializers.SerializerMethodField()
    
    def get_category(self, obj):
        return [category.name for category in obj.category.all()]
    
    def get_tags(self, obj):
        return [tag.title for tag in obj.tags.all()]
    
    def get_specials(self, obj):
        return [special.text for special in obj.specials.all()] 
    class Meta:
        model = Service
        fields = '__all__'
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        