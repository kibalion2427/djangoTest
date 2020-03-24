from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    publication_date=models.DateTimeField("date published")
    question_description=models.CharField(max_length=200,default='')

    def __str__(self):
        return self.question_text

    def was_publised_recently(self):
        return self.publication_date >=timezone.now()

    datetime.timedelta(days=1)

class Choice(models.Model):
    choice_text=models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    questionFk = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
