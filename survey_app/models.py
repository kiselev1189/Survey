from django.db import models
from django.contrib.auth.models import User
import django

class Survey(models.Model):     # collection of unique questions
    name = models.CharField(max_length=400)
    description = models.TextField()

    def questions(self):
        if self.pk:
            return Question.objects.filter(survey=self.pk)
        else:
            return None



class Question(models.Model):       # linked to it's survey
    text = models.TextField()
    survey = models.ForeignKey(Survey)

    def save(self, *args, **kwargs):
        super(Question, self).save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(User)

class Response(models.Model):       # questions + answers + unique id
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    survey = models.ForeignKey(Survey)
    user = models.ForeignKey(UserProfile)
    uuid = models.CharField(max_length=32)


class Answer(models.Model):
    question = models.ForeignKey(Question)
    response = models.ForeignKey(Response)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class AnswerText(Answer):
    body = models.TextField(blank=True, null=True)

