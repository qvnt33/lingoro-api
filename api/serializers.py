from rest_framework import serializers

from api.models import Translation, User, Vocabulary, WordPair


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = '__all__'


class WordPairSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordPair
        fields = '__all__'


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = '__all__'
