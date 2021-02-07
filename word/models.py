from django.db import models

class Word(models.Model):
    thai = models.CharField(max_length=20)
    phonetic = models.CharField(max_length=20)
    meaning = models.CharField(max_length=50)
    notes = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.thai

    class Meta:
        ordering = ('phonetic', 'meaning')