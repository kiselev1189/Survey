__author__ = 'kis'
from django import forms
from django.forms import models
from survey_app.models import Question, Survey, Response, AnswerText
import uuid

class ResponseForm(models.ModelForm):
    class Meta:
        model = Response
        fields = ()

    def __init__(self, *args, **kwargs):
        self.survey = kwargs.pop('survey')
        super(ResponseForm, self).__init__(*args, **kwargs)

        self.uuid = uuid.uuid4().hex

        data = kwargs.get('data')

        for question in self.survey.questions():
            self.fields["question_%d" % question.pk] = forms.CharField(label=question.text, widget=forms.Textarea)

            if data:
                self.fields["question_%d" % question.pk].initial = data.get('question_%d' % question.pk)


    def save(self, commit=True):
        response = super(ResponseForm, self).save(commit=False)
        response.survey = self.survey
        response.uuid = self.uuid
        response.save()

        for field_name, field_value in self.cleaned_data.items():
            if field_name.startswith("question_"):
                question_id = int(field_name.split("_")[1])
                question = Question.objects.get(pk=question_id)

                answer = AnswerText(question=question)
                answer.body = field_value
                answer.response = response
                answer.save()

        return response