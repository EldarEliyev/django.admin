from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200, blank=False)  # Sorunun metni
    pub_date = models.DateTimeField('date published')  # Yayınlanma tarihi

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Hangi soru ile ilişkili olduğunu belirler
    choice_text = models.CharField(max_length=200)  # Seçenek metni
    votes = models.IntegerField(default=0)  # Oylama sayısı

    def __str__(self):
        return self.choice_text
