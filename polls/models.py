import datetime

from django.db import models
from django.db.models import Max, Min
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self) -> bool:
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def get_choices(self) -> list["Choice"]:
        return Choice.objects.filter(question_id=self.id)

    def age(self) -> timezone.timedelta:
        return self.pub_date - timezone.now()

    def get_max_choice(self) -> int:
        return max([i.votes for i in self.get_choices()])

    def get_most_popular(self) -> dict:
        max_votes = Choice.objects.aggregate(Max("votes", default=0))
        max_votes['question'] = Choice.objects.filter(
                                                      votes=max_votes
                                                      ['votes__max']
                                                     ).first()
        max_votes["question_id"] = max_votes["question"].question_id
        return max_votes

    def get_least_popular(self) -> int:
        return Choice.objects.aggregate(Min("votes", default=0))


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
