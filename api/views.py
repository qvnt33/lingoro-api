from .models import Translation, User, Vocabulary, WordPair
from .serializers import TranslationSerializer, UserSerializer, VocabularySerializer, WordPairSerializer
from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class VocabularyViewSet(ModelViewSet):
    queryset = Vocabulary.objects.all()
    serializer_class = VocabularySerializer




class WordPairViewSet(ModelViewSet):
    queryset = WordPair.objects.all()
    serializer_class = WordPairSerializer



class TranslationViewSet(ModelViewSet):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
