from django.db.models.manager import BaseManager
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from api.filters import VocabularyFilter, WordPairFilter
from api.models import Translation, User, Vocabulary, WordPair
from api.serializers import TranslationSerializer, UserSerializer, VocabularySerializer, WordPairSerializer


class UserViewSet(ModelViewSet):
    queryset: BaseManager[User] = User.objects.all()
    serializer_class = UserSerializer

    filter_backends: list = [OrderingFilter]  # Додаємо фільтрування

    ordering_fields = '__all__'  # Сортування за всіма полями
    ordering = ['created_at']  # Сортування за замовчуванням


class VocabularyViewSet(ModelViewSet):
    queryset: BaseManager[Vocabulary] = Vocabulary.objects.all()
    serializer_class = VocabularySerializer

    filter_backends: list = [DjangoFilterBackend, OrderingFilter]  # Додаємо фільтрування
    filterset_class = VocabularyFilter  # Прив'язуємо фільтр до ViewSet

    ordering_fields = ['id', 'name', 'created_at']  # Сортування за всіма полями
    ordering = ['name']  # Сортування за замовчуванням


class WordPairViewSet(ModelViewSet):
    queryset: BaseManager[WordPair] = WordPair.objects.all()
    serializer_class = WordPairSerializer

    filter_backends: list = [DjangoFilterBackend, OrderingFilter]  # Додаємо фільтрування
    filterset_class = WordPairFilter  # Прив'язуємо фільтр до ViewSet

    ordering_fields = ['id', 'number_errors']  # Сортування за всіма полями
    ordering = ['number_errors']  # Сортування за замовчуванням


class TranslationViewSet(ModelViewSet):
    queryset: BaseManager[Translation] = Translation.objects.all()
    serializer_class = TranslationSerializer

    filter_backends: list = [OrderingFilter]  # Додаємо фільтрування

    ordering_fields = ['id']  # Сортування за всіма полями
    ordering = ['id']  # Сортування за замовчуванням
