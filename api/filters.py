from django_filters import rest_framework as filters

from api.models import Vocabulary, WordPair


class VocabularyFilter(filters.FilterSet):
    # Фільтр для перевірки, чи є опис у словника
    has_description = filters.BooleanFilter(
        field_name='description',
        lookup_expr='isnull',
        exclude=True,  # Перевертаємо логіку: True = є, False = немає
    )

    class Meta:
        model = Vocabulary
        fields: list[str] = ['has_description']  # Додаємо поле для фільтрації


class WordPairFilter(filters.FilterSet):
    # Фільтр для перевірки, чи є анотація у словникової пари
    has_annotation = filters.BooleanFilter(
        field_name='annotation',
        lookup_expr='isnull',
        exclude=True,  # Перевертаємо логіку: True = є, False = немає
    )

    class Meta:
        model = WordPair
        fields: list[str] = ['has_annotation']  # Додаємо поле для фільтрації
