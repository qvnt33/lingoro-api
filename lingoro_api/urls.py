from rest_framework.routers import DefaultRouter

from api.views import TranslationViewSet, UserViewSet, VocabularyViewSet, WordPairViewSet

router = DefaultRouter()

# Реєстрація маршрутів
router.register('users', UserViewSet, basename='user')
router.register('vocabularies', VocabularyViewSet, basename='vocabulary')
router.register('word_pairs', WordPairViewSet, basename='word_pair')
router.register('translations', TranslationViewSet, basename='translation')

# Додавання всіх маршрутів, створених роутером, у кінцевий список
urlpatterns = router.urls
