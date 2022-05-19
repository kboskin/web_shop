from rest_framework import serializers

from catalogue.models import Category, StaticItem


class CategorySerializer(serializers.ModelSerializer):

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['parent_category'] = CategorySerializer(many=True)
        return fields

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'category_description', 'parent_category', 'is_active']


class StaticItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = StaticItem
        fields = ['id', 'category', 'html_content']
