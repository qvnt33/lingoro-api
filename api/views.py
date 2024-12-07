from django.db.models.manager import BaseManager
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from api.filters import VocabularyFilter, WordPairFilter
from api.models import Translation, User, Vocabulary, WordPair
from api.serializers import TranslationSerializer, UserSerializer, VocabularySerializer, WordPairSerializer


class UserViewSet(ModelViewSet):
    queryset: BaseManager[User] = User.objects.all()
    serializer_class = UserSerializer


class VocabularyViewSet(ModelViewSet):
    queryset: BaseManager[Vocabulary] = Vocabulary.objects.all()
    serializer_class = VocabularySerializer

    filter_backends: list[type[DjangoFilterBackend]] = [DjangoFilterBackend]  # Додаємо фільтрування
    filterset_class = VocabularyFilter  # Прив'язуємо фільтр до ViewSet


class WordPairViewSet(ModelViewSet):
    queryset: BaseManager[WordPair] = WordPair.objects.all()
    serializer_class = WordPairSerializer

    filter_backends: list[type[DjangoFilterBackend]] = [DjangoFilterBackend]  # Додаємо фільтрування
    filterset_class = WordPairFilter  # Прив'язуємо фільтр до ViewSet


class TranslationViewSet(ModelViewSet):
    queryset: BaseManager[Translation] = Translation.objects.all()
    serializer_class = TranslationSerializer
