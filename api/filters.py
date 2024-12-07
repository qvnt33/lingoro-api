from django_filters import rest_framework as filters

from api.models import Translation, Vocabulary, WordPair


class VocabularyFilter(filters.FilterSet):
    # Фільтр для перевірки, чи є опис у словника
    has_description = filters.BooleanFilter(
        field_name='description',
        lookup_expr='isnull',
        exclude=True,  # Перевертаємо логіку: True = є, False = немає
    )

    # Фільтр по user_id користувача
    user_id = filters.NumberFilter(
        field_name='user',
        lookup_expr='exact',
    )

    class Meta:
        model = Vocabulary
        fields: list[str] = ['has_description', 'user_id']  # Додаємо поле для фільтрації


class WordPairFilter(filters.FilterSet):
    # Фільтр для перевірки, чи є анотація у словникової пари
    has_annotation = filters.BooleanFilter(
        field_name='annotation',
        lookup_expr='isnull',
        exclude=True,  # Перевертаємо логіку: True = є, False = немає
    )

    # Фільтр по vocab_id словника
    vocab_id = filters.NumberFilter(
        field_name='vocab',
        lookup_expr='exact',
    )

    class Meta:
        model = WordPair
        fields: list[str] = ['has_annotation', 'vocab_id']  # Додаємо поле для фільтрації


class TranslationFilter(filters.FilterSet):
    # Фільтр по wordpair_id словникової пари
    wordpair_id = filters.NumberFilter(
        field_name='word_pair',
        lookup_expr='exact',
    )

    class Meta:
        model = Translation
        fields: list[str] = ['wordpair_id']  # Додаємо поле для фільтрації
