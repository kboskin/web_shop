from rest_framework import serializers


class InformationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'information_cat', 'category_name']


class InformationItemSerializer(serializers.ModelSerializer):
    information_cat = InformationCategorySerializer()

    class Meta:
        fields = ['id', 'information_cat', 'content_path']


class InlineInformationItemSerializer(serializers.ModelSerializer):
    information_cat = InformationCategorySerializer()
    content_path = InformationItemSerializer()

    class Meta:
        fields = ['id', 'information_cat', 'content_path', 'marqup']