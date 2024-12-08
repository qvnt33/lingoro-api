from django.db import models


class User(models.Model):
    login = models.CharField(max_length=150, unique=True)

    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    created_at = models.DateField(auto_now_add=True)


class Vocabulary(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, related_name='vocabularies', on_delete=models.CASCADE)

    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class WordPair(models.Model):
    vocab = models.ForeignKey(Vocabulary, related_name='wordpairs', on_delete=models.CASCADE)
    annotation = models.TextField(blank=True, null=True)
    word = models.CharField(max_length=100)

    number_errors = models.IntegerField(default=0)

    def __str__(self) -> str:
        translations = self.translations.all()
        if translations.exists():
            formatted_translations: str = ', '.join(t.translation for t in translations)
        else:
            formatted_translations: str = 'Немає перекладу'
        return f'{self.word} -> {formatted_translations}'


class Translation(models.Model):
    translation = models.CharField(max_length=100)
    transcription = models.CharField(max_length=100, blank=True, null=True)

    word_pair = models.ForeignKey(WordPair, related_name='translations', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.translation} (for "{self.word_pair.word}")'
