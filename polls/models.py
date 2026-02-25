import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self) -> bool:
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def get_choices(self) -> list["Choice"]:
        return Choice.objects.filter(question_id=self.id)

    def age(self) -> timezone.timedelta:
        return self.pub_date - timezone.now()

    def get_max_choice(self) -> list[float]:
        return max(self.get_choices())


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
